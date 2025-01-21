# Clean Code Beispiele (Teil 4)

## 9. Logging & Monitoring

### ❌ DON'T
```java
@Service
class OrderService {
    public void processOrder(Order order) {
        System.out.println("Processing order: " + order.getId());
        try {
            // Geschäftslogik
            System.out.println("Order processed successfully");
        } catch (Exception e) {
            e.printStackTrace();
            System.err.println("Error processing order: " + e.getMessage());
        }
    }
}
```

### ✅ DO
```java
@Service
@Slf4j
class OrderService {
    private final MeterRegistry meterRegistry;
    private final OrderTracer orderTracer;

    @Timed(value = "order.processing", description = "Time taken to process order")
    public Order processOrder(ProcessOrderCommand command) {
        OrderId orderId = command.orderId();
        log.info("Starting order processing for orderId={}", orderId);
        
        Timer.Sample timer = Timer.start(meterRegistry);
        
        try (var span = orderTracer.startProcessing(orderId)) {
            Order order = findAndValidateOrder(orderId);
            
            span.addEvent("Validation completed");
            
            // Geschäftslogik
            processValidOrder(order);
            
            meterRegistry.counter("orders.processed").increment();
            log.info("Order processed successfully for orderId={}", orderId);
            
            timer.stop(meterRegistry.timer("order.processing.time"));
            return order;
            
        } catch (OrderNotFoundException e) {
            meterRegistry.counter("orders.not_found").increment();
            log.warn("Order not found for orderId={}", orderId, e);
            throw e;
            
        } catch (Exception e) {
            meterRegistry.counter("orders.failed").increment();
            log.error("Order processing failed for orderId={}", orderId, e);
            throw e;
        }
    }
}

@Component
class OrderTracer {
    private final Tracer tracer;

    public Span startProcessing(OrderId orderId) {
        return tracer.spanBuilder("process-order")
            .setAttribute("orderId", orderId.toString())
            .setAttribute("service.name", "order-service")
            .startSpan();
    }
}

@Configuration
class LoggingConfig {
    @Bean
    public LoggingEventCompositeJsonEncoder encoder() {
        LoggingEventCompositeJsonEncoder encoder = new LoggingEventCompositeJsonEncoder();
        encoder.setProviders(List.of(
            new LoggingEventJsonProviders() {{
                add(new TimestampJsonProvider());
                add(new LogLevelJsonProvider());
                add(new ThreadNameJsonProvider());
                add(new MessageJsonProvider());
                add(new StackTraceJsonProvider());
                add(new MdcJsonProvider());
            }}
        ));
        return encoder;
    }
}

// Aspect für Method-Level Monitoring
@Aspect
@Component
class MonitoringAspect {
    private final MeterRegistry meterRegistry;
    
    @Around("@annotation(Monitored)")
    public Object monitorMethod(ProceedingJoinPoint joinPoint) throws Throwable {
        String methodName = joinPoint.getSignature().getName();
        Timer.Sample timer = Timer.start(meterRegistry);
        
        try {
            Object result = joinPoint.proceed();
            timer.stop(meterRegistry.timer("method.execution", 
                "method", methodName,
                "status", "success"
            ));
            return result;
        } catch (Exception e) {
            timer.stop(meterRegistry.timer("method.execution",
                "method", methodName,
                "status", "error"
            ));
            throw e;
        }
    }
}
```

## 10. Fortgeschrittenes Testing

### ❌ DON'T
```java
@Test
void testOrder() {
    // Unspezifischer Test mit vielen Assertions
    Order order = new Order();
    order.addItem(new Item("product1", 10));
    order.process();
    
    assertTrue(order.isProcessed());
    assertEquals(10, order.getTotal());
    assertNotNull(order.getProcessedDate());
    // ... weitere Assertions
}
```

