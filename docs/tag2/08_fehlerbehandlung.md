# Fehlerbehandlung

## Worum geht's

Wenn etwas schiefgeht, „wirft" Python eine **Exception**. Mit `try`/`except` fängst du sie ab und reagierst kontrolliert — statt das Programm crashen zu lassen.

## Grundform

```python
try:
    riskanter_code
except Fehlerklasse:
    fehlerbehandlung
```

## Beispiel

```python
text = input("Zahl? ")
try:
    zahl = int(text)
except ValueError:
    print(f"'{text}' ist keine Zahl.")
```

`int("abc")` → `ValueError`. Mit `except` fangen wir ihn ab, das Programm läuft weiter.

## Mehrere Exceptions

```python
try:
    a = int(input("Zähler: "))
    b = int(input("Nenner: "))
    print(a / b)
except ValueError:
    print("Bitte ganze Zahlen.")
except ZeroDivisionError:
    print("Nicht durch 0 teilen.")
```

Pro `try`-Block greift der **erste passende** `except`.

## Mehrere Exceptions in einem Zweig

```python
try:
    ...
except (ValueError, TypeError):
    print("Wert oder Typ falsch.")
```

## `else` und `finally`

```python
try:
    x = int("123")
except ValueError:
    print("Fehler.")
else:
    # läuft NUR, wenn KEIN Fehler kam
    print(f"OK: {x}")
finally:
    # läuft IMMER (Aufräumen, Logging, …)
    print("Ende.")
```

| Zweig      | Wann läuft er?                            |
|------------|-------------------------------------------|
| `try`      | immer (bis ein Fehler kommt)              |
| `except`   | wenn passende Exception kommt             |
| `else`     | wenn KEIN Fehler kam                      |
| `finally`  | IMMER (auch bei Fehler / `return` / …)    |

## Wichtige eingebaute Exceptions

| Exception            | Wann?                                  |
|----------------------|----------------------------------------|
| `ValueError`         | falscher Wert (`int("abc")`)           |
| `TypeError`          | falscher Typ (`"a" + 1`)               |
| `ZeroDivisionError`  | Division durch 0                       |
| `FileNotFoundError`  | Datei nicht da                         |
| `KeyError`           | Schlüssel nicht im Dict                |
| `IndexError`         | Index außerhalb der Liste              |
| `NameError`          | Variable nicht definiert               |
| `KeyboardInterrupt`  | Strg+C                                 |
| `Exception`          | Mutter aller normalen Exceptions       |

## Selbst Fehler werfen: `raise`

```python
alter = -3
if alter < 0:
    raise ValueError("Alter darf nicht negativ sein!")
```

→ Das Programm bricht ab — **außer** ein `try`/`except` fängt es.

Wann nützlich?

- **Validierung** früh abbrechen, bevor Folgefehler entstehen.
- **Eigene Fehler signalisieren** (eigene Exception-Klassen kommen später).

## Anti-Patterns

```python
try:
    ...
except:                       # zu breit!
    pass                      # Fehler verschluckt!
```

❌ Ein nacktes `except:` fängt **alles** — sogar `KeyboardInterrupt`. Immer **konkrete** Exceptions fangen.

```python
try:
    ...
except Exception:
    pass                      # immer noch heikel
```

→ Wenn du nicht weißt, was schiefgehen kann, **ist das Pattern wahrscheinlich falsch**.

## Stolpersteine

- **`except:` ohne Klasse** → fängt zu viel.
- **`pass` im `except`** ohne Logging → Fehler unsichtbar.
- **`raise Exception("...")`** statt einer spezifischen Klasse → schlechte Diagnose beim Aufrufer.
- **`finally` läuft IMMER** — auch bei `return`. Kann Rückgabewerte überschreiben.

## Schnellreferenz

```python
try:
    ...
except SpezifischerFehler:
    ...
except (Fehler1, Fehler2):
    ...
else:
    # nur wenn KEIN Fehler kam
    ...
finally:
    # IMMER
    ...

raise ValueError("…")
```
