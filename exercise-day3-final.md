# Abschlussprojekt: Online-Shop Refactoring

## Ausgangssituation
Ein bestehender Online-Shop mit technischen Schulden soll refaktoriert werden. Das System zeigt mehrere Clean Code Verletzungen und soll unter Verwendung aller gelernten Konzepte verbessert werden.

```java
public class Shop {
    private static Shop INSTANCE;
    public static HashMap<String, HashMap<String, Object>> products = new HashMap<>();
    public static ArrayList<HashMap<String, Object>> orders = new ArrayList<>();
    private static double DISCOUNT_THRESHOLD = 100.0;
    private static String DB_URL = "jdbc:mysql://localhost:3306/shop";
    
    public static Shop get() {
        if(INSTANCE == null) {
            INSTANCE = new Shop();
            INSTANCE.loadProducts();
        }
        return INSTANCE;
    }
    
    private void loadProducts() {
        try {
            Connection conn = DriverManager.getConnection(DB_URL, "user", "pass");
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery("SELECT * FROM products");
            while(rs.next()) {
                HashMap<String, Object> p = new HashMap<>();
                p.put("id", rs.getString("id"));
                p.put("name", rs.getString("name"));
                p.put("price", rs.getDouble("price"));
                p.put("stock", rs.getInt("stock"));
                products.put(rs.getString("id"), p);
            }
        } catch(Exception e) {
            System.out.println("DB Error: " + e.getMessage());
        }
    }
    
    public boolean addToCart(String sessionId, String productId, int quantity) {
        HashMap<String, Object> product = products.get(productId);
        if(product == null || (int)product.get("stock") < quantity) {
            return false;
        }
        
        HashMap<String, Object> cart = getCart(sessionId);
        ArrayList<HashMap<String, Object>> items = (ArrayList<HashMap<String, Object>>)cart.get("items");
        
        boolean found = false;
        for(HashMap<String, Object> item : items) {
            if(item.get("productId").equals(productId)) {
                item.put("quantity", (int)item.get("quantity") + quantity);
                found = true;
                break;
            }
        }
        
        if(!found) {
            HashMap<String, Object> item = new HashMap<>();
            item.put("productId", productId);
            item.put("quantity", quantity);
            items.add(item);
        }
        
        return true;
    }
    
    public double checkout(String sessionId, String creditCard) {
        HashMap<String, Object> cart = getCart(sessionId);
        ArrayList<HashMap<String, Object>> items = (ArrayList<HashMap<String, Object>>)cart.get("items");
        
        double total = 0.0;
        for(HashMap<String, Object> item : items) {
            String pid = (String)item.get("productId");
            int qty = (int)item.get("quantity");
            HashMap<String, Object> product = products.get(pid);
            total += (double)product.get("price") * qty;
            
            // Update stock
            product.put("stock", (int)product.get("stock") - qty);
        }
        
        // Apply discount
        if(total >= DISCOUNT_THRESHOLD) {
            total *= 0.9; // 10% discount
        }
        
        // Process payment
        if(processPayment(creditCard, total)) {
            // Create order
            HashMap<String, Object> order = new HashMap<>();
            order.put("items", new ArrayList<>(items));
            order.put("total", total);
            order.put("date", new Date());
            orders.add(order);
            
            // Clear cart
            items.clear();
            return total;
        }
        
        return -1;
    }
    
    private boolean processPayment(String creditCard, double amount) {
        // Payment processing simulation
        return creditCard != null && creditCard.length() == 16;
    }
    
    private HashMap<String, Object> getCart(String sessionId) {
        // Cart handling logic
        return new HashMap<>(); // Simplified for example
    }
}
```

## Aufgaben

### 1. Domain Modellierung (45 Minuten)
- Identifizieren Sie die Kerndomänen
- Erstellen Sie Value Objects
- Definieren Sie Aggregate und Entities
- Dokumentieren Sie Geschäftsregeln

### 2. Clean Architecture (45 Minuten)
- Erstellen Sie eine Schichtenarchitektur
- Definieren Sie klare Interfaces
- Implementieren Sie Repositories
- Trennen Sie Geschäftslogik von technischen Details

### 3. Implementation (90 Minuten)

