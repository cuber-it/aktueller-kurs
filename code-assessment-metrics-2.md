# Code Assessment Metriken und Beispiele - Fortsetzung

## 7. Clean Code Metriken

### Namen-Qualität

```java
// ❌ Schlechte Namen
class Mgr {
    private List<Obj> l;
    public void proc(Obj o) {
        for(Obj i : l) {
            doStuff(i);
        }
    }
    private void doStuff(Obj o) { }
}

// ✅ Sprechende Namen
class CustomerManager {
    private List<Customer> activeCustomers;
    
    public void processCustomerOrder(Customer customer) {
        activeCustomers.stream()
            .filter(Customer::hasValidSubscription)
            .forEach(this::sendOrderConfirmation);
    }
    
    private void sendOrderConfirmation(Customer customer) {
        // Implementation
    }
}
```

### Methoden-Qualität
Bewertungskriterien:
1. Länge (max. 20 Zeilen)
2. Parameter (max. 3)
3. Abstraktionsebene (einheitlich)
4. Rückgabewerte (konsistent)

```java
// ❌ Schlechte Methode
public Object handleData(String type, Map<String, Object> data, 
    boolean validate, String format, Object... args) {
    
    // 50 Zeilen gemischter Code mit verschiedenen Abstraktionsebenen
    if(validate) {
        // 20 Zeilen Validierung
    }
    
    if(type.equals("customer")) {
        // 15 Zeilen Kundenverarbeitung
    } else if(type.equals("order")) {
        // 15 Zeilen Bestellverarbeitung
    }
    
    return someResult;
}

// ✅ Gute Methoden
public class DataProcessor {
    public ProcessingResult processCustomerData(CustomerData data) {
        validateCustomerData(data);
        Customer customer = createCustomer(data);
        notifyCustomerCreated(customer);
        return new ProcessingResult(customer.getId(), Status.SUCCESS);
    }
    
    public ProcessingResult processOrderData(OrderData data) {
        validateOrderData(data);
        Order order = createOrder(data);
        notifyOrderCreated(order);
        return new ProcessingResult(order.getId(), Status.SUCCESS);
    }
}
```

## 8. Architektur-Metriken

### Package-Struktur
Bewertungskriterien:
1. Zyklische Abhängigkeiten (0 erlaubt)
2. Abstraktionsgrad (ausgeglichen)
3. Stabilität (höher = besser)

```java
// ❌ Schlechte Package-Struktur
package com.company.app;
// Alles in einem Package

// ✅ Gute Package-Struktur
com.company.app
  ├── domain/           // Kerndomäne
  │   ├── model/       // Entitäten
  │   ├── service/     // Geschäftslogik
  │   └── repository/  // Abstrakte Repos
  ├── infrastructure/  // Technische Implementierung
  │   ├── persistence/ // Konkrete Repos
  │   └── messaging/   // Messaging
  └── application/     // Anwendungsfälle
      ├── api/         // REST Controller
      ├── dto/         // DTOs
      └── mapper/      // Mapper
```

### Schichten-Metrics
```java
// ❌ Verletzung der Schichtenarchitektur
@RestController
class OrderController {
    @Autowired
    private JdbcTemplate jdbc;  // Direkter Datenbankzugriff
    
    @PostMapping("/orders")
    public void createOrder(@RequestBody Order order) {
        jdbc.update("INSERT INTO orders ...");  // 🚫
    }
}

// ✅ Saubere Schichtenarchitektur
@RestController
class OrderController {
    private final OrderApplicationService orderService;
    
    @PostMapping("/orders")
    public ResponseEntity<OrderResponse> createOrder(
            @Valid @RequestBody OrderRequest request) {
        OrderId orderId = orderService.createOrder(
            CreateOrderCommand.from(request)
        );
        return ResponseEntity
            .created(orderUri(orderId))
            .body(new OrderResponse(orderId));
    }
}
```

## 9. Test-Qualitäts-Metriken

### Test-Isolation

```java
// ❌ Abhängige Tests
class OrderTest {
    static Order sharedOrder;
    
    @Test
    void test1() {
        sharedOrder = new Order();  // Seiteneffekt
    }
    
    @Test
    void test2() {
        assertNotNull(sharedOrder);  // Abhängig von test1
    }
}

// ✅ Isolierte Tests
class OrderTest {
    @Test
    void shouldCalculateTotal() {
        Order order = new OrderBuilder()
            .withItem(Money.of(10))
            .withItem(Money.of(20))
            .build();
            
        Money total = order.calculateTotal();
        
        assertThat(total).isEqualTo(Money.of(30));
    }
    
    @Test
    void shouldNotAllowNegativeQuantities() {
        assertThatThrownBy(() -> 
            new OrderBuilder()
                .withItem(Money.of(10), Quantity.of(-1))
                .build()
        )
        .isInstanceOf(IllegalArgumentException.class)
        .hasMessage("Quantity must be positive");
    }
}
```

### Test-Lesbarkeit

```java
// ❌ Schwer lesbare Tests
@Test
void t1() {
    Order o = new Order();
    o.addItem("123", 1);
    o.addItem("456", 2);
    assertTrue(o.getTotal() == 49.98);
}

// ✅ Gut strukturierte Tests
@Test
void shouldCalculateTotalForMultipleItems() {
    // Arrange
    Order order = OrderBuilder.create()
        .withItem(ProductId.of("BOOK-123"), Quantity.of(1), Money.of(29.99))
        .withItem(ProductId.of("DVD-456"), Quantity.of(2), Money.of(9.99))
        .build();
        
    // Act
    Money total = order.calculateTotal();
    
    // Assert
    assertThat(total)
        .isEqualTo(Money.of(49.97))
        .describedAs("Total should be sum of book and DVDs");
}
```

## 10. Performance-Metriken

### Response Time Verteilung

```java
// ❌ Langsame Implementierung
@GetMapping("/dashboard")
public DashboardData getDashboard() {
    List<Order> orders = orderRepository.findAll();  // N+1
    List<Customer> customers = customerRepository.findAll();
    List<Product> products = productRepository.findAll();
    
    return new DashboardData(
        orders.stream().mapToDouble(Order::getTotal).sum(),
        customers.size(),
        products.stream().filter(Product::isLowStock).count()
    );
}

// ✅ Optimierte Implementierung
@GetMapping("/dashboard")
@Cacheable(value = "dashboard", key = "#root.method.name")
public DashboardData getDashboard() {
    return dashboardRepository.getDashboardMetrics();
}

@Repository
interface DashboardRepository {
    @Query("""
        SELECT new com.example.DashboardData(
            COALESCE(SUM(o.total), 0),
            COUNT(DISTINCT c.id),
            COUNT(p) FILTER (WHERE p.stock < p.minimumStock)
        )
        FROM Order o
        CROSS JOIN Customer c
        CROSS JOIN Product p
        WHERE o.createdAt >= :startOfDay
    """)
    DashboardData getDashboardMetrics();
}
```

[Fortsetzung folgt...]

Soll ich mit weiteren spezifischen Metriken und Beispielen fortfahren?