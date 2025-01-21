# Clean Code Beispiele (Teil 2)

## 3. Event Handling & Domain Events

### ❌ DON'T
```java
class OrderService {
    @Autowired
    private EmailService emailService;
    @Autowired
    private InventoryService inventoryService;
    
    public void placeOrder(Order order) {
        // Direkte Aufrufe aller Nebeneffekte
        order.setStatus("PLACED");
        orderRepository.save(order);
        emailService.sendOrderConfirmation(order);
        inventoryService.reduceStock(order.getItems());
        notificationService.notifyCustomer(order);
    }
}
```

### ✅ DO
```java
// Domain Event
public sealed interface DomainEvent permits OrderPlaced, OrderCancelled, 
    OrderShipped, StockReduced {
    UUID getEventId();
    LocalDateTime getOccurredAt();
}

public record OrderPlaced(
    UUID eventId,
    LocalDateTime occurredAt,
    OrderId orderId,
    CustomerId customerId,
    Money totalAmount,
    List<OrderItem> items
) implements DomainEvent {
}

// Aggregate Root
@Entity
public class Order extends AggregateRoot {
    private OrderStatus status;
    private final CustomerId customerId;
    private final List<OrderItem> items;
    private final Money totalAmount;
    
    public void place() {
        validateState();
        this.status = OrderStatus.PLACED;
        registerEvent(new OrderPlaced(
            UUID.randomUUID(),
            LocalDateTime.now(),
            getId(),
            customerId,
            totalAmount,
            List.copyOf(items)
        ));
    }
}

// Event Handler
@Component
public class OrderEventHandler {
    private final EmailService emailService;
    private final InventoryService inventoryService;
    
    @EventListener
    public void handleOrderPlaced(OrderPlaced event) {
        // Separate Logik für jeden Handler
        sendOrderConfirmation(event);
        reduceInventory(event);
    }
    
    private void sendOrderConfirmation(OrderPlaced event) {
        var emailDetails = new OrderConfirmationEmail(
            event.customerId(),
            event.orderId(),
            event.totalAmount()
        );
        emailService.sendOrderConfirmation(emailDetails);
    }
    
    private void reduceInventory(OrderPlaced event) {
        event.items().forEach(item -> 
            inventoryService.reduceStock(item.productId(), item.quantity())
        );
    }
}

// Service
@Service
@Transactional
public class OrderService {
    private final OrderRepository orderRepository;
    private final ApplicationEventPublisher eventPublisher;
    
    public Order placeOrder(PlaceOrderCommand command) {
        Order order = orderRepository.findById(command.orderId())
            .orElseThrow(() -> new OrderNotFoundException(command.orderId()));
            
        order.place();
        Order savedOrder = orderRepository.save(order);
        
        order.getDomainEvents().forEach(eventPublisher::publishEvent);
        
        return savedOrder;
    }
}
```

## 4. Async-Operationen & Reactive Programming

### ❌ DON'T
```java
@Service
class ProductService {
    @Async
    public void updateProducts() {
        try {
            Thread.sleep(1000);
            // Lange laufende Operation
            List<Product> products = repository.findAll();
            for(Product p : products) {
                try {
                    updatePrice(p);
                    repository.save(p);
                } catch(Exception e) {
                    log.error("Error updating product", e);
                }
            }
        } catch(Exception e) {
            log.error("Error in update", e);
        }
    }
}
```

### ✅ DO
```java
@Service
class ProductService {
    private final ProductRepository repository;
    private final PriceCalculator priceCalculator;
    private final ApplicationEventPublisher eventPublisher;

    public Flux<Product> updateProducts() {
        return repository.findAll()
            .flatMap(this::updateProductPrice)
            .doOnError(this::handleError)
            .doOnNext(this::publishUpdateEvent);
    }
    
    private Mono<Product> updateProductPrice(Product product) {
        return Mono.just(product)
            .map(this::calculateNewPrice)
            .flatMap(repository::save)
            .onErrorResume(e -> handleProductError(product, e));
    }
    
    private Product calculateNewPrice(Product product) {
        return product.updatePrice(
            priceCalculator.calculatePrice(product)
        );
    }
    
    private void publishUpdateEvent(Product product) {
        eventPublisher.publishEvent(new ProductUpdated(
            product.getId(),
            product.getPrice(),
            LocalDateTime.now()
        ));
    }
    
    private Mono<Product> handleProductError(Product product, Throwable error) {
        log.error("Error updating product {}: {}", 
            product.getId(), error.getMessage());
        return Mono.empty();
    }
    
    private void handleError(Throwable error) {
        log.error("Batch update error: {}", error.getMessage());
    }
}

// Controller
@RestController
@RequestMapping("/api/v1/products")
class ProductController {
    private final ProductService productService;
    
    @GetMapping(produces = MediaType.APPLICATION_NDJSON_VALUE)
    public Flux<ProductResponse> streamProducts() {
        return productService.updateProducts()
            .map(mapper::toResponse)
            .onErrorResume(this::handleStreamError);
    }
    
    private Flux<ProductResponse> handleStreamError(Throwable error) {
        log.error("Stream error: {}", error.getMessage());
        return Flux.empty();
    }
}
```

## 5. Caching & Performance

### ❌ DON'T
```java
@Service
class ProductService {
    private Map<String, Product> cache = new HashMap<>();
    
    public Product getProduct(String id) {
        if (cache.containsKey(id)) {
            return cache.get(id);
        }
        Product product = repository.findById(id);
        if (product != null) {
            cache.put(id, product);
        }
        return product;
    }
    
    public void updateProduct(Product product) {
        repository.save(product);
        cache.put(product.getId(), product);
    }
}
```

### ✅ DO
```java
@Service
class ProductService {
    private final ProductRepository repository;
    private final CacheManager cacheManager;
    private final ProductValidator validator;
    
    @Cacheable(
        cacheNames = "products", 
        key = "#id",
        unless = "#result == null"
    )
    public Optional<Product> findProduct(ProductId id) {
        return repository.findById(id);
    }
    
    @CacheEvict(
        cacheNames = "products", 
        key = "#result.id"
    )
    @Transactional
    public Product updateProduct(UpdateProductCommand command) {
        Product product = repository.findById(command.productId())
            .orElseThrow(() -> new ProductNotFoundException(command.productId()));
            
        validator.validateUpdate(command);
        
        Product updatedProduct = product.update(command);
        return repository.save(updatedProduct);
    }
    
    @CacheEvict(
        cacheNames = "products",
        allEntries = true
    )
    @Scheduled(fixedRate = 3600000) // 1 Stunde
    public void evictCache() {
        log.info("Evicting product cache");
    }
}

@Configuration
class CacheConfig extends CachingConfigurerSupport {
    @Bean
    public CacheManager cacheManager() {
        SimpleCacheManager cacheManager = new SimpleCacheManager();
        
        CaffeineCache productsCache = new CaffeineCache("products",
            Caffeine.newBuilder()
                .expireAfterWrite(1, TimeUnit.HOURS)
                .maximumSize(10000)
                .recordStats()
                .build());
        
        cacheManager.setCaches(List.of(productsCache));
        return cacheManager;
    }
    
    @Bean
    public CacheErrorHandler errorHandler() {
        return new SimpleCacheErrorHandler() {
            @Override
            public void handleCacheGetError(RuntimeException e, Cache cache, Object key) {
                log.error("Cache get error: {}", e.getMessage());
                super.handleCacheGetError(e, cache, key);
            }
        };
    }
}
```

[Fortsetzung folgt...]

Soll ich mit weiteren Beispielen fortfahren, z.B. für Validation, Security oder Error Handling?