# Mehrere Kennzahlen zurückgeben

**Schwerpunkt:** Flexible Argumente, Tupel und klarer Fehlervertrag.

## Aufgabe

1. Schreibe `statistik(*zahlen)`. Die Funktion liefert ein Tupel aus Minimum, Maximum und arithmetischem Mittelwert.
2. Ohne Argumente löst die Funktion `ValueError` aus.
3. Die Funktion rundet keine Zwischen- oder Rückgabewerte. Nur das Hauptprogramm formatiert die Ausgabe.
4. Verwende die Funktion zusätzlich aus `use_statistik.py`: Entpacke eine Liste beim Aufruf und das Ergebnistupel bei der Rückgabe.

## Prüfe dein Programm

- `statistik(7, 2, 9, 4)` liefert `(2, 9, 5.5)`.
- `statistik(-1, 0, 1)` liefert `(-1, 1, 0.0)`.
- Bei nur einer Zahl sind alle drei Kennzahlen gleich dieser Zahl.
- `statistik()` löst `ValueError` aus.
- Für Dezimalzahlen werden Fließkommaergebnisse mit Toleranz geprüft.

## Ausführen

Vom Hauptordner des Repositories:

```bash
python3 -m tag4.loesungen.erfahren.use_statistik
```

## Referenz

- [Funktion](../../loesungen/erfahren/statistik.py)
- [Nutzendes Modul](../../loesungen/erfahren/use_statistik.py)
