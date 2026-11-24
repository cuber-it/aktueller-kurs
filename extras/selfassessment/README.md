# Python Self-Assessment

Start: `python3 extras/selfassessment/selfassessment.py` (Python 3.10+, Tkinter/Tcl/Tk).
Unter Debian/Ubuntu/Mint ggf. `sudo apt install python3-tk`. Keine pip-Pakete nötig.

Lernmodus: sofortige Rückmeldung und Begründung. Prüfungsmodus: Lösungen erst nach Abschluss. Auswahl nach Tag, Thema und Schwierigkeit; Fragenzahl ist eine Obergrenze. Nicht beantwortete Fragen zählen bei Abschluss als falsch. Wiederholung verwendet die zuletzt falsch oder nicht beantworteten Fragen. Multiple Choice wird nur bei exakt richtiger Auswahl gewertet.

Lückentexte erwarten den fehlenden Ausdruck, nicht die ganze Zeile. Leerraum außerhalb von Literalen wird ignoriert, andere semantisch gleichwertige Lösungen müssen im Katalog ausdrücklich angegeben sein. Ausgabeantworten beachten Großschreibung, Leerzeichen und Zeilenumbrüche. Eingaben werden niemals als Python ausgeführt.

Fragen: JSON-Dateien in fragen/; IDs dauerhaft stabil halten. Fortschritt: lokale SQLite-Datei unter ~/.python-selfassessment/progress.sqlite3 (keine Netzwerkzugriffe). Löschen dieser Datei setzt den Verlauf zurück.

Tests: `python3 -m unittest discover -s extras/selfassessment/tests -v` vom Kurs-Hauptordner aus.

## Starter

- Linux/macOS: `./start.sh` im Anwendungsverzeichnis (oder per absolutem Pfad).
- Windows: `start.bat` per Doppelklick oder in der Eingabeaufforderung. Verwendet `py -3`, falls verfügbar, sonst `python`.

Beide Starter wechseln selbstständig in das Anwendungsverzeichnis. Python 3.10+ mit Tkinter muss installiert sein.
