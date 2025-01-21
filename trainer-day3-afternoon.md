# Trainer-Handreichung: Tag 3 - Nachmittag

## 13:00-14:15 - Technische Schulden

### Erkennen und Vermeiden (Kapitel 21)

1. Arten von Schulden präsentieren
   ```java
   // Beispiele für technische Schulden
   
   // 1. Dokumentationsschulden
   void x() { } // Was macht diese Methode?
   
   // 2. Testschulden
   // TODO: Add tests later
   
   // 3. Architekturschulden
   class GodClass { // 3000 Zeilen, 50 Methoden
   
   // 4. Codeschulden
   String status = "A"; // Magic String
   ```

2. Metriken und Tools
   - Zyklomatische Komplexität
   - Coupling
   - Test Coverage
   - SonarQube Demo

### Refactoring-Strategien

1. Boy Scout Rule
   ```java
   // Vor dem Refactoring
   public void processItem(Item item) {
       if(item.getStatus().equals("A")) {
           item.setProcessed(true);
       }
   }
   
   // Nach dem Refactoring
   public void processItem(Item item) {
       if(item.isActive()) {
           item.markAsProcessed();
       }
   }
   ```

2. Strangler Fig Pattern
   - Legacy-System schrittweise ersetzen
   - Beispiele für Migrationsstrategien

## 14:15-14:30 - Pause
- Vorbereitung Abschlussprojekt
- Gruppen einteilen
- Materialien verteilen

## 14:30-16:15 - Abschlussprojekt

### Legacy-Code Refactoring (60 min)

1. Projekt-Setup
   ```java
   // Beispiel Legacy-Code
   class CustomerManager {
       private static CustomerManager instance;
       private ArrayList data = new ArrayList();
       
       private CustomerManager() {}
       
       public static CustomerManager getInstance() {
           if (instance == null) instance = new CustomerManager();
           return instance;
       }
       
       public boolean addCustomer(String n, String a, int v) {
           if (n != null && a != null && v > 0) {
               HashMap c = new HashMap();
               c.put("name", n);
               c.put("address", a);
               c.put("value", v);
               return data.add(c);
           }
           return false;
       }
       
       public ArrayList getCustomers() {
           return data;
       }
   }
   ```

2. Aufgaben für Teams
   - Code Smells identifizieren
   - Tests schreiben
   - Refactoring durchführen
   - Dokumentation erstellen

### Team-Präsentationen (45 min)
- Jedes Team stellt Lösungsansatz vor
- Diskussion der verschiedenen Ansätze
- Feedback durch Trainer

## 16:15-17:00 - Workshop-Abschluss

### Zusammenfassung (20 min)
1. Wichtigste Erkenntnisse
   - Clean Code Prinzipien
   - Praktische Techniken
   - Tools und Methoden

2. Nächste Schritte
   - Implementierung im Team
   - Weitere Lernressourcen
   - Community und Support

### Feedback-Runde (15 min)
- Was war besonders hilfreich?
- Was könnte verbessert werden?
- Offene Fragen klären

### Abschluss (10 min)
- Zertifikate austeilen
- Kontaktinformationen austauschen
- Ressourcen-Links teilen

### Trainer-Checkliste
- [ ] Alle Materialien digital bereitstellen
- [ ] Feedback-Bögen einsammeln
- [ ] Zertifikate unterschreiben
- [ ] Fotodokumentation sichern
- [ ] Raum aufräumen

### Follow-up Planung
1. Feedback auswerten
2. Materialien aktualisieren
3. Verbesserungsvorschläge dokumentieren
4. Follow-up E-Mail vorbereiten

