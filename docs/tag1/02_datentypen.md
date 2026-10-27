# Skalare Datentypen + None

## Worum geht's

„Skalar" = ein einzelner Wert (im Gegensatz zu Sammlungen wie Listen). Heute: **vier skalare Typen plus `None`**.

## Die vier Skalartypen

| Typ     | Beispiel                | Bedeutung      |
|---------|-------------------------|----------------|
| `int`   | `42`, `-7`, `1_000_000` | Ganzzahl       |
| `float` | `3.14`, `-0.5`, `2e10`  | Fließkomma     |
| `str`   | `"Hallo"`, `'Welt'`     | Zeichenkette   |
| `bool`  | `True`, `False`         | Wahrheitswert  |

### `int`

Beliebig große Ganzzahlen — kein Überlauf wie in C/Java.

```python
n = 10 ** 100              # geht problemlos
einwohner = 1_500_000      # Unterstrich als Tausender-Trenner
```

### `float`

Fließkommazahlen nach IEEE 754 (64 bit).

```python
preis = 3.99
exponent = 2.5e3       # 2500.0
```

⚠️ `0.1 + 0.2 != 0.3` — keine Python-Macke, sondern IEEE 754. Für Geld → später `decimal.Decimal`.

### `str`

In `'…'` oder `"…"`, beides gleichwertig. Mehrzeilig mit `"""…"""`.

```python
gruss = "Hallo"
text = 'Hi'
absatz = """Mehrere
Zeilen"""
```

### `bool`

Nur `True` und `False` (groß!). Im Hintergrund sind es `int` (`True == 1`, `False == 0`).

```python
ist_offen = True
```

## `None` — kein Wert

Eigener Wert, der „nichts / noch nicht gesetzt / kein Ergebnis" bedeutet:

```python
ergebnis = None
```

Sein Typ ist `NoneType`.

## Typ prüfen

```python
type(7)         # <class 'int'>
type(3.14)      # <class 'float'>
type("Hi")      # <class 'str'>
type(True)      # <class 'bool'>
type(None)      # <class 'NoneType'>
```

## Ausblick: nicht-skalare Typen

| Typ     | Beispiel              |
|---------|-----------------------|
| `list`  | `[1, 2, 3]`           |
| `tuple` | `(1, 2, 3)`           |
| `dict`  | `{"name": "Ulrich"}`  |
| `set`   | `{1, 2, 3}`           |

Diese **sammeln mehrere Werte** und kommen später im Kurs.

## Stolpersteine

- **`0.1 + 0.2 != 0.3`** — Fließkomma-Falle.
- **`bool("False")` ist `True`!** — jeder nicht-leere String ist truthy.
- **`True + True == 2`** — bools sind technisch ints.
- **`None` vergleichen** mit `is`, nicht mit `==`: `if x is None`.

## Schnellreferenz

```python
n = 42                  # int
x = 3.14                # float
s = "text"              # str
b = True                # bool
nichts = None           # NoneType

type(n)                 # Typ ansehen
```
