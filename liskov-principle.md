# Das Liskovsche Substitutionsprinzip (LSP)

## Definition
Das LSP besagt, dass Objekte einer Basisklasse durch Objekte ihrer abgeleiteten Klassen ersetzt werden können müssen, ohne dass dabei die korrekte Funktionsweise des Programms beeinträchtigt wird.

## Kernaspekte
- Unterklassen dürfen Vorbedingungen nicht verschärfen
- Unterklassen dürfen Nachbedingungen nicht abschwächen
- Invarianten der Basisklasse müssen erhalten bleiben
- History Constraint (Verhalten muss konsistent sein)

## Klassisches Negativbeispiel: Rechteck und Quadrat

```java
// Verletzung des LSP
class Rechteck {
    protected double breite;
    protected double hoehe;
    
    public void setBreite(double breite) {
        this.breite = breite;
    }
    
    public void setHoehe(double hoehe) {
        this.hoehe = hoehe;
    }
    
    public double getFlaeche() {
        return breite * hoehe;
    }
}

class Quadrat extends Rechteck {
    @Override
    public void setBreite(double breite) {
        this.breite = breite;
        this.hoehe = breite;  // Verletzt LSP!
    }
    
    @Override
    public void setHoehe(double hoehe) {
        this.hoehe = hoehe;
        this.breite = hoehe;  // Verletzt LSP!
    }
}

// Dieser Code funktioniert nicht wie erwartet
void verarbeiteRechteck(Rechteck r) {
    r.setBreite(5);
    r.setHoehe(4);
    assert r.getFlaeche() == 20; // Schlägt bei Quadrat fehl!
}
```

## Korrektes Beispiel: Vogelwelt

```java
interface Vogel {
    void bewege();
}

interface FlugfaehigerVogel extends Vogel {
    void fliege();
}

class Spatz implements FlugfaehigerVogel {
    @Override
    public void bewege() {
        // Normale Bewegung am Boden
    }
    
    @Override
    public void fliege() {
        // Flugbewegung
    }
}

class Pinguin implements Vogel {
    @Override
    public void bewege() {
        // Watscheln
    }
}

// Korrekte Verwendung des LSP
class VogelSimulation {
    public void simuliereBewegung(Vogel vogel) {
        vogel.bewege();  // Funktioniert für alle Vögel
    }
    
    public void simuliereFlug(FlugfaehigerVogel vogel) {
        vogel.fliege();  // Nur für flugfähige Vögel
    }
}
```

## Praktische Anwendung des LSP

1. **Verhaltensgarantien**
   - Unterklassen müssen ALLE Versprechen der Basisklasse einhalten
   - Keine unerwarteten Ausnahmen oder Nebenwirkungen

2. **Design by Contract**
   - Vorbedingungen können nur gelockert werden
   - Nachbedingungen können nur verschärft werden
   - Invarianten müssen erhalten bleiben

3. **Typische Warnzeichen für LSP-Verletzungen**
   - Prüfung auf konkrete Typen (instanceof)
   - Überschreiben mit leeren Implementierungen
   - Werfen von UnsupportedOperationException

## Best Practices

1. **Komposition statt Vererbung**
   ```java
   class Form {
       private FlächenBerechnungsstrategie berechnung;
       
       public double getFlaeche() {
           return berechnung.berechne();
       }
   }
   ```

2. **Interface Segregation**
   - Kleine, spezifische Interfaces
   - Klare Verhaltensverträge

3. **Abstrakte Basisklassen**
   - Gemeinsames Verhalten in Basisklasse
   - Spezifisches Verhalten in Unterklassen

## Vorteile der LSP-Einhaltung

1. **Austauschbarkeit**
   - Polymorphismus funktioniert zuverlässig
   - Wartbare und erweiterbare Codebasis

2. **Testbarkeit**
   - Tests der Basisklasse gelten für alle Unterklassen
   - Weniger spezifische Tests nötig

3. **Flexibilität**
   - Einfache Erweiterung durch neue Unterklassen
   - Zuverlässige Abstraktion