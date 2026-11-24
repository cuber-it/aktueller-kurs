# Sets – Mengen

## Worum geht's

Ein Set (`set`) enthält **eindeutige Elemente**. Es eignet sich zum Entfernen von Duplikaten, für Mitgliedschaftsprüfungen und zum Vergleichen von Gruppen. Es hat keine garantierte Einfügereihenfolge und keine Indizes.

## Erstellen und verändern

```python
obst = {"Apfel", "Birne", "Apfel"}
print(len(obst))            # 2
print("Apfel" in obst)      # True

obst.add("Kirsche")
obst.discard("Mango")
print(sorted(obst))        # ['Apfel', 'Birne', 'Kirsche']
```

`add` ergänzt einen Wert. `discard` entfernt ihn, falls vorhanden. `remove` entfernt ebenfalls, erzeugt bei einem fehlenden Wert aber `KeyError`.

## Leere Menge und Umwandlung

```python
leer = set()               # {} wäre ein leeres Dictionary.
namen = ["Anna", "Ben", "Anna"]
eindeutig = set(namen)
print(sorted(eindeutig))   # ['Anna', 'Ben']
```

Die ursprüngliche Reihenfolge und die Anzahl gleicher Werte gehen beim Umwandeln verloren. `sorted` erzeugt für die Ausgabe eine neue Liste; das Set selbst bleibt ungeordnet.

## Mengen vergleichen

```python
python_kurs = {"Anna", "Ben", "Cem"}
sql_kurs = {"Ben", "Dora"}

print(sorted(python_kurs & sql_kurs))   # ['Ben']
print(sorted(python_kurs - sql_kurs))   # ['Anna', 'Cem']
```

| Ausdruck | Ergebnis |
| --- | --- |
| `python_kurs \| sql_kurs` | Alle Personen aus mindestens einem Kurs |
| `python_kurs & sql_kurs` | Personen in beiden Kursen |
| `python_kurs - sql_kurs` | Personen in Python, aber nicht in SQL |
| `python_kurs ^ sql_kurs` | Personen in genau einem der beiden Kurse |
| `python_kurs <= sql_kurs` | Ist der Python-Kurs eine Teilmenge des SQL-Kurses? |

`<=` erlaubt gleiche Mengen; `<` verlangt eine echte Teilmenge. Mit `==` vergleichst du den Inhalt unabhängig von der Reihenfolge.

## Welche Elemente sind erlaubt?

Set-Elemente müssen **hashbar** sein. Python verwendet ihren Hashwert zum Auffinden; dieser muss während ihrer Lebensdauer gleich bleiben.

Strings und ganze Zahlen sind hashbar. Listen, Dictionaries und Sets sind es nicht. Ein Tupel ist hashbar, wenn alle seine Elemente hashbar sind.

## `frozenset`

```python
feste_menge = frozenset({"Anna", "Ben"})
print("Anna" in feste_menge)    # True
```

Ein `frozenset` kann nachträglich nicht verändert werden. Es ist selbst hashbar und eignet sich dadurch auch als Dictionary-Schlüssel oder als Element eines weiteren Sets.

## Stolpersteine

- `menge[0]` funktioniert nicht: Sets unterstützen keine Indexzugriffe.
- Die Ausgabe eines Sets hat keine verlässlich vorgegebene Reihenfolge.
- `a - b` ist im Allgemeinen etwas anderes als `b - a`.
- Duplikate lassen sich nach der Umwandlung in ein Set nicht mehr zählen.

## Schnellreferenz

| Aufgabe | Ausdruck |
| --- | --- |
| Leeres Set | `set()` |
| Eindeutige Werte | `set(werte)` |
| Ergänzen / tolerant entfernen | `add(wert)` / `discard(wert)` |
| Vereinigung / Schnittmenge | `a \| b` / `a & b` |
| Differenz / symmetrische Differenz | `a - b` / `a ^ b` |

**Beispiel:** [Sets](../../tag3/04_sets.py)  
**Übungen:** [Eindeutige Wörter](../../tag3/aufgaben/basic/eindeutige_woerter.md), [Kursmengen](../../tag3/aufgaben/erfahren/kurs_mengen.md), [Lottoziehung](../../tag3/aufgaben/basic/lottobude.md), [Lottovergleich](../../tag3/aufgaben/erfahren/lottobudeNG.md)
