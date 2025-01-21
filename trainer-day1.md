# Trainer-Handreichung: Tag 1 - Grundlagen

## Vorbereitung
- Raum ab 8:30 zugänglich
- Beamer & Präsentationsfläche testen
- WLAN-Zugangsdaten bereitstellen
- USB-Sticks mit Backup-Material vorbereiten
- Teilnehmerliste ausdrucken

## 09:00-09:30 - Begrüßung und Vorstellung

### Ziele
- Teilnehmer kennenlernen
- Erwartungen abfragen
- Agenda vorstellen

### Durchführung
1. Eigene Vorstellung (max. 3 min)
2. Teilnehmer-Vorstellung mit Fragen:
   - Name und Rolle
   - Programmiererfahrung
   - Eine Sache, die sie an ihrem Code nicht mögen
3. Erwartungen auf Flipchart sammeln

### Mögliche Probleme
- Teilnehmer zu spät → Kurze Nachholrunde in erster Pause
- Sehr unterschiedliche Erfahrungslevel → Notieren für Gruppenbildung

## 09:30-10:30 - Clean Code Grundlagen

### Hauptthemen
1. Was ist Clean Code?
   - Definitionen aus dem Buch zeigen
   - Eigene Erfahrungen einbringen
   - Beispiele: gut vs. schlecht

2. Code Smells (aus Kapitel 1)
   - Definitionen
   - Praktische Beispiele
   - Erste Erkennungsmuster

### Live-Coding Beispiel
```java
// Schlechtes Beispiel
public class Data {
    public String n;
    public int v;
    public void p() {
        System.out.println(n + ": " + v);
    }
}

// Gutes Beispiel
public class Measurement {
    private String name;
    private int value;
    
    public void print() {
        System.out.println(String.format("%s: %d", name, value));
    }
}
```

### Übungsaufgabe
Teilnehmer sollen ein kleines Code-Snippet verbessern (10 min)

## 10:30-10:45 - Pause
- Raum lüften
- Informelle Gespräche ermöglichen
- Flipchart-Notizen sichern

## 10:45-12:00 - Namensgebung & Standards

### Theorie (Kapitel 7 & 9)
1. Namensgebung
   - Abkürzungen
   - Länge vs. Aussagekraft
   - Konsistenz

2. Standards
   - Sprachspezifische Konventionen
   - Team-Standards
   - Automatische Formatierung

### Praktische Übungen
1. "Naming Challenge" (30 min)
   - Schlechte Namen identifizieren
   - Bessere Alternativen finden
   - Gruppendiskussion

2. Standards-Review (30 min)
   - Code-Beispiele analysieren
   - Verbesserungen vorschlagen
   - Tools vorstellen (z.B. SonarQube)

[Fortsetzung folgt mit Nachmittagsprogramm...]
