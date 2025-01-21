# Code Assessment Metriken und Beispiele

## 1. Quantitative Metriken

### Komplexitätsmetriken
```java
// ❌ Hohe zyklomatische Komplexität (>10)
public boolean validateOrder(Order order) {
    if (order == null) return false;
    if (order.getCustomer() == null) return false;
    if (order.getItems() == null) return false;
    if (order.getItems().isEmpty()) return false;
    if (order.getTotal().isNegative()) return false;
    if (!order.getCustomer().isActive()) return false;
    for (OrderItem item : order.getItems()) {
        if (item.getQuantity() <= 0) return false;
        if (item.getPrice().isNegative()) return false;
        if (!isProductAvailable(item.getProductId())) return false;
    }
    return true;
}

// ✅ Niedrige Komplexität durch Extraktion
public boolean validateOrder(Order order) {
    return Optional.ofNullable(order)
        .filter(this::hasValidCustomer)
        .filter(this::hasValidItems)
        .filter(this::hasValidTotal)
        .isPresent();
}

private boolean hasValidItems(Order order) {
    return order.getItems().stream()
        .allMatch(this::isValidOrderItem);
}
```

### Kopplungsmetriken
```java
// ❌ Hohe Kopplung
class OrderProcessor {
    private CustomerRepository customerRepo;
    private ProductRepository productRepo;
    private InventoryService inventory;
    private PaymentService payment;
    private EmailService email;
    private AuditService audit;
    private MetricsService metrics;
    // Zu viele Abhängigkeiten
}

// ✅ Reduzierte Kopplung
class OrderProcessor {
    private final OrderRepository orderRepository;
    private final OrderEventPublisher eventPublisher;
    // Nur die notwendigsten Abhängigkeiten
}
```

### Kohäsionsmetriken
```java
// ❌ Niedrige Kohäsion
class UserUtility {
    public void saveUser() { }
    public void calculateTax() { }
    public void sendEmail() { }
    public void validateAddress() { }
}

// ✅ Hohe Kohäsion
class UserRegistrationService {
    public User registerUser(RegistrationRequest request) {
        validateRequest(request);
        User user = createUser(request);
        notifyUser(user);
        return user;
    }
}
```

## 2. Code Coverage Ziele

### Unit Test Coverage
```java
// Minimale Testabdeckung: 80%
class OrderTest {
    @Test
    void shouldCalculateTotalWithTax() {
        Order order = new OrderBuilder()
            .withItem("Book", Money.of(10))
            .withItem("DVD", Money.of(20))
            .build();
            
        Money total = order.calculateTotal();
        
        assertThat(total).isEqualTo(Money.of(30));
    }
    
    @Test
    void shouldApplyDiscountForLargeOrders() {
        Order order = new OrderBuilder()
            .withItem("TV", Money.of(1000))
            .build();
            
        Money total = order.calculateTotal();
        
        assertThat(total).isEqualTo(Money.of(900)); // 10% Rabatt
    }
}
```

### Integration Test Coverage
```java
// Minimale Testabdeckung: 60%
@SpringBootTest
class OrderIntegrationTest {
    @Test
    void shouldSaveOrderAndUpdateInventory() {
        OrderRequest request = new OrderRequest(
            CustomerId.of("123"),
            List.of(new OrderItemRequest("P1", 2))
        );
        
        orderService.createOrder(request);
        
        assertThat(inventoryService.getStock("P1")).isEqualTo(8);
    }
}
```

## 3. Qualitative Metriken

### Code Duplication Schwellwerte
```java
// ❌ Duplizierter Code (>3 Zeilen identisch)
class UserService {
    public void createUser(UserDto dto) {
        validateEmail(dto.getEmail());
        validatePassword(dto.getPassword());
        validateAge(dto.getAge());
        // ... weitere Validierungen
    }
    
    public void updateUser(UserDto dto) {
        validateEmail(dto.getEmail());
        validatePassword(dto.getPassword());
        validateAge(dto.getAge());
        // ... gleiche Validierungen
    }
}

// ✅ Extrahierte Validierung
class UserService {
    private final UserValidator validator;
    
    public void createUser(UserDto dto) {
        validator.validate(dto);
        // create logic
    }
    
    public void updateUser(UserDto dto) {
        validator.validate(dto);
        // update logic
    }
}
```

