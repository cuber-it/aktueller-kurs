# Listen auswerten

## Worum geht's

Listen lassen sich umformen, filtern, nummerieren und gemeinsam durchlaufen. Eine kurze Schreibweise hilft, wenn die Verarbeitung dabei gut erkennbar bleibt.

## Schleife und List Comprehension

```python
zahlen = [1, 2, 3, 4, 5, 6]
quadrate = []
for zahl in zahlen:
    quadrate.append(zahl ** 2)

print(quadrate)    # [1, 4, 9, 16, 25, 36]
```

Dieselbe Umformung als **List Comprehension**:

```python
zahlen = [1, 2, 3, 4, 5, 6]
quadrate = [zahl ** 2 for zahl in zahlen]
gerade = [zahl for zahl in zahlen if zahl % 2 == 0]

print(quadrate)    # [1, 4, 9, 16, 25, 36]
print(gerade)      # [2, 4, 6]
```

Der Ausdruck vor `for` liefert den neuen Wert. Das optionale `if` filtert die Eingaben. Beide Varianten erzeugen neue Listen; `zahlen` bleibt unverändert.

Bei mehreren Arbeitsschritten, Fehlerbehandlung oder Ausgaben ist eine normale Schleife meist besser lesbar.

## Nummer und Wert: `enumerate`

```python
obst = ["Apfel", "Birne", "Kirsche"]
for nummer, name in enumerate(obst, start=1):
    print(f"{nummer}. {name}")
# 1. Apfel
# 2. Birne
# 3. Kirsche
```

`start=1` bestimmt nur die ausgegebene Nummerierung. Die Indizes der ursprünglichen Liste beginnen weiterhin bei `0`.

## Zusammengehörige Folgen: `zip`

```python
obst = ["Apfel", "Birne", "Kirsche"]
preise = [2.50, 1.20, 3.00]

for name, preis in zip(obst, preise, strict=True):
    print(f"{name}: {preis:.2f}")
# Apfel: 2.50
# Birne: 1.20
# Kirsche: 3.00
```

`zip` verbindet Elemente gleicher Position. Ohne `strict=True` endet es mit der kürzesten Folge. Mit `strict=True` wird beim Durchlaufen eine abweichende Länge als `ValueError` gemeldet. Die Option gibt es ab Python 3.10.

## Nach einem Merkmal sortieren

```python
woerter = ["Banane", "Ei", "Apfel"]
print(sorted(woerter, key=len))    # ['Ei', 'Apfel', 'Banane']
print(woerter)                    # ['Banane', 'Ei', 'Apfel']
```

`key=len` übergibt die Funktion selbst. Python ermittelt damit für jedes Wort die Länge und vergleicht diese Werte. `reverse=True` kehrt die Sortierrichtung um.

`key=str.casefold` ermöglicht eine Sortierung ohne Unterscheidung der Großschreibung. `casefold()` normalisiert Text für solche Vergleiche; die Originalwerte bleiben erhalten.

## Kennzahlen

```python
werte = [10, 5, 8, 3]
print(sum(werte))                  # 26
print(min(werte), max(werte))      # 3 10
print(sum(werte) / len(werte))     # 6.5
```

Bei leeren Daten liefern `min` und `max` ohne Standardwert einen `ValueError`. Die gezeigte Mittelwertberechnung würde durch `0` teilen.

## Stolpersteine

- Eine Comprehension erzeugt ihre vollständige Ergebnisliste im Speicher.
- `zip` prüft ohne `strict=True` keine übereinstimmenden Längen.
- `key=len` und `key=len(...)` bedeuten etwas anderes: benötigt wird die Funktion.

## Schnellreferenz

| Aufgabe | Schreibweise |
| --- | --- |
| Umformen | `[ausdruck for element in daten]` |
| Filtern | `[element for element in daten if bedingung]` |
| Nummerieren | `enumerate(daten, start=1)` |
| Paarweise durchlaufen | `zip(a, b, strict=True)` |
| Nach Merkmal sortieren | `sorted(daten, key=funktion)` |

**Beispiel:** [Listen auswerten](../../tag3/05_arbeitstechniken_listen.py)  
**Übung:** [Notenauswertung](../../tag3/aufgaben/erfahren/notenauswertung.md)
