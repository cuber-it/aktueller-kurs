# Clean Code Manifest für Java-Projekte

## 0. Java-Spezifische Grundsätze

### JVM-Optimierung
- Effiziente Nutzung des Garbage Collectors
- Vermeidung von Memory Leaks durch WeakReferences
- ThreadLocal nur wenn unbedingt nötig
- Beachtung der JVM Ergonomics

### Java Ecosystem
- Spring Framework Best Practices befolgen
- Reactive Programming wo sinnvoll (Project Reactor/RxJava)
- Jakarta EE Standards einhalten
- Microprofile für Microservices

### Java Language Features
- Records für DTOs
- Sealed Classes für beschränkte Hierarchien
- Pattern Matching in Switch Statements
- Text Blocks für mehrzeilige Strings

## 1. Codestruktur und Organisation

### Projektstruktur
- Einheitliche Verzeichnisstruktur nach Maven/Gradle-Standards
- Feature-basierte Packagestruktur statt technischer Schichten
- Maximale Dateigröße: 400 Zeilen
- Maximale Methodengröße: 20 Zeilen

### Namenskonventionen
- Aussagekräftige, englische Namen für Klassen, Methoden und Variablen
- CamelCase für Klassen und Methoden
- Keine Abkürzungen außer etablierte (z.B. DTO, URL)
- Präfixe/Suffixe nach Funktion (z.B. Service, Repository, Exception)

## 2. Code-Design

### Klassen
- Single Responsibility Principle strikt befolgen
- Maximale Anzahl von Dependencies: 5
- Immutability wo möglich
- Privater Konstruktor für Utility-Klassen

### Methoden
- Ein Abstraktionslevel pro Methode
- Maximal 3 Parameter pro Methode
- Keine Boolean-Parameter (Split in zwei Methoden)
- Rückgabewert oder Seiteneffekt, nicht beides

## 3. Fehlerbehandlung

### Exception Handling
- Checked Exceptions nur für recoverable Conditions
- Custom Exceptions für Domain-spezifische Fehler
- Keine leeren catch Blöcke
- Logging bei allen Exception-Behandlungen

### Null-Handling
- Optional<T> statt null-Rückgabewerte
- Null-Checks am Methodeneingang
- Validierung von Parameters mit Objects.requireNonNull
- Keine null als Methodenparameter

## 4. Testing

### Java Testing Frameworks
- JUnit 5 Features nutzen (Parametrized Tests, Extensions)
- Mockito für Mocking (keine PowerMock)
- AssertJ für lesbare Assertions
- Testcontainers für Integrationstests
- ArchUnit für Architektur-Tests

### Testorganisation
- Given-When-Then Pattern
- Ein Assert pro Test
- Beschreibende Testnamen (should_doSomething_when_condition)
- Separate Tests für Happy Path und Edge Cases

### Testqualität
- Keine Produktionslogik in Tests
- Mocks nur für externe Abhängigkeiten
- Test Data Builder Pattern
- 80% Testabdeckung Minimum

## 5. Dokumentation

### Code-Dokumentation
- JavaDoc für öffentliche API
- Keine offensichtlichen Kommentare
- Kommentare erklären das Warum, nicht das Was
- TODO-Kommentare nur mit Issue-Referenz

### Commit Messages
- Präfix für Commit-Typ (feat:, fix:, refactor:)
- Verb im Imperativ
- Maximale Länge: 72 Zeichen
- Issue-Referenz wenn vorhanden

## 6. Build und Deployment

### Java Tools
- Maven/Gradle Best Practices
- JIB für Container-Builds
- Quarkus/Spring Native für native Kompilierung
- jlink für modulare Runtime-Images
- jdeps für Dependency-Analyse

### Build-Konfiguration
- Reproduzierbare Builds durch fixierte Versionen
- Keine hartcodierten Pfade oder Credentials
- Separate Profile für Entwicklung und Produktion
- Automatische Style-Checks im Build

### Continuous Integration
- Automatische Tests bei jedem Push
- Statische Code-Analyse
- Dependency-Updates automatisch prüfen
- Performance-Tests für kritische Pfade

## 7. Performance und Sicherheit

### Performance
- Lazy Loading wo sinnvoll
- Bulk Operations statt Schleifen
- Caching-Strategie dokumentieren
- Regelmäßige Performance-Tests

### Sicherheit
- Input-Validierung an System-Grenzen
- Keine sensiblen Daten in Logs
- Aktuelle Dependency-Versionen
- Regelmäßige Security Audits

## 8. Review-Prozess

### Code Review Guidelines
- Maximale Review-Größe: 400 Zeilen
- Checkliste für Reviews
- Peer Reviews obligatorisch
- Automatische Checks vor Review

### Quality Gates
- Keine Compiler Warnungen
- Sonar Rules Compliance
- Test Coverage
- Performance Benchmarks

Dieses Manifest wird kontinuierlich weiterentwickelt und an Teamanforderungen angepasst.

_Version: 1.0_
_Letzte Aktualisierung: [DATUM]_