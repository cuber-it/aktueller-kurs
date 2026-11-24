# Tupel

## Worum geht's

Ein Tupel (`tuple`) fasst Werte in einer festen Reihenfolge zusammen. Seine Einträge lassen sich nach dem Erstellen nicht ersetzen, ergänzen oder entfernen. Es eignet sich etwa für Koordinaten oder zusammengehörige Rückgabewerte einer Funktion.

## Erstellen und lesen

```python
punkt = (3, 4)
print(punkt[0])      # 3
print(punkt[-1])     # 4
print(len(punkt))    # 2
print(3 in punkt)    # True
```

Indexzugriffe und Slices funktionieren wie bei Listen. Ein Slice eines Tupels ist wieder ein Tupel.

## Das Komma ist entscheidend

```python
ein_wert = (42,)
nur_klammern = (42)
leer = ()

print(type(ein_wert))       # <class 'tuple'>
print(type(nur_klammern))   # <class 'int'>
```

`(42)` ist nur ein geklammerter Ausdruck. Für ein Tupel mit genau einem Element ist das Komma nötig. Bei mehreren Werten können die Klammern häufig entfallen; sie machen die Zusammengehörigkeit deutlicher.

## Entpacken und vertauschen

```python
punkt = (3, 4)
x, y = punkt
print(x, y)    # 3 4

links, rechts = "Apfel", "Birne"
links, rechts = rechts, links
print(links, rechts)    # Birne Apfel
```

Beim Entpacken werden die Elemente auf einzelne Namen verteilt. Ohne einen Sternausdruck müssen Anzahl der Namen und Anzahl der Elemente übereinstimmen. Das Entpacken funktioniert auch mit Listen und anderen Iterables.

## Unveränderlich – mit einer Grenze

```python
punkt = (3, 4)
try:
    punkt[0] = 9
except TypeError:
    print("Eintrag nicht ersetzbar.")

profil = ("Anna", ["Python"])
profil[1].append("SQL")
print(profil)    # ('Anna', ['Python', 'SQL'])
```

Das Tupel hält weiterhin dieselben beiden Objekte. Die enthaltene Liste darf sich verändern. „Unveränderlich“ beschreibt hier die Tupelstruktur, nicht automatisch alle verschachtelten Daten.

## Wann Tupel, wann Liste?

| Tupel | Liste |
| --- | --- |
| Fester Verbund, etwa `(x, y)` | Veränderbare Folge, etwa eine Einkaufsliste |
| Positionen haben eine vereinbarte Bedeutung | Elemente werden ergänzt, entfernt oder umgeordnet |
| Keine Methoden wie `append` | Methoden zum Verändern vorhanden |

Ein Tupel ist nur dann [hashbar](04_sets.md#welche-elemente-sind-erlaubt), wenn alle enthaltenen Elemente hashbar sind. Ein Tupel mit einer Liste darin kann daher weder Dictionary-Schlüssel noch Set-Element sein.

## Stolpersteine

- `(wert)` erzeugt kein Tupel mit einem Element.
- Unpassende Anzahl beim Entpacken erzeugt `ValueError`.
- `punkt[0] = 9` erzeugt `TypeError`.
- Lange Datensätze mit vielen Positionsnummern werden schwer lesbar; benannte Felder passen dann oft besser.

## Schnellreferenz

```python
punkt = (3, 4)
x, y = punkt
erster_wert = punkt[0]
ausschnitt = punkt[:1]    # (3,)
```

**Beispiel:** [Tupel](../../tag3/03_tupel.py)  
**Vertiefung:** [Referenz und Kopien](../../tag3/experimente/referenz_vs_copy.py)
