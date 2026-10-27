# Sonderkapitel: Moderne Operatoren

## Worum geht's

Python entwickelt sich weiter. Hier ein prominenter neuer Operator, den du in modernem Code immer öfter siehst.

## Walross-Operator `:=` (seit Python 3.8)

### Was tut er?

Erlaubt eine **Zuweisung mitten in einem Ausdruck**. Damit lassen sich Wert berechnen, speichern und gleich verwenden — in einer einzigen Zeile.

### Klassisch vs. mit Walross

**Klassisch:**

```python
zahl = len("Python")
if zahl > 3:
    print(f"{zahl} Zeichen ist genug.")
```

**Mit Walross:**

```python
if (zahl := len("Python")) > 3:
    print(f"{zahl} Zeichen ist genug.")
```

### Wofür nützlich?

Vor allem in **Schleifen** und **`if`-Bedingungen**, wenn du einen Wert berechnest, **prüfst** und **gleich weiterverwendest**:

```python
# Datei zeilenweise lesen, bis EOF
while (zeile := datei.readline()):
    print(zeile)

# Eingabe lesen und Länge prüfen
if (n := len(input("Tippe was: "))) > 10:
    print(f"Lang: {n} Zeichen")
```

### Klammern sind oft Pflicht

```python
x := 5            # SyntaxError — nicht alleine erlaubt
(x := 5)          # OK — Klammern um den Walross-Ausdruck
```

## Faustregel

Walross **nur einsetzen, wenn der Code dadurch kürzer UND klarer wird**. Sonst lieber zwei Zeilen.

## Andere „moderne" Schreibweisen (Tag 2)

- **Pattern Matching** mit `match` / `case` (Python 3.10+)
- **Union-Types** in Typhinweisen: `int | str` (Python 3.10+)

## Stolpersteine

- **Klammern vergessen** → SyntaxError.
- **Übermäßiger Einsatz** → Lesbarkeit leidet. Walross ist optional, kein Pflicht-Idiom.
- **Verwechslung mit `=`** — `:=` ist **nur** in Ausdrücken erlaubt, `=` nur in Anweisungen.
- **Auf Python < 3.8** → `SyntaxError`. Bei Legacy-Code aufpassen.

## Schnellreferenz

```python
# Walross — Zuweisung als Ausdruck (Python 3.8+)
if (n := compute()) > 0:
    print(n)

while (line := f.readline()):
    process(line)
```
