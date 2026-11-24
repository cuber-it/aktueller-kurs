# Listen – Methoden

## Worum geht's

Listenmethoden ergänzen, entfernen und ordnen Elemente. Entscheidend ist, ob ein Aufruf die vorhandene Liste verändert und welchen Wert er zurückgibt.

## Elemente hinzufügen

```python
obst = ["Birne", "Apfel"]
obst.append("Kirsche")
obst.extend(["Orange", "Banane"])
obst.insert(0, "Mango")

print(obst)
# ['Mango', 'Birne', 'Apfel', 'Kirsche', 'Orange', 'Banane']
```

| Methode | Wirkung |
| --- | --- |
| `append(wert)` | Ein Element am Ende anfügen |
| `extend(werte)` | Elemente eines Iterables einzeln anfügen |
| `insert(index, wert)` | Vor der angegebenen Position einfügen |

**Iterable** bezeichnet ein Objekt, über das eine Schleife laufen kann, etwa eine Liste oder einen String.

## `append` und `extend` unterscheiden

```python
mit_append = ["Apfel"]
mit_append.append(["Birne", "Kirsche"])
print(mit_append)    # ['Apfel', ['Birne', 'Kirsche']]

mit_extend = ["Apfel"]
mit_extend.extend(["Birne", "Kirsche"])
print(mit_extend)    # ['Apfel', 'Birne', 'Kirsche']
```

Die angehängte Liste ist bei `append` ein einzelnes Element. `extend("Kiwi")` würde dagegen vier einzelne Zeichen ergänzen.

## Elemente entfernen

```python
obst = ["Mango", "Apfel", "Birne", "Apfel"]
obst.remove("Apfel")     # Nur den ersten passenden Wert entfernen.
entnommen = obst.pop()  # Letztes Element entfernen und zurückgeben.

print(entnommen)        # Apfel
print(obst)             # ['Mango', 'Birne']
```

`pop(index)` entfernt an einer bestimmten Position. `clear()` leert die gesamte Liste. `del obst[0]` ist eine weitere Möglichkeit, ein Element anhand seiner Position zu löschen.

## Sortieren und umdrehen

```python
obst = ["Birne", "Apfel", "Kirsche"]
rueckgabe = obst.sort()

print(obst)         # ['Apfel', 'Birne', 'Kirsche']
print(rueckgabe)    # None

obst.reverse()
print(obst)         # ['Kirsche', 'Birne', 'Apfel']
```

`sort()` verändert die Liste. `sorted(obst)` liefert eine neue sortierte Liste. `reverse()` kehrt nur die vorhandene Reihenfolge um; es sortiert nicht.

## Suchen und zählen

- `obst.count("Apfel")` zählt passende Elemente; kein Treffer ergibt `0`.
- `obst.index("Apfel")` liefert die Position des ersten Treffers.
- `"Apfel" in obst` genügt, wenn nur das Vorhandensein interessiert.

## Stolpersteine

- `obst = obst.sort()` bindet den Namen `obst` anschließend an `None`.
- `remove` und `index` erzeugen bei fehlendem Wert `ValueError`.
- `pop` auf einer leeren Liste erzeugt `IndexError`.
- Unverträgliche Typen wie Zahlen und Strings lassen sich nicht gemeinsam mit der Standardsortierung ordnen.

## Schnellreferenz

| Ergänzen | Entfernen | Ordnen |
| --- | --- | --- |
| `append(wert)` | `remove(wert)` | `sort()` |
| `extend(werte)` | `pop(index)` | `reverse()` |
| `insert(index, wert)` | `clear()` | `sorted(liste)` erzeugt eine Kopie |

**Beispiel:** [Listenmethoden](../../tag3/02_listen_methoden.py)  
**Übung:** [Einkaufsliste](../../tag3/aufgaben/basic/einkaufsliste.md)
