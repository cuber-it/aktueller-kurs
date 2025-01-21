# Folie 1: Tag 3 - Architektur & Praxis
```
Clean Code Workshop
Tag 3: Architektur, Testing & Best Practices
[Datum]
[Trainer Name]
```

# Folie 2: Agenda Tag 3
```
Vormittag (9:00 - 12:00)
• Wiederholung Tag 2
• Kopplung & Kohäsion
• Clean Architecture
• Testbare Architektur

Nachmittag (13:00 - 17:00)
• Technische Schulden
• Testing Best Practices
• Abschlussprojekt
• Workshop-Zusammenfassung
```

# Folie 3: Kopplung & Kohäsion
```
Kopplung:
• Grad der Abhängigkeit zwischen Modulen
• Lose Kopplung = besser wartbar
• Hohe Kopplung = schwer zu ändern

Kohäsion:
• Zusammenhalt innerhalb eines Moduls
• Hohe Kohäsion = klare Verantwortlichkeit
• Niedrige Kohäsion = vermischen von Aufgaben

Ziel:
• Lose Kopplung
• Hohe Kohäsion
```

# Folie 4: Kopplung in der Praxis
```
❌ Starke Kopplung:
class OrderProcessor {
    private MySQLDatabase db = new MySQLDatabase();
    private SmtpEmailSender emailSender = new SmtpEmailSender();
}

✅ Lose Kopplung:
class OrderProcessor {
    private final OrderRepository repository;
    private final NotificationService notifier;
    
    OrderProcessor(
        OrderRepository repository,
        NotificationService notifier
    ) {
        this.repository = repository;
        this.notifier = notifier;
    }
}
```

# Folie 5: Clean Architecture
```
Schichten von innen nach außen:
1. Entities (Domain Model)
   • Geschäftsregeln
   • Unabhängig von Framework

2. Use Cases (Application)
   • Anwendungsfälle
   • Orchestrierung

3. Interface Adapters
   • Controller
   • Presenter
   • Gateways

4. Frameworks & Drivers
   • Web
   • Datenbank
   • UI

Dependency Rule:
• Abhängigkeiten nur nach innen
• Innere Schichten wissen nichts von äußeren
```

# Folie 6: Ports & Adapters
```
Ports:
• Definieren Schnittstellen
• Gehören zur Domäne
• Unabhängig von Technologie

Beispiel Port:
interface OrderRepository {
    Order save(Order order);
    Optional<Order> findById(OrderId id);
}

Adapters:
• Implementieren Ports
• Technologie-spezifisch
• Austauschbar

Beispiel Adapter:
class JpaOrderRepository 
    implements OrderRepository {
    // Implementierung mit JPA
}
```

# Folie 7: Dependency Injection
```
Prinzip:
• Abhängigkeiten werden injiziert
• Keine direkte Instanziierung
• Bessere Testbarkeit

Typen:
1. Constructor Injection (bevorzugt)
2. Setter Injection
3. Field Injection (vermeiden)

Beispiel:
@Service
class OrderService {
    private final OrderRepository repository;
    private final PaymentService paymentService;
    
    @Autowired // Constructor Injection
    OrderService(
        OrderRepository repository,
        PaymentService paymentService
    ) {
        this.repository = repository;
        this.paymentService = paymentService;
    }
}
```

# Folie 8: Testbare Architektur
```
Grundprinzipien:
1. Dependency Injection
2. Interface-basiertes Design
3. Kleine, fokussierte Klassen
4. Separation of Concerns

Eigenschaften:
• Einfach zu mocken
• Unabhängig testbar
• Kontrollierbare Abhängigkeiten
• Deterministisches Verhalten

Anti-Patterns vermeiden:
• Statische Methoden
• Singleton
• Versteckte Abhängigkeiten
• Globaler Zustand
```

# Folie 9: Testing Best Practices
```
Test-Pyramide:
1. Unit Tests (viele)
   • Schnell
   • Isoliert
   • Fokussiert

2. Integration Tests (mittel)
   • Komponenten-Zusammenspiel
   • Reale Abhängigkeiten

3. E2E Tests (wenige)
   • Gesamtsystem
   • Benutzer-Perspektive

Eigenschaften guter Tests:
• Lesbar
• Wartbar
• Zuverlässig
• Aussagekräftig
```

# Folie 10: Unit Test Beispiele
```
❌ Schlechter Test:
@Test
void test1() {
    var calc = new Calculator();
    assertTrue(calc.sum(2,2) == 4);
}

✅ Guter Test:
class CalculatorTest {
    @Test
    void shouldAddPositiveNumbers() {
        // Arrange
        Calculator calculator = new Calculator();
        
        // Act
        int result = calculator.add(2, 2);
        
        // Assert
        assertThat(result)
            .isEqualTo(4)
            .describedAs("Simple addition");
    }
}
```

# Folie 11: Technische Schulden
```
Definition:
• Kompromisse in der Codequalität
• "Kredit" auf Kosten der Wartbarkeit
• Muss "zurückgezahlt" werden

Arten:
1. Bewusste Schulden
   • Zeitdruck
   • Strategische Entscheidungen

2. Unbewusste Schulden
   • Mangelndes Wissen
   • Schleichende Verschlechterung

Management:
• Dokumentieren
• Priorisieren
• Regelmäßig abbauen
```

# Folie 12: Code Metrics
```
Wichtige Metriken:

1. Komplexität
   • Zyklomatische Komplexität
   • Cognitive Complexity
   • Max: 10-15 pro Methode

2. Größe
   • Zeilen Code pro Methode (< 20)
   • Zeilen Code pro Klasse (< 200)
   • Anzahl Methoden pro Klasse (< 10)

3. Coverage
   • Unit Test Coverage (> 80%)
   • Branch Coverage
   • Mutation Coverage
```

# Folie 13: Refactoring Strategien
```
Systematisches Refactoring:

1. Boy Scout Rule
   • Leichte Verbesserungen
   • Bei jeder Änderung

2. Opportunistisches Refactoring
   • Bei Änderungen in der Nähe
   • Kleine Schritte

3. Geplantes Refactoring
   • Dedizierte Zeit
   • Größere Umstrukturierungen

Vorgehen:
1. Tests schreiben
2. Refactoring durchführen
3. Tests prüfen
4. Committen
```

# Folie 14: Abschlussprojekt
```
Praktische Übung (120 Min):

Legacy Code verbessern:
• Code Smells identifizieren
• Tests schreiben
• Refactoring durchführen
• Clean Architecture anwenden

Teamarbeit:
• 3-4 Personen pro Team
• Code Review
• Präsentation der Lösung

Bewertungskriterien:
• Testbarkeit
• Clean Code Prinzipien
• Architektur
• Dokumentation
```

# Folie 15: Workshop Zusammenfassung
```
Tag 1:
• Clean Code Grundlagen
• Namensgebung
• Funktionen

Tag 2:
• Value Objects
• Komplexität
• Exception Handling

Tag 3:
• Architektur
• Testing
• Refactoring

Nächste Schritte:
• Praktische Anwendung
• Team-Guidelines
• Kontinuierliche Verbesserung
```

# Folie 16: Ressourcen
```
Bücher:
• Clean Architecture (Robert C. Martin)
• Working Effectively with Legacy Code
• Test Driven Development

Online:
• Clean Code Cheat Sheet
• Refactoring Guru
• Martin Fowler's Blog

Tools:
• SonarQube
• JaCoCo
• ArchUnit
```