### ✅ DO
```java
class OrderTest {
    
    @Nested
    class OrderCreation {
        @Test
        void shouldCreateOrderWithValidItems() {
            // Given
            var items = List.of(
                new OrderItem(ProductId.of("P1"), Quantity.of(2)),
                new OrderItem(ProductId.of("P2"), Quantity.of(1))
            );
            
            // When
            Order order = Order.create(
                OrderId.generate(),
                CustomerId.of("C1"),
                items
            );
            
            // Then
            assertThat(order)
                .isNotNull()
                .satisfies(o -> {
                    assertThat(o.getStatus()).isEqualTo(OrderStatus.CREATED);
                    assertThat(o.getItems()).hasSize(2);
                });
        }
        
        @Test
        void shouldThrowExceptionForEmptyItems() {
            assertThatThrownBy(() -> 
                Order.create(
                    OrderId.generate(),
                    CustomerId.of("C1"),
                    List.of()
                ))
                .isInstanceOf(InvalidOrderException.class)
                .hasMessage("Order must contain at least one item");
        }
    }
    
    @Nested
    class OrderProcessing {
        private OrderTestBuilder orderBuilder;
        private MockPaymentGateway paymentGateway;
        
        @BeforeEach
        void setUp() {
            orderBuilder = new OrderTestBuilder();
            paymentGateway = new MockPaymentGateway();
        }
        
        @Test
        void shouldProcessOrderSuccessfully() {
            // Given
            Order order = orderBuilder
                .withItem(ProductId.of("P1"), Quantity.of(2))
                .withStatus(OrderStatus.CREATED)
                .build();
                
            paymentGateway.willAcceptPayment();
            
            // When
            order.process(paymentGateway);
            
            // Then
            assertThat(order.getStatus()).isEqualTo(OrderStatus.PROCESSED);
            verify(paymentGateway).hasProcessedAmount(order.getTotal());
        }
    }
}

// Test Data Builder
class OrderTestBuilder {
    private OrderId id = OrderId.generate();
    private CustomerId customerId = CustomerId.of("C1");
    private List<OrderItem> items = new ArrayList<>();
    private OrderStatus status = OrderStatus.CREATED;
    
    public OrderTestBuilder withItem(ProductId productId, Quantity quantity) {
        items.add(new OrderItem(productId, quantity));
        return this;
    }
    
    public OrderTestBuilder withStatus(OrderStatus status) {
        this.status = status;
        return this;
    }
    
    public Order build() {
        return new Order(id, customerId, items, status);
    }
}

// Integration Tests
@SpringBootTest
@TestPropertySource(locations = "classpath:test.properties")
class OrderProcessingIntegrationTest {
    
    @Autowired
    private OrderRepository orderRepository;
    
    @Autowired
    private PaymentGateway paymentGateway;
    
    @Test
    void shouldPersistProcessedOrder() {
        // Given
        Order order = new OrderTestBuilder()
            .withItem(ProductId.of("P1"), Quantity.of(2))
            .build();
            
        // When
        Order savedOrder = orderRepository.save(order);
        savedOrder.process(paymentGateway);
        orderRepository.save(savedOrder);
        
        // Then
        Order foundOrder = orderRepository.findById(savedOrder.getId())
            .orElseThrow();
            
        assertThat(foundOrder)
            .isNotNull()
            .extracting(Order::getStatus)
            .isEqualTo(OrderStatus.PROCESSED);
    }
}

// Property-Based Testing
class MoneyProperties {
    @Property
    void additionIsCommutative(
        @ForAll @BigDecimalRange(min = "0.00", max = "1000000.00") 
        BigDecimal amount1,
        @ForAll @BigDecimalRange(min = "0.00", max = "1000000.00") 
        BigDecimal amount2
    ) {
        Money m1 = Money.of(amount1);
        Money m2 = Money.of(amount2);
        
        assertThat(m1.add(m2))
            .isEqualTo(m2.add(m1));
    }
}
```

[Fortsetzung folgt...]

Soll ich mit weiteren Beispielen fortfahren, etwa für Microservices-Kommunikation, API-Design oder Performance-Optimierung?