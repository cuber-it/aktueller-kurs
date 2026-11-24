# Tag 3 – Verschachtelte Datenstrukturen
# Der JSON-Datensatz verbindet ein Dictionary mit Listen und weiteren Dicts.

import json
from pathlib import Path

datei = Path(__file__).resolve().parent.parent / "materialien" / "person.json"
with datei.open(encoding="utf-8") as quelle:
    person = json.load(quelle)

print("Name:", person["name"])
print("Stadt:", person["adresse"]["stadt"])
print("Erste Kenntnis:", person["kenntnisse"][0])

for nummer, kenntnis in enumerate(person["kenntnisse"], start=1):
    print(f"{nummer}. {kenntnis}")

# Die Liste bewahrt die Reihenfolge; das Set dient dem Mengenvergleich.
vorhanden = set(person["kenntnisse"])
gefragt = {"Python", "SQL"}
print("Gemeinsam:", sorted(vorhanden & gefragt))
print("Noch nicht im Datensatz:", sorted(gefragt - vorhanden))

# list: veränderbare Folge; tuple: fester Verbund von Werten.
# set: eindeutige Elemente; dict: benannte Felder und Zuordnungen.
