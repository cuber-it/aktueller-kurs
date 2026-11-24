# Die Standardbibliothek verwenden

## Worum geht's

Die Standardbibliothek enthält Module für Dateipfade, Textverarbeitung, Berechnungen und Datenformate. Das Beispiel verbindet mehrere davon zu einer Logauswertung. Zusätzliche Pakete sind dafür nicht erforderlich.

## Module nach Aufgabe auswählen

| Modul | Aufgabe im Kurs |
| --- | --- |
| `pathlib` | Materialpfade zusammensetzen und Dateien öffnen |
| `re` | Logstufen mit einem Muster erkennen |
| `collections` | Häufigkeiten mit `Counter` zählen |
| `csv` | Felder aus `HistoricalQuotes.csv` lesen |
| `json` | Personen laden und einen Bericht speichern |
| `sqlite3` | Kursdaten in einer lokalen Datenbank speichern |
| `math` | Kreisberechnung mit `pi` |
| `random` | Würfelwerte und Lottoziehungen erzeugen |
| `datetime` | Datumstexte in Datumswerte umwandeln |
| `sys` | Verwendeten Interpreter und Suchpfad prüfen |

Die Auswahl richtet sich nach der Aufgabe: Ein CSV-Parser berücksichtigt beispielsweise auch Anführungszeichen und eingebettete Trennzeichen, die ein einfaches `split(",")` nicht korrekt behandeln würde.

## Logstufen erkennen und zählen

Die vorhandene Datei enthält unter anderem Zeilen dieser Form:

```text
03/22 08:51:01 INFO   :.main: *************** RSVP Agent started ***************
```

```python
from collections import Counter
from pathlib import Path
import re


def zaehle_stufen(pfad):
    """Zählt erkannte Logstufen in der übergebenen Datei."""
    anzahl = Counter()
    with Path(pfad).open(encoding="utf-8") as quelle:
        for zeile in quelle:
            treffer = re.search(r"\s([A-Z]+)\s*:", zeile)
            if treffer:
                anzahl[treffer.group(1)] += 1
    return anzahl
```

- `Path(pfad).open(...)` öffnet die Datei; `with` schließt sie am Blockende.
- `re.search` sucht die Logstufe nach einem Leerraumzeichen und vor dem Doppelpunkt.
- `([A-Z]+)` ist die erste Gruppe; `group(1)` liefert ihren Text.
- `Counter` erhöht den Zähler dieser Stufe.
- Zeilen ohne passenden Treffer bleiben ungezählt.

Die Funktion erhält einen Pfad und liefert Daten zurück. Sie legt weder den Materialordner noch die Darstellung des Ergebnisses fest.

## Vorhandenes Material auswerten

Vom Hauptordner des Repositories, im Anschluss an die Funktionsdefinition:

```python
pfad = Path("materialien/small_sample.log")
anzahl = zaehle_stufen(pfad)

for stufe in sorted(anzahl):
    print(f"{stufe}: {anzahl[stufe]}")
print("Erkannte Logzeilen:", sum(anzahl.values()))
```

Für die vorhandene Datei:

```text
EVENT: 2
INFO: 77
TRACE: 17
WARNING: 4
Erkannte Logzeilen: 100
```

Das vollständige Kursskript leitet den Materialpfad aus `__file__` ab. Sein Start hängt deshalb nicht vom aktuellen Arbeitsverzeichnis ab.

## Funktionen zusammenfügen

Die Logauswertung trennt drei Schritte: Daten lesen, Logstufen zählen und Ergebnisse ausgeben. In der Kursdatenaufgabe wird derselbe Aufbau für CSV, SQLite und einen JSON-Bericht verwendet.

`data_source.py` liefert eine nach Datum sortierte Liste von Dictionaries: `date` als ISO-Datumstext, `close` als Zahl und `volume` als Ganzzahl. Dadurch können dieselben Auswertungsfunktionen Daten aus beiden Quellen verarbeiten.

## Stolpersteine

- Dateiinhalte sind zunächst Text; Zahlenfelder müssen bei Bedarf umgewandelt werden.
- Reguläre Ausdrücke müssen zum tatsächlichen Dateiformat passen.
- Ein relativer `Path` bezieht sich auf das Arbeitsverzeichnis.
- Standardbibliotheksmodule werden importiert, nicht mit pip nachinstalliert.

## Schnellreferenz

| Verarbeitungsschritt | Werkzeug |
| --- | --- |
| Pfad und Datei | `Path`, `open`, `with` |
| Treffer suchen | `re.search` |
| Häufigkeiten | `Counter` |
| Geordnete Ausgabe | `sorted` und `for` |

**Beispiel:** [Logauswertung](../../tag4/07_standardbibliothek.py)  
**Material:** [small_sample.log](../../materialien/small_sample.log)  
**Übung:** [Kursdatenanalyse](../../tag4/aufgaben/erfahren/kursanalyse.md)
