# `for`-Schleife

## Worum geht's

Mit `for` iterierst du über etwas „Durchlaufbares" (Iterable). Heute: **`range()`** und **Strings** (Dateizeilen folgen beim Datei-Input).

## Grundform

```python
for buchstabe in "Python":
    print(buchstabe)
```

## `range()` — Zahlenfolgen

| Aufruf            | Zahlen               |
|-------------------|----------------------|
| `range(5)`        | 0, 1, 2, 3, 4        |
| `range(1, 6)`     | 1, 2, 3, 4, 5        |
| `range(0, 10, 2)` | 0, 2, 4, 6, 8        |
| `range(10, 0, -1)`| 10, 9, 8, …, 1       |

`range(stop)` startet bei 0 und endet **vor** `stop`.

```python
for i in range(5):
    print(i)
```

## Über einen String iterieren

```python
for zeichen in "Hallo":
    print(zeichen)
```

`for` greift zeichenweise.

## `break` und `continue`

Funktionieren wie bei `while`:

```python
for i in range(10):
    if i == 5:
        break          # Schleife verlassen
    print(i)           # 0..4

for i in range(6):
    if i == 3:
        continue       # 3 überspringen
    print(i)           # 0, 1, 2, 4, 5
```

## Klassiker: Quersumme

```python
zahl = input("ganze Zahl: ")
summe = 0
for ziffer in zahl:
    summe += int(ziffer)
print(f"Quersumme: {summe}")
```

## `enumerate()` — Index mitgeben

Wenn du Index UND Wert brauchst:

```python
for i, zeichen in enumerate("ABC"):
    print(i, zeichen)
# 0 A
# 1 B
# 2 C
```

## `for` vs. `while`

| `for`                              | `while`                    |
|------------------------------------|----------------------------|
| Anzahl bekannt / Sammlung          | Bedingung-getrieben        |
| `for i in range(10)`               | `while x > 0`              |
| Zähler wird automatisch hochgezählt| Du musst manuell zählen    |

## Stolpersteine

- **`range(start, stop)`** — `stop` ist **exklusiv**.
- **`range(0, 10, 0)`** — Schrittweite 0 → `ValueError`.
- **`for i in 5:`** — eine `int` ist nicht iterable → `TypeError`. Stattdessen `for i in range(5):`.
- **Iterator im `for`-Block verändern** → meist verwirrendes Verhalten.

## Schnellreferenz

```python
for x in iterable:
    ...
    break
    continue

range(stop)
range(start, stop)
range(start, stop, step)

for i, x in enumerate(iterable):
    ...
```
