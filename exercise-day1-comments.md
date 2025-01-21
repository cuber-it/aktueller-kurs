# Übung 2: Kommentare

## Ziel
Lernen, wann Kommentare sinnvoll sind und wann Code selbsterklärend sein sollte.

## Ausgangscode
```java
// Manager class for data
public class DataManager {
    // List of items
    private List<Integer> items;
    
    // Constructor
    public DataManager() {
        items = new ArrayList<>();
    }
    
    // Add item to list
    public void addItem(int i) {
        items.add(i);  // Add to list
    }
    
    // Process all items in list
    public void processItems() {
        // Loop through all items
        for(int i = 0; i < items.size(); i++) {
            // Get current item
            int currentItem = items.get(i);
            // Process item
            if(currentItem > 0) {  // If positive
                doProcessing(currentItem);  // Process it
            }
        }
    }
    
    // Do the processing
    private void doProcessing(int item) {
        // Multiply by 2
        int result = item * 2;
        // Print result
        System.out.println(result);
    }
}
```

## Aufgaben

### 1. Analyse (10 Minuten)
- Markieren Sie überflüssige Kommentare
- Identifizieren Sie, wo Code selbsterklärend sein könnte
- Finden Sie Stellen, wo Kommentare tatsächlich hilfreich wären

### 2. Refactoring (20 Minuten)
- Entfernen Sie überflüssige Kommentare
- Machen Sie den Code selbsterklärend
- Fügen Sie dort sinnvolle Kommentare hinzu, wo sie wirklich nötig sind

### 3. Dokumentation (15 Minuten)
- Erstellen Sie eine sinnvolle API-Dokumentation
- Dokumentieren Sie wichtige Geschäftsregeln
- Kommentieren Sie komplexe Algorithmen (falls vorhanden)

[Fortsetzung folgt mit weiteren Übungen...]

Soll ich mit den weiteren Übungen für Tag 1 fortfahren?