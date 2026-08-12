# Lottobude – Trainingskonzept

## Ziel

Lottobude ist nicht nur eine Demo-Anwendung. Sie soll Teilnehmern eine realistische, zusammenhängende QA-Aufgabe geben.

Die Teilnehmer sollen nicht bloß vorgegebene Testverfahren anwenden, sondern den vollständigen Weg erleben:

```text
Story
  -> verstehen
  -> challengen
  -> Akzeptanzkriterien verbessern
  -> Risiken erkennen
  -> Testideen entwickeln
  -> Testfälle ableiten
  -> Testdaten erzeugen
  -> Tests durchführen
  -> Defects finden
  -> neue Testfälle ergänzen
  -> Regression bestimmen
  -> Automatisierung auswählen
```

## Teilnehmerperspektive

Die Teilnehmer erhalten:

- ausgewählte Stories,
- eine laufende Lottobude-Instanz,
- Weboberfläche,
- API/OpenAPI,
- CSV-Beispieldateien,
- bei Bedarf eingeschränkte Einsicht in gespeicherte Daten.

Sie erhalten **nicht**:

- die vollständige Liste der eingebauten Fehler,
- interne Lösungsunterlagen,
- alle Business Rules auf einmal.

## Kursleitungsperspektive

Die Kursleitung besitzt:

- vollständige Business Rules,
- Sollverhalten,
- Bug-Katalog,
- Reset-Funktion,
- vorbereitete Fixtures,
- Muster-Testideen,
- erwartete Ergebnisse.

## Übungsphasen

### 1. Refinement

Teilnehmer bekommen eine realistisch unvollständige Story.

Aufgabe:

- Unklarheiten finden
- fehlende Regeln erkennen
- Fragen an den Product Owner formulieren
- Akzeptanzkriterien verbessern

### 2. Testdesign

Aufgabe:

- Happy Path
- relevante Negativfälle
- Grenzfälle
- Zustände
- Kombinationen
- Risiken

Methoden werden dort eingesetzt, wo sie einen konkreten Nutzen haben.

### 3. Testdaten

Teilnehmer erzeugen konkrete Daten für ihre Testfälle.

Mögliche Hilfsmittel:

- manuell
- Generatoren
- Skripte
- KI

### 4. Durchführung

Tests werden gegen die echte Trainingsanwendung ausgeführt.

### 5. Defects

Gefundene Abweichungen werden reproduzierbar dokumentiert.

### 6. Review

Verglichen werden:

- gefundene Fehler
- nicht gefundene Fehler
- redundante Tests
- fehlende Tests
- Qualität der Testdaten
- Qualität des Testorakels

### 7. Automatisierungsentscheidung

Für ausgewählte Tests wird entschieden:

- Unit
- Integration
- API
- GUI
- nicht automatisieren

## Geplante Fehlerklassen

Die konkrete Implementierung der Bugs wird separat geführt.

Die Trainingsversion sollte Fehler aus mehreren Kategorien enthalten:

### Grenzwerte

Beispiele:

- 0 Tipps akzeptiert
- 11 Tipps akzeptiert
- Lottozahl 50 akzeptiert

### Äquivalenzklassen / Validierung

Beispiele:

- nicht numerischer Wert führt zu falscher Behandlung
- Duplikate werden nicht erkannt

### CSV / Syntax

Beispiele:

- leere Datei meldet Erfolg
- falscher Header wird akzeptiert
- Separator-/Encoding-Sonderfall

### Entscheidungslogik

Beispiele:

- falsche Gewinnklasse bei bestimmter Trefferzahl
- eine Kombination von Bedingungen wird falsch behandelt

### Zustände

Beispiele:

- abgegebener Tippschein kann geändert werden
- abgeschlossene Ziehung kann erneut verändert werden
- Auswertung kann im falschen Zustand gestartet werden

### Integration / Persistenz

Beispiele:

- UI meldet Erfolg, Datensatz fehlt in DB
- Teilimport erzeugt inkonsistente Zähler
- Transaktionsfehler hinterlässt halbe Daten

### Berechtigungen

Beispiel:

- Benutzer kann fremden Tippschein über direkte URL/API sehen

### API / GUI-Divergenz

Beispiel:

- GUI validiert einen Wert, API akzeptiert ihn trotzdem

## Anzahl eingebauter Bugs

Empfehlung für die erste Version:

- 10 bis 15 reproduzierbare Bugs
- unterschiedliche Schweregrade
- nicht alle über denselben Testansatz auffindbar
- mindestens ein Fehler nur über API/DB gut erkennbar
- mindestens ein Fehler aus einem Zustandsübergang
- mindestens ein Fehler aus einer Kombination mehrerer Bedingungen

## Bug-Konfiguration

Bugs sollten möglichst über Feature-/Bug-Toggles aktivierbar sein.

Beispielkonzept:

```text
BUG_ACCEPT_ZERO_TIPS=true
BUG_ACCEPT_NUMBER_50=true
BUG_ALLOW_EDIT_SUBMITTED=true
```

Damit können unterschiedliche Trainingsstände erzeugt werden, ohne verschiedene Codebasen zu pflegen.

## Fixtures

Definierter Ausgangszustand:

- 2 Benutzer
- 2 Annahmestellen
- 1 offene Ziehung
- 1 abgeschlossene Ziehung
- einige vorhandene Tippscheine
- definierte CSV-Beispieldateien

## Reset

Die Kursleitung benötigt einen zuverlässigen Reset:

```text
reset
 -> Daten löschen
 -> Fixtures laden
 -> Bug-Konfiguration beibehalten
 -> Anwendung wieder im definierten Zustand
```

## KI im Training

KI soll als QA-Sparringspartner eingesetzt werden, nicht als automatische Lösungsmaschine.

Geeignete Aufgaben:

- Story challengen
- fehlende Akzeptanzkriterien suchen
- Risiken ergänzen
- Testideen challengen
- Testdaten erzeugen
- Testfallmenge auf Redundanz prüfen
- mögliche Edge Cases suchen

Interessanter Vergleich:

1. Teilnehmer erstellt eigene Testideen.
2. KI challenged diese.
3. Teilnehmer entscheidet, welche Vorschläge fachlich sinnvoll sind.
4. Tests werden tatsächlich gegen Lottobude ausgeführt.

## Erfolgskriterium der Gesamtübung

Die Übung ist erfolgreich, wenn die Teilnehmer am Ende nicht nur eine Liste von Testfällen besitzen, sondern nachvollziehen können, **warum genau diese Tests ausgewählt wurden, welches Risiko sie adressieren, welche Daten sie benötigen und woran das korrekte Ergebnis erkannt wird.**
