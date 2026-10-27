# Trinkgeld und Kosten pro Person berechnen

**Schwerpunkt:** Mehrere Eingaben verarbeiten, Prozentrechnung und Geldbeträge formatieren.

## Grundaufgabe

Eine Gruppe möchte ihre Rechnung einschließlich Trinkgeld gleichmäßig aufteilen.

1. Lies den Rechnungsbetrag, den gewünschten Trinkgeld-Prozentsatz und die Personenzahl ein.
2. Akzeptiere beim Rechnungsbetrag Dezimalkomma und Dezimalpunkt.
3. Berechne das Trinkgeld aus Rechnungsbetrag und Prozentsatz.
4. Berechne den Gesamtbetrag einschließlich Trinkgeld.
5. Berechne den Anteil pro Person.
6. Gib Rechnungsbetrag, Trinkgeld, Gesamtbetrag und Anteil pro Person mit jeweils zwei Nachkommastellen aus.

Der Prozentsatz wird als Prozentzahl eingegeben: `10` bedeutet zehn Prozent. Ein gebrochener Prozentsatz wird für diese Aufgabe mit Punkt eingegeben, zum Beispiel `7.5`.

Du darfst einen nichtnegativen Rechnungsbetrag und Prozentsatz sowie eine positive ganze Personenzahl voraussetzen. Runde erst bei der Ausgabe.

## Prüfe dein Programm

| Rechnung | Prozent | Personen | Trinkgeld | Gesamtbetrag | Pro Person |
|---|---|---|---|---|---|
| 42,50 | 10 | 3 | 4.25 | 46.75 | 15.58 |
| 80 | 5 | 2 | 4.00 | 84.00 | 42.00 |
| 100 | 0 | 4 | 0.00 | 100.00 | 25.00 |

Alle Geldwerte in der Tabelle sind Eurobeträge. Eine Verteilung verbleibender Rundungs-Cents auf einzelne Personen gehört nicht zur Aufgabe.

## Erweiterung: durch null teilen verhindern

Sobald du `if` kennengelernt hast, fange eine Personenzahl von null ab. Gib eine verständliche Fehlermeldung aus und beende den Vorgang ohne Berechnung des Anteils.

Probiere denselben Rechnungsbetrag einmal mit Komma und einmal mit Punkt. Das Ergebnis muss gleich sein.

**Eigene Datei:** `tag1/loesungen/trinkgeld.py`
