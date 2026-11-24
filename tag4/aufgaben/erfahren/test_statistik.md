# Den Funktionsvertrag automatisch prüfen

**Schwerpunkt:** Normalfälle, Grenzfälle und erwartete Exceptions.

## Aufgabe

1. Schreibe mit `unittest` Tests für die Funktion aus der Statistik-Aufgabe.
2. Prüfe positive und negative Werte, gemischte Vorzeichen und einen einzelnen Wert.
3. Prüfe Dezimalzahlen mit `assertAlmostEqual` für den Mittelwert.
4. Prüfe, dass ein Aufruf ohne Argumente `ValueError` auslöst.
5. Importiere die Funktion, statt ihre Berechnung im Test nachzubauen.

## Prüfe dein Programm

- Alle Tests laufen ohne Benutzereingaben.
- Die Tests erkennen eine absichtlich falsch berechnete Kennzahl.
- Wird die Ausnahme für leere Eingaben entfernt, muss der entsprechende Test fehlschlagen.
- Die Datei benennt Tests mit `test_`, damit unittest sie erkennt.

## Ausführen

Vom Hauptordner des Repositories:

```bash
python3 -m unittest -v tag4.loesungen.erfahren.test_statistik
```

## Referenz

- [Referenztests](../../loesungen/erfahren/test_statistik.py)
- [Getestete Funktion](../../loesungen/erfahren/statistik.py)
