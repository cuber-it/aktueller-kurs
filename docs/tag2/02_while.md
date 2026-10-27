# `while`-Schleife

## Worum geht's

Eine `while`-Schleife wiederholt einen Block, **solange** ihre Bedingung wahr ist.

## Grundform

```python
zaehler = 1
while zaehler <= 5:
    print(zaehler)
    zaehler += 1
```

## Wann `while` (vs. `for`)?

- **`while`** — wenn du **vorher nicht weißt**, wie oft wiederholt wird (z. B. „bis Nutzer Enter drückt").
- **`for`** — wenn die Anzahl klar ist oder du eine Sammlung durchläufst.

## `break` — sofort raus

```python
while True:
    eingabe = input("ende? ")
    if eingabe == "ende":
        break
    print("weiter...")
print("fertig")
```

`while True` ist eine **bewusste Endlosschleife**, gepaart mit `break` für den Ausstieg — ein häufiges Muster.

## `continue` — diesen Durchlauf überspringen

Springt zur Bedingungsprüfung zurück, ohne den Rest des Blocks auszuführen:

```python
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue           # gerade überspringen
    print(i)               # 1, 3, 5, 7, 9
```

## Endlosschleifen

Eine Schleife endet **nie**, wenn:

- Bedingung **immer** `True` bleibt
- **kein** `break` greift
- **kein** Fehler fliegt

```python
while True:
    print("immer und ewig")    # Strg+C zum Abbrechen
```

Häufige Ursache: **Bedingung wird nicht aktualisiert**:

```python
zaehler = 0
while zaehler < 5:
    print(zaehler)
    # zaehler += 1  ← VERGESSEN -> Endlosschleife!
```

## `else`-Zweig (selten)

```python
while bedingung:
    ...
else:
    # läuft, wenn die Schleife "normal" endete
    # (NICHT bei break)
    ...
```

Selten benutzt, nice to know.

## Stolpersteine

- **Zähler nicht hochzählen** → Endlosschleife.
- **Bedingung mit `=` statt `==`** → SyntaxError.
- **`break`/`continue` außerhalb einer Schleife** → SyntaxError.
- **`while True`** ohne `break`-Pfad → tot.

## Schnellreferenz

```python
while bedingung:
    ...
    break        # Schleife verlassen
    continue     # zum nächsten Durchgang
```
