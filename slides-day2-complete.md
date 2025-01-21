# Folie 1: Tag 2 - Clean Code Techniken
```
Clean Code Workshop
Tag 2: Fortgeschrittene Techniken
[Datum]
[Trainer Name]
```

# Folie 2: Agenda Tag 2
```
Vormittag (9:00 - 12:00)
• Wiederholung Tag 1
• Primitive Obsession & Value Objects
• Clean Functions & Methoden vertiefen

Nachmittag (13:00 - 17:00)
• Komplexität reduzieren
• Umgang mit if-Anweisungen
• Nullwerte behandeln
• Praktische Übungen
```

# Folie 3: Primitive Obsession
```
Was ist Primitive Obsession?
• Übermäßige Verwendung primitiver Datentypen
• Fehlende Kapselung von Geschäftsregeln
• Verlust von Typ-Sicherheit

Beispiele:
❌ Primitiv:
String email;
int age;
String phoneNumber;

✅ Value Objects:
EmailAddress email;
Age age;
PhoneNumber phoneNumber;

Vorteile:
• Validierung bei Erstellung
• Unmögliche Zustände ausgeschlossen
• Bessere Domänenmodellierung
```

# Folie 4: Value Objects Implementation
```
Beispiel eines Value Objects:

public final class EmailAddress {
    private final String value;

    public EmailAddress(String value) {
        if (!isValid(value)) {
            throw new IllegalArgumentException(
                "Invalid email format"
            );
        }
        this.value = value;
    }

    private boolean isValid(String email) {
        return email != null &&
               email.contains("@") &&
               email.length() >= 5;
    }

    // Equals & HashCode nicht vergessen!
}

Eigenschaften:
• Unveränderlich (immutable)
• Selbst-validierend
• Wertbasierte Gleichheit
```

# Folie 5: Anwendung von Value Objects
```
Vorher:
class User {
    private String email;
    private String password;
    private int age;
    
    public void setEmail(String email) {
        this.email = email;
    }
}

Nachher:
class User {
    private EmailAddress email;
    private Password password;
    private Age age;
    
    public void updateEmail(EmailAddress email) {
        this.email = Objects.requireNonNull(email);
    }
}

Vorteile:
• Typ-Sicherheit
• Geschäftsregeln gekapselt
• Bessere API
```

# Folie 6: Clean Functions vertieft
```
Fortgeschrittene Konzepte:

1. Command Query Separation (CQS)
   • Commands ändern Zustand
   • Queries liefern Werte
   • Nicht beides mischen

2. Tell, Don't Ask
   • Objekte um Aktionen bitten
   • Nicht Daten abfragen und selbst verarbeiten

3. Law of Demeter
   • Nur mit direkten "Freunden" sprechen
   • Keine "Übersprungkommunikation"

Beispiel CQS:
❌ boolean deleteUser(int id) // Mixed
✅ void deleteUser(UserId id) // Command
✅ User findUser(UserId id)   // Query
```

# Folie 7: Komplexität reduzieren
```
Quellen von Komplexität:

1. Zyklomatische Komplexität
   • Anzahl der Entscheidungspfade
   • Durch if/else, switch, loops

2. Kognitive Komplexität
   • Wie schwer ist Code zu verstehen
   • Verschachtelungen, Abhängigkeiten

3. Strukturelle Komplexität
   • Klassenbeziehungen
   • Abhängigkeitsgraph

Metriken:
• Maximal 10 Entscheidungspunkte pro Methode
• Maximal 3 Verschachtelungsebenen
• Klare Verantwortlichkeiten
```

# Folie 8: If-Anweisungen optimieren
```
Strategien zur Vereinfachung:

1. Guard Clauses
   ❌ if (valid) {
        // lange Logik
      }
   ✅ if (!valid) return;
      // lange Logik

2. Polymorphismus statt if
   ❌ if (type == "A") { ... }
      else if (type == "B") { ... }
   ✅ interface Handler {
        void handle();
      }

3. Strategy Pattern
   • Verschiedene Algorithmen kapseln
   • Zur Laufzeit austauschbar

4. Early Return
   • Frühe Validierung
   • Klare Codepfade
```

