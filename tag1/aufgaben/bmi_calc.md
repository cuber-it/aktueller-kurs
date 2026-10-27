# BMI berechnen

**Schwerpunkt:** Eingabe, Typkonvertierung, Rechnen, Vergleiche und formatierte Ausgabe.

## Aufgabe

Schreibe ein Konsolenprogramm, das aus Körpergröße und Gewicht einen BMI berechnet.

1. Lies einen Namen, die Körpergröße in Metern und das Gewicht in Kilogramm ein.
2. Akzeptiere bei Größe und Gewicht sowohl ein Dezimalkomma als auch einen Dezimalpunkt.
3. Wandle die Zahlen in einen passenden Datentyp um.
4. Berechne: **BMI = Gewicht / (Körpergröße × Körpergröße)**.
5. Prüfe, ob der BMI im vorgegebenen Intervall **18,5 bis einschließlich 24,9** liegt.
6. Gib den BMI mit genau zwei Nachkommastellen und das Prüfergebnis als `True` oder `False` aus.

Für die Grundaufgabe darfst du gültige Eingaben und eine Größe größer als null voraussetzen. Der Name wird erfasst; du kannst ihn zusätzlich in der Ausgabe verwenden.

## Prüfe dein Programm

| Größe in m | Gewicht in kg | Angezeigter BMI | Im vorgegebenen Intervall? |
|---|---|---|---|
| 1,80 | 75 | 23.15 | True |
| 2 | 74 | 18.50 | True |
| 2 | 99,6 | 24.90 | True |
| 2 | 100 | 25.00 | False |
| 2 | 99,61 | 24.90 | False |

Die letzte Zeile ist beabsichtigt: Die Bereichsprüfung verwendet den **ungerundeten** Wert. Nur die Anzeige wird gerundet. Das Intervall ist eine Vorgabe dieser Rechenaufgabe.

## Hinweise

- Trenne gedanklich Eingabe, Verarbeitung und Ausgabe.
- Eingaben sind zunächst Strings.
- Für die Bereichsprüfung reicht ein Vergleichsausdruck; eine Verzweigung ist nicht nötig.

**Eigene Datei:** `tag1/loesungen/bmi_calc.py`
