# Tag 3 – Listen, Tupel, Sets und Dictionaries

Sammlungen erstellen, verändern und auswerten. Die Beispiele bauen auf den
Kontrollstrukturen, Dateioperationen und Imports aus Tag 1 und Tag 2 auf.

## Beispiele

| Datei | Inhalt | Handout |
| --- | --- | --- |
| [01_listen_grundlagen.py](01_listen_grundlagen.py) | Reihenfolge, Index, Slice, Veränderbarkeit, Referenz und flache Kopie | [Markdown](../docs/tag3/01_listen_grundlagen.md) |
| [02_listen_methoden.py](02_listen_methoden.py) | Elemente ergänzen, entfernen und sortieren | [Markdown](../docs/tag3/02_listen_methoden.md) |
| [03_tupel.py](03_tupel.py) | Unveränderliche Struktur, Entpacken und veränderliche enthaltene Objekte | [Markdown](../docs/tag3/03_tupel.md) |
| [04_sets.py](04_sets.py) | Eindeutige Elemente, Mitgliedschaft und Mengenoperationen | [Markdown](../docs/tag3/04_sets.md) |
| [05_arbeitstechniken_listen.py](05_arbeitstechniken_listen.py) | Comprehensions, `enumerate`, `zip`, Sortierung und Kennzahlen | [Markdown](../docs/tag3/05_arbeitstechniken_listen.md) |
| [06_dict_grundlagen.py](06_dict_grundlagen.py) | Schlüssel, Werte, Zugriff und Änderungen | [Markdown](../docs/tag3/06_dict_grundlagen.md) |
| [07_dict_methoden.py](07_dict_methoden.py) | Ansichten, Iteration, `setdefault` und `update` | [Markdown](../docs/tag3/07_dict_methoden.md) |
| [08_arbeitstechniken_dict.py](08_arbeitstechniken_dict.py) | Zählen, Gruppieren und Sortieren | [Markdown](../docs/tag3/08_arbeitstechniken_dict.md) |
| [09_verschachtelt_und_wahl.py](09_verschachtelt_und_wahl.py) | Verschachtelte Daten anhand der vorhandenen `person.json` | [Markdown](../docs/tag3/09_verschachtelt_und_wahl.md) |

Ausführen vom Hauptordner des Repositories, beispielsweise:

```bash
python3 tag3/01_listen_grundlagen.py
```

Die Beispiele benötigen Python ab 3.10 und ausschließlich die Standardbibliothek.
Pfade zu Materialien werden aus dem Speicherort des Skripts abgeleitet.

## Übungen

- [Grundaufgaben](aufgaben/basic/): Einkaufsliste, Telefonbuch, eindeutige Wörter und Lottoziehung.
- [Vertiefungen](aufgaben/erfahren/): Mengenvergleich, Lottovergleich, Noten, Worthäufigkeiten, Kontaktverwaltung und Ordnervergleich.
- [Referenzlösungen](loesungen/): vollständige Lösungen zu den jeweiligen Grundaufgaben; optionale Erweiterungen sind gesondert beschrieben.

Jede Aufgabenbeschreibung nennt Anforderungen und überprüfbare Ergebnisse.
Eigene Lösungen in einem eigenen Arbeitsordner ablegen.

## Ergänzende Experimente

`experimente/` enthält einzelne Vertiefungen, unter anderem zu verschachtelten
Listen, Dateidaten sowie flachen und tiefen Kopien.

`rolo_gui.py` ist ein optionaler Ausblick auf eine Oberfläche mit Tkinter und
Klassen. Diese Techniken gehören nicht zu den Voraussetzungen der Übungen.
Der CSV-Export nach SQLite liegt bei Tag 4, da er eigene Funktionen und Module nutzt.
