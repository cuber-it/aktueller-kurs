# BMI mit Dialogfenstern berechnen

**Zusatzaufgabe. Schwerpunkt:** Eine bekannte Berechnung mit einer anderen Ein- und Ausgabe verbinden.

## Aufgabe

Erstelle eine Variante des [BMI-Rechners](bmi_calc.md), bei der die Ein- und Ausgabe über grafische Dialogfenster erfolgt.

1. Frage Name, Größe in Metern und Gewicht in Kilogramm jeweils in einem Eingabedialog ab.
2. Akzeptiere bei Größe und Gewicht Dezimalkomma und Dezimalpunkt.
3. Berechne den BMI als Gewicht geteilt durch die quadrierte Körpergröße.
4. Prüfe das vorgegebene Intervall von **18,5 bis einschließlich 24,9**.
5. Zeige den BMI mit zwei Nachkommastellen und das Prüfergebnis als `True` oder `False` in einem Meldungsfenster an.

Die Bereichsprüfung verwendet den ungerundeten Wert. Für die Aufgabe darfst du gültige Zahlen, eine Größe größer als null und bestätigte Eingabedialoge voraussetzen. Die Behandlung der Schaltfläche „Abbrechen“ ist eine mögliche spätere Erweiterung.

## Vorbereitung

Du brauchst eine grafische Umgebung und eine Python-Installation mit Tkinter. Die Dialogfunktionen können als vorbereitete Bausteine übernommen werden; ihre interne Umsetzung ist kein Lernziel der Grundübung.

Die Berechnung soll unabhängig davon gleich bleiben, ob die Werte aus der Konsole oder aus Dialogfenstern stammen.

## Prüfe dein Programm

| Name | Größe in m | Gewicht in kg | Erwartetes Ergebnis im Meldungsfenster |
|---|---|---|---|
| Anna | 1,80 | 75 | BMI 23.15 und True |
| Ben | 2 | 100 | BMI 25.00 und False |

Prüfe zusätzlich dieselben Zahlen einmal mit Komma und einmal mit Punkt.

**Eigene Datei:** `tag1/loesungen/bmi_calc_win.py`
