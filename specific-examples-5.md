# Clean Code Beispiele (Teil 5)

## 11. Microservices-Kommunikation

### ❌ DON'T
```java
@Service
class OrderService {
    @Value("${inventory.service.url}")
    private String inventoryUrl;
    
    public void processOrder(Order order) {
        // Direkter REST-Call ohne Fehlerbehandlung
        RestTemplate rest = new RestTemplate();
        String url = inventoryUrl + "/check-stock";
        
        try {
            ResponseEntity<String> response = rest.postForEntity(
                url, 
                order.getItems(), 
                String.class
            );
            if (response.getStatusCode() == HttpStatus.OK) {
                // Weiterverarbeitung...
            }
        } catch (Exception e) {
            log.error("Error calling inventory", e);
        }
    }
}
```

### ✅ DO
```java
@Service
class OrderService {
    private final InventoryClient inventoryClient;
    private final CircuitBreaker circuitBreaker;
    private final OrderRepository orderRepository;

    @Transactional
    public Order processOrder(ProcessOrderCommand command) {
        return circuitBreaker.executeWithFallback(
            () -> processOrderWithInventoryCheck(command),
            this::handleInventoryServiceFailure
        );
    }
    
    private Order processOrderWithInventoryCheck(ProcessOrderCommand command) {
        Order order = orderRepository.findById(command.orderId())
            .orElseThrow(() -> new OrderNotFoundException(command.orderId()));
            
        // Asynchrone Inventarprüfung
        List<StockReservation> reservations = order.getItems().stream()
            .map(item -> InventoryRequest.builder()
                .productId(item.getProductId())
                .quantity(item.getQuantity())
                .orderId(order.getId())
                .build())
            .map(inventoryClient::checkAndReserveStock)
            .toList();
            
        // Warten auf alle Reservierungen
        CompletableFuture.allOf(
            reservations.toArray(new CompletableFuture[0])
        ).join();
        
        // Validieren der Ergebnisse
        validateReservations(reservations);
        
        return orderRepository.save(order);
    }
}

@Component
class InventoryClient {
    private final WebClient webClient;
    private final RetryPolicy<StockReservation> retryPolicy;

    public CompletableFuture<StockReservation> checkAndReserveStock(
            InventoryRequest request) {
        return Failsafe.with(retryPolicy)
            .executeAsync(() -> webClient
                .post()
                .uri("/api/v1/inventory/reserve")
                .body(Mono.just(request), InventoryRequest.class)
                .retrieve()
                .bodyToMono(StockReservation.class)
                .toFuture());
    }
}

@Configuration
class ClientConfig {
    @Bean
    public WebClient inventoryWebClient(
            LoadBalancedExchangeFilterFunction loadBalancer) {
        return WebClient.builder()
            .baseUrl("lb://inventory-service")
            .filter(loadBalancer)
            .filter(errorHandlingFilter())
            .build();
    }
    
    @Bean
    public RetryPolicy<StockReservation> retryPolicy() {
        return RetryPolicy.<StockReservation>builder()
            .handle(ServiceUnavailableException.class)
            .withDelay(Duration.ofMillis(100))
            .withMaxRetries(3)
            .withJitter(0.25)
            .build();
    }
    
    @Bean
    public CircuitBreakerConfig circuitBreakerConfig() {
        return CircuitBreakerConfig.custom()
            .failureRateThreshold(50)
            .waitDurationInOpenState(Duration.ofSeconds(10))
            .slidingWindowSize(10)
            .build();
    }
}

// Event-basierte Kommunikation
@Configuration
class EventConfig {
    @Bean
    public Function<OrderCreatedEvent, Message<InventoryCheckEvent>> processOrder() {
        return event -> {
            // Verarbeitung des Events
            return MessageBuilder
                .withPayload(new InventoryCheckEvent(event.getOrderId()))
                .setHeader("X-Correlation-ID", event.getCorrelationId())
                .build();
        };
    }
}
```

## 12. API-Design

