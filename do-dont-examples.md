# Clean Code Do's and Don'ts

## 1. Namensgebung

### ❌ DON'T
```java
class Calc {
    private List<Obj> l = new ArrayList<>();
    
    public double p(Obj o) {
        double t = 0;
        for(Obj i : l) {
            t += i.getVal() * o.getQ();
        }
        return t;
    }
}
```

### ✅ DO
```java
class PriceCalculator {
    private List<OrderItem> items = new ArrayList<>();
    
    public Money calculateTotal(OrderItem newItem) {
        return items.stream()
            .map(item -> item.getPrice().multiply(newItem.getQuantity()))
            .reduce(Money.ZERO, Money::add);
    }
}
```

## 2. Methoden

### ❌ DON'T
```java
public void doStuff(String input) {
    // Methode macht zu viel
    validateInput(input);
    processData(input);
    saveToDatabase(input);
    sendEmail("admin@company.com", "Processed: " + input);
    updateCache();
    logActivity("stuff done");
}
```

### ✅ DO
```java
public class OrderProcessor {
    private final EmailService emailService;
    private final OrderRepository repository;

    public OrderResult processOrder(Order order) {
        validateOrder(order);
        Order processedOrder = applyBusinessRules(order);
        Order savedOrder = repository.save(processedOrder);
        emailService.sendConfirmation(savedOrder);
        return OrderResult.success(savedOrder);
    }
}
```

## 3. Fehlerbehandlung

### ❌ DON'T
```java
public void processUser(String userData) {
    try {
        // Alles in einem try-catch Block
        User user = parseUser(userData);
        validateUser(user);
        saveUser(user);
        sendEmail(user);
    } catch(Exception e) {
        // Generischer Catch
        System.out.println("Error: " + e.getMessage());
        return;
    }
}
```

### ✅ DO
```java
public void processUser(String userData) {
    try {
        User user = userParser.parse(userData);
        userValidator.validate(user);
        userRepository.save(user);
        notificationService.notifyUserCreated(user);
    } catch (UserValidationException e) {
        log.warn("Invalid user data: {}", e.getMessage());
        throw new BusinessException("User validation failed", e);
    } catch (PersistenceException e) {
        log.error("Database error: {}", e.getMessage());
        throw new BusinessException("Could not save user", e);
    }
}
```

## 4. Klassen-Design

### ❌ DON'T
```java
// God Class
class UserManager {
    private Connection dbConnection;
    private EmailServer emailServer;
    private PDFGenerator pdfGenerator;
    private PaymentProcessor paymentProcessor;
    
    public void createUser() { /* ... */ }
    public void sendEmail() { /* ... */ }
    public void generateReport() { /* ... */ }
    public void processPayment() { /* ... */ }
    public void validateAddress() { /* ... */ }
    public void updateDatabase() { /* ... */ }
}
```

### ✅ DO
```java
class UserService {
    private final UserRepository repository;
    private final UserValidator validator;

    public User createUser(UserCreationRequest request) {
        validator.validate(request);
        return repository.save(new User(request));
    }
}

class UserNotificationService {
    private final EmailService emailService;

    public void notifyUserCreated(User user) {
        emailService.sendWelcomeEmail(user);
    }
}
```

## 5. Primitive Obsession

### ❌ DON'T
```java
class Order {
    private String email;
    private double amount;
    private String status;
    
    public boolean isValidOrder() {
        return email != null && 
               email.contains("@") &&
               amount > 0 &&
               (status.equals("NEW") || status.equals("PROCESSED"));
    }
}
```

### ✅ DO
```java
class Order {
    private final EmailAddress email;
    private final Money amount;
    private final OrderStatus status;
    
    public Order(EmailAddress email, Money amount, OrderStatus status) {
        this.email = requireNonNull(email);
        this.amount = requireNonNull(amount);
        this.status = requireNonNull(status);
    }
    
    public boolean isValidOrder() {
        return amount.isPositive() && status.canBeProcessed();
    }
}
```

## 6. Bedingungen und Verzweigungen

### ❌ DON'T
```java
if (user != null) {
    if (user.getAge() >= 18) {
        if (user.getCountry().equals("DE")) {
            if (user.hasValidLicense()) {
                if (car.isAvailable()) {
                    // Geschachtelte Hölle
                    rentCar(user, car);
                }
            }
        }
    }
}
```

