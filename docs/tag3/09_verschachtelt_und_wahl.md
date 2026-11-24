# Verschachtelte Daten und die passende Struktur

## Worum geht's

Sammlungen lassen sich kombinieren: Ein Dictionary kann Listen und weitere Dictionaries enthalten. Jeder Zugriffsschritt folgt dem Typ des gerade erreichten Objekts.

## Vorhandene JSON-Daten lesen

Dieses Beispiel wird im Hauptordner des Repositories gestartet:

```python
import json
from pathlib import Path

datei = Path("materialien/person.json")
with datei.open(encoding="utf-8") as quelle:
    person = json.load(quelle)

print(person["name"])                # Ulrich
print(person["adresse"]["stadt"])    # Berlin
print(person["kenntnisse"][0])       # Python
print(person["telefon"])             # None
```

`person` ist ein Dictionary. Unter `adresse` liegt ein weiteres Dictionary, unter `kenntnisse` eine Liste. `json.load` wandelt JSON-`null` in Python-`None` um.

Das zugehörige Kursskript bestimmt den Materialpfad über seinen eigenen Speicherort. Es funktioniert dadurch auch beim Start aus einem anderen Arbeitsverzeichnis.

## Zugriff Schritt für Schritt

```python
person = {
    "adresse": {"stadt": "Berlin", "plz": "10115"},
    "kenntnisse": ["Python", "JavaScript", "Perl"],
}

adresse = person["adresse"]
stadt = adresse["stadt"]

for nummer, kenntnis in enumerate(person["kenntnisse"], start=1):
    print(f"{nummer}. {kenntnis}")
# 1. Python
# 2. JavaScript
# 3. Perl
```

Benannte Zwischenschritte helfen bei langen Zugriffsketten. Ein `KeyError` betrifft einen fehlenden Schlüssel, ein `IndexError` eine ungültige Listenposition.

## Liste und Set für unterschiedliche Aufgaben

```python
kenntnisse = ["Python", "JavaScript", "Perl"]
vorhanden = set(kenntnisse)
gefragt = {"Python", "SQL"}

print(sorted(vorhanden & gefragt))    # ['Python']
print(sorted(gefragt - vorhanden))   # ['SQL']
```

Die Liste erhält die ursprüngliche Reihenfolge. Das zusätzliche Set dient dem Mengenvergleich. Keine der beiden Ausgangssammlungen wird hier verändert.

## Mehrere Datensätze: Liste von Dictionaries

```python
kontakte = [
    {"name": "Anna", "ort": "Hamburg"},
    {"name": "Ben", "ort": "Bremen"},
]

for kontakt in kontakte:
    if kontakt["ort"] == "Hamburg":
        print(kontakt["name"])    # Anna
```

Die äußere Liste hält die Datensätze. Jeder Datensatz besitzt benannte Felder. Zusätzliche Datensätze lassen sich ergänzen, ohne neue Variablennamen einzuführen.

## Welche Struktur passt?

| Typ | Typische Aufgabe | Zugriff |
| --- | --- | --- |
| `list` | Veränderbare Folge, etwa Kontakte | Position |
| `tuple` | Fester Verbund, etwa Koordinaten | Position oder Entpacken |
| `set` | Eindeutige Werte und Mengenvergleiche | Mitgliedschaft |
| `dict` | Benannte Felder und Zuordnungen | Schlüssel |

Auch Dictionaries bewahren ihre Einfügereihenfolge. Für den Zugriff ist trotzdem der Schlüssel maßgeblich, nicht seine Position.

## Stolpersteine

- `person.copy()` kopiert nur das äußere Dictionary; verschachtelte Sammlungen bleiben geteilt.
- Für eine unabhängige Kopie der hier verwendeten verschachtelten Daten eignet sich `copy.deepcopy`.
- `get("adresse", {})` schützt nicht vor einem vorhandenen Wert `None`.
- Eine Listenposition ist keine dauerhafte Kennung eines Datensatzes: Einfügen, Sortieren und Löschen können sie verändern.

## Schnellreferenz

| Struktur | Beispielzugriff |
| --- | --- |
| Dictionary im Dictionary | `person["adresse"]["stadt"]` |
| Liste im Dictionary | `person["kenntnisse"][0]` |
| Dictionary in einer Liste | `kontakte[0]["name"]` |
| Alle Datensätze durchlaufen | `for kontakt in kontakte:` |

**Beispiel:** [Verschachtelte Daten](../../tag3/09_verschachtelt_und_wahl.py)  
**Material:** [person.json](../../materialien/person.json)  
**Übung:** [Kontaktverwaltung](../../tag3/aufgaben/erfahren/rolodex.md)  
**Vertiefung:** [Ordnervergleich](../../tag3/aufgaben/erfahren/cmp_folder.md)
