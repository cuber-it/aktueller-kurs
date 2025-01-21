# Trainer-Handreichung: Tag 1 - Nachmittag

## 13:00-14:30 - Kommentare & Dokumentation

### Theorie (Kapitel 8)
1. Arten von Kommentaren
   ```java
   // Schlecht: Offensichtliches kommentieren
   i = i + 1; // Erhöhe i um 1
   
   // Gut: Geschäftsregeln dokumentieren
   if (employee.age >= 65) { // Gesetzliches Renteneintrittsalter
   ```

2. Wann sind Kommentare sinnvoll?
   - Rechtliche Anforderungen
   - Komplexe Algorithmen
   - Workarounds für bekannte Probleme
   - API-Dokumentation

3. Alternativen zu Kommentaren
   - Aussagekräftige Namen
   - Extraktion von Methoden
   - Tests als Dokumentation

### Praktische Übungen (45 min)
1. "Kommentar-Refactoring"
   ```java
   // Teilnehmer bekommen Code mit überflüssigen/schlechten Kommentaren
   // Aufgabe: Kommentare durch besseren Code ersetzen
   ```

2. "Documentation Kata"
   - API dokumentieren
   - Code-Beispiele schreiben
   - Review in Kleingruppen

## 14:30-14:45 - Pause
- Checkliste für Nachmittagsübungen vorbereiten
- Beispielcode für Workshop bereitstellen

## 14:45-16:15 - Hands-on Workshop Teil 1

### Code Review Übungen (90 min)

1. Setup (15 min)
   - Teams von 2-3 Personen bilden
   - Repository bereitstellen
   - Aufgaben verteilen

2. Review-Phasen (60 min)
   ```java
   // Beispiel für Review-Aufgaben:
   class UserManager {
       private ArrayList<String> userList = new ArrayList<String>();
       
       public boolean add(String u) {
           return userList.add(u);  // Was könnte hier besser sein?
       }
       
       public boolean checkIfUsrExist(String u) {
           return userList.contains(u);  // Mehrere Probleme identifizieren
       }
   }
   ```

3. Gemeinsame Besprechung (15 min)
   - Häufigste Findings
   - Best Practices
   - Lösungsansätze

### Trainer-Hinweise
- Auf unterschiedliche Erfahrungslevel achten
- Bei Bedarf Hilfestellung geben
- Diskussionen moderieren
- Keine "perfekten" Lösungen erzwingen

## 16:15-17:00 - Tagesrückblick & Diskussion

### Review des Tages (30 min)
1. Hauptthemen rekapitulieren
   - Clean Code Grundlagen
   - Namensgebung
   - Kommentare
   - Standards

2. Offene Fragen sammeln
   - Flipchart nutzen
   - Themen für morgen notieren

### Ausblick auf Tag 2 (15 min)
- Primitive Obsession
- Funktionen & Methoden
- Komplexität

### Hausaufgabe (optional)
```java
// Code für Heimübung bereitstellen
// Fokus auf heute gelernte Konzepte
```

### Abschluss-Checkliste
- [ ] Offene Fragen dokumentiert
- [ ] Feedback eingesammelt
- [ ] Materialien für Tag 2 vorbereitet
- [ ] Raum aufgeräumt
- [ ] Teilnehmer-Notizen gesichert

## Notizen für Tag 2
- Schwierige Konzepte von Tag 1 aufgreifen
- Gruppendynamik beobachten
- Tempo anpassen
- Praxisbeispiele vorbereiten

