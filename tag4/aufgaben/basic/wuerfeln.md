# Würfe in einer Funktion aufsummieren

**Schwerpunkt:** Parameter prüfen und Zufallswerte verarbeiten.

## Aufgabe

1. Schreibe `wuerfeln(anzahl)`. Jeder Wurf liefert eine ganze Zahl von 1 bis 6.
2. Die Funktion liefert die Augensumme zurück; die Ausgabe erfolgt im Hauptprogramm.
3. Null Würfe liefern 0. Eine negative oder nicht ganzzahlige Anzahl wird mit `ValueError` abgewiesen.
4. Zeige einen Aufruf mit drei Würfen und einen mit null Würfen.

## Prüfe dein Programm

- Bei einem Wurf liegt das Ergebnis zwischen 1 und 6.
- Bei drei Würfen liegt es zwischen 3 und 18.
- `wuerfeln(0)` liefert 0.
- -1, 1.5 und True sind keine gültigen Anzahlen.
- Teste Zufallsergebnisse über ihre Eigenschaften, nicht gegen eine beliebige feste Augensumme.

## Ausführen

Vom Hauptordner des Repositories:

```bash
python3 tag4/loesungen/basic/wuerfeln.py
```

## Referenz

- [Referenzlösung](../../loesungen/basic/wuerfeln.py)
