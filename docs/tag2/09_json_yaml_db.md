# Extrakapitel: JSON, YAML, SQLite

## Worum geht's

Sobald Dateien laufen, kommt schnell der Wunsch nach **strukturierten Daten** statt purem Text. Drei Klassiker im Anriss:

| Format / DB | Wofür                          | Modul       | Installation       |
|-------------|--------------------------------|-------------|--------------------|
| **JSON**    | Konfigurationen, Web-APIs      | `json`      | Standardbibliothek |
| **YAML**    | Konfigurationen, lesbarer als JSON | `yaml`  | `pip install pyyaml` |
| **SQLite**  | leichtgewichtige Datenbank     | `sqlite3`   | Standardbibliothek |

## JSON

### String ↔ Python

```python
import json

# String -> Python (loads = "load string")
daten = json.loads('{"name": "Ulrich", "alter": 42}')

# Python -> String (dumps)
text = json.dumps({"name": "Ulrich"}, indent=2, ensure_ascii=False)
```

### Datei ↔ Python

```python
# Schreiben (dump)
with open("person.json", "w", encoding="utf-8") as f:
    json.dump(person, f, indent=2, ensure_ascii=False)

# Lesen (load)
with open("person.json", "r", encoding="utf-8") as f:
    person = json.load(f)
```

**Merksatz:** `loads`/`dumps` arbeiten mit **Strings**, `load`/`dump` mit **Datei-Objekten**.

### Wichtige Optionen

| Option              | Bedeutung                              |
|---------------------|----------------------------------------|
| `indent=2`          | hübsche Einrückung                     |
| `ensure_ascii=False`| Umlaute bleiben Umlaute (nicht `ä`)|
| `sort_keys=True`    | Schlüssel alphabetisch sortieren       |

## YAML

Externes Paket — vorher installieren:

```bash
pip install pyyaml
```

```python
import yaml

# Aus String
config = yaml.safe_load("""
name: Ulrich
alter: 42
hobbies:
  - lesen
  - kochen
""")

# Aus Datei
with open("config.yaml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

# In Datei schreiben
with open("config.yaml", "w", encoding="utf-8") as f:
    yaml.safe_dump(config, f, allow_unicode=True)
```

⚠️ **Immer `safe_load` / `safe_dump`** — `yaml.load()` ohne „safe" kann beliebigen Python-Code ausführen, der in einer YAML-Datei stehen könnte.

### Wann YAML statt JSON?

- **Konfigurationsdateien** (kürzer, lesbarer, Kommentare erlaubt)
- **Mehrere Dokumente** in einer Datei (`---` als Trenner)

## SQLite

Eine **Datei = eine Datenbank**. Kein Server, kein Setup. Perfekt für kleine Projekte und Lernzwecke.

### Verbindung & Cursor

```python
import sqlite3

conn = sqlite3.connect("kurs.db")     # Datei wird angelegt
cur  = conn.cursor()
```

### Tabelle anlegen

```python
cur.execute("""
    CREATE TABLE IF NOT EXISTS personen (
        id           INTEGER PRIMARY KEY AUTOINCREMENT,
        name         TEXT NOT NULL,
        lebensjahre  INTEGER
    )
""")
```

### Einfügen (parametrisiert!)

```python
cur.execute(
    "INSERT INTO personen (name, lebensjahre) VALUES (?, ?)",
    ("Ulrich", 42),
)
conn.commit()           # ohne commit bleibt nichts gespeichert
```

⚠️ **Niemals** Werte mit f-String einbauen:

```python
cur.execute(f"INSERT ... VALUES ('{name}', ...)")    # SQL-INJECTION!
```

Immer Platzhalter `?` mit Tupel-Werten.

### Lesen

```python
cur.execute("SELECT name, lebensjahre FROM personen")

# alle auf einmal
for name, alter in cur.fetchall():
    ...

# einer nach dem anderen (für viele Zeilen besser)
for name, alter in cur:
    ...
```

### Mit `with`

```python
with sqlite3.connect("kurs.db") as conn:
    conn.execute("INSERT INTO personen (name, lebensjahre) VALUES (?, ?)",
                 ("Anna", 30))
# commit / close passieren automatisch
```

## Stolpersteine

- **JSON:** Schlüssel müssen Strings sein, kein einfaches `'`-Quoting wie in Python — JSON kennt nur `"`.
- **JSON + Datum:** `datetime` ist nicht direkt JSON-serialisierbar — als String speichern (`isoformat()`).
- **YAML:** Einrückung mit **Leerzeichen**, niemals Tabs. Inkonsistente Einrückung → kryptische Fehler.
- **SQLite + `commit()` vergessen** → nach Programmende sind die Änderungen weg.
- **SQL-Injection:** Werte **immer** als Parameter, nie per String-Interpolation.
- **Mehrere Verbindungen** auf dieselbe SQLite-Datei → Lock-Probleme bei parallelem Schreiben.

## Schnellreferenz

```python
# JSON
json.loads(text)           json.dumps(obj, indent=2, ensure_ascii=False)
json.load(file)            json.dump(obj, file, indent=2, ensure_ascii=False)

# YAML  (pip install pyyaml)
yaml.safe_load(text_or_file)
yaml.safe_dump(obj, file, allow_unicode=True)

# SQLite
conn = sqlite3.connect("name.db")
cur  = conn.cursor()
cur.execute("SQL ?, ?", (wert1, wert2))
conn.commit()
conn.close()
```
