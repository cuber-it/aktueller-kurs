# Dictionaries – Zählen und Gruppieren

## Worum geht's

Dictionaries eignen sich für Häufigkeiten, Gruppen und berechnete Zuordnungen. Für wiederkehrende Aufgaben bietet `collections` die Typen `Counter` und `defaultdict`.

## Zuordnungen erzeugen: Dict Comprehension

```python
woerter = ["Apfel", "Birne", "Apfel", "Kirsche"]
laengen = {wort: len(wort) for wort in woerter}
print(laengen)    # {'Apfel': 5, 'Birne': 5, 'Kirsche': 7}
```

Vor `for` steht das Paar `schluessel: wert`. Wiederholte Schlüssel überschreiben ihren bisherigen Wert. `Apfel` steht deshalb nur einmal im Ergebnis.

## Mit einem Dictionary zählen

```python
woerter = ["Apfel", "Birne", "Apfel", "Kirsche", "Birne"]
haeufigkeit = {}

for wort in woerter:
    haeufigkeit[wort] = haeufigkeit.get(wort, 0) + 1

print(haeufigkeit)    # {'Apfel': 2, 'Birne': 2, 'Kirsche': 1}
```

Ein neues Wort startet beim Standardwert `0`. Jeder Durchlauf erhöht seinen Zähler um `1`.

## Häufigkeiten mit `Counter`

```python
from collections import Counter

woerter = ["Apfel", "Birne", "Apfel", "Kirsche", "Birne"]
zaehler = Counter(woerter)

print(zaehler["Apfel"])         # 2
print(zaehler["Mango"])         # 0
print(zaehler.most_common(2))   # [('Apfel', 2), ('Birne', 2)]
```

`Counter` zählt die Elemente eines Iterables. `most_common(n)` liefert höchstens `n` Paare aus Element und Anzahl, nach Häufigkeit absteigend. Bei Gleichstand bleibt die Reihenfolge des ersten Auftretens erhalten.

Vor dem Zählen muss feststehen, was als gleiches Wort gilt: `"Apfel"` und `"apfel"` sind zunächst verschieden. Für Vergleiche ohne Großschreibung kann der Text zuvor mit `casefold()` normalisiert werden.

## Gruppen mit `defaultdict`

```python
from collections import defaultdict

gruppen = defaultdict(list)
for wort in ["Apfel", "Ananas", "Birne", "Banane"]:
    gruppen[wort[0]].append(wort)

print(dict(gruppen))
# {'A': ['Apfel', 'Ananas'], 'B': ['Birne', 'Banane']}
```

Beim Zugriff mit `[]` auf einen fehlenden Schlüssel erzeugt `defaultdict(list)` eine neue leere Liste und speichert sie unter diesem Schlüssel. Anschließend wird das Wort angehängt.

`list` wird ohne Klammern übergeben. Python ruft `list()` für jeden neuen Schlüssel gesondert auf. `get` löst diese Erzeugung nicht aus.

## Nach Häufigkeit ausgeben

```python
haeufigkeit = {"Apfel": 2, "Birne": 2, "Kirsche": 1}
for wort in sorted(haeufigkeit, key=haeufigkeit.get, reverse=True):
    print(f"{wort}: {haeufigkeit[wort]}")
# Apfel: 2
# Birne: 2
# Kirsche: 1
```

`sorted` liefert hier eine Liste der Schlüssel. Die Zähler bleiben im Dictionary. Gleich große Sortierschlüssel behalten ihre bisherige Reihenfolge.

## Stolpersteine

- Ein Set entfernt Duplikate; danach kann `Counter` ihre ursprüngliche Häufigkeit nicht mehr ermitteln.
- Ein leerer String hat kein Zeichen an Position `0`; vor einer Gruppierung gegebenenfalls prüfen.
- Eine Dict Comprehension sammelt gleiche Schlüssel nicht automatisch in Listen.
- `defaultdict(list())` funktioniert nicht: benötigt wird ein aufrufbarer Erzeuger.

## Schnellreferenz

| Aufgabe | Werkzeug |
| --- | --- |
| Werte je Schlüssel berechnen | Dict Comprehension |
| Häufigkeiten ermitteln | `Counter(werte)` |
| Häufigste Elemente | `zaehler.most_common(n)` |
| Listen je Schlüssel sammeln | `defaultdict(list)` |

**Beispiel:** [Zählen und Gruppieren](../../tag3/08_arbeitstechniken_dict.py)  
**Übungen:** [Worthäufigkeiten](../../tag3/aufgaben/erfahren/wort_top3.md), [Notenauswertung](../../tag3/aufgaben/erfahren/notenauswertung.md)
