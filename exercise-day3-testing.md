# Übung: Testbare Architektur

## Ausgangssituation: Online-Shop Payment Service
```java
public class PaymentProcessor {
    private static final String API_KEY = "sk_test_123456";
    private static PaymentProcessor instance;
    
    public static PaymentProcessor getInstance() {
        if (instance == null) {
            instance = new PaymentProcessor();
        }
        return instance;
    }

    public boolean processPayment(String creditCardNumber, double amount) {
        // Direct API call to payment provider
        PaymentProvider provider = new PaymentProvider(API_KEY);
        PaymentResult result = provider.charge(creditCardNumber, amount);
        
        if (result.isSuccess()) {
            Database.getInstance().save(new Payment(amount, new Date()));
            EmailService.getInstance().sendReceipt(creditCardNumber, amount);
            return true;
        }
        return false;
    }
}
```

## Aufgaben

### 1. Architektur verbessern (30 Minuten)
1. Dependency Injection einführen
2. Interfaces für externe Services definieren
3. Value Objects für Geschäftsobjekte erstellen

### 2. Tests implementieren (45 Minuten)

[Fortsetzung folgt...]

Soll ich fortfahren mit dem Rest der Testübung und den weiteren Übungen?