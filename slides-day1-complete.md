[Vorherige Folien 1-8 bleiben bestehen, Fortsetzung mit:]

# Folie 9: Namensbeispiele aus der Praxis
```
❌ Schlechte Namen und warum:
int d;                   // Nicht aussagekräftig
List<String> lst;        // Unnötige Abkürzung
boolean flag;            // Zu generisch
void process();          // Zu unspezifisch
UserManager umgr;        // Unnötige Abkürzung

✅ Gute Namen und warum:
int daysSinceLastLogin;  // Selbsterklärend
List<String> customers;  // Spezifischer Inhalt
boolean isActive;        // Boolescher Zustand klar
void processOrder();     // Spezifische Aktion
UserManager userManager; // Vollständig ausgeschrieben
```

# Folie 10: Funktionen - Grundregeln
```
Die wichtigsten Regeln für Funktionen:

1. Größe
   • Klein und fokussiert
   • Idealerweise 4-20 Zeilen
   • Eine Abstraktionsebene

2. Single Responsibility Principle (SRP)
   • Eine Funktion = Eine Aufgabe
   • "Do one thing, and do it well"

3. Parameter
   • Maximal 3 Parameter
   • Bei mehr: Parameter Object verwenden

4. DRY - Don't Repeat Yourself
   • Keine Code-Duplikate
   • Wiederverwendung fördern
```

# Folie 11: Clean Functions Beispiel
```
❌ Problematische Funktion:
void processOrder(Order order, boolean sendEmail, 
                 boolean validate, String format) {
    if (validate) {
        // 20 Zeilen Validierung
    }
    // 30 Zeilen Verarbeitung
    if (sendEmail) {
        // 15 Zeilen Email-Logik
    }
}

✅ Clean Functions:
void processOrder(Order order) {
    validateOrder(order);
    saveOrder(order);
    notifyCustomer(order);
}

private void validateOrder(Order order) {
    // Fokussierte Validierung
}
```

# Folie 12: SOLID Prinzipien - Überblick
```
S - Single Responsibility Principle
• Eine Klasse = Eine Verantwortlichkeit
• "Eine Klasse sollte nur einen Grund haben, sich zu ändern"

O - Open/Closed Principle
• Offen für Erweiterung
• Geschlossen für Änderung

L - Liskov Substitution Principle
• Unterklassen müssen sich wie Oberklassen verhalten
• Keine Überraschungen bei Vererbung

I - Interface Segregation Principle
• Kleine, spezifische Interfaces
• Keine "Fat Interfaces"

D - Dependency Inversion Principle
• Abhängigkeit von Abstraktionen
• Nicht von konkreten Implementierungen
```

# Folie 13: Kommentare - Wann und Wie
```
Gute Kommentare:
• Erklären das WARUM (nicht das WAS)
• Dokumentieren komplexe Algorithmen
• Warnen vor Konsequenzen
• API-Dokumentation

Überflüssige Kommentare:
• Beschreiben offensichtlichen Code
• Auskommentierter Code
• Redundante Javadoc
• Versionierungskommentare

Beispiel:
// Schlecht:
i = i + 1; // Erhöhe i um 1

// Gut:
retryCount++; // Maximale Anzahl Versuche gemäß RFC-123
```

# Folie 14: Clean Code Formatierung
```
Allgemeine Regeln:
• Konsistente Einrückung
• Logische Gruppierung
• Maximale Zeilenlänge (oft 80-120 Zeichen)
• Leerzeilen zur Strukturierung

Vertikale Formatierung:
• Zusammengehöriges nah beieinander
• Logische Abschnitte trennen
• Abstraktionsebenen gruppieren

Horizontale Formatierung:
• Einrückung zeigt Hierarchie
• Klammern-Stil konsistent halten
• Operatoren mit Leerzeichen umgeben
```

# Folie 15: Code Review Prinzipien
```
Ziele eines Code Reviews:
• Qualitätssicherung
• Wissensaustausch
• Konsistenz sicherstellen
• Fehler früh finden

Review-Checkliste:
1. Clean Code Prinzipien erfüllt?
2. Tests vorhanden und sinnvoll?
3. Architektur-Konformität?
4. Keine offensichtlichen Bugs?
5. Performance-Aspekte beachtet?

Feedback-Regeln:
• Konstruktiv und respektvoll
• Konkret und nachvollziehbar
• Lösungsorientiert
```

# Folie 16: Best Practices im Team
```
Teamweite Standards:
• Code Style Guide definieren
• Automatische Formatierung
• Gemeinsame Namenskonventionen
• Dokumentationsstandards

Prozesse:
• Regelmäßige Code Reviews
• Pair Programming
• Continuous Integration
• Automatisierte Qualitätschecks

Tools:
• IDE-Plugins für Formatierung
• Linting-Tools
• SonarQube o.ä.
• Code Coverage Tools
```

# Folie 17: Übungen für Tag 1
```
Praktische Übungen:

1. Namensgebung (30 Min)
   • Code-Beispiele analysieren
   • Namen verbessern
   • Peer Review

2. Funktionen refactoren (45 Min)
   • Lange Methode aufteilen
   • Parameter reduzieren
   • SRP anwenden

3. Code Review (45 Min)
   • Realen Code reviewen
   • Probleme identifizieren
   • Verbesserungen vorschlagen
```

# Folie 18: Zusammenfassung Tag 1
```
Kernpunkte:
• Clean Code ist lesbar und wartbar
• Namen sind entscheidend für Verständlichkeit
• Funktionen: klein und fokussiert
• SOLID Prinzipien als Leitfaden
• Kommentare sparsam und sinnvoll einsetzen

Nächste Schritte:
• Best Practices anwenden
• Team-Standards etablieren
• Continuous Improvement
• Code Reviews einführen
```

# Folie 19: Ressourcen & Links
```
Bücher:
• "Clean Code" - Robert C. Martin
• "Refactoring" - Martin Fowler

Online-Ressourcen:
• Clean Code Cheat Sheet
• SOLID Principles Guide
• Code Review Guidelines

Tools:
• SonarQube
• CheckStyle
• PMD
• Spotbugs
```

