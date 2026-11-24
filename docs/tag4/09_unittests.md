# Funktionen mit unittest prüfen

## Worum geht's

Ein Unittest prüft ein festgelegtes Verhalten einer kleinen Programmeinheit, hier einer Funktion. `unittest` führt die Prüfungen automatisch aus und meldet Abweichungen. Es gehört zur Standardbibliothek.

## Was wird geprüft?

`rechner.py` stellt `addiere`, `teile` und `ist_gerade` bereit. Die Tests importieren diese Funktionen. Erwartete Ergebnisse werden unabhängig von ihrer Umsetzung festgelegt.

| Fall | Beispiel | Erwartung |
| --- | --- | --- |
| Normalfall | `addiere(2, 3)` | `5` |
| Negative Werte | `addiere(-1, -1)` | `-2` |
| Dezimalzahlen | `addiere(0.1, 0.2)` | Näherungsweise `0.3` |
| Grenzfall | `teile(0, 2)` | `0` |
| Fehlerfall | `teile(5, 0)` | `ZeroDivisionError` |

## Tests schreiben

Diese Testdatei liegt wie `rechner.py` im Ordner `tag4`:

```python
import unittest
from rechner import addiere, teile, ist_gerade


class TestRechner(unittest.TestCase):
    def test_addiere_positive_zahlen(self):
        self.assertEqual(addiere(2, 3), 5)

    def test_addiere_negative_zahlen(self):
        self.assertEqual(addiere(-1, -1), -2)

    def test_addiere_dezimalzahlen(self):
        self.assertAlmostEqual(addiere(0.1, 0.2), 0.3)

    def test_teile_normal(self):
        self.assertEqual(teile(10, 2), 5)

    def test_teile_null_durch_zahl(self):
        self.assertEqual(teile(0, 2), 0)

    def test_teile_durch_null(self):
        with self.assertRaises(ZeroDivisionError):
            teile(5, 0)

    def test_ist_gerade(self):
        for zahl, erwartet in [(4, True), (7, False), (0, True), (-2, True)]:
            with self.subTest(zahl=zahl):
                self.assertEqual(ist_gerade(zahl), erwartet)


if __name__ == "__main__":
    unittest.main()
```

Die Klassenhülle fasst die Tests zusammen. `unittest.TestCase` stellt die Prüfmethoden bereit; `self` bezeichnet die jeweilige Testinstanz. Die Namen der Testmethoden beginnen mit `test_`.

`subTest` kennzeichnet einzelne Datensätze innerhalb einer Testmethode. So zeigt ein Fehlschlag, welche Eingabe betroffen war.

## Prüfmethoden

| Methode | Prüfung |
| --- | --- |
| `assertEqual(ist, soll)` | Werte sind gleich |
| `assertAlmostEqual(ist, soll)` | Differenz ist innerhalb der gewählten Genauigkeit |
| `assertTrue(wert)` / `assertFalse(wert)` | Wahrheitswert ist wahr / falsch |
| `assertRaises(Fehlerklasse)` | Der eingerückte Aufruf erzeugt den erwarteten Fehler |

Fließkommaergebnisse sind nicht immer exakt darstellbar. `assertAlmostEqual` prüft standardmäßig die auf sieben Nachkommastellen gerundete Differenz. Bei anderen Anforderungen kann die Genauigkeit ausdrücklich festgelegt werden.

## Tests starten

Vom Hauptordner des Repositories:

```bash
python3 tag4/09_unittests.py -v
python3 -m unittest -v tag4.loesungen.erfahren.test_statistik
```

`-v` zeigt die einzelnen Testnamen. `OK` bedeutet: Die ausgeführten Prüfungen haben bestanden. `FAIL` meldet eine verletzte Prüfbedingung; `ERROR` einen unerwarteten Fehler im Testablauf.

## Stolpersteine

- Ein Test ohne Prüfbedingung kann laufen, ohne das gewünschte Ergebnis zu kontrollieren.
- Die Berechnung im Test nicht nachbauen; sonst können beide Stellen denselben Fehler enthalten.
- Tests dürfen nicht von einer bestimmten Ausführungsreihenfolge abhängen.
- Zufallswerte oder Benutzereingaben erschweren wiederholbare Tests; Berechnung und Bedienung getrennt halten.
- Bestandene Tests belegen die geprüften Fälle, nicht die Fehlerfreiheit aller möglichen Eingaben.

## Schnellreferenz

```bash
python3 tag4/09_unittests.py -v
python3 -m unittest -v tag4.loesungen.erfahren.test_statistik
```

**Beispiel:** [Rechnertests](../../tag4/09_unittests.py)  
**Übung:** [Statistik testen](../../tag4/aufgaben/erfahren/test_statistik.md)
