# Listen – Grundlagen

## Worum geht's

Eine Liste (`list`) speichert Elemente in einer **Reihenfolge**. Sie ist veränderbar und darf Werte mehrfach enthalten. Damit eignet sie sich etwa für eine Einkaufsliste, eingelesene Dateizeilen oder eine Folge von Messwerten.

## Erstellen und prüfen

```python
obst = ["Apfel", "Birne", "Kirsche", "Zwetschge"]
leer = []

print(len(obst))              # 4
print("Birne" in obst)        # True
print("Mango" not in obst)    # True
```

Eine Liste sortiert ihre Elemente nicht automatisch. Eine Liste kann verschiedene Typen enthalten; gleichartige Einträge lassen sich meist einfacher verarbeiten.

## Einzelne Elemente: Indizes

Der erste Index ist `0`. Negative Indizes zählen vom Ende:

```python
obst = ["Apfel", "Birne", "Kirsche", "Zwetschge"]
print(obst[0])     # Apfel
print(obst[-1])    # Zwetschge

obst[1] = "Orange"
print(obst[1])     # Orange
```

Ein Zugriff außerhalb der Liste erzeugt `IndexError`. Bei einer leeren Liste gibt es auch kein letztes Element.

## Ausschnitte: Slices

```python
obst = ["Apfel", "Birne", "Kirsche", "Zwetschge"]
print(obst[1:3])    # ['Birne', 'Kirsche']
print(obst[:2])     # ['Apfel', 'Birne']
print(obst[::2])    # ['Apfel', 'Kirsche']
print(obst[::-1])   # ['Zwetschge', 'Kirsche', 'Birne', 'Apfel']
```

Das Muster lautet `[start:stop:step]`. `stop` gehört nicht dazu. Ein Slice erzeugt eine neue äußere Liste; Grenzen außerhalb der Liste werden angepasst.

## Zuweisung oder Kopie?

```python
obst = ["Apfel", "Birne"]
zweiter_name = obst
zweiter_name.append("Kirsche")

kopie = obst.copy()
kopie.append("Mango")

print(obst)    # ['Apfel', 'Birne', 'Kirsche']
print(kopie)   # ['Apfel', 'Birne', 'Kirsche', 'Mango']
```

`zweiter_name` bezeichnet dieselbe Liste wie `obst`. `copy()` erzeugt eine **flache Kopie**: Die äußere Liste ist neu, enthaltene Objekte werden weiterhin gemeinsam verwendet. Bei verschachtelten Listen können dadurch Änderungen auch im Original sichtbar werden.

## Stolpersteine

- `obst = andere_liste` kopiert keine Liste.
- `obst[1:3]` enthält zwei Elemente, nicht drei.
- Eine Liste während ihrer Iteration zu verkürzen kann Elemente überspringen.
- `if obst:` prüft, ob mindestens ein Element vorhanden ist.

## Schnellreferenz

| Ausdruck | Bedeutung |
| --- | --- |
| `liste[index]` | Ein Element lesen oder ersetzen |
| `liste[start:stop]` | Ausschnitt als neue Liste |
| `len(liste)` | Anzahl der Elemente |
| `wert in liste` | Auf enthaltenen Wert prüfen |
| `liste.copy()` | Flache Kopie erstellen |

**Beispiel:** [Listen-Grundlagen](../../tag3/01_listen_grundlagen.py)  
**Übung:** [Einkaufsliste](../../tag3/aufgaben/basic/einkaufsliste.md)