### ✅ DO
```java
public void rentCar(User user, Car car) {
    if (!user.isEligibleToRent()) {
        throw new UserNotEligibleException("User cannot rent cars");
    }
    
    if (!car.isAvailableForRent()) {
        throw new CarNotAvailableException("Car is not available");
    }
    
    RentalAgreement agreement = RentalAgreement.create(user, car);
    rentalRepository.save(agreement);
}
```

## 7. Kommentare

### ❌ DON'T
```java
// Get user from database
User user = userRepo.findById(id);

// Check if user exists
if (user != null) {
    // Update user name
    user.setName(newName);
    // Save user to database
    userRepo.save(user);
}
```

### ✅ DO
```java
/**
 * Berechnet die Versicherungsprämie basierend auf Alter und Risikofaktoren.
 * Formel gemäß Versicherungsrichtlinie VP-2024/A3.
 */
public Money calculatePremium(Age age, RiskFactors factors) {
    requireNonNull(age, "Age is required");
    requireNonNull(factors, "Risk factors are required");
    
    return basePremium
        .multiply(age.getRiskMultiplier())
        .multiply(factors.getCombinedRiskFactor());
}
```

## 8. Tests

### ❌ DON'T
```java
@Test
void test1() {
    var calc = new Calculator();
    assertEquals(4, calc.add(2, 2));
}

@Test
void test2() {
    var calc = new Calculator();
    var result = calc.add(2, 2);
    assertTrue(result > 0);
    assertEquals(4, result);
}
```

### ✅ DO
```java
class CalculatorTest {
    private Calculator calculator;
    
    @BeforeEach
    void setUp() {
        calculator = new Calculator();
    }
    
    @Test
    void shouldAddPositiveNumbers() {
        assertEquals(
            Money.of(4), 
            calculator.add(Money.of(2), Money.of(2))
        );
    }
    
    @Test
    void shouldThrowForNegativeResults() {
        assertThrows(
            NegativeAmountException.class,
            () -> calculator.subtract(Money.of(1), Money.of(2))
        );
    }
}
```

## 9. Dependency Injection

### ❌ DON'T
```java
class OrderService {
    private final Database database = new MySQLDatabase();
    private final EmailSender emailSender = new SmtpEmailSender();
    
    public void processOrder(Order order) {
        database.save(order);
        emailSender.send("New order: " + order.getId());
    }
}
```

### ✅ DO
```java
class OrderService {
    private final OrderRepository orderRepository;
    private final NotificationService notificationService;
    
    @Inject
    public OrderService(
            OrderRepository orderRepository,
            NotificationService notificationService) {
        this.orderRepository = requireNonNull(orderRepository);
        this.notificationService = requireNonNull(notificationService);
    }
    
    public void processOrder(Order order) {
        Order savedOrder = orderRepository.save(order);
        notificationService.notifyOrderCreated(savedOrder);
    }
}
```

## 10. Validierung

### ❌ DON'T
```java
public void createUser(String name, String email, int age) {
    if (name != null && !name.isEmpty() && email != null && 
        email.contains("@") && age > 0) {
        User user = new User();
        user.setName(name);
        user.setEmail(email);
        user.setAge(age);
        userRepo.save(user);
    } else {
        throw new RuntimeException("Invalid input");
    }
}
```

### ✅ DO
```java
public User createUser(UserCreationRequest request) {
    validateUserCreationRequest(request);
    
    User user = new User(
        new Username(request.getName()),
        new EmailAddress(request.getEmail()),
        new Age(request.getAge())
    );
    
    return userRepository.save(user);
}

private void validateUserCreationRequest(UserCreationRequest request) {
    List<String> violations = new ArrayList<>();
    
    if (!request.hasValidName()) {
        violations.add("Name must be between 2 and 100 characters");
    }
    
    if (!request.hasValidEmail()) {
        violations.add("Email must be a valid email address");
    }
    
    if (!request.hasValidAge()) {
        violations.add("Age must be between 18 and 150");
    }
    
    if (!violations.isEmpty()) {
        throw new ValidationException("Invalid user data", violations);
    }
}
```

