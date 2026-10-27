# Eingabe mit `input()`

## Worum geht's

`input()` liest **eine Zeile** von der Tastatur ein und liefert sie als **`str`** zurück — egal was eingetippt wurde.

## Grundform

```python
name = input("Wie heißt du? ")
print("Hallo,", name)
```

Der Text in der Klammer ist der **Prompt** — er erscheint vor der Eingabe.

## Wichtig: das Ergebnis ist immer ein String

Auch wenn der Nutzer `42` eintippt — Python sieht `"42"`.

```python
text = input("Alter? ")     # text == "42"
print(text + 1)             # TypeError!
```

Wenn du rechnen willst, **musst du konvertieren**:

```python
alter = int(input("Alter? "))
print(alter + 1)            # OK
```

## Was bekommt man bei leerer Eingabe?

Drückt der Nutzer nur Enter, kommt ein **leerer String** `""` zurück:

```python
eingabe = input("Sag was: ")
if eingabe == "":
    print("Nichts eingegeben.")
```

## Mehrere Eingaben

Mehrere Werte → mehrere `input()`-Aufrufe:

```python
name = input("Name? ")
alter = int(input("Alter? "))
print(f"{name}, {alter}")
```

## Whitespace strippen

Tab, Leerzeichen, Zeilenende werden mit übernommen — bei Bedarf entfernen:

```python
name = input("Name? ").strip()
```

## Stolpersteine

- **Kein Konvertieren** → `TypeError` beim Rechnen.
- **`int(input(...))` mit Buchstaben** → `ValueError`. Abfangen kommt an Tag 2.
- **`raw_input()`** ist Python 2 — gibt es nicht mehr. Immer `input()`.
- **Eingabe in Skripten ungetestet lassen** — was passiert bei Leerzeile, Sonderzeichen, Umlauten?

## Schnellreferenz

```python
text  = input("Prompt: ")              # str
zahl  = int(input("Zahl? "))           # int
preis = float(input("Preis? "))        # float
name  = input("Name? ").strip()        # ohne Whitespace
```