### ❌ DON'T
```java
@RestController
@RequestMapping("/api")
class OrderController {
    @PostMapping("/orders")
    public Map<String, Object> createOrder(@RequestBody Map<String, Object> data) {
        // Untypisierte Daten
        String userId = (String) data.get("user_id");
        List<Map<String, Object>> items = (List<Map<String, Object>>) data.get("items");
        
        // Direkte Rückgabe von Implementierungsdetails
        Order order = orderService.createOrder(userId, items);
        return Map.of(
            "id", order.getId(),
            "status", order.getStatus(),
            "items", order.getItems()
        );
    }
}
```

### ✅ DO
```java
@RestController
@RequestMapping("/api/v1/orders")
@Tag(name = "Orders", description = "Order management endpoints")
class OrderController {
    private final OrderFacade orderFacade;
    
    @Operation(
        summary = "Create a new order",
        description = "Creates a new order for the given user with specified items"
    )
    @ApiResponses({
        @ApiResponse(
            responseCode = "201",
            description = "Order created successfully",
            content = @Content(schema = @Schema(implementation = OrderResponse.class))
        ),
        @ApiResponse(
            responseCode = "400",
            description = "Invalid request data",
            content = @Content(schema = @Schema(implementation = ErrorResponse.class))
        )
    })
    @PostMapping
    public ResponseEntity<OrderResponse> createOrder(
            @Valid @RequestBody CreateOrderRequest request) {
        Order order = orderFacade.createOrder(
            CreateOrderCommand.from(request)
        );
        
        OrderResponse response = OrderResponse.from(order);
        
        return ResponseEntity
            .status(HttpStatus.CREATED)
            .location(orderLocation(order))
            .body(response);
    }
    
    @Operation(
        summary = "Get order details",
        description = "Retrieves detailed information about a specific order"
    )
    @GetMapping("/{orderId}")
    public ResponseEntity<OrderResponse> getOrder(
            @PathVariable UUID orderId) {
        return orderFacade.findOrder(new OrderId(orderId))
            .map(OrderResponse::from)
            .map(ResponseEntity::ok)
            .orElseThrow(() -> new OrderNotFoundException(orderId));
    }
    
    private URI orderLocation(Order order) {
        return ServletUriComponentsBuilder
            .fromCurrentRequest()
            .path("/{id}")
            .buildAndExpand(order.getId().getValue())
            .toUri();
    }
}

@Value
class CreateOrderRequest {
    @NotNull(message = "Customer ID is required")
    UUID customerId;
    
    @NotEmpty(message = "Order must contain at least one item")
    List<OrderItemRequest> items;
    
    @Valid
    DeliveryDetailsRequest deliveryDetails;
}

@Value
class OrderResponse {
    UUID orderId;
    UUID customerId;
    OrderStatus status;
    Money total;
    List<OrderItemResponse> items;
    LocalDateTime createdAt;
    
    public static OrderResponse from(Order order) {
        return new OrderResponse(
            order.getId().getValue(),
            order.getCustomerId().getValue(),
            order.getStatus(),
            order.getTotal(),
            order.getItems().stream()
                .map(OrderItemResponse::from)
                .toList(),
            order.getCreatedAt()
        );
    }
}

@ControllerAdvice
class ApiExceptionHandler extends ResponseEntityExceptionHandler {
    
    @ExceptionHandler(OrderNotFoundException.class)
    public ResponseEntity<ProblemDetail> handleOrderNotFound(
            OrderNotFoundException ex, WebRequest request) {
        ProblemDetail problem = ProblemDetail
            .forStatusAndDetail(HttpStatus.NOT_FOUND, ex.getMessage());
            
        problem.setTitle("Order Not Found");
        problem.setType(URI.create("https://api.example.com/errors/not-found"));
        
        return ResponseEntity
            .status(HttpStatus.NOT_FOUND)
            .body(problem);
    }
}
```

[Fortsetzung folgt...]

Soll ich mit Performance-Optimierung und weiteren fortgeschrittenen Beispielen fortfahren?