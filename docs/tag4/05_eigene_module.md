# Eigene Module

## Worum geht's

Eine Python-Datei kann Funktionen und Konstanten für andere Programme bereitstellen. Du importierst dieses **Modul**, statt seine Funktionen in mehrere Dateien zu kopieren.

## Ein Modul anlegen

Die Datei heißt `geometrie.py`:

```python
"""Berechnungen für Kreise mit nicht negativem Radius."""

from math import pi as PI


def kreis_flaeche(radius):
    """Liefert die Kreisfläche."""
    if radius < 0:
        raise ValueError("Der Radius darf nicht negativ sein.")
    return PI * radius ** 2


def kreis_umfang(radius):
    """Liefert den Kreisumfang."""
    if radius < 0:
        raise ValueError("Der Radius darf nicht negativ sein.")
    return 2 * PI * radius
```

Der Modulname beim Import lautet `geometrie`, ohne `.py`. `PI` ist ein konventionell großgeschriebener Konstantenname. Python verhindert dadurch keine Neuzuweisung.

## Das Modul verwenden

Eine zweite Datei liegt im selben Ordner:

```python
import geometrie

flaeche = geometrie.kreis_flaeche(2)
umfang = geometrie.kreis_umfang(2)

print(f"Fläche: {flaeche:.2f}")    # Fläche: 12.57
print(f"Umfang: {umfang:.2f}")     # Umfang: 12.57
```

Beim normalen direkten Skriptstart gehört der Skriptordner zum Modulsuchpfad. So wird das benachbarte `geometrie.py` gefunden.

Der Punkt verbindet Modul und darin definierten Namen. `geometrie.kreis_flaeche` bezeichnet die Funktion; die nachfolgenden Klammern rufen sie auf.

## Drei Importformen

| Form | Funktionsaufruf |
| --- | --- |
| `import geometrie` | `geometrie.kreis_flaeche(2)` |
| `from geometrie import kreis_flaeche` | `kreis_flaeche(2)` |
| `import geometrie as geo` | `geo.kreis_flaeche(2)` |

`from` bindet den ausgewählten Namen im importierenden Modul. Ein Modulpräfix macht dessen Herkunft beim Lesen sichtbar. Ein Alias sollte kurz, aber noch verständlich sein.

Das Kursbeispiel lässt sich vom Hauptordner aus starten:

```bash
python3 tag4/05_eigene_module.py
```

## Was beim Import geschieht

Beim ersten Import in einem Interpreterprozess führt Python die Anweisungen auf Modulebene aus. Dazu gehören die Funktionsdefinitionen; ihre Körper laufen erst bei einem Aufruf.

Weitere normale Imports verwenden das bereits geladene Modul. Sie führen seinen Code nicht jedes Mal neu aus. Eine Änderung an einer Moduldatei wird deshalb nicht automatisch in einen laufenden Interpreter übernommen.

Ausführbare Demos gehören unter eine `__main__`-Bedingung; das folgt im nächsten Kapitel.

## Zusammengehörige Funktionen bündeln

`geometrie.py` enthält Kreisberechnungen, `rechner.py` kleine Rechenfunktionen und `data_source.py` das Laden und Auswerten von Kursdaten. Ein Aufrufer kann diese Bausteine verwenden, ohne ihre Umsetzung zu wiederholen.

## Stolpersteine

- Eigene Dateien wie `random.py` oder `json.py` können gleichnamige Bibliotheksmodule verdecken.
- Für direkte `import`-Anweisungen müssen Modulnamen gültige Python-Bezeichner sein: etwa `geometrie`, mit Buchstaben oder `_` beginnend.
- Ein nicht auffindbares Modul erzeugt `ModuleNotFoundError`.
- Gegenseitige Imports können auf nur teilweise initialisierte Module treffen.
- Eine Ausgabe auf Modulebene läuft auch beim Import.

## Schnellreferenz

```python
import geometrie
from geometrie import kreis_flaeche
import geometrie as geo

print(geometrie.kreis_flaeche(2))
print(kreis_flaeche(2))
print(geo.kreis_umfang(2))
```

**Beispiel:** [Eigene Module](../../tag4/05_eigene_module.py)  
**Modul:** [geometrie.py](../../tag4/geometrie.py)  
**Übung:** [Eigenes Textmodul](../../tag4/aufgaben/erfahren/eigenes_modul.md)
