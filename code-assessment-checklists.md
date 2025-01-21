# Clean Code Assessment Checklisten

## 1. Grundlegende Code-Qualität

### Namensgebung
- [ ] Sind Variablennamen aussagekräftig?
- [ ] Folgen Methodennamen einem konsistenten Verb-Nomen-Schema?
- [ ] Sind Klassennamen als Nomen formuliert?
- [ ] Werden keine Abkürzungen verwendet (außer allgemein bekannte wie ID, HTTP)?
- [ ] Spiegeln die Namen den Business-Kontext wider?
- [ ] Sind die Namen sprachlich konsistent (entweder Deutsch oder Englisch)?
- [ ] Werden keine ungarische Notation oder Präfixe verwendet?
- [ ] Sind die Namen SearchEngine-freundlich?

### Funktionen/Methoden
- [ ] Sind alle Methoden kürzer als 20 Zeilen?
- [ ] Haben Methoden maximal 3 Parameter?
- [ ] Wird das Single Responsibility Principle eingehalten?
- [ ] Gibt es keine doppelten Parameter?
- [ ] Sind die Rückgabewerte konsistent?
- [ ] Werden Exceptions sinnvoll verwendet?
- [ ] Gibt es keine Flag-Parameter?
- [ ] Ist die Abstraktionsebene konsistent?

### Klassen
- [ ] Sind Klassen kleiner als 300 Zeilen?
- [ ] Haben Klassen eine klare Verantwortlichkeit?
- [ ] Sind die Attribute private?
- [ ] Gibt es keine public static Methoden?
- [ ] Ist die Vererbungshierarchie flach (max. 2-3 Ebenen)?
- [ ] Werden Interfaces sinnvoll eingesetzt?
- [ ] Sind Abhängigkeiten explizit (Dependency Injection)?
- [ ] Gibt es keine zyklischen Abhängigkeiten?

## 2. Architektur & Design

### SOLID Prinzipien
- [ ] Single Responsibility Principle
  - [ ] Klasse hat nur einen Grund sich zu ändern
  - [ ] Funktionalitäten sind klar getrennt
  - [ ] Keine "God Classes"

- [ ] Open/Closed Principle
  - [ ] Erweiterungen ohne Codeänderungen möglich
  - [ ] Verwendung von Abstraktion und Polymorphie
  - [ ] Konfigurierbarkeit statt Hardcoding

- [ ] Liskov Substitution Principle
  - [ ] Unterklassen sind austauschbar
  - [ ] Keine Verletzung der Vorbedingungen
  - [ ] Einhaltung der Nachbedingungen

- [ ] Interface Segregation
  - [ ] Kleine, spezifische Interfaces
  - [ ] Keine "fat interfaces"
  - [ ] Klienten-spezifische Schnittstellen

- [ ] Dependency Inversion
  - [ ] Abhängigkeit von Abstraktionen
  - [ ] Keine direkten Implementierungsabhängigkeiten
  - [ ] Verwendung von Dependency Injection

### Architekturmuster
- [ ] Klare Schichtenarchitektur
  - [ ] Präsentationsschicht
  - [ ] Geschäftslogikschicht
  - [ ] Datenzugriffsschicht
  
- [ ] Saubere Abhängigkeiten
  - [ ] Abhängigkeiten nur nach innen
  - [ ] Keine Layer-Übersprünge
  - [ ] Verwendung von Interfaces zwischen Schichten

## 3. Code-Hygiene

### Kommentare
- [ ] Keine redundanten Kommentare
- [ ] JavaDoc für öffentliche API
- [ ] Keine auskommentierten Code-Blöcke
- [ ] Dokumentation von Geschäftsregeln
- [ ] TODO-Kommentare mit Ticket-Referenz

### Formatierung
- [ ] Konsistente Einrückung
- [ ] Maximale Zeilenlänge eingehalten
- [ ] Leerzeilen zur Gruppierung
- [ ] Klammern-Style einheitlich
- [ ] Keine übermäßigen Leerzeilen

