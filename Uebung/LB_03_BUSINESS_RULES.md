# Lottobude – Business Rules

Diese Datei beschreibt den fachlichen Sollzustand. Die Stories dürfen absichtlich weniger vollständig formuliert sein, damit sie im Training analysiert und challenged werden können.

## Tipps

### BR-TIP-001 – Anzahl Zahlen
Ein Tipp enthält genau sechs Zahlen.

### BR-TIP-002 – Wertebereich
Jede Tippzahl ist eine ganze Zahl zwischen 1 und 49 einschließlich.

### BR-TIP-003 – Eindeutigkeit
Innerhalb eines Tipps darf jede Zahl nur einmal vorkommen.

### BR-TIP-004 – Reihenfolge
Die Reihenfolge der Zahlen hat fachlich keine Bedeutung.

## Tippscheine

### BR-TICKET-001 – Anzahl Tipps
Ein Tippschein enthält mindestens 1 und höchstens 10 Tipps.

### BR-TICKET-002 – Ziehung
Ein Tippschein muss einer existierenden, noch offenen Ziehung zugeordnet sein.

### BR-TICKET-003 – Abgabe
Ein Tippschein im Status `ABGEGEBEN` darf fachlich nicht mehr verändert werden.

### BR-TICKET-004 – Quelle
Ein Tippschein stammt entweder aus der Webeingabe oder aus einem CSV-Import.

## Ziehungen

### BR-DRAW-001 – Gewinnzahlen
Eine Ziehung besteht aus genau sechs unterschiedlichen Zahlen aus 1..49.

### BR-DRAW-002 – Statusfolge
Zulässige Statusfolge:

`GEPLANT -> DURCHGEFUEHRT -> AUSGEWERTET`

### BR-DRAW-003 – Auswertung
Nur eine durchgeführte Ziehung darf ausgewertet werden.

### BR-DRAW-004 – Wiederholung
Eine bereits ausgewertete Ziehung darf nicht erneut ausgewertet werden.

## Gewinnermittlung

Für die Trainingsversion gilt:

| Treffer | Gewinn |
|---:|---:|
| 6 | 1.000.000 € |
| 5 | 10.000 € |
| 4 | 100 € |
| 3 | 10 € |
| 0–2 | 0 € |

### BR-WIN-001
Die Trefferzahl ist die Anzahl der Tippzahlen, die in den sechs Gewinnzahlen enthalten sind.

### BR-WIN-002
Jeder Tipp wird unabhängig ausgewertet.

### BR-WIN-003
Das Auswertungsergebnis wird persistiert.

## CSV-Import

### BR-CSV-001
Eine Datei gehört genau zu einer Annahmestelle.

### BR-CSV-002
Ein importierter Tippschein enthält 1 bis 10 Tipps.

### BR-CSV-003
Für importierte Tipps gelten dieselben fachlichen Regeln wie für Web-Tipps.

### BR-CSV-004
Syntaktisch oder fachlich fehlerhafte Datensätze werden nicht als gültige Tipps gespeichert.

### BR-CSV-005
Fehler müssen mit Zeilennummer und Fehlergrund nachvollziehbar sein.

### BR-CSV-006
Die Importstatistik unterscheidet mindestens Gesamtzahl, erfolgreich importiert und abgewiesen.

### BR-CSV-007
Wie mit teilweise fehlerhaften Dateien umgegangen wird, ist eine explizite Produktentscheidung und soll in einer Story festgelegt werden.

## Benutzer

### BR-USER-001
Nur aktive Benutzer dürfen neue Tippscheine abgeben.

### BR-USER-002
Ein Benutzer sieht nur seine eigenen Tippscheine und Ergebnisse.

## Annahmestellen

### BR-OUTLET-001
Nur aktive Annahmestellen dürfen CSV-Dateien importieren.

## Konsistenz

### BR-CONS-001
GUI, API und CSV-Import müssen dieselben fachlichen Regeln anwenden.

### BR-CONS-002
Eine erfolgreiche Antwort darf nicht gemeldet werden, wenn die zugehörigen Daten nicht dauerhaft gespeichert wurden.
