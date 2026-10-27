# Tag 2 – Extrakapitel: JSON, YAML, SQLite
#
# Wenn du Dateien liest UND mit Struktur arbeiten willst, helfen
# fertige Formate. Hier ein Anriss von drei Klassikern:
#
#   1. JSON    – in der Standardbibliothek (json)
#   2. YAML    – externes Paket  (pip install pyyaml)
#   3. SQLite  – in der Standardbibliothek, eine Datei = eine DB

# =============================================================
# 1. JSON
# =============================================================
import json

# JSON aus String parsen
text = '{"name": "Ulrich", "alter": 42, "hobbies": ["lesen", "kochen"]}'
daten = json.loads(text)
print(daten["name"])
print(daten["hobbies"][0])

# Python -> JSON-String
person = {"name": "Anna", "alter": 30}
print(json.dumps(person, indent=2, ensure_ascii=False))

# JSON in Datei schreiben
with open("person.json", "w", encoding="utf-8") as f:
    json.dump(person, f, indent=2, ensure_ascii=False)

# JSON aus Datei lesen
with open("person.json", "r", encoding="utf-8") as f:
    geladen = json.load(f)
print(geladen)

# Merke:
#   loads / dumps -> arbeiten mit Strings
#   load  / dump  -> arbeiten mit Datei-Objekten

# =============================================================
# 2. YAML   (pip install pyyaml)
# =============================================================
try:
    import yaml
except ImportError:
    print("\nYAML übersprungen – nachholen mit:  pip install pyyaml")
else:
    config_text = """
    name: Ulrich
    alter: 42
    hobbies:
      - lesen
      - kochen
    """
    config = yaml.safe_load(config_text)
    print(config["hobbies"])

    with open("config.yaml", "w", encoding="utf-8") as f:
        yaml.safe_dump(config, f, allow_unicode=True)

    with open("config.yaml", "r", encoding="utf-8") as f:
        geladen = yaml.safe_load(f)
    print(geladen)

    # WICHTIG: immer safe_load / safe_dump verwenden!
    # yaml.load() ohne "safe_" kann beliebigen Python-Code ausführen.

# =============================================================
# 3. SQLite   (eingebaut, eine Datei = eine Datenbank)
# =============================================================
import sqlite3

# Verbindung öffnen – Datei wird angelegt, falls nicht vorhanden
conn = sqlite3.connect("kurs.db")
cur = conn.cursor()

# Tabelle anlegen (idempotent dank IF NOT EXISTS)
cur.execute("""
    CREATE TABLE IF NOT EXISTS personen (
        id           INTEGER PRIMARY KEY AUTOINCREMENT,
        name         TEXT NOT NULL,
        lebensjahre  INTEGER
    )
""")

# Einfügen – IMMER parametrisiert (Platzhalter "?"),
# sonst droht SQL-Injection!
cur.execute(
    "INSERT INTO personen (name, lebensjahre) VALUES (?, ?)",
    ("Ulrich", 42),
)
cur.execute(
    "INSERT INTO personen (name, lebensjahre) VALUES (?, ?)",
    ("Anna", 30),
)
conn.commit()           # ohne commit() bleibt nichts gespeichert!

# Lesen
cur.execute("SELECT name, lebensjahre FROM personen")
for name, lebensjahre in cur.fetchall():
    print(f"{name}: {lebensjahre} Jahre")

conn.close()

# Eleganter mit "with":
#
#   with sqlite3.connect("kurs.db") as conn:
#       conn.execute("INSERT INTO ...", (...,))
#   # commit / close passieren automatisch
