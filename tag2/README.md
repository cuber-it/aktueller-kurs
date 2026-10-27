# Tag 2 – Kontrollstrukturen, Imports, Regex, Dateien, Fehlerbehandlung, Datenformate

Aufbauend auf Tag 1: Programme verzweigen und wiederholen, Module nutzen, Texte mit Mustern durchsuchen, Dateien einlesen, Fehler abfangen und einen ersten Blick auf strukturierte Daten werfen.

## Themen

1. **`if` / `elif` / `else`**
   - klassische Verzweigung
   - **Einzeiler** (ternärer Ausdruck): `wert = a if bedingung else b`
   - Wahrheitswerte und Truthiness
   - Einrückung als Syntaxelement

2. **`while`-Schleife** – inkl. `break`, `continue`

3. **`for`-Schleife** – mit `range()` und über Strings / Dateizeilen

4. **Sonderkapitel: Moderne Kontrollstrukturen**
   - `match` / `case` (seit Python 3.10) – Anriss

5. **Import-Grundlagen**
   - `import modul`, `from modul import name`, `as`
   - kurzer Streifzug durch die Standardbibliothek (`math`, `random`, …)

6. **Regex (Anriss)**
   - `import re`, `re.search`, `re.findall`, `re.sub`
   - Basics: `\d`, `\w`, `\s`, `[abc]`, `*`, `+`, `?`, `^`, `$`, `\b`
   - Hinweis: für Extraktion super, für strikte Validierung andere Tools

7. **Datei-Input**
   - `with open(...) as f:`
   - zeilenweise lesen

8. **Fehlerbehandlung**
   - `try` / `except` / `else` / `finally`
   - typische Exceptions (`ValueError`, `ZeroDivisionError`, `FileNotFoundError`)
   - bewusst Fehler werfen mit `raise`

9. **Extrakapitel: JSON, YAML, SQLite**
   - JSON in Strings und Dateien (`json.loads/dumps`, `json.load/dump`)
   - YAML als lesbare Konfiguration (externes Paket `pyyaml`)
   - SQLite als eingebaute Datei-Datenbank, parametrisierte Queries

## Lernziel

Du kannst Programme schreiben, die auf Eingaben unterschiedlich reagieren, vorhandene Module nutzen, Texte mit Mustern durchsuchen, Dateien einlesen, mit Fehlern sauber umgehen und einfache strukturierte Daten lesen und schreiben.

## Ordnerinhalt

- Beispiele und Übungen zum jeweiligen Thema
- Eigene Lösungen idealerweise unter `loesungen/` ablegen