### Methoden-Metriken
- Maximale Länge: 20 Zeilen
- Maximale Parameter: 3
- Maximale Verschachtelungstiefe: 2

```java
// ❌ Übermäßige Parameter
public void updateUser(
    String id, 
    String name, 
    String email, 
    String password, 
    int age, 
    String country, 
    boolean active
) { }

// ✅ Parameter-Objekt
public void updateUser(UserUpdateCommand command) { }

// ❌ Tiefe Verschachtelung
if (user != null) {
    if (user.getAddress() != null) {
        if (user.getAddress().getCountry() != null) {
            if (user.getAddress().getCountry().equals("DE")) {
                // Logik
            }
        }
    }
}

// ✅ Frühe Returns
if (user == null) return;
if (user.getAddress() == null) return;
if (user.getAddress().getCountry() == null) return;
if (!user.getAddress().getCountry().equals("DE")) return;
// Logik
```

## 4. Performance Metriken

### Response Time
```java
// ❌ Langsame Verarbeitung
@GetMapping("/users")
public List<UserDto> getUsers() {
    return userRepository.findAll()  // N+1 Problem
        .stream()
        .map(user -> {
            UserDto dto = new UserDto();
            dto.setOrders(orderRepository.findByUserId(user.getId()));
            return dto;
        })
        .collect(Collectors.toList());
}

// ✅ Optimierte Verarbeitung
@GetMapping("/users")
public List<UserDto> getUsers() {
    return userRepository
        .findAllWithOrders()  // JOIN FETCH
        .stream()
        .map(userMapper::toDto)
        .collect(Collectors.toList());
}
```

### Memory Usage
```java
// ❌ Hoher Speicherverbrauch
public void processLargeFile(File file) {
    List<String> lines = Files.readAllLines(file.toPath());  // Lädt alles in den Speicher
    lines.forEach(this::processLine);
}

// ✅ Stream-basierte Verarbeitung
public void processLargeFile(File file) {
    Files.lines(file.toPath())  // Streaming
        .forEach(this::processLine);
}
```

## 5. Security Metrics

### OWASP Top 10 Compliance
```java
// ❌ SQL Injection anfällig
public User findUser(String id) {
    return jdbcTemplate.queryForObject(
        "SELECT * FROM users WHERE id = " + id,  // Unsicher
        User.class
    );
}

// ✅ Prepared Statement
public User findUser(String id) {
    return jdbcTemplate.queryForObject(
        "SELECT * FROM users WHERE id = ?",
        User.class,
        id  // Parameter werden escaped
    );
}
```

### Authentication & Authorization
```java
// ❌ Unsichere Passwort-Handhabung
@Entity
class User {
    private String password;  // Plaintext
}

// ✅ Sichere Passwort-Handhabung
@Entity
class User {
    @Column(name = "password_hash")
    private String passwordHash;
    
    @Column(name = "password_salt")
    private String salt;
    
    public void setPassword(String password) {
        this.salt = generateSalt();
        this.passwordHash = hashPassword(password, salt);
    }
}
```

## 6. Wartbarkeits-Metriken

### Dokumentationsgrad
```java
// ❌ Unzureichende Dokumentation
public void process() { }

// ✅ Aussagekräftige Dokumentation
/**
 * Verarbeitet eine Bestellung und aktualisiert den Bestand.
 * 
 * @throws InsufficientStockException wenn nicht genügend Lagerbestand
 * @throws PaymentFailedException bei Zahlungsproblemen
 * @return OrderConfirmation mit Tracking-Nummer
 */
@Transactional
public OrderConfirmation processOrder(Order order) { }
```

### Technical Debt Ratio
- Maximal 5% der Code-Basis sollte als "debt" markiert sein
- Schulden müssen dokumentiert und terminiert sein

```java
// ❌ Undokumentierte technische Schulden
// TODO: Refactoring needed

// ✅ Dokumentierte technische Schulden
/**
 * @deprecated This implementation is temporary and should be replaced
 * with a proper caching solution by Q2 2024 (JIRA-1234)
 */
@Deprecated
public class TemporaryCache { }
```

[Fortsetzung folgt...]

Soll ich mit weiteren spezifischen Metriken und Beispielen fortfahren?