# Clean Code Akronyme und Prinzipien

## DRY - Don't Repeat Yourself
- Code-Duplikation vermeiden
- Jedes Stück Wissen sollte eine einzige, eindeutige Repräsentation haben

## YAGNI - You Ain't Gonna Need It  
- Implementiere Dinge erst wenn sie wirklich gebraucht werden
- Keine Features "auf Vorrat" entwickeln

## KISS - Keep It Simple, Stupid
- Halte Lösungen so einfach wie möglich
- Vermeide unnötige Komplexität

## SOLID
- **S** - Single Responsibility Principle
  - Eine Klasse sollte nur einen Grund zur Änderung haben
- **O** - Open/Closed Principle
  - Offen für Erweiterungen, geschlossen für Änderungen
- **L** - Liskov Substitution Principle
  - Subtypen müssen ihre Basistypen ersetzen können
- **I** - Interface Segregation Principle
  - Viele spezifische statt einem großen Interface
- **D** - Dependency Inversion Principle
  - Abhängigkeiten von Abstraktionen statt konkreten Implementierungen

## DIE - Duplication Is Evil
- Ähnlich wie DRY
- Fokus auf das Vermeiden von Duplikationen im Code

## GRASP - General Responsibility Assignment Software Patterns
- Richtlinien für die Zuweisung von Verantwortlichkeiten an Klassen und Objekte

## TDA - Tell Don't Ask
- Objekte sollen Operationen selbst ausführen statt ihre Daten preiszugeben

## LoD - Law of Demeter
- Auch bekannt als "Principle of Least Knowledge"
- Ein Objekt sollte nur mit seinen unmittelbaren "Freunden" sprechen

## CQS - Command Query Separation
- Methoden sollten entweder Kommandos (Änderungen) oder Abfragen (Rückgaben) sein, aber nicht beides