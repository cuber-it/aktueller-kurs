# Tag 4 – Funktionen, Module und Tests

Abläufe in Funktionen zerlegen, Daten über Parameter übergeben und Ergebnisse
zurückgeben. Imports aus Tag 2 werden um eigene Module ergänzt.

## Beispiele

| Datei | Inhalt | Handout |
| --- | --- | --- |
| [01_funktionen_grundlagen.py](01_funktionen_grundlagen.py) | Definition, Aufruf, Rückgabe, Ausgabe und Docstrings | [Markdown](../docs/tag4/01_funktionen_grundlagen.md) |
| [02_parameter.py](02_parameter.py) | Positionsargumente, Schlüsselwortargumente und Standardwerte | [Markdown](../docs/tag4/02_parameter.md) |
| [03_args_kwargs.py](03_args_kwargs.py) | Argumente sammeln und beim Aufruf entpacken | [Markdown](../docs/tag4/03_args_kwargs.md) |
| [04_rueckgabe_und_scope.py](04_rueckgabe_und_scope.py) | Tupel als Rückgabe, frühes `return`, lokale Namen und `lambda` als Sortierschlüssel | [Markdown](../docs/tag4/04_rueckgabe_und_scope.md) |
| [05_eigene_module.py](05_eigene_module.py) | Funktionen aus dem Modul `geometrie` verwenden | [Markdown](../docs/tag4/05_eigene_module.md) |
| [06_import_varianten.py](06_import_varianten.py) | Importformen, Suchpfad und `__name__` | [Markdown](../docs/tag4/06_import_varianten.md) |
| [07_standardbibliothek.py](07_standardbibliothek.py) | Logstufen mit `pathlib`, `re` und `Counter` zählen | [Markdown](../docs/tag4/07_standardbibliothek.md) |
| [08_pip_und_pakete.py](08_pip_und_pakete.py) | Interpreter, virtuelle Umgebung und Paketversion prüfen | [Markdown](../docs/tag4/08_pip_und_pakete.md) |
| [09_unittests.py](09_unittests.py) | Normalfälle und Fehlerfälle mit `unittest` prüfen | [Markdown](../docs/tag4/09_unittests.md) |

Die Beispiele benötigen Python ab 3.10 und ausschließlich die Standardbibliothek.
Ausführen vom Hauptordner des Repositories:

```bash
python3 tag4/01_funktionen_grundlagen.py
python3 tag4/09_unittests.py -v
```

## Module und Umgebung

- [geometrie.py](geometrie.py): Kreisfläche und Kreisumfang; negative Radien werden abgewiesen.
- [rechner.py](rechner.py): Funktionen für das Testbeispiel.
- [data_source.py](data_source.py): gemeinsame Bibliothek für die Kursdatenaufgabe. Lädt CSV und SQLite in dieselbe Datenstruktur und berechnet Kennzahlen.
- [VENV.md](VENV.md): virtuelle Umgebungen und Paketverwaltung.

Die Kursdatenbibliothek erwartet Datensätze mit `date` im ISO-Format,
`close` als Zahl und `volume` als ganzer Zahl. Ladefunktionen sortieren
aufsteigend nach Datum. Kennzahlen bleiben bis zur Ausgabe ungerundet.
`save_sql()` ersetzt die vorhandenen Datensätze der Tabelle `quotes`.

## Übungen

- [Grundaufgaben](aufgaben/basic/): Begrüßung, Temperaturumrechnung, Würfeln und Lottofunktionen.
- [Vertiefungen](aufgaben/erfahren/): Statistik, Tests, ein eigenes Modul und Kursdatenanalyse.
- [Referenzlösungen](loesungen/): vollständige Lösungen mit getrennten Funktionsbausteinen und Hauptprogramm.

Eigene Lösungen in einem eigenen Arbeitsordner ablegen.
Programme mit mehreren zusammengehörenden Modulen werden vom Hauptordner aus
mit `-m` gestartet. Die Aufgabenbeschreibungen nennen den passenden Aufruf:

```bash
python3 -m tag4.loesungen.erfahren.use_statistik
python3 -m tag4.loesungen.erfahren.eigenes_modul
python3 -m unittest -v tag4.loesungen.erfahren.test_statistik
python3 -m tag4.loesungen.erfahren.kursanalyse
```

Die Kursdatenanalyse erzeugt Datenbank und JSON-Bericht in `tag4/ausgabe/`.
Der Ordner ist von Git ausgeschlossen.

## Ergänzende Experimente

`experimente/` zeigt eigene Imports, Namenskonflikte bei `from ... import`
und den CSV-Export nach SQLite. Die Programme ebenfalls als Module starten:

```bash
python3 -m tag4.experimente.import_1
python3 -m tag4.experimente.import_2
python3 -m tag4.experimente.quotes_2_sqlite
```
