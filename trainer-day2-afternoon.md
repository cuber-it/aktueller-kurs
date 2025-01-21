# Trainer-Handreichung: Tag 2 - Nachmittag

## 13:00-14:30 - Komplexität reduzieren

### If-Anweisungen optimieren (Kapitel 14)

1. Probleme mit komplexen If-Statements
   ```java
   // Problematisch
   if (user != null && user.isActive() 
       && (!user.isBlocked() || user.isAdmin()) 
       && user.hasPermission("edit")) {
       // ...
   }
   ```

2. Lösungsstrategien demonstrieren
   ```java
   // Besser
   class User {
       public boolean canEdit() {
           if (!isActive()) return false;
           if (isBlocked() && !isAdmin()) return false;
           return hasPermission("edit");
       }
   }
   ```

3. Übungen (30 min)
   - Verschachtelte IFs vereinfachen
   - Switch/Case durch Polymorphie ersetzen
   - Early Return Pattern anwenden

### Nullwerte behandeln (Kapitel 15)

1. Null Object Pattern
   ```java
   // Statt null
   class NullUser extends User {
       @Override
       public boolean canEdit() {
           return false;
       }
   }
   ```

2. Optional/Maybe Typen
   ```java
   // Modern
   Optional<User> findUser(String id) {
       return Optional.ofNullable(repository.findById(id));
   }
   ```

## 14:30-14:45 - Pause
- Beispielcode für Workshop vorbereiten
- Gruppen für Nachmittag einteilen

## 14:45-16:15 - Hands-on Workshop

### Komplexen Code vereinfachen (45 min)

1. Legacy-Code-Beispiel
   ```java
   class OrderProcessor {
       public void process(Order order) {
           if (order != null && order.getItems() != null) {
               double total = 0;
               for (Item item : order.getItems()) {
                   if (item.getPrice() != null) {
                       if (item.getQuantity() > 0) {
                           double itemTotal = item.getPrice() * item.getQuantity();
                           if (item.getDiscount() != null) {
                               itemTotal = itemTotal * (1 - item.getDiscount());
                           }
                           total += itemTotal;
                       }
                   }
               }
               order.setTotal(total);
           }
       }
   }
   ```

2. Schrittweise Verbesserung
   - Nullchecks eliminieren
   - Geschäftslogik extrahieren
   - Value Objects einführen
   - Tests schreiben

### Code Katas (45 min)

1. Gilded Rose Kata
   - Repository bereitstellen
   - Tests vorgeben
   - Schrittweise Refactoring

2. Alternative Katas
   - Tennis Game
   - Bowling Game
   - String Calculator

### Trainer-Hinweise
- Verschiedene Lösungsansätze zulassen
- Auf Clean Code Prinzipien fokussieren
- Regelmäßiges Feedback geben
- Bei Bedarf Hilfestellung leisten

## 16:15-17:00 - Tagesrückblick

### Review (30 min)
1. Hauptthemen zusammenfassen
   - Primitive Obsession
   - Clean Functions
   - Komplexitätsreduktion
   - Null-Handling

2. Lessons Learned sammeln
   - Was war überraschend?
   - Was war besonders hilfreich?
   - Wo gibt es noch Unklarheiten?

### Ausblick Tag 3 (15 min)
- Kopplung & Hierarchien
- Testing
- Technische Schulden
- Abschlussprojekt ankündigen

### Abschluss-Checkliste
- [ ] Codebeispiele sichern
- [ ] Offene Fragen notieren
- [ ] Materialien für Tag 3 prüfen
- [ ] Feedback zu Übungen sammeln
- [ ] Raumorganisation für Tag 3

### Notizen für Tag 3
- Schwierige Konzepte von Tag 2 aufgreifen
- Praxisbeispiele anpassen
- Gruppen für Abschlussprojekt planen
- Zeitpuffer für offene Fragen einplanen

