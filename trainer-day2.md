# Trainer-Handreichung: Tag 2 - Clean Code Techniken

## Vorbereitung
- Codebeispiele für Primitive Obsession vorbereiten
- IDE-Projekte testen
- Übungsaufgaben in verschiedenen Schwierigkeitsgraden
- Flipchart vom Vortag aufhängen

## 09:00-09:30 - Recap Tag 1

### Durchführung
1. Kurze Wiederholung durch Teilnehmer
2. Hausaufgaben besprechen (falls vergeben)
3. Offene Fragen vom Vortag klären

### Quick Quiz
```java
// Teilnehmer sollen Probleme identifizieren
class DataProcessor {
    private List<String> data_list;
    
    public boolean processData(String d) {
        // Adds data to list
        return data_list.add(d);
    }
}
```

## 09:30-10:30 - Primitive Obsession & Objektorientierung

### Value Objects (aus Kapitel 4)
1. Theoretische Grundlagen
   ```java
   // Schlecht
   String emailAddress;
   
   // Gut
   class EmailAddress {
       private final String value;
       
       public EmailAddress(String value) {
           if (!isValid(value)) 
               throw new IllegalArgumentException("Invalid email");
           this.value = value;
       }
   }
   ```

2. Übliche Anwendungsfälle
   - Geldbeträge
   - Datumsangaben
   - IDs
   - Geschäftsspezifische Typen

### Rich Domain Models (aus Kapitel 3)
1. Anämische vs. Rich Models
   ```java
   // Anämisch
   class Order {
       private List<Item> items;
       public List<Item> getItems() { return items; }
       public void setItems(List<Item> items) { this.items = items; }
   }
   
   // Reich
   class Order {
       private final List<Item> items = new ArrayList<>();
       
       public void addItem(Item item) {
           validateItem(item);
           calculateNewTotal(item);
           items.add(item);
       }
   }
   ```

## 10:30-10:45 - Pause

## 10:45-12:00 - Funktionen & Methoden

### Clean Functions (Kapitel 6)
1. Prinzipien
   - Single Responsibility
   - Command Query Separation
   - Don't Repeat Yourself
   - Small Functions

2. Praktische Beispiele
   ```java
   // Schlecht
   void processUserData(User user, boolean sendEmail, boolean validate) {
       if (validate) {
           // 20 Zeilen Validierung
       }
       // 30 Zeilen Datenverarbeitung
       if (sendEmail) {
           // 15 Zeilen Email-Logik
       }
   }
   
   // Gut
   void processUserData(User user) {
       validateUser(user);
       updateUserData(user);
       notifyUser(user);
   }
   ```

### Übungen zur Refaktorierung
1. Code-Kata "Extract Method"
2. Pair-Programming Übung
3. Review in der Gruppe

### Trainer-Hinweise
- Auf häufige Fragen vorbereitet sein:
  - "Wie klein ist klein genug?"
  - "Was ist mit Performance?"
  - "Wann breche ich DRY?"
- Praktische Beispiele aus eigener Erfahrung
- IDE-Shortcuts für Refactoring zeigen

[Fortsetzung mit Nachmittagsprogramm folgt...]