### Code-Duplikate
- [ ] Keine kopierten Code-Blöcke
- [ ] Ähnliche Logik abstrahiert
- [ ] Wiederverwendung durch Vererbung/Komposition
- [ ] Keine duplizierten String-Literale
- [ ] Keine kopierten Validierungen

## 4. Technische Exzellenz

### Performance
- [ ] Effiziente Datenstrukturen
- [ ] Vermeidung von N+1 Queries
- [ ] Sinnvolle Indexierung
- [ ] Caching-Strategie
- [ ] Ressourcen-Freigabe
- [ ] Keine unnötigen Objekterzeugungen
- [ ] Batch-Verarbeitung wo sinnvoll

### Sicherheit
- [ ] Input-Validierung
- [ ] SQL-Injection Prevention
- [ ] XSS-Schutz
- [ ] CSRF-Schutz
- [ ] Sichere Passwort-Handhabung
- [ ] Logging sensitiver Daten
- [ ] Zugriffskontrolle

### Testbarkeit
- [ ] Unit Tests vorhanden
- [ ] Testabdeckung > 80%
- [ ] Mocks/Stubs sinnvoll eingesetzt
- [ ] Integrationstests
- [ ] Testbare Architektur
- [ ] Keine statischen Abhängigkeiten
- [ ] Deterministische Tests

## 5. Domänen-Design

### Business Logic
- [ ] Domänenmodell abgebildet
- [ ] Geschäftsregeln klar erkennbar
- [ ] Fachliche Begriffe verwendet
- [ ] Validierungen vollständig
- [ ] Status-Übergänge definiert

### Value Objects
- [ ] Unveränderliche Objekte
- [ ] Validierung bei Erzeugung
- [ ] Semantische Gleichheit
- [ ] Keine primitiven Obsessionen
- [ ] Type Safety

## 6. Technische Schulden

### Code Smells
- [ ] Keine Feature Envy
- [ ] Keine Data Classes
- [ ] Keine Message Chains
- [ ] Keine Switch Statements
- [ ] Keine temporären Felder

### Wartbarkeit
- [ ] Verständliche Strukturen
- [ ] Dokumentierte Abhängigkeiten
- [ ] Keine veralteten APIs
- [ ] Aktuelle Bibliotheken
- [ ] Keine deprecated Features

## 7. DevOps & Build

### Build System
- [ ] Automatisierter Build
- [ ] Reproduzierbare Builds
- [ ] Dependency Management
- [ ] Version Control
- [ ] CI/CD Pipeline

### Monitoring & Logging
- [ ] Strukturiertes Logging
- [ ] Performance Metrics
- [ ] Health Checks
- [ ] Error Tracking
- [ ] Business Metrics

## 8. Review Prozess

### Vor dem Review
- [ ] Code kompiliert
- [ ] Tests laufen
- [ ] Linter-Checks bestanden
- [ ] Dokumentation aktualisiert
- [ ] Changelog gepflegt

### Während des Reviews
- [ ] Architektur-Konformität
- [ ] Code-Style-Guidelines
- [ ] Testabdeckung
- [ ] Performance-Implikationen
- [ ] Sicherheitsaspekte

### Nach dem Review
- [ ] Feedback eingearbeitet
- [ ] Tests angepasst
- [ ] Dokumentation finalisiert
- [ ] Code Squad informiert
- [ ] Deployment geplant

## 9. Spezifische Aspekte

### API Design
- [ ] RESTful Prinzipien
- [ ] Versionierung
- [ ] Konsistente Fehlerbehandlung
- [ ] API Dokumentation
- [ ] Rate Limiting

### Datenbank
- [ ] Normalisierung
- [ ] Indizes
- [ ] Constraints
- [ ] Migrations
- [ ] Backup-Strategie

### Concurrency
- [ ] Thread Safety
- [ ] Deadlock Prevention
- [ ] Resource Locking
- [ ] Transaction Management
- [ ] State Management

### Security
- [ ] Authentication
- [ ] Authorization
- [ ] Secure Communication
- [ ] Data Protection
- [ ] Audit Logging

