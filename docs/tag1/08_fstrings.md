# f-Strings

## Worum geht's

Mit `f"..."` lassen sich Werte direkt in einen Text einsetzen — die moderne und empfohlene Art, Strings zu formatieren.

## Grundform

`f` direkt vor dem öffnenden Anführungszeichen, Werte in `{...}`:

```python
name = "Ulrich"
alter = 42

print(f"Hallo {name}, du bist {alter} Jahre alt.")
# Hallo Ulrich, du bist 42 Jahre alt.
```

## Ausdrücke sind erlaubt

Innerhalb der `{}` darf alles stehen, was Python auswerten kann:

```python
print(f"Nächstes Jahr: {alter + 1}")
print(f"Großbuchstaben: {name.upper()}")
print(f"{2 ** 10} Bytes pro KB")
```

## Format-Spezifizierer

Nach einem `:` folgt ein Format:

```python
preis = 3.14159

f"{preis:.2f}"        # '3.14'      (2 Nachkommastellen)
f"{preis:.0f}"        # '3'         (gerundet)
f"{preis:+.2f}"       # '+3.14'     (mit Vorzeichen)
f"{1234:,}"           # '1,234'     (Tausender-Komma)
f"{0.5:.0%}"          # '50%'       (Prozent)
```

## Breite & Ausrichtung

Nützlich für Tabellen:

```python
f"{'Name':<10}"      # 'Name      '   (links, Breite 10)
f"{'Name':>10}"      # '      Name'   (rechts)
f"{'Name':^10}"      # '   Name   '   (zentriert)
f"{42:>5}"           # '   42'        (rechtsbündig)
f"{42:05}"           # '00042'        (mit Nullen aufgefüllt)
```

## Debug-Modus (Python 3.8+)

`{x=}` gibt **Name = Wert** aus — sehr nützlich beim Debuggen:

```python
n = 42
print(f"{n=}")           # n=42
print(f"{n + 1=}")       # n + 1=43
```

## Mehrzeilige f-Strings

Mit `"""…"""`:

```python
print(f"""
Name:  {name}
Alter: {alter}
""")
```

## Stolpersteine

- **`f` vergessen** → es wird kein Wert eingesetzt, nur der Text mit `{...}` ausgegeben.
- **Geschweifte Klammern als Text** → `{{` für `{`, `}}` für `}`:

  ```python
  print(f"{{geschweift}}")     # {geschweift}
  ```
- Anführungszeichen *innerhalb* eines f-Strings → anderes Quote-Zeichen verwenden:

  ```python
  d = {"name": "Ulrich"}
  print(f"{d['name']}")
  ```

## Alte Schreibweisen (zur Wiedererkennung)

Du wirst in altem Code sehen:

```python
"%s ist %d" % ("Alter", 42)              # %-Formatierung
"{} ist {}".format("Alter", 42)          # str.format()
```

→ In neuem Code: **immer f-Strings**.

## Schnellreferenz

```python
f"{wert}"            # einsetzen
f"{wert:.2f}"        # 2 Nachkommastellen
f"{wert:>10}"        # rechtsbündig auf 10 Zeichen
f"{wert=}"           # 'wert=42' (Debug, 3.8+)
```
