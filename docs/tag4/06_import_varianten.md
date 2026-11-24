# Import-Varianten und Programmstart

## Worum geht's

Ein Modul besitzt einen eigenen Namensraum. Importformen bestimmen, welche Namen beim Aufrufer verfügbar sind. `__name__` unterscheidet den direkten Programmstart vom Import.

## Modulname, Alias und Funktionsname

```python
import geometrie as geo
from geometrie import kreis_flaeche

print(geo.__name__)                    # geometrie
print(f"{geo.kreis_flaeche(2):.2f}")    # 12.57
print(f"{kreis_flaeche(2):.2f}")        # 12.57
```

`geo` ist ein lokaler Alias für dasselbe Modul. Dessen eigener Name bleibt `geometrie`. `kreis_flaeche` wird durch `from` zusätzlich direkt verfügbar.

`from modul import *` macht die Herkunft der eingebundenen Namen schwer erkennbar und kann vorhandene Namen überdecken. Die Kursbeispiele benennen ihre Imports ausdrücklich.

## `__name__` und `main`

```python
import geometrie


def main():
    """Führt das Hauptprogramm aus."""
    print("Programmname:", __name__)
    print(f"Fläche: {geometrie.kreis_flaeche(2):.2f}")


if __name__ == "__main__":
    main()
```

| Verwendung dieser Datei | Wert von `__name__` | Läuft `main()`? |
| --- | --- | --- |
| Direkt als Skript gestartet | `"__main__"` | Ja |
| Mit `-m` als Hauptprogramm gestartet | `"__main__"` | Ja |
| Als Modul importiert | Importname des Moduls | Nein |

`main` ist ein frei gewählter Funktionsname; Python ruft diese Funktion nicht automatisch auf. Erst die letzte Zeile tut das, wenn die Bedingung zutrifft.

Die Bedingung schützt nur ihren eingerückten Block. Andere Anweisungen auf Modulebene werden beim Import weiterhin ausgeführt.

## Wo Python Module findet

Bereits geladene Module werden normalerweise aus dem Modulcache verwendet. Für weitere Imports berücksichtigt Python unter anderem eingebaute Module und die Einträge in `sys.path`.

Beim normalen Start gilt:

- `python3 pfad/programm.py` nimmt den Skriptordner an den Anfang von `sys.path`.
- `python3 -m paket.modul` verwendet dafür das aktuelle Arbeitsverzeichnis.
- Weitere Einträge ergeben sich unter anderem aus `PYTHONPATH`, Standardbibliothek und installierten Paketen.

`sys.path` lässt sich zur Fehlersuche ausgeben:

```python
import sys
print(sys.path)
```

## Zusammengehörige Module als Paket

Die Referenzlösungen von Tag 4 liegen in Paketen mit `__init__.py`. In `use_statistik.py` verweist dieser Import auf das benachbarte Modul im selben Paket:

```python
from .statistik import statistik

print(statistik(7, 2, 9, 4))    # (2, 9, 5.5)
```

Der führende Punkt bedeutet „aus diesem Paket“. Der Aufruf erfolgt vom Hauptordner des Repositories:

```bash
python3 -m tag4.loesungen.erfahren.use_statistik
```

`-m` stellt den Paketkontext her. Der direkte Dateistart dieses Moduls ist für den relativen Import nicht geeignet. Ein reguläres Paket verwendet `__init__.py`; daneben gibt es Namespace-Pakete ohne diese Datei.

## Stolpersteine

- `main` allein startet keine Funktion; erforderlich ist `main()`.
- Ein Alias benennt das Modul selbst nicht um.
- Relative Imports brauchen einen Paketkontext.
- Eine fehlende Importquelle zuerst anhand von Dateinamen, Startverzeichnis und Interpreter prüfen.

## Schnellreferenz

| Zweck | Schreibweise |
| --- | --- |
| Modul mit Alias | `import geometrie as geo` |
| Einen Namen importieren | `from geometrie import kreis_flaeche` |
| Skriptstart erkennen | `if __name__ == "__main__":` |
| Modul im Paket starten | `python3 -m paket.modul` |

**Beispiel:** [Import und Programmstart](../../tag4/06_import_varianten.py)  
**Vertiefung:** [Namenskonflikte bei Imports](../../tag4/experimente/import_2.py)
