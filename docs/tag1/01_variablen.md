# Variablen

## Worum geht's

Eine Variable ist ein **Name** für einen **Wert**. Du speicherst Werte unter einem Namen und greifst später wieder darauf zu.

## Zuweisung

```python
name = "Ulrich"
alter = 42
preis = 3.99
```

`=` ist **kein Vergleich** (das ist `==`), sondern eine *Anweisung*: „Speichere den Wert rechts unter dem Namen links."

## Mehrere Zuweisungen auf einmal

```python
a, b, c = 1, 2, 3        # Tuple-Unpacking
x = y = z = 0            # Kette
```

## Dynamische Typisierung

Python merkt sich den Typ automatisch. Derselbe Name darf später einen Wert anderen Typs aufnehmen:

```python
zahl = 10           # int
zahl = "Text"       # jetzt str — erlaubt
```

In Java/C wäre das verboten. In Python geht's, kann aber Code unleserlich machen — sparsam einsetzen.

## Typ prüfen

```python
type(zahl)          # <class 'str'>
```

## Namensregeln

- Beginnt mit Buchstabe oder `_`
- Danach Buchstaben, Ziffern, `_`
- Case-sensitive: `name` ≠ `Name`
- Keine reservierten Wörter (`if`, `for`, `class`, `True`, …)

## Konvention: snake_case

```python
mein_lieblings_essen = "Pasta"
geburts_jahr = 1980
```

NICHT `MeinLieblingsEssen` — CamelCase ist für Klassen reserviert.

## Stolpersteine

- **Variable nicht definiert** → `NameError`
- **Tippfehler im Namen** → still gegen andere Variable, oder `NameError`
- **Reserviertes Wort als Name** → `SyntaxError` (z. B. `class = 5`)
- **`=` statt `==`** in Bedingungen → SyntaxError

## Schnellreferenz

```python
name = "Ulrich"            # Zuweisung
a, b = 1, 2                # Mehrfach-Zuweisung
type(name)                 # Typ ansehen

# Konvention
snake_case_variable = 7
```