# Folie 9: Nullwerte behandeln
```
Probleme mit null:
• NullPointerException
• Unklare Semantik
• Implizite Bedingungen

Lösungsstrategien:

1. Optional<T>
   • Explizite Behandlung
   • Funktionale Verkettung

2. Null Object Pattern
   • Standardverhalten definieren
   • Null-Checks vermeiden

3. Assertions
   • Früh prüfen
   • Klare Fehlermeldungen

Beispiel:
Optional<User> findUser(UserId id) {
    return Optional.ofNullable(
        repository.findById(id)
    );
}
```

# Folie 10: Design Patterns
```
Relevante Patterns für Clean Code:

1. Builder
   • Komplexe Objekterzeugung
   • Fluent Interface

2. Strategy
   • Algorithmen kapseln
   • Austauschbare Logik

3. Factory Method
   • Objekterzeugung kapseln
   • Abhängigkeiten reduzieren

4. Template Method
   • Algorithmusstruktur definieren
   • Teilschritte anpassbar

Beispiel Builder:
User user = User.builder()
    .withName("John")
    .withEmail(email)
    .withAge(age)
    .build();
```

# Folie 11: Exceptions richtig nutzen
```
Best Practices:

1. Exception Hierarchie
   • Fachliche Exceptions
   • Technische Exceptions

2. Exception Handling
   • Nur behandelbare Exceptions fangen
   • Ressourcen korrekt schließen

3. Exception Design
   • Informative Meldungen
   • Kontext mitgeben
   • Stack Trace erhalten

Beispiel:
try {
    processOrder(order);
} catch (ValidationException e) {
    // Behandelbar
    logValidationError(e);
} catch (RuntimeException e) {
    // Unbehandelbar
    throw new SystemException("Order processing failed", e);
}
```

# Folie 12: Praktische Übungen
```
Übung 1: Value Objects (45 Min)
• Email, Telefon, Geld implementieren
• Validierungen einbauen
• Tests schreiben

Übung 2: Refactoring (60 Min)
• Komplexe if-Struktur vereinfachen
• Strategy Pattern anwenden
• Null-Handling verbessern

Übung 3: Exception Handling (45 Min)
• Exception Hierarchie aufbauen
• Handler implementieren
• Tests für Fehlerfälle
```

# Folie 13: Code Review Workshop
```
Gruppenübung (60 Min):

1. Code analysieren
   • Komplexität identifizieren
   • Primitive Obsession finden
   • Exception Handling prüfen

2. Verbesserungen vorschlagen
   • Value Objects einführen
   • Patterns anwenden
   • Nullwerte eliminieren

3. Refactoring durchführen
   • Paarweise Implementation
   • Gegenseitiges Review
   • Diskussion der Lösungen
```

# Folie 14: Zusammenfassung Tag 2
```
Kernpunkte:
• Value Objects statt primitive Typen
• Komplexität aktiv reduzieren
• Nullwerte vermeiden
• Exceptions gezielt einsetzen
• Patterns sinnvoll nutzen

Erreichte Ziele:
• Verbesserte Codequalität
• Erhöhte Typsicherheit
• Reduzierte Komplexität
• Bessere Fehlerbehandlung
```

# Folie 15: Hausaufgaben & Vorbereitung Tag 3
```
Hausaufgaben:
• Value Objects in eigenem Code identifizieren
• Komplexe if-Strukturen analysieren
• Exception Handling überprüfen

Vorbereitung Tag 3:
• Code für Refactoring mitbringen
• Fragen zu Design Patterns vorbereiten
• Team-spezifische Probleme notieren
```

