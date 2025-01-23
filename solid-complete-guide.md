# SOLID Prinzipien - Komplettguide mit Beispielen

## Schlechtes Beispiel (Verstöße gegen alle SOLID-Prinzipien)

```java
public class OrderProcessor {
    private MySQLDatabase database;
    private EmailSender emailSender;
    private PDFInvoiceGenerator invoiceGenerator;
    
    public OrderProcessor() {
        this.database = new MySQLDatabase();  // Verletzt DIP
        this.emailSender = new EmailSender();
        this.invoiceGenerator = new PDFInvoiceGenerator();
    }
    
    // Verletzt SRP - Klasse hat zu viele Verantwortlichkeiten
    public void processOrder(Order order) {
        // Validierung
        if (order.getCustomerId() == null || order.getItems().isEmpty()) {
            throw new IllegalArgumentException("Invalid order");
        }
        
        // Preisberechnung
        double total = 0;
        for (OrderItem item : order.getItems()) {
            if (item.getType().equals("BOOK")) {
                total += item.getPrice() * 0.9; // 10% Rabatt auf Bücher
            } else if (item.getType().equals("ELECTRONICS")) {
                total += item.getPrice() * 1.2; // 20% Aufschlag auf Elektronik
            } else {
                total += item.getPrice();
            }
        }
        
        // Speichern in Datenbank
        try {
            database.connect("jdbc:mysql://localhost:3306/shop");
            database.executeUpdate("INSERT INTO orders...");
        } catch (Exception e) {
            e.printStackTrace();
        }
        
        // Rechnung generieren
        String invoice = invoiceGenerator.generatePDF(order, total);
        
        // Email senden
        emailSender.sendOrderConfirmation("Order " + order.getId(), 
                                        order.getCustomerEmail(), 
                                        invoice);
    }
    
    // Verletzt OCP - Muss für neue Zahlungsmethoden geändert werden
    public void processPayment(Order order, String paymentMethod) {
        if (paymentMethod.equals("CREDIT_CARD")) {
            processCreditCardPayment(order);
        } else if (paymentMethod.equals("PAYPAL")) {
            processPayPalPayment(order);
        } else if (paymentMethod.equals("BANK_TRANSFER")) {
            processBankTransferPayment(order);
        }
    }
    
    // Verletzt LSP - Ändert Basisverhalten
    class PremiumOrder extends Order {
        @Override
        public void addItem(OrderItem item) {
            if (getItems().size() >= 100) {
                throw new RuntimeException("Premium orders cannot have more than 100 items");
            }
            super.addItem(item);
        }
    }
    
    // Verletzt ISP - Interface hat zu viele Methoden
    interface OrderHandler {
        void validateOrder(Order order);
        void calculatePrice(Order order);
        void saveOrder(Order order);
        void generateInvoice(Order order);
        void sendConfirmation(Order order);
        void processPayment(Order order);
        void updateInventory(Order order);
        void generateReports(Order order);
        void archiveOrder(Order order);
    }
}
```

## Analyse der SOLID-Verstöße

### 1. Single Responsibility Principle (SRP)
- **Problem**: Die OrderProcessor-Klasse übernimmt zu viele Aufgaben
  - Validierung von Bestellungen
  - Preisberechnung
  - Datenbankoperationen
  - PDF-Generierung
  - E-Mail-Versand
- **Folge**: Änderungen an einer Funktionalität erfordern Änderungen an der gesamten Klasse
- **Lösung**: Aufteilung in spezialisierte Klassen

```java
class BestellungsValidator {
    public boolean validiere(Bestellung bestellung) {
        // Validierungslogik
    }
}

class PreisRechner {
    public double berechnePreis(Bestellung bestellung) {
        // Preisberechnungslogik
    }
}

class BestellungsRepository {
    public void speichere(Bestellung bestellung) {
        // Datenbanklogik
    }
}
```

### 2. Open/Closed Principle (OCP)
- **Problem**: Zahlungsmethoden sind hart kodiert
- **Folge**: Code-Änderungen für jede neue Zahlungsmethode nötig
- **Lösung**: Strategie-Muster für Zahlungsmethoden

```java
interface ZahlungsProcessor {
    void verarbeiteZahlung(Bestellung bestellung);
}

class KreditkartenProcessor implements ZahlungsProcessor {
    @Override
    public void verarbeiteZahlung(Bestellung bestellung) {
        // Kreditkarten-spezifische Logik
    }
}

class PayPalProcessor implements ZahlungsProcessor {
    @Override
    public void verarbeiteZahlung(Bestellung bestellung) {
        // PayPal-spezifische Logik
    }
}
```

### 3. Liskov Substitution Principle (LSP)
- **Problem**: PremiumOrder verletzt das Grundverhalten von Order
- **Folge**: Nicht-austauschbare Unterklassen
- **Lösung**: Komposition statt Vererbung

