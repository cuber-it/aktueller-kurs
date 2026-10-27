# Import-Grundlagen

## Worum geht's

Python bringt eine umfangreiche **Standardbibliothek** mit — fertige Module mit Funktionen, Konstanten, Klassen. Mit `import` machst du sie verfügbar.

## Drei Formen

### 1. Komplettes Modul importieren

```python
import math

print(math.pi)
print(math.sqrt(2))
```

→ Aufruf mit Modulpräfix `math.foo`.

### 2. Einzelne Namen importieren

```python
from math import pi, sqrt

print(pi)
print(sqrt(2))
```

→ Aufruf **ohne** Präfix.

### 3. Mit `as` umbenennen

Praktisch bei langen Namen oder Kollisionen:

```python
import math as m
print(m.pi)

from math import sqrt as wurzel
print(wurzel(9))
```

## Was bedeutet was?

| Form                                 | Verfügbar als   |
|--------------------------------------|-----------------|
| `import math`                        | `math.pi`       |
| `import math as m`                   | `m.pi`          |
| `from math import pi`                | `pi`            |
| `from math import pi as konst`       | `konst`         |

## `from modul import *` (vermeiden!)

```python
from math import *      # importiert ALLES — schlechte Idee
```

Macht den Namensraum unübersichtlich, kann Variablen überschreiben. **Nicht verwenden** außer in REPL-Experimenten.

## Häufige Module der Standardbibliothek

| Modul        | Wofür                                |
|--------------|--------------------------------------|
| `math`       | mathematische Funktionen             |
| `random`     | Zufallszahlen                        |
| `datetime`   | Datum und Zeit                       |
| `os`         | Betriebssystem-Funktionen            |
| `sys`        | Interpreter, Argumente, exit         |
| `pathlib`    | Pfade objektorientiert               |
| `json`       | JSON lesen/schreiben                 |
| `re`         | Reguläre Ausdrücke                   |
| `csv`        | CSV-Dateien                          |
| `statistics` | Mittelwert, Median, …                |

```python
import random
random.randint(1, 6)             # Würfel

import datetime
datetime.date.today()

from pathlib import Path
Path.cwd()
```

## Wo werden Module gefunden?

Python sucht in dieser Reihenfolge:

1. eingebaute Module
2. Verzeichnis des aktuellen Skripts
3. `PYTHONPATH`-Umgebungsvariable
4. Standardbibliothek
5. installierte Pakete (z. B. via `pip`)

## Eigene Module

Jede `.py`-Datei ist ein Modul. Liegt `meinmodul.py` neben dem Skript:

```python
import meinmodul
meinmodul.meine_funktion()
```

## Externe Pakete (Ausblick)

Für alles außerhalb der Standardbibliothek → **`pip install paketname`** (mit aktivem venv). Beispiele: `requests`, `numpy`, `pandas`.

## Stolpersteine

- **Modul nicht installiert** → `ModuleNotFoundError`.
- **Zirkulärer Import** → A importiert B importiert A → mysteriöse Fehler.
- **Mehrfacher `import`** ist OK — Python cached.
- **Eigenes Skript heißt wie ein Standardmodul** (z. B. `random.py`!) → Konflikte. Niemals so benennen.

## Schnellreferenz

```python
import modul
import modul as kuerzel
from modul import name
from modul import name as alias

# vermeiden:
# from modul import *
```
