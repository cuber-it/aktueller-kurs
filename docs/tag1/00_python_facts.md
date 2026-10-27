# Python — Kurz-Fakten

## Steckbrief

- **Erstveröffentlichung:** 1991
- **Schöpfer:** Guido van Rossum (Niederlande)
- **Name:** kein Bezug zur Schlange, sondern zur britischen Comedy-Truppe **Monty Python**
- **Lizenz:** Open Source (Python Software Foundation License)
- **Aktuelle Version (Stand 2026):** Python 3.13
- **Referenzimplementierung:** CPython (in C geschrieben)

## Philosophie

- **Lesbarkeit vor Cleverness** — „Code wird öfter gelesen als geschrieben"
- **Eine offensichtliche Lösung** — Stichwort *Zen of Python*
- **Batteries included** — riesige Standardbibliothek
- **Multiparadigma** — prozedural, objektorientiert, funktional

Tippe einmal `import this` in den Interpreter — die 19 Leitsätze von Tim Peters (Easter Egg).

## Einsatzgebiete

| Feld                     | Typische Tools / Bibliotheken         |
|--------------------------|----------------------------------------|
| Web-Backend              | Django, Flask, FastAPI                 |
| Datenanalyse / Data Science | pandas, NumPy, Jupyter              |
| Machine Learning / KI    | PyTorch, TensorFlow, scikit-learn      |
| DevOps / Automatisierung | Ansible, Skripte, CI-Pipelines         |
| Wissenschaftliches Rechnen | SciPy, Astropy, BioPython            |
| Spiele / Grafik          | pygame                                 |
| Embedded                 | MicroPython, CircuitPython             |
| Testautomatisierung      | pytest, Selenium, Robot Framework      |

## Verbreitung

- Seit Jahren regelmäßig in den **Top 3** der Programmiersprachen-Rankings (TIOBE, Stack Overflow, GitHub).
- **De-facto-Standard** in Data Science, Machine Learning und wissenschaftlicher Programmierung.
- Auf praktisch jedem Linux/macOS-System vorinstalliert; auf Windows ein Installer-Klick.

## Python 2 vs. Python 3

Es gab einen großen, jahrelangen Bruch zwischen den beiden Hauptversionen.

- **Python 3.0** erschien 2008 — **bewusst inkompatibel** zu Python 2.
- **Python 2.7**, die letzte 2er-Version, wurde am **1. Januar 2020** offiziell **End-of-Life**.
- **Heute schreiben wir Python 3.** Punkt.

### Was sieht in Python 2.7 anders aus?

Du wirst diese Schreibweisen in altem Code antreffen:

| Python 2 (alt)                    | Python 3 (heute)               |
|-----------------------------------|--------------------------------|
| `print "Hallo"`                   | `print("Hallo")`               |
| `5 / 2 == 2` (Integer-Division)   | `5 / 2 == 2.5` (immer float)   |
| `raw_input()`                     | `input()`                      |
| `xrange()`                        | `range()`                      |
| getrennte Typen `str` + `unicode` | nur `str` (immer Unicode)      |
| `.iteritems()`, `.iterkeys()`     | `.items()`, `.keys()`          |
| `except Exception, e:`            | `except Exception as e:`       |
| `# -*- coding: utf-8 -*-` nötig   | UTF-8 ist Standard             |

### Wo lebt Python 2 noch?

- **Legacy-Systeme** in Banken, Behörden, älteren Industrieanlagen.
- **Embedded** in einzelnen Tools (alte Git-Hooks, ältere Linux-Distros).
- macOS hatte bis Catalina (2019) ein vorinstalliertes Python 2.7 — auf neueren Macs weg.

### Wenn du auf Python-2-Code triffst

- **Nicht in Panik geraten** — die Kernideen sind dieselben.
- **`2to3`** — mitgeliefertes Tool, das viele Patterns automatisch konvertiert.
- **Nicht als Vorlage für neuen Code verwenden.**

## Versionsverlauf (Highlights)

| Version | Jahr | Neuerung                                       |
|---------|------|------------------------------------------------|
| 2.7     | 2010 | letzte Python-2-Version (EOL 2020)             |
| 3.0     | 2008 | großer Reset                                   |
| 3.6     | 2016 | f-Strings                                      |
| 3.7     | 2018 | dataclasses, garantiert geordnete Dicts        |
| 3.8     | 2019 | Walross-Operator `:=`                          |
| 3.10    | 2021 | `match`/`case`, bessere Fehlermeldungen, `int \| str` |
| 3.11    | 2022 | ~25 % Performance-Schub                        |
| 3.12    | 2023 | f-Strings flexibler, bessere Diagnostik        |
| 3.13    | 2024 | experimenteller JIT, optionaler GIL-Free-Modus |

## Wo läuft Python?

- Linux, macOS, Windows, BSD
- im Browser (Pyodide, PyScript)
- auf Mikrocontrollern (MicroPython auf z. B. ESP32, Raspberry Pi Pico)
- eingebettet in Anwendungen (Blender, GIMP, FreeCAD, QGIS, …)

## Faustregeln für heute

- **Python 3** — nichts anderes.
- **Mindestens 3.10**, wenn du frei wählen kannst (`match`/`case`, `int | str`).
- **`venv` pro Projekt** — keine globalen Pakete installieren.
- **`pip`** für externe Pakete (PyPI).
- **`import this`** einmal gesehen haben.