```java
interface BestellungsLimits {
    boolean kannArtikelHinzufuegen(Bestellung bestellung);
}

class StandardLimits implements BestellungsLimits {
    @Override
    public boolean kannArtikelHinzufuegen(Bestellung bestellung) {
        return true;
    }
}

class PremiumLimits implements BestellungsLimits {
    @Override
    public boolean kannArtikelHinzufuegen(Bestellung bestellung) {
        return bestellung.getArtikel().size() < 100;
    }
}

class Bestellung {
    private BestellungsLimits limits;
    
    public void addItem(BestellungsArtikel artikel) {
        if (limits.kannArtikelHinzufuegen(this)) {
            items.add(artikel);
        }
    }
}
```

### 4. Interface Segregation Principle (ISP)
- **Problem**: Überladenes OrderHandler Interface
- **Folge**: Unnötige Methodenimplementierungen
- **Lösung**: Spezialisierte Interfaces

```java
interface BestellungsValidator {
    boolean validiere(Bestellung bestellung);
}

interface PreisBerechner {
    double berechnePreis(Bestellung bestellung);
}

interface BestellungsSpeicher {
    void speichere(Bestellung bestellung);
}

interface Benachrichtigung {
    void sendeBestaetigung(Bestellung bestellung);
}
```

### 5. Dependency Inversion Principle (DIP)
- **Problem**: Direkte Abhängigkeiten zu konkreten Implementierungen
- **Folge**: Schlechte Testbarkeit und hohe Kopplung
- **Lösung**: Dependency Injection und Interfaces

```java
interface Datenbank {
    void speichere(Bestellung bestellung);
}

interface EmailService {
    void sendeEmail(String empfaenger, String betreff, String inhalt);
}

class BestellungsVerarbeiter {
    private final Datenbank datenbank;
    private final EmailService emailService;
    
    // Dependency Injection über Konstruktor
    public BestellungsVerarbeiter(Datenbank datenbank, EmailService emailService) {
        this.datenbank = datenbank;
        this.emailService = emailService;
    }
    
    public void verarbeiteBestellung(Bestellung bestellung) {
        // Nutzung der Interfaces statt konkreter Implementierungen
        datenbank.speichere(bestellung);
        emailService.sendeEmail(bestellung.getEmail(), "Bestellung", "Details...");
    }
}
```

## Refactored Clean Code Version

```java
// Hauptklasse - Nur noch Orchestrierung
class BestellungsVerarbeiter {
    private final BestellungsValidator validator;
    private final PreisBerechner preisRechner;
    private final BestellungsSpeicher speicher;
    private final RechnungsGenerator rechnungsGenerator;
    private final Benachrichtigung benachrichtigung;
    private final ZahlungsProcessor zahlungsProcessor;
    
    public BestellungsVerarbeiter(
            BestellungsValidator validator,
            PreisBerechner preisRechner,
            BestellungsSpeicher speicher,
            RechnungsGenerator rechnungsGenerator,
            Benachrichtigung benachrichtigung,
            ZahlungsProcessor zahlungsProcessor) {
        this.validator = validator;
        this.preisRechner = preisRechner;
        this.speicher = speicher;
        this.rechnungsGenerator = rechnungsGenerator;
        this.benachrichtigung = benachrichtigung;
        this.zahlungsProcessor = zahlungsProcessor;
    }
    
    public void verarbeiteBestellung(Bestellung bestellung) {
        validator.validiere(bestellung);
        double gesamtpreis = preisRechner.berechnePreis(bestellung);
        speicher.speichere(bestellung);
        String rechnung = rechnungsGenerator.generiere(bestellung, gesamtpreis);
        benachrichtigung.sendeBestaetigung(bestellung);
        zahlungsProcessor.verarbeiteZahlung(bestellung);
    }
}
```

## Vorteile der SOLID-konformen Implementierung

1. **Bessere Wartbarkeit**
   - Klare Verantwortlichkeiten
   - Lokalisierte Änderungen
   - Übersichtlichere Codestruktur

2. **Erhöhte Testbarkeit**
   - Isolierte Komponenten
   - Mockbare Abhängigkeiten
   - Kleinere Testeinheiten

3. **Verbesserte Erweiterbarkeit**
   - Neue Funktionen ohne Codeänderungen
   - Pluggable Komponenten
   - Flexible Konfiguration

4. **Reduzierte Kopplung**
   - Unabhängige Komponenten
   - Austauschbare Implementierungen
   - Bessere Skalierbarkeit

## Best Practices für SOLID

1. **Regelmäßige Code-Reviews**
   - Früherkennung von Verstößen
   - Gemeinsames Verständnis
   - Kontinuierliche Verbesserung

2. **Automatisierte Tests**
   - Unit Tests für Komponenten
   - Integrationstests für Zusammenspiel
   - Schnelles Feedback

3. **Dokumentation**
   - Klare Schnittstellenbeschreibungen
   - Dokumentierte Abhängigkeiten
   - Beispiele für Verwendung

4. **Continuous Refactoring**
   - Regelmäßige Überarbeitung
   - Schrittweise Verbesserungen
   - Technische Schuld vermeiden