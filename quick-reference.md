# Clean Code Quick Reference Cards

## 1. Namensgebung Cheat Sheet

### Variablen
```java
// SCHLECHT                     // GUT
int d;                         int daysSinceStart;
User u;                        User activeUser;
List<String> l;                List<String> userNames;
boolean flag;                  boolean isActive;
```

### Funktionen
```java
// SCHLECHT                     // GUT
getData()                      retrieveUserProfile()
process()                      calculateMonthlyRevenue()
check()                        validateEmailAddress()
save()                        persistCustomerData()
```

### Klassen
```java
// SCHLECHT                     // GUT
Data                          CustomerProfile
Processor                     PaymentProcessor
Manager                       OrderFulfillment
Helper                        EmailValidator
```

## 2. SOLID Prinzipien Referenz

### Single Responsibility
```java
// SCHLECHT
class OrderProcessor {
    void processOrder() { /* ... */ }
    void sendEmail() { /* ... */ }
    void updateDatabase() { /* ... */ }
}

// GUT
class OrderProcessor {
    void processOrder() { /* ... */ }
}
class OrderNotifier {
    void sendEmail() { /* ... */ }
}
class OrderRepository {
    void save() { /* ... */ }
}
```

### Open/Closed
```java
// SCHLECHT
if (shape.type == "circle") { ... }
else if (shape.type == "square") { ... }

// GUT
interface Shape {
    double calculateArea();
}
class Circle implements Shape { ... }
class Square implements Shape { ... }
```

## 3. Code Smells Erkennungsmerkmale

### Long Method
- Mehr als 20 Zeilen
- Mehrere Abstraktionsebenen
- Viele verschachtelte if/for
- Viele lokale Variablen

### Feature Envy
```java
// SCHLECHT
class Order {
    private Customer customer;
    
    void process() {
        if (customer.getStatus().equals("PREMIUM") &&
            customer.getCreditLimit() > 1000 &&
            customer.getLastOrderDate()...)) {
            // ...
        }
    }
}

// GUT
class Customer {
    boolean canPlaceOrder(Money amount) {
        return isPremium() && 
               hasSufficientCredit(amount) &&
               isRecentlyActive();
    }
}
```

## 4. Test-Patterns

### Arrange-Act-Assert
```java
@Test
void shouldCalculateTotal() {
    // Arrange
    ShoppingCart cart = new ShoppingCart();
    cart.add(new Product("Book", 29.99));
    
    // Act
    double total = cart.calculateTotal();
    
    // Assert
    assertEquals(29.99, total);
}
```

### Given-When-Then
```java
@Test
void shouldApplyDiscount() {
    // Given
    Order order = OrderBuilder.create()
        .withItems(items)
        .withTotal(100.0)
        .build();
        
    // When
    order.applyDiscount(0.1);
    
    // Then
    assertEquals(90.0, order.getTotal());
}
```

## 5. Refactoring-Patterns

### Extract Method
```java
// VORHER
void processOrder() {
    // 20 Zeilen Code
}

// NACHHER
void processOrder() {
    validateOrder();
    calculateTotals();
    applyDiscounts();
    updateInventory();
    notifyCustomer();
}
```

### Replace Temp with Query
```java
// VORHER
double calculateTotal() {
    double basePrice = quantity * itemPrice;
    double discount = Math.max(0, quantity - 500) * itemPrice * 0.05;
    double shipping = Math.min(basePrice * 0.1, 100);
    return basePrice - discount + shipping;
}

// NACHHER
double calculateTotal() {
    return basePrice() - discount() + shipping();
}

private double basePrice() {
    return quantity * itemPrice;
}
```

## 6. Clean Architecture Übersicht

```
[UI/API] -> [Controllers] -> [Use Cases] -> [Entities]
                ↓              ↓               ↓
           [Presenters]  [Business Rules]  [Domain Model]
                ↓              ↓               ↓
         [View Models]    [Services]     [Repositories]
```

### Schichten
1. Entities (Innerster Kreis)
   - Domain Models
   - Business Rules

2. Use Cases
   - Application Services
   - Domain Services

3. Interface Adapters
   - Controllers
   - Repositories
   - Presenters

4. Frameworks & Drivers
   - UI
   - Datenbank
   - External Services

## 7. Performance Tipps

### Datenstrukturen
```java
// SCHLECHT (bei häufiger Suche)
List<User> users = new ArrayList<>();

// GUT
Set<User> uniqueUsers = new HashSet<>();
Map<String, User> usersByEmail = new HashMap<>();
```

### String-Operationen
```java
// SCHLECHT
String result = "";
for (String item : items) {
    result += item;
}

// GUT
StringBuilder result = new StringBuilder();
for (String item : items) {
    result.append(item);
}
```

## 8. Exception Handling

### Best Practices
```java
// SCHLECHT
try {
    // Viel Code
} catch (Exception e) {
    e.printStackTrace();
}

// GUT
try {
    doSpecificOperation();
} catch (SpecificException e) {
    log.error("Operation failed: {}", e.getMessage());
    throw new BusinessException("Could not process order", e);
}
```

### Exception Hierarchie
```java
public class BusinessException extends RuntimeException { }
public class ValidationException extends BusinessException { }
public class NotFoundException extends BusinessException { }
```

