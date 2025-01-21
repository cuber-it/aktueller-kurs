# Clean Code Beispiele (Teil 6)

## 13. Performance-Optimierung

### ❌ DON'T
```java
@Service
class ProductService {
    public List<ProductDto> getAllProducts() {
        // Lädt alle Produkte auf einmal
        List<Product> products = repository.findAll();
        
        // N+1 Problem
        return products.stream()
            .map(product -> {
                ProductDto dto = new ProductDto();
                dto.setId(product.getId());
                dto.setName(product.getName());
                dto.setCategory(categoryRepository.findById(product.getCategoryId()));
                dto.setStock(inventoryService.getStock(product.getId()));
                return dto;
            })
            .collect(Collectors.toList());
    }
}
```

### ✅ DO
```java
@Service
@Slf4j
class ProductService {
    private final ProductRepository productRepository;
    private final CategoryRepository categoryRepository;
    private final InventoryClient inventoryClient;
    private final CacheManager cacheManager;
    
    public Flux<ProductDto> getProducts(ProductSearchCriteria criteria) {
        return Flux.deferContextual(ctx -> {
            String correlationId = ctx.get("correlationId");
            Timer.Sample timer = Timer.start();
            
            return findProducts(criteria)
                .transform(this::enrichWithCategories)
                .transform(this::enrichWithInventory)
                .doOnComplete(() -> 
                    recordQueryMetrics(timer, criteria, correlationId)
                );
        });
    }
    
    private Flux<Product> findProducts(ProductSearchCriteria criteria) {
        return criteria.hasCategory()
            ? findProductsByCategory(criteria)
            : findAllProducts(criteria);
    }
    
    private Flux<Product> findProductsByCategory(ProductSearchCriteria criteria) {
        return productRepository
            .findByCategory(criteria.getCategory())
            .filter(product -> meetsSearchCriteria(product, criteria));
    }
    
    private Flux<ProductDto> enrichWithCategories(Flux<Product> products) {
        return products
            .bufferTimeout(100, Duration.ofMillis(50))
            .flatMap(batch -> {
                Set<CategoryId> categoryIds = batch.stream()
                    .map(Product::getCategoryId)
                    .collect(Collectors.toSet());
                    
                return categoryRepository
                    .findAllById(categoryIds)
                    .collectMap(Category::getId)
                    .flatMapMany(categories -> 
                        Flux.fromIterable(batch)
                            .map(product -> 
                                enrichWithCategory(product, 
                                    categories.get(product.getCategoryId())
                                )
                            )
                    );
            });
    }
    
    private Flux<ProductDto> enrichWithInventory(Flux<ProductDto> products) {
        return products
            .bufferTimeout(100, Duration.ofMillis(50))
            .flatMap(batch -> {
                List<ProductId> productIds = batch.stream()
                    .map(ProductDto::getId)
                    .collect(Collectors.toList());
                    
                return inventoryClient
                    .getStockLevels(productIds)
                    .collectMap(StockLevel::getProductId)
                    .flatMapMany(stockLevels ->
                        Flux.fromIterable(batch)
                            .map(product ->
                                enrichWithStock(product,
                                    stockLevels.get(product.getId())
                                )
                            )
                    );
            });
    }
    
    @Cacheable(
        cacheNames = "product-categories",
        key = "#product.categoryId",
        unless = "#result == null"
    )
    private Category getCachedCategory(Product product) {
        return categoryRepository
            .findById(product.getCategoryId())
            .orElseThrow(() -> 
                new CategoryNotFoundException(product.getCategoryId())
            );
    }
    
    private void recordQueryMetrics(
            Timer.Sample timer, 
            ProductSearchCriteria criteria,
            String correlationId) {
            
        timer.stop(meterRegistry.timer("product.search.duration",
            "category", criteria.getCategory().toString(),
            "correlationId", correlationId
        ));
    }
}

@Configuration
class PerformanceConfig {
    @Bean
    public ConnectionPool connectionPool() {
        return ConnectionPool.builder()
            .maxIdleTime(Duration.ofMinutes(10))
            .maxSize(10)
            .build();
    }
    
    @Bean
    public ThreadPoolTaskExecutor asyncExecutor() {
        ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
        executor.setCorePoolSize(10);
        executor.setMaxPoolSize(50);
        executor.setQueueCapacity(500);
        executor.setThreadNamePrefix("async-");
        return executor;
    }
    
    @Bean
    public CacheManager cacheManager() {
        return RedisCacheManager.builder(redisConnectionFactory())
            .cacheDefaults(defaultConfig())
            .withInitialCacheConfigurations(customConfigs())
            .build();
    }
    
    private RedisCacheConfiguration defaultConfig() {
        return RedisCacheConfiguration.defaultCacheConfig()
            .entryTtl(Duration.ofMinutes(10))
            .serializeKeysWith(
                RedisSerializationContext
                    .SerializationPair
                    .fromSerializer(new StringRedisSerializer())
            )
            .serializeValuesWith(
                RedisSerializationContext
                    .SerializationPair
                    .fromSerializer(new GenericJackson2JsonRedisSerializer())
            );
    }
}

@Repository
interface ProductRepository extends ReactiveCrudRepository<Product, ProductId> {
    @Query("""
        SELECT p FROM Product p
        LEFT JOIN FETCH p.category
        WHERE p.category.id = :categoryId
        AND p.status = 'ACTIVE'
        ORDER BY p.name
        """
    )
    Flux<Product> findByCategory(CategoryId categoryId);
    
    @Query(value = """
        SELECT p.* FROM products p
        WHERE p.status = 'ACTIVE'
        AND (:categoryId IS NULL OR p.category_id = :categoryId)
        AND (:minPrice IS NULL OR p.price >= :minPrice)
        AND (:maxPrice IS NULL OR p.price <= :maxPrice)
        ORDER BY p.created_at DESC
        LIMIT :limit OFFSET :offset
        """,
        countQuery = """
        SELECT COUNT(*) FROM products p
        WHERE p.status = 'ACTIVE'
        AND (:categoryId IS NULL OR p.category_id = :categoryId)
        AND (:minPrice IS NULL OR p.price >= :minPrice)
        AND (:maxPrice IS NULL OR p.price <= :maxPrice)
        """
    )
    Flux<Product> findAllByCriteria(
        @Param("categoryId") CategoryId categoryId,
        @Param("minPrice") Money minPrice,
        @Param("maxPrice") Money maxPrice,
        @Param("limit") int limit,
        @Param("offset") int offset
    );
}
```

[Fortsetzung folgt mit weiteren Beispielen für Batch-Verarbeitung, Daten-Export und andere fortgeschrittene Szenarien...]

Soll ich fortfahren?