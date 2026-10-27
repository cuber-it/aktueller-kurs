# Regex (Anriss)

## Worum geht's

Regex = **Reguläre Ausdrücke**. Eine kompakte Sprache, um **Muster in Texten** zu beschreiben — „alle PLZs", „alle E-Mails", „alles, was einer Telefonnummer ähnelt". In Python steckt das im Modul `re`.

## Grundpaket

```python
import re

re.search(muster, text)        # erstes Vorkommen oder None
re.findall(muster, text)       # alle Treffer als Liste
re.sub(muster, ersatz, text)   # ersetzen
re.match(muster, text)         # nur am String-Anfang
```

## Raw Strings: `r"..."`

Backslashes haben in Python eine eigene Bedeutung (`\n`). Damit Regex-Backslashes nicht kollidieren: **immer mit `r` davor**.

```python
re.search(r"\d+", text)        # GUT
re.search("\d+", text)         # geht oft, aber riskant
```

## Wichtigste Bausteine

| Muster   | Bedeutung                                  |
|----------|--------------------------------------------|
| `.`      | beliebiges Zeichen (außer `\n`)            |
| `\d`     | eine Ziffer (0–9)                          |
| `\D`     | KEINE Ziffer                               |
| `\w`     | Buchstabe, Ziffer oder `_`                 |
| `\W`     | das Gegenteil                              |
| `\s`     | Whitespace                                 |
| `[abc]`  | a, b oder c                                |
| `[a-z]`  | Bereich                                    |
| `[^abc]` | alles AUSSER a, b, c                       |
| `^`      | Anfang                                     |
| `$`      | Ende                                       |
| `\b`     | Wortgrenze                                 |

## Quantifizierer (gelten für das Zeichen davor)

| Quant.   | Bedeutung           |
|----------|---------------------|
| `*`      | 0 oder mehr         |
| `+`      | 1 oder mehr         |
| `?`      | 0 oder 1            |
| `{n}`    | genau n             |
| `{n,m}`  | n bis m             |

## Match-Objekte

```python
m = re.search(r"\d+", "Test 42 mehr")
if m:
    m.group()     # '42'
    m.start()     # 5
    m.end()       # 7
```

`re.search` liefert `None`, wenn nichts gefunden wurde — vor `.group()` immer prüfen.

## Beispiele

```python
# deutsche Postleitzahl: 5 Ziffern, isoliert
re.search(r"\b\d{5}\b", "10115 Berlin")

# einfache E-Mail (NICHT für strikte Validierung!)
re.findall(r"\S+@\S+\.\S+", "max@uc-it.de admin@example.org")

# Datum tt.mm.jjjj
re.search(r"\d{2}\.\d{2}\.\d{4}", "Geboren am 15.05.1980")

# alles Nicht-Ziffern entfernen
re.sub(r"\D", "", "Tel: 030-1234567")    # '0301234567'

# Eingabe in Großbuchstaben anonymisieren (alle Buchstaben -> X)
re.sub(r"[A-Za-zÄÖÜäöü]", "X", "Hallo Welt")    # 'XXXXX XXXX'

# Einfache IP-Adresse mit Zahlengruppen
matches = re.finditer(r"\b(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})\b", text)
for match in matches:
    ...
```

## Stolpersteine

- **Backslash-Salat ohne `r"..."`** → unerwartete Ergebnisse.
- **`re.match` vs. `re.search`** — `match` greift nur am Anfang!
- **Greedy vs. lazy** — `.*` ist gefräßig (`.*?` ist sparsam). Wenn dein Match „zu viel mitnimmt", ist das oft die Ursache.
- **E-Mail/IBAN-Validierung mit Regex** ist ein Wespennest — für Extraktion super, für strikte Prüfung andere Tools.
- **Regex auf HTML/XML** — schlechte Idee, dafür Parser nutzen.
- **Performance** — bei riesigen Texten: einmal `re.compile(...)` und wiederverwenden.

## Schnellreferenz

```python
import re

re.search(r"muster", text)           # erstes Vorkommen oder None
re.findall(r"muster", text)          # alle Treffer als Liste
re.sub(r"muster", "ersatz", text)    # ersetzen

# Klassen
\d  \D  \w  \W  \s  \S
[abc]  [a-z]  [^abc]

# Anker
^  $  \b

# Quantifizierer
*  +  ?  {n}  {n,m}

# raw string immer:  r"..."
```