Beispielstruktur:
```java
// Domain Models
public class Product {
    private final ProductId id;
    private final String name;
    private final Money price;
    private int stockLevel;
    
    public boolean hasEnoughStock(Quantity quantity) {
        return stockLevel >= quantity.getValue();
    }
    
    public void reduceStock(Quantity quantity) {
        if (!hasEnoughStock(quantity)) {
            throw new InsufficientStockException(id, quantity);
        }
        stockLevel -= quantity.getValue();
    }
}

public class Cart {
    private final CartId id;
    private final Map<ProductId, CartItem> items;
    
    public void addItem(Product product, Quantity quantity) {
        items.compute(product.getId(), (key, existingItem) -> 
            existingItem == null ? 
                new CartItem(product, quantity) : 
                existingItem.increaseQuantity(quantity));
    }
    
    public Money calculateTotal() {
        return items.values().stream()
            .map(CartItem::getSubtotal)
            .reduce(Money.ZERO, Money::add);
    }
}

// Application Services
@Service
@Transactional
public class CheckoutService {
    private final CartRepository cartRepository;
    private final ProductRepository productRepository;
    private final OrderRepository orderRepository;
    private final PaymentGateway paymentGateway;
    
    public OrderConfirmation checkout(CartId cartId, PaymentDetails payment) {
        Cart cart = cartRepository.findById(cartId)
            .orElseThrow(() -> new CartNotFoundException(cartId));
            
        Order order = Order.fromCart(cart);
        
        // Validate stock
        order.getItems().forEach(item -> {
            Product product = productRepository.findById(item.getProductId())
                .orElseThrow(() -> new ProductNotFoundException(item.getProductId()));
            product.reduceStock(item.getQuantity());
            productRepository.save(product);
        });
        
        // Process payment
        PaymentResult result = paymentGateway.process(payment, order.getTotal());
        if (!result.isSuccessful()) {
            throw new PaymentFailedException(result.getError());
        }
        
        // Save order
        order = orderRepository.save(order);
        cartRepository.delete(cart);
        
        return new OrderConfirmation(order.getId(), order.getTotal());
    }
}

// Infrastructure
@Repository
public class JpaProductRepository implements ProductRepository {
    private final JpaProductEntityRepository jpaRepository;
    private final ProductMapper mapper;
    
    @Override
    public Optional<Product> findById(ProductId id) {
        return jpaRepository.findById(id.getValue())
            .map(mapper::toDomain);
    }
}
```

### 4. Tests (45 Minuten)

```java
class CheckoutServiceTest {
    private CheckoutService service;
    private CartRepository mockCartRepo;
    private ProductRepository mockProductRepo;
    private OrderRepository mockOrderRepo;
    private PaymentGateway mockPaymentGateway;
    
    @Test
    void shouldSuccessfullyCheckoutCart() {
        // Arrange
        Cart cart = CartTestBuilder.aCart()
            .withItem(ProductTestBuilder.aProduct().build(), Quantity.of(2))
            .build();
        when(mockCartRepo.findById(any())).thenReturn(Optional.of(cart));
        when(mockPaymentGateway.process(any(), any())).thenReturn(PaymentResult.successful());
        
        // Act
        OrderConfirmation confirmation = service.checkout(
            cart.getId(), 
            PaymentDetails.withCreditCard("4111111111111111")
        );
        
        // Assert
        assertNotNull(confirmation);
        verify(mockProductRepo).save(any());
        verify(mockOrderRepo).save(any());
        verify(mockCartRepo).delete(cart);
    }
}
```

### 5. Dokumentation (30 Minuten)
- Architekturübersicht
- Domänenmodell-Dokumentation
- API-Dokumentation
- Betriebsdokumentation

## Bewertungskriterien
- [ ] Clean Architecture Prinzipien
- [ ] Domain-Driven Design
- [ ] SOLID Prinzipien
- [ ] Testabdeckung
- [ ] Fehlerbehandlung
- [ ] Dokumentation
- [ ] Performance-Überlegungen
- [ ] Sicherheitsaspekte

## Bonus-Aufgaben
1. Implementieren Sie Event Sourcing
2. Fügen Sie Caching hinzu
3. Implementieren Sie eine API-Versionierung
4. Erstellen Sie eine Monitoring-Lösung

[Ende des Workshops]

