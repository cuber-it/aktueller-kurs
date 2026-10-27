# Ausgabe mit `print()`

## Worum geht's

`print()` schreibt Werte auf die Konsole — die wichtigste Funktion für Output, die du heute lernst.

## Grundform

```python
print("Hallo Welt")
```

## Mehrere Werte

Per Komma getrennt — `print` setzt automatisch ein Leerzeichen zwischen die Werte:

```python
print("Name:", "Ulrich", "Alter:", 42)
# Name: Ulrich Alter: 42
```

## Trenner ändern: `sep=`

```python
print("2026", "05", "06", sep="-")
# 2026-05-06
```

## Zeilenende ändern: `end=`

Standard ist `"\n"` (Zeilenumbruch).

```python
print("ohne Umbruch...", end=" ")
print("weiter in derselben Zeile")
# ohne Umbruch... weiter in derselben Zeile
```

## Sonderzeichen in Strings (Escapes)

| Escape | Bedeutung              |
|--------|------------------------|
| `\n`   | Zeilenumbruch          |
| `\t`   | Tabulator              |
| `\\`   | Backslash              |
| `\"`   | Anführungszeichen      |
| `\'`   | einfaches Anf.zeichen  |

```python
print("Zeile 1\nZeile 2")
print("Spalte1\tSpalte2")
print("Sie sagte: \"Hallo\"")
```

## Mehrzeilige Strings

Mit dreifachen Anführungszeichen — Zeilenumbrüche bleiben erhalten:

```python
print("""Erste Zeile
Zweite Zeile
Dritte Zeile""")
```

## Datentypen mischen

`print` wandelt automatisch in str um:

```python
n = 42
print("Zahl:", n)        # "Zahl: 42"
```

Du **musst nichts manuell konvertieren** — anders als bei String-Verkettung mit `+`:

```python
print("Zahl: " + n)              # TypeError!
print("Zahl: " + str(n))         # OK
print("Zahl:", n)                # einfacher
```

## Stolpersteine

- **`print(a, b)` vs. `print(a + b)`** — bei `+` müssen beide Strings sein.
- Vergessenes `\n` → alles in einer Zeile.
- `end=""` → keine sichtbare Trennung mehr zwischen Ausgaben.
- **`print` Python 2** ist eine Anweisung (`print "Hi"`), in Python 3 eine Funktion.

## Schnellreferenz

```python
print("a", "b", "c")                 # a b c
print("a", "b", sep="-")             # a-b
print("a", end=" ")                  # ohne Umbruch

# Escapes:  \n  \t  \\  \"
```
