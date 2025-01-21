# Übung: Primitive Obsession bekämpfen

## Ausgangssituation
```java
public class UserRegistration {
    private String email;
    private String password;
    private String phoneNumber;
    private int age;
    private String postalCode;
    private double accountBalance;
    
    public boolean register(String email, String password, String phone, 
                          int age, String postal, double balance) {
        if (!email.contains("@") || email.length() < 5) return false;
        if (password.length() < 8) return false;
        if (!phone.matches("\\d{10}")) return false;
        if (age < 18 || age > 120) return false;
        if (!postal.matches("\\d{5}")) return false;
        if (balance < 0) return false;
        
        this.email = email;
        this.password = password;
        this.phoneNumber = phone;
        this.age = age;
        this.postalCode = postal;
        this.accountBalance = balance;
        return true;
    }
    
    public void updateBalance(double amount) {
        if (accountBalance + amount >= 0) {
            accountBalance += amount;
        }
    }
}
```

## Aufgaben

### 1. Value Objects erstellen (30 Minuten)
Erstellen Sie Value Objects für:
- EmailAddress
- Password
- PhoneNumber
- Age
- PostalCode
- Money

Beispiel für einen Value Object:
```java
public class EmailAddress {
    private final String value;
    
    public EmailAddress(String email) {
        if (!isValid(email)) {
            throw new IllegalArgumentException("Invalid email format");
        }
        this.value = email;
    }
    
    private boolean isValid(String email) {
        return email != null && email.contains("@") && email.length() >= 5;
    }
    
    @Override
    public String toString() {
        return value;
    }
    
    // Equals und HashCode nicht vergessen!
}
```

### 2. Refactoring (45 Minuten)
- Ersetzen Sie alle primitiven Typen durch Ihre Value Objects
- Implementieren Sie entsprechende Validierungen
- Stellen Sie Unveränderlichkeit sicher
- Fügen Sie sinnvolle Geschäftsmethoden hinzu

### 3. Tests schreiben (30 Minuten)
```java
class EmailAddressTest {
    @Test
    void shouldCreateValidEmail() {
        EmailAddress email = new EmailAddress("test@example.com");
        assertEquals("test@example.com", email.toString());
    }
    
    @Test
    void shouldRejectInvalidEmail() {
        assertThrows(IllegalArgumentException.class, 
            () -> new EmailAddress("invalid"));
    }
}
```

## Bonus-Aufgaben
1. Implementieren Sie eine Builder-Pattern für die UserRegistration
2. Fügen Sie Serialisierung/Deserialisierung hinzu
3. Implementieren Sie Domain-spezifische Validierungen

## Hinweise für Trainer
- Auf korrekte Implementierung von equals/hashCode achten
- Unveränderlichkeit betonen
- Validierungslogik diskutieren
