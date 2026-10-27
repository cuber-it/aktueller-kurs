# Den BMI mit Verzweigungen einordnen

**Schwerpunkt:** `if`, `elif`, `else` und lückenlose Wertebereiche.

## Aufgabe

Erweitere den [BMI-Rechner aus dem ersten Tag](../../tag1/aufgaben/bmi_calc.md). Ersetze die bisherige reine Wahrheitswert-Ausgabe durch die passende Kategorie.

1. Lies Name, Größe in Metern und Gewicht in Kilogramm ein.
2. Akzeptiere bei Größe und Gewicht Dezimalkomma und Dezimalpunkt.
3. Berechne den BMI als Gewicht geteilt durch die quadrierte Körpergröße.
4. Ermittle anhand der folgenden Tabelle genau eine Kategorie.
5. Gib den Namen, den BMI mit zwei Nachkommastellen und die Kategorie aus.

Du darfst gültige Eingaben und eine Größe größer als null voraussetzen.

## Vorgegebene Kategorien

Für diese Programmierübung verwenden wir folgende BMI-Kategorien für Erwachsene ab 20 Jahren:

| Ungerundeter BMI | Kategorie |
|---|---|
| kleiner als 18,5 | Untergewicht |
| ab 18,5 und kleiner als 25 | Normalgewicht |
| ab 25 und kleiner als 30 | Übergewicht |
| ab 30 und kleiner als 35 | Adipositas Grad I |
| ab 35 und kleiner als 40 | Adipositas Grad II |
| ab 40 | Adipositas Grad III |

Ordne den **ungerundeten** Wert ein. Die Bereiche müssen lückenlos sein; jeder BMI darf genau einer Kategorie zugeordnet werden.

Quelle der Bereichsgrenzen: [CDC – Adult BMI Categories](https://www.cdc.gov/bmi/adult-calculator/bmi-categories.html), geprüft am 27.10.2026.

## Prüfe dein Programm

Mit einer Größe von 2 Metern lassen sich die Grenzen leicht kontrollieren:

| Gewicht in kg | BMI | Erwartete Kategorie |
|---|---|---|
| 72 | 18.00 | Untergewicht |
| 74 | 18.50 | Normalgewicht |
| 99,8 | 24.95 | Normalgewicht |
| 100 | 25.00 | Übergewicht |
| 120 | 30.00 | Adipositas Grad I |
| 140 | 35.00 | Adipositas Grad II |
| 160 | 40.00 | Adipositas Grad III |

Prüfe zusätzlich Werte knapp unter den Grenzen. Achte darauf, dass eine gerundete Anzeige die Kategorie nicht nachträglich verändert.

**Eigene Datei:** `tag2/loesungen/bmi_ng.py`
