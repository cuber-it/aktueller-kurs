# Typkonvertierung (Casting)

## Worum geht's

Werte zwischen Typen umwandeln. Sehr wichtig im Zusammenspiel mit `input()`, das immer einen `str` liefert.

## Die vier Konverter

| Funktion   | Wandelt um zu  |
|------------|----------------|
| `int(x)`   | Ganzzahl       |
| `float(x)` | Fließkomma     |
| `str(x)`   | Zeichenkette   |
| `bool(x)`  | Wahrheitswert  |

## Beispiele

```python
int("42")        # 42       (str -> int)
int(7.9)         # 7        (float -> int, schneidet ab!)
float("3.14")    # 3.14     (str -> float)
float(7)         # 7.0
str(2026)        # "2026"
str(3.14)        # "3.14"
```

## `bool(x)` — Truthiness

Was ist „falsy" (gilt als `False`)?

| Wert       | `bool(...)` |
|------------|-------------|
| `False`    | `False`     |
| `None`     | `False`     |
| `0`, `0.0` | `False`     |
| `""`       | `False`     |

**Alles andere ist `True`** — auch der String `"False"`!

```python
bool("")         # False
bool("nein")     # True   (nicht-leerer String!)
bool("False")    # True   (Klassiker-Falle)
bool(0)          # False
bool(-1)         # True
```

## Klassisches Pattern: Eingabe in Zahl

```python
text = input("Alter? ")
alter = int(text)              # str -> int
print(alter + 1)
```

In einem Schritt:

```python
alter = int(input("Alter? "))
```

## Stolpersteine

- `int(7.9)` → `7` — **schneidet ab**, rundet **nicht**. Für Runden: `round(7.9)` → `8`.
- `int("3.14")` → `ValueError`. Erst `float`, dann `int`:

  ```python
  int(float("3.14"))   # 3
  ```
- `int("abc")` → `ValueError`. Abfangen → Tag 2 (`try/except`).
- `bool("False")` ist `True` — als String, nicht als bool gelesen.

## Schnellreferenz

```python
int(x)           # Ganzzahl
float(x)         # Fließkomma
str(x)           # String
bool(x)          # Wahrheitswert

# Falsy:  False, None, 0, 0.0, ""
# Alles andere ist truthy.
```
