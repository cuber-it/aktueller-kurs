# Datei-Input

## Worum geht's

Dateien lesen ist eine Kernaufgabe. In Python: `open()` zum Öffnen, `with` als Schutzgürtel — Datei wird **automatisch geschlossen**, auch wenn ein Fehler fliegt.

## Grundmuster

# Old fashioned
```python
fd = open("daten.txt") # default: r, encoding default utf-8
inhalt = fd.read()
close(fd)
```
# Modern style
```python
with open("daten.txt", "r", encoding="utf-8") as f:
    inhalt = f.read()
```
# Slurp - die Funktion zum lesen
```python
def readfile(fname, encoding="utf-8"):
    with open(fname, "r", encoding=encoding) as f:
        return f.read()
```

- `"r"` — Modus „read" (Standard, kann weggelassen werden).
- `encoding="utf-8"` — **immer angeben**, sonst zicken Umlaute.
- `as f` — die Datei wird unter dem Namen `f` verfügbar.
- `with` — sorgt dafür, dass die Datei am Blockende geschlossen wird.

## Drei Lese-Varianten

### Alles auf einmal (`.read()`)

```python
with open("daten.txt", "r", encoding="utf-8") as f:
    inhalt = f.read()         # ein einziger str
```

→ Praktisch für **kleine** Dateien.

### Zeilenweise (Standardfall)

```python
with open("daten.txt", "r", encoding="utf-8") as f:
    for zeile in f:
        print(zeile.strip())
```

→ **Empfohlen** für lange Dateien — speichert nicht alles im RAM.

⚠️ Jede `zeile` enthält `\n` mit — meist will man `.strip()`.

### Alle Zeilen als Liste

```python
with open("daten.txt", "r", encoding="utf-8") as f:
    zeilen = f.readlines()    # ['zeile1\n', 'zeile2\n', ...]

oder

zeilen = f.read().splitlines() # - da werden "\n" gleich mit entsorgt
```

→ Bequem, lädt aber alles in den Speicher.

## Modi für `open()`

| Modus | Bedeutung                       |
|-------|---------------------------------|
| `"r"` | lesen (Standard)                |
| `"w"` | schreiben (**überschreibt!**)   |
| `"a"` | anhängen (append)               |
| `"x"` | exklusiv schreiben (Fehler, wenn Datei existiert) |
| `"b"` | binär (z. B. `"rb"`)            |

## Pfade robust angeben

Mit `pathlib`:

```python
from pathlib import Path

datei = Path(__file__).parent / "daten.txt"
with open(datei, "r", encoding="utf-8") as f:
    ...
```

→ Funktioniert egal aus welchem Arbeitsverzeichnis das Skript gestartet wird.

## Häufige Fehler abfangen

```python
try:
    with open("daten.txt", "r", encoding="utf-8") as f:
        ...
except FileNotFoundError:
    print("Datei nicht da.")
```

(Mehr zu `try`/`except` im nächsten Kapitel.)

## Stolpersteine

- **`with` vergessen** — die Datei bleibt offen, bis sie der Garbage Collector schließt. Nicht zuverlässig.
- **`encoding=` vergessen** — auf Linux/macOS oft UTF-8, auf Windows oft cp1252 → kaputte Umlaute.
- **`"w"` versehentlich** — überschreibt die Datei kommentarlos. Wichtige Daten weg.
- **Zeilenende nicht gestrippt** — Vergleiche schlagen fehl: `"hallo\n" != "hallo"`.
- **Datei existiert nicht** → `FileNotFoundError`.

## Schnellreferenz

```python
# lesen
with open(pfad, "r", encoding="utf-8") as f:
    inhalt = f.read()           # alles
    f.readline()                # eine Zeile
    f.readlines()               # alle Zeilen als Liste
    for zeile in f: ...         # zeilenweise iterieren

# schreiben (kommt bei Bedarf)
with open(pfad, "w", encoding="utf-8") as f:
    f.write("hallo\n")

# robuste Pfade
from pathlib import Path
p = Path(__file__).parent / "daten.txt"
```
## Anmerkung - chunkwise read für sehr grosse Dateien
```python
def read_chunks(path, size=4096):
    with open(path, "rb") as f:
        while chunk := f.read(size):
            yield chunk

for chunk in read_chunks("datei.bin"):
    print(len(chunk))
```
