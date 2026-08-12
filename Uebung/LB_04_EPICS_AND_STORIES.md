# Lottobude – Epics und Stories

## Ziel

Die Stories sind absichtlich **projektähnlich und nicht lehrbuchmäßig vollständig**. Sie sollen im Kurs gelesen, hinterfragt und gemeinsam mit einem simulierten Product Owner verbessert werden.

Die vollständigen fachlichen Regeln stehen separat in `BUSINESS_RULES.md`.

---

# EPIC-1 – Tipps abgeben

## LOTTO-101 – Tippschein anlegen

### User Story

Als Spieler möchte ich einen Tippschein für die nächste Ziehung anlegen, damit ich am Spiel teilnehmen kann.

### Beschreibung

Ein Tippschein kann mehrere Tipps enthalten. Jeder Tipp besteht aus sechs Lottozahlen.

### Akzeptanzkriterien

- Ein neuer Tippschein kann angelegt werden.
- Es können mehrere Tipps hinzugefügt werden.
- Ungültige Lottozahlen dürfen nicht gespeichert werden.
- Der Tippschein kann abgegeben werden.

### Offene Punkte für das Refinement

Bewusst nicht in der Story beantwortet.

---

## LOTTO-102 – Abgegebene Tipps ansehen

### User Story

Als Spieler möchte ich meine abgegebenen Tipps ansehen können.

### Akzeptanzkriterien

- Abgegebene Tippscheine werden angezeigt.
- Die zugehörige Ziehung ist erkennbar.
- Die Lottozahlen werden angezeigt.

---

# EPIC-2 – CSV-Import für Annahmestellen

## LOTTO-201 – Tipps per CSV importieren

### User Story

Als Annahmestelle möchte ich Lotto-Tipps per CSV-Datei hochladen, damit die Tipps nicht einzeln erfasst werden müssen.

### Beschreibung

Eine Datei enthält Tippscheine mit jeweils einem oder mehreren Tipps. Die Daten werden eingelesen und in der Datenbank bereitgestellt.

### Akzeptanzkriterien

- Eine CSV-Datei kann hochgeladen werden.
- Gültige Tipps werden gespeichert.
- Ungültige Daten werden abgewiesen.
- Nach dem Import wird ein Ergebnis angezeigt.

### Hinweise

Das genaue CSV-Format ist separat beschrieben.

---

## LOTTO-202 – Importfehler ansehen

### User Story

Als Annahmestelle möchte ich sehen, welche Daten beim Import nicht verarbeitet werden konnten.

### Akzeptanzkriterien

- Fehlerhafte Datensätze sind erkennbar.
- Ein Fehlergrund wird angezeigt.
- Die betroffene Stelle in der Datei soll nachvollziehbar sein.

---

## LOTTO-203 – Importhistorie

### User Story

Als Annahmestelle möchte ich frühere Importe sehen können.

### Akzeptanzkriterien

- Frühere Importe werden aufgelistet.
- Dateiname, Zeitpunkt und Ergebnis werden angezeigt.

---

# EPIC-3 – Ziehung

## LOTTO-301 – Ziehung anlegen

### User Story

Als Spielleitung möchte ich eine neue Ziehung anlegen.

### Akzeptanzkriterien

- Ein Ziehungstermin kann angelegt werden.
- Die Ziehung steht anschließend für Tippscheine zur Verfügung.

---

## LOTTO-302 – Gewinnzahlen erfassen

### User Story

Als Spielleitung möchte ich die Gewinnzahlen einer Ziehung erfassen, damit die Tipps ausgewertet werden können.

### Akzeptanzkriterien

- Sechs Gewinnzahlen können erfasst werden.
- Ungültige Gewinnzahlen werden nicht akzeptiert.
- Nach Abschluss gilt die Ziehung als durchgeführt.

---

# EPIC-4 – Auswertung

## LOTTO-401 – Tipps auswerten

### User Story

Als Spielleitung möchte ich nach einer Ziehung alle abgegebenen Tipps auswerten lassen.

### Akzeptanzkriterien

- Alle Tipps der Ziehung werden berücksichtigt.
- Die Trefferzahl wird bestimmt.
- Der zugehörige Gewinn wird ermittelt.
- Das Ergebnis wird gespeichert.

---

## LOTTO-402 – Spielergebnis anzeigen

### User Story

Als Spieler möchte ich nach der Auswertung sehen, wie meine Tipps abgeschnitten haben.

### Akzeptanzkriterien

- Gewinnzahlen werden angezeigt.
- Für jeden Tipp wird die Trefferzahl angezeigt.
- Ein Gewinn wird angezeigt, sofern einer entstanden ist.

---

# EPIC-5 – Administration / Trainingsbetrieb

## LOTTO-501 – Trainingsdaten zurücksetzen

### User Story

Als Kursleitung möchte ich die Trainingsumgebung auf einen definierten Ausgangszustand zurücksetzen können.

### Akzeptanzkriterien

- Trainingsdaten können vollständig zurückgesetzt werden.
- Definierte Benutzer, Annahmestellen und Ziehungen werden wiederhergestellt.
- Der Reset ist für normale Teilnehmer nicht verfügbar.

---

# Refinement-Fragen, die sich aus den Stories ergeben können

Diese Fragen gehören **nicht** zwingend in die Teilnehmerfassung. Sie dienen der Kursvorbereitung.

- Wie viele Tipps darf ein Tippschein enthalten?
- Was bedeutet „ungültige Lottozahlen“?
- Darf ein abgegebener Tippschein geändert werden?
- Was passiert mit teilweise fehlerhaften CSV-Dateien?
- Wie werden doppelte Importe behandelt?
- Welche Zeichencodierung hat eine CSV-Datei?
- Was passiert bei einer nicht existierenden Ziehung?
- Was passiert bei einem Datenbankfehler während eines Imports?
- Wann gilt eine Ziehung als abgeschlossen?
- Kann eine Ziehung erneut ausgewertet werden?
- Was passiert mit Tipps, die nach Durchführung einer Ziehung eintreffen?
- Welche Informationen darf ein Benutzer über andere Spieler sehen?
