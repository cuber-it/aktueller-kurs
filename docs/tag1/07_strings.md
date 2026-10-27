# Strings

## Worum geht's

Strings sind in Python eine eigene Welt: mächtig, **unveränderlich** (immutable), mit vielen eingebauten Methoden.

## Erzeugen

```python
s = "Hallo"
s = 'Welt'
s = """mehrere
Zeilen"""
```

## Länge & enthält

```python
len("Python")            # 6
"Py" in "Python"         # True
"x" not in "Python"      # True
```

## Indizierung

0-basiert, von links und negativ von rechts:

```python
s = "Python"
s[0]      # 'P'
s[-1]     # 'n'   (letztes Zeichen)
s[2]      # 't'
```

## Slicing — `[start:stop:step]`

`stop` ist **exklusiv**.

```python
s = "Python"
s[0:3]    # 'Pyt'
s[:3]     # 'Pyt'        (von Anfang)
s[3:]     # 'hon'        (bis Ende)
s[::2]    # 'Pto'        (jedes zweite)
s[::-1]   # 'nohtyP'     (umdrehen)
```

## Wichtige Methoden

| Methode             | Was tut sie                          |
|---------------------|--------------------------------------|
| `.upper()`          | Großbuchstaben                       |
| `.lower()`          | Kleinbuchstaben                      |
| `.strip()`          | Whitespace außen entfernen           |
| `.replace(a, b)`    | `a` durch `b` ersetzen               |
| `.split(sep)`       | An `sep` zerlegen → Liste            |
| `.find(sub)`        | Position oder `-1`                   |
| `.startswith(sub)`  | beginnt mit?                         |
| `.endswith(sub)`    | endet auf?                           |
| `.count(sub)`       | wie oft enthalten?                   |
| `.title()`          | Wort-Anfänge groß                    |

```python
"  Hallo  ".strip()                  # 'Hallo'
"Hallo".replace("a", "ä")            # 'Hällo'
"a;b;c".split(";")                   # ['a', 'b', 'c']
"Python".find("th")                  # 2
"Python".startswith("Py")            # True
```

## Verketten & Wiederholen

```python
"Hallo" + " " + "Welt"        # 'Hallo Welt'
"ha" * 3                       # 'hahaha'
```

## Immutability

Strings können **nicht direkt verändert** werden:

```python
s = "Hallo"
s[0] = "h"            # TypeError!
```

Stattdessen einen **neuen** String bauen:

```python
s = "h" + s[1:]       # 'hallo'
```

Methoden wie `.upper()` ändern den Original-String **nicht**, sie liefern einen neuen:

```python
s = "Hallo"
s.upper()             # 'HALLO'
print(s)              # 'Hallo'  (unverändert!)
s = s.upper()         # so wird zugewiesen
```

## Iterieren

Per `for` zeichenweise:

```python
for buchstabe in "Python":
    print(buchstabe)
```

## Stolpersteine

- **`s.upper()` ohne Zuweisung** → das Ergebnis verpufft.
- **Index außerhalb des Strings** → `IndexError`. Slicing ist toleranter und liefert leeren String.
- **Whitespace nach `input()`** vergessen zu strippen → unerwartete Vergleiche schlagen fehl.
- **`==` vs. `is`** — Strings vergleicht man mit `==`.

## Schnellreferenz

```python
len(s)                      # Länge
s[i]                        # einzelnes Zeichen
s[i:j:k]                    # Slice
"x" in s                    # enthält?

s.upper() / s.lower()
s.strip()
s.replace(a, b)
s.split(sep)
s.find(sub)
s.startswith(sub) / .endswith(sub)
s.count(sub)
```
