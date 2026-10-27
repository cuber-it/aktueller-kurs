# Sonderkapitel: Moderne Kontrollstrukturen

## Worum geht's

Pattern Matching mit **`match` / `case`** — seit Python 3.10. Erinnert auf den ersten Blick an `switch`/`case` aus C/Java, kann aber deutlich mehr.

## Grundform

```python
match wert:
    case muster1:
        ...
    case muster2:
        ...
    case _:                  # "wildcard" — fängt alles
        ...
```

## Einfacher Vergleich

```python
farbe = input("Ampel? ").lower()

match farbe:
    case "rot":
        print("Stehen.")
    case "gelb":
        print("Achtung.")
    case "grün":
        print("Fahren.")
    case _:
        print("Unbekannt.")
```

## Mehrere Werte zusammenfassen

Mit `|` (Oder):

```python
match befehl:
    case "hilfe" | "?" | "h":
        print("Hilfe...")
    case "ende" | "exit" | "quit":
        print("Tschüss")
    case _:
        print("Hä?")
```

## `match` vs. `if`/`elif`-Kette

Viele `elif`-Ketten lassen sich kürzer mit `match` schreiben — vor allem wenn alle Zweige **denselben Wert** prüfen.

**Mit `if`-Kette:**

```python
if farbe == "rot":
    ...
elif farbe == "gelb":
    ...
elif farbe == "grün":
    ...
else:
    ...
```

**Mit `match`:**

```python
match farbe:
    case "rot":  ...
    case "gelb": ...
    case "grün": ...
    case _:      ...
```

## Was kann `match` noch?

`match`/`case` ist **kein normales switch** — es macht **Strukturvergleiche**:

- Tupel zerlegen: `case (x, y):`
- Listen prüfen: `case [1, 2, *rest]:`
- Dicts matchen: `case {"name": str(name)}:`
- Klassen-Felder prüfen: `case Punkt(x=0, y=y):`

Diese fortgeschrittenen Formen schauen wir an, **wenn die Typen** (Listen, Dicts, Klassen) im Kurs eingeführt sind.

## Stolpersteine

- **Verfügbar erst ab Python 3.10** — auf älteren Systemen → `SyntaxError`.
- **`case "wert":`** — Strings in Anführungszeichen, sonst hält Python sie für Variablennamen!
- **`case _:`** ist der **Wildcard**, fängt alles. Eine Variable namens `_` ist es **nicht**.
- **Reihenfolge zählt** — der erste Match gewinnt.

## Schnellreferenz

```python
match wert:
    case "literal":          # Literalvergleich
        ...
    case 1 | 2 | 3:          # mehrere Werte
        ...
    case x:                  # bindet wert an x (Capture)
        ...
    case _:                  # Wildcard
        ...
```
