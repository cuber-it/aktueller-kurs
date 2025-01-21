# Clean Code Workshop Handouts

## Tag 1 - Grundlagen

### 1. Clean Code Prinzipien
```java
// Code-Beispiele für jeden Punkt
// SCHLECHT - Verletzt mehrere Prinzipien
void process(List l) {
    for(int i=0;i<l.size();i++) {
        Object o = l.get(i);
        // Verarbeitung...
    }
}

// GUT - Folgt Clean Code Prinzipien
void processOrders(List<Order> orders) {
    orders.forEach(order -> {
        validateOrder(order);
        calculateTotal(order);
    });
}
```

### 2. Namensgebung
- Sprechende Namen verwenden
- Konsistente Terminologie
- Domänenspezifische Begriffe
- Konventionen der Sprache folgen

#### Beispiele:
```java
// Variablen
userAccount   // statt ua
isActive      // statt flag
orderItems    // statt list

// Methoden
calculateTotal()      // statt calc()
validateAddress()     // statt checkAddr()
retrieveUserProfile() // statt getData()

// Klassen
OrderProcessor    // statt Processor
PaymentGateway   // statt PaymentManager
EmailValidator   // statt Validator
```

### 3. Kommentare
- Wann sind Kommentare sinnvoll?
- Wann sind sie überflüssig?
- Alternativen zu Kommentaren

```java
// SCHLECHT - Überflüssiger Kommentar
// Erhöht den Zähler um 1
counter++;

// GUT - Erklärt das Warum
// Erhöhung um 1 gemäß ISO-27001 Audit-Anforderungen
auditCounter++;
```

## Tag 2 - Techniken

### 1. Value Objects
```java
public class Money {
    private final BigDecimal amount;
    private final Currency currency;

    public Money(BigDecimal amount, Currency currency) {
        this.amount = requireNonNull(amount);
        this.currency = requireNonNull(currency);
    }

    public Money add(Money other) {
        requireSameCurrency(other);
        return new Money(amount.add(other.amount), currency);
    }
}
```

### 2. Clean Functions
#### Regeln:
1. Klein und fokussiert
2. Eine Aufgabe
3. Eine Abstraktionsebene
4. Wenige Parameter
5. Keine Seiteneffekte

```java
// SCHLECHT
void processSale(Sale sale) {
    // 100 Zeilen mit verschiedenen Aufgaben
}

// GUT
void processSale(Sale sale) {
    validateSale(sale);
    calculateTotals(sale);
    applyDiscounts(sale);
    saveSale(sale);
    notifyCustomer(sale);
}
```

### 3. Error Handling
```java
// Exceptions richtig nutzen
public class BusinessException extends RuntimeException {
    private final ErrorCode code;
    
    public BusinessException(ErrorCode code, String message) {
        super(message);
        this.code = code;
    }
}

// Exception Handling
try {
    processOrder(order);
} catch (ValidationException e) {
    logValidationError(e);
    throw new BusinessException(ErrorCode.INVALID_ORDER, e.getMessage());
} catch (PaymentException e) {
    logPaymentError(e);
    throw new BusinessException(ErrorCode.PAYMENT_FAILED, e.getMessage());
}
```

## Tag 3 - Architektur & Praxis

### 1. Clean Architecture
```
[Entities] <- [Use Cases] <- [Interface Adapters] <- [Frameworks]

Beispiel:
[Order] <- [OrderService] <- [OrderController] <- [Web Framework]
```

#### Schichten:
1. Entities (Domain Models)
2. Use Cases (Application Services)
3. Interface Adapters (Controllers, Repositories)
4. Frameworks & Drivers (UI, DB, External Services)

### 2. Testing Best Practices
```java
class OrderServiceTest {
    @Test
    void shouldCalculateOrderTotal() {
        // Arrange
        Order order = new OrderBuilder()
            .withProducts(List.of(
                new Product("Book", Money.of(29.99)),
                new Product("DVD", Money.of(19.99))
            ))
            .build();

        // Act
        Money total = order.calculateTotal();

        // Assert
        assertEquals(Money.of(49.98), total);
    }
}
```

### 3. Refactoring Patterns
```java
// Extract Method
// VORHER
void processOrder() {
    // 50 Zeilen Code
}

// NACHHER
void processOrder() {
    validateOrder();
    updateInventory();
    notifyCustomer();
}

// Replace Conditional with Polymorphism
// VORHER
if (employee instanceof Manager) {
    bonus = salary * 0.2;
} else if (employee instanceof Developer) {
    bonus = salary * 0.1;
}

// NACHHER
interface Employee {
    Money calculateBonus();
}

class Manager implements Employee {
    public Money calculateBonus() {
        return salary.multiply(0.2);
    }
}
```

### 4. Performance Optimierung
```java
// Datenstrukturen richtig wählen
Map<String, User> usersByEmail = new HashMap<>();  // O(1) Zugriff
Set<String> uniqueTokens = new HashSet<>();        // Keine Duplikate

// Ressourcen richtig verwalten
try (Connection conn = dataSource.getConnection()) {
    // Datenbankoperationen
}
```

### 5. Checkliste für Code Reviews
- [ ] Folgt der Code den Clean Code Prinzipien?
- [ ] Sind die Tests aussagekräftig?
- [ ] Ist die Dokumentation aktuell?
- [ ] Gibt es potenzielle Performance-Probleme?
- [ ] Sind Sicherheitsaspekte berücksichtigt?
- [ ] Ist der Code wartbar?

### 6. Best Practices für den Alltag
1. Boy Scout Rule: Leave the code better than you found it
2. Single Responsibility: Eine Klasse, eine Aufgabe
3. DRY: Don't Repeat Yourself
4. KISS: Keep It Simple, Stupid
5. YAGNI: You Ain't Gonna Need It
6. Fail Fast: Fehler früh erkennen und behandeln

```java
// Beispiel für guten alltäglichen Code
public class OrderProcessor {
    private final OrderRepository repository;
    private final OrderValidator validator;
    private final CustomerNotifier notifier;

    public OrderResult processOrder(Order order) {
        validator.validate(order);
        Order savedOrder = repository.save(order);
        notifier.notifyCustomer(savedOrder);
        return OrderResult.success(savedOrder);
    }
}
```

