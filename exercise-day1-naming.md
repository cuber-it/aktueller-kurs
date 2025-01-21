# Übung 1: Namensgebung

## Ziel
Verbesserung der Namensgebung in bestehendem Code unter Berücksichtigung der Clean Code Prinzipien.

## Aufgaben

### 1. Code Review (15 Minuten)
Analysieren Sie den folgenden Code und identifizieren Sie Probleme in der Namensgebung:

```java
class DM {
    private List<String> dl;
    private boolean p;
    private int n;
    
    public void proc() {
        for(String s : dl) {
            if(p) {
                doStuff(s);
            }
        }
    }
    
    private void doStuff(String s) {
        // Verarbeitung
    }
    
    public void setFlag(boolean b) {
        p = b;
    }
    
    public void setValue(int v) {
        n = v;
    }
}
```

### 2. Refactoring (20 Minuten)
Verbessern Sie den Code mit aussagekräftigen Namen. Berücksichtigen Sie:
- Klassennamen
- Variablennamen
- Methodennamen
- Parameternamen

### 3. Erweiterung (25 Minuten)
Erweitern Sie den Code um eine sinnvolle Geschäftslogik Ihrer Wahl und achten Sie dabei besonders auf sprechende Namen.

## Testfälle

```java
class DMTest {
    @Test
    void testProc() {
        DM dm = new DM();
        dm.setFlag(true);
        dm.setValue(42);
        dm.proc(); // Was testet dieser Test eigentlich?
    }
}
```

## Hinweise
- Namen sollten selbsterklärend sein
- Domain-spezifische Begriffe verwenden
- Abkürzungen vermeiden
- Konsistente Begriffe verwenden

## Erweiterung: Pair Review (15 Minuten)
- Tauschen Sie Ihren Code mit einem Partner
- Reviewen Sie gegenseitig die gewählten Namen
- Diskutieren Sie Alternativen

## Beispiellösung
```java
class DocumentManager {
    private List<String> documentList;
    private boolean isProcessingEnabled;
    private int maxDocuments;
    
    public void processDocuments() {
        for(String document : documentList) {
            if(isProcessingEnabled) {
                processDocument(document);
            }
        }
    }
    
    private void processDocument(String document) {
        // Dokumentenverarbeitung
    }
    
    public void enableProcessing(boolean enabled) {
        isProcessingEnabled = enabled;
    }
    
    public void setMaxDocuments(int maximum) {
        maxDocuments = maximum;
    }
}
```

## Bewertungskriterien
- [ ] Aussagekräftige Klassennamen
- [ ] Klare Methodennamen
- [ ] Beschreibende Variablennamen
- [ ] Konsistente Namensgebung
- [ ] Domänenspezifische Begriffe
- [ ] Keine unnötigen Abkürzungen

## Bonus-Aufgabe
Erstellen Sie eine zweite Version des Codes in einer anderen Programmiersprache Ihrer Wahl und vergleichen Sie die Namenskonventionen.
