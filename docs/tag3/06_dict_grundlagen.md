# Dictionaries – Grundlagen

## Worum geht's

Ein Dictionary (`dict`) ordnet **Schlüsseln Werte** zu. Du greifst über einen passenden Schlüssel zu, etwa einen Feldnamen oder einen Namen im Telefonbuch. Schlüssel sind eindeutig; Werte dürfen mehrfach vorkommen.

## Erstellen und zugreifen

```python
person = {"name": "Anna", "alter": 30}

print(person["name"])    # Anna
print(len(person))       # 2
```

Ein Schlüssel kann beispielsweise ein String, eine Zahl oder ein hashbares Tupel sein. Listen, Dictionaries und Sets eignen sich nicht als Schlüssel. Die Werte dürfen beliebige Python-Objekte sein, auch weitere Sammlungen.

## Einfügen und ändern

```python
person = {"name": "Anna", "alter": 30}
person["beruf"] = "Entwicklerin"
person["alter"] = 31

print(person["beruf"])    # Entwicklerin
print(person["alter"])    # 31
```

Ein neuer Schlüssel ergänzt einen Eintrag. Ein vorhandener Schlüssel erhält einen neuen Wert. Die Anzahl der Einträge steigt dabei nicht.

Dictionaries bewahren die **Einfügereihenfolge**. Das Ändern eines Wertes verschiebt seinen Schlüssel nicht. Eine alphabetische Sortierung entsteht dadurch nicht.

## Fehlende Schlüssel: `[]` oder `get`

```python
person = {"name": "Anna"}

print(person.get("beruf"))                 # None
print(person.get("beruf", "unbekannt"))    # unbekannt

try:
    print(person["beruf"])
except KeyError:
    print("Beruf fehlt.")
```

| Zugriff | Bei fehlendem Schlüssel |
| --- | --- |
| `person["beruf"]` | `KeyError` |
| `person.get("beruf")` | `None` |
| `person.get("beruf", "unbekannt")` | Angegebener Standardwert |

`get` ergänzt keinen Eintrag. Ein gespeicherter Wert `None` bleibt ebenfalls `None`; der Standardwert greift nur bei einem fehlenden Schlüssel.

## Was prüft `in`?

```python
person = {"name": "Anna", "alter": 30}
print("name" in person)           # True
print("Anna" in person)           # False
print("Anna" in person.values()) # True
```

`in` prüft beim Dictionary die Schlüssel. Für Werte braucht es ausdrücklich `values()`.

## Einträge entfernen

```python
person = {"name": "Anna", "beruf": "Entwicklerin"}
beruf = person.pop("beruf")
print(beruf)               # Entwicklerin
print(person)              # {'name': 'Anna'}

del person["name"]
print(person)              # {}
```

`pop` entfernt und liefert den Wert. `del` entfernt ohne Rückgabewert. Beide erzeugen bei fehlendem Schlüssel `KeyError`; `pop(schluessel, standardwert)` erlaubt einen Ersatzwert.

## Stolpersteine

- `person[0]` fragt nach dem Schlüssel `0`, nicht nach dem ersten Eintrag.
- Jeder Schlüssel kommt pro Dictionary nur einmal vor; eine erneute Zuweisung ersetzt seinen Wert.
- `get` mit einem Standardwert verändert das Dictionary nicht.
- Telefonnummern und Postleitzahlen als Strings speichern, damit führende Nullen erhalten bleiben.

## Schnellreferenz

| Aufgabe | Ausdruck |
| --- | --- |
| Lesen / zuweisen | `daten[schluessel]` / `daten[schluessel] = wert` |
| Optional lesen | `daten.get(schluessel, standardwert)` |
| Schlüssel prüfen | `schluessel in daten` |
| Entfernen und zurückgeben | `daten.pop(schluessel)` |

**Beispiel:** [Dictionary-Grundlagen](../../tag3/06_dict_grundlagen.py)  
**Übung:** [Telefonbuch](../../tag3/aufgaben/basic/telefonbuch.md)
