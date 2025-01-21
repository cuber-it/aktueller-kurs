# Trainer-Handreichung: Tag 3 - Architektur & Praxis

## Vorbereitung
- Komplexes Beispielprojekt für Abschlussübung bereitstellen
- Test-Frameworks vorbereiten
- SOLID-Beispiele testen
- Feedback-Bögen ausdrucken

## 09:00-09:30 - Recap Tag 2

### Durchführung
1. Blitzlicht-Runde
   - Was war die wichtigste Erkenntnis?
   - Wo gibt es noch Fragen?
2. Code-Review der Hausaufgaben (falls vergeben)

### Quick Check
```java
// Teilnehmer sollen SOLID-Verstöße finden
public class ReportGenerator {
    private MySQLDatabase db;
    private PDFWriter writer;
    
    public void createAndSendReport() {
        // Violation: Single Responsibility, Dependencies
    }
}
```

## 09:30-10:30 - Kopplung & Hierarchien

### Lose Kopplung (Kapitel 17)

1. Probleme erkennen
   ```java
   // Stark gekoppelt
   class OrderProcessor {
       private MySQLDatabase db = new MySQLDatabase();
       private EmailService emailService = new EmailService();
       private PDFGenerator pdfGenerator = new PDFGenerator();
   }
   ```

2. Dependency Injection
   ```java
   // Besser
   class OrderProcessor {
       private final Database db;
       private final NotificationService notifier;
       private final DocumentGenerator docGen;
       
       public OrderProcessor(Database db, 
                           NotificationService notifier,
                           DocumentGenerator docGen) {
           this.db = db;
           this.notifier = notifier;
           this.docGen = docGen;
       }
   }
   ```

### Hierarchien optimieren (Kapitel 19)

1. Vererbung vs. Komposition
   - Wann ist was angebracht?
   - Praktische Beispiele
   - Refactoring-Strategien

2. Code-Beispiele
   ```java
   // Problematische Vererbung
   class Animal {
       void fly() { }
       void swim() { }
   }
   class Dog extends Animal { } // Problem: Dogs can't fly
   
   // Bessere Komposition
   interface Flyable {
       void fly();
   }
   interface Swimmable {
       void swim();
   }
   ```

## 10:30-10:45 - Pause

## 10:45-12:00 - Testing & Clean Code

### Testbare Architektur (Kapitel 20)

1. Prinzipien
   - Dependency Injection
   - Interface-basiertes Design
   - Single Responsibility
   - Testbare Größe der Units

2. Praktische Beispiele
   ```java
   // Schwer testbar
   class PaymentProcessor {
       public boolean processPayment(double amount) {
           PayPalAPI paypal = new PayPalAPI();
           return paypal.sendPayment(amount);
       }
   }
   
   // Gut testbar
   class PaymentProcessor {
       private final PaymentGateway gateway;
       
       public PaymentProcessor(PaymentGateway gateway) {
           this.gateway = gateway;
       }
       
       public boolean processPayment(Money amount) {
           return gateway.sendPayment(amount);
       }
   }
   ```

3. Unit-Test Workshop (30 min)
   - Test-First Entwicklung
   - Mocking vs. echte Objekte
   - Test-Doubles richtig einsetzen

[Fortsetzung mit Nachmittagsprogramm folgt...]

