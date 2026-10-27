# Einen interaktiven Taschenrechner schreiben

**Schwerpunkt:** Verzweigungen, Wiederholungen und gezielte Fehlerbehandlung.

## Schritt 1: eine Berechnung

1. Lies zwei Zahlen ein. Beide sollen Dezimalkomma und Dezimalpunkt erlauben.
2. Frage anschließend nach einem Operator: `+`, `-`, `*` oder `/`.
3. Führe die gewählte Rechenoperation aus.
4. Gib beide Zahlen, den Operator und das Ergebnis als nachvollziehbare Rechnung aus.

Es werden einzelne Rechnungen mit genau zwei Zahlen verarbeitet. Eine Auswertung zusammengesetzter Formeln ist nicht gefordert.

## Schritt 2: weitere Berechnungen

- Wiederhole die Abfragen nach jeder Rechnung.
- Frage nach jedem Durchlauf, ob weitergerechnet oder beendet werden soll.
- Die Eingabe `ende` an dieser Stelle beendet das Programm. Groß- und Kleinschreibung sollen dabei keine Rolle spielen.
- Verabschiede dich mit einer kurzen Ausgabe.
- Jede Rechnung verwendet zwei neu eingegebene Zahlen; das vorherige Ergebnis wird nicht automatisch übernommen.

## Schritt 3: Eingabefehler behandeln

Behandle diese Fälle mit jeweils einer verständlichen Meldung:

- Eine Zahl lässt sich nicht in eine Dezimalzahl umwandeln.
- Bei einer Division ist die zweite Zahl null.
- Der eingegebene Operator ist nicht unterstützt.

Nach einem Fehler muss die Frage „Weiter oder Ende?“ ebenfalls erscheinen. Bei Fortsetzung beginnt eine neue Rechnung.

Fange die Fehler gezielt ab. Eine eigene Exception für unbekannte Operatoren ist eine mögliche Zusatzaufgabe; für die Grundanforderungen brauchst du keine eigene Klasse.

## Prüfe dein Programm

| Erste Zahl | Zweite Zahl | Operator | Erwartetes Ergebnis oder Verhalten |
|---|---|---|---|
| 7,5 | 2 | / | 3.75 |
| 10 | 3 | - | 7.0 |
| -4 | 2,5 | * | -10.0 |
| 1.5 | 2,5 | + | 4.0 |
| abc | 2 | + | Meldung über ungültige Zahleneingabe |
| 8 | 0 | / | Meldung über Division durch null |
| 8 | 2 | % | Meldung über unbekannten Operator |

Bei einer ungültigen Zahl muss das Programm den Operator nicht mehr abfragen.

Prüfe außerdem eine Folge aus erfolgreicher Rechnung, fehlerhaftem Versuch und erfolgreicher Rechnung. Beende anschließend mit `ENDE`.

**Eigene Datei:** `tag2/loesungen/calculator.py`
