# Dictionaries – Methoden und Iteration

## Worum geht's

Mit `keys`, `values` und `items` durchläufst du Schlüssel, Werte oder Schlüssel-Wert-Paare. Weitere Methoden ergänzen vorhandene Daten und vereinfachen Auswertungen.

## Drei Sichten auf dieselben Daten

```python
lager = {"Apfel": 50, "Birne": 20, "Kirsche": 120}

print(list(lager.keys()))      # ['Apfel', 'Birne', 'Kirsche']
print(list(lager.values()))    # [50, 20, 120]
print(list(lager.items()))     # [('Apfel', 50), ('Birne', 20), ('Kirsche', 120)]
```

Die Methoden liefern **Sichten** (Views), keine unabhängigen Kopien. Sie spiegeln Änderungen am Dictionary wider. `list(...)` hält dagegen die gerade enthaltenen Elemente in einer neuen Liste fest.

`for produkt in lager:` läuft direkt über die Schlüssel; `keys()` ist dafür nicht erforderlich.

## Schlüssel und Wert gemeinsam

```python
lager = {"Apfel": 50, "Birne": 20, "Kirsche": 120}

for produkt, menge in lager.items():
    print(f"{produkt}: {menge} Stück")
# Apfel: 50 Stück
# Birne: 20 Stück
# Kirsche: 120 Stück

print(sum(lager.values()))    # 190
```

`items()` liefert je Durchlauf ein Paar, das in `produkt` und `menge` entpackt wird. Für eine Summe reichen die Werte.

## Nur bei Bedarf ergänzen: `setdefault`

```python
lager = {"Apfel": 50}
print(lager.setdefault("Apfel", 0))    # 50
print(lager.setdefault("Mango", 0))    # 0
print(lager)                         # {'Apfel': 50, 'Mango': 0}
```

Ein bestehender Wert bleibt erhalten. Bei einem fehlenden Schlüssel wird der Standardwert eingefügt. In beiden Fällen liefert `setdefault` den anschließend gespeicherten Wert.

`get` liest dagegen nur; es ergänzt keine Einträge.

## Mehrere Einträge aktualisieren: `update`

```python
lager = {"Apfel": 50, "Birne": 20}
lager.update({"Birne": 25, "Banane": 60})
print(lager)    # {'Apfel': 50, 'Birne': 25, 'Banane': 60}
```

Vorhandene Schlüssel erhalten neue Werte, weitere Schlüssel kommen hinzu. `update` verändert das Dictionary und liefert `None`. Das vollständige Leeren übernimmt `clear()`.

## Den Schlüssel zum größten Wert finden

```python
lager = {"Apfel": 50, "Birne": 20, "Kirsche": 120}
produkt = max(lager, key=lager.get)

print(produkt)          # Kirsche
print(lager[produkt])   # 120
```

`max` durchläuft die Schlüssel. `key=lager.get` liefert zu jedem Schlüssel den zu vergleichenden Bestand. Zurück kommt der **Schlüssel**, nicht der Bestand. Bei Gleichstand gewinnt der zuerst durchlaufene Schlüssel.

## Stolpersteine

- `max(lager)` vergleicht die Schlüssel selbst, hier also Produktnamen.
- Während der Iteration keine Schlüssel ergänzen oder löschen; das kann `RuntimeError` erzeugen.
- `list(lager.items())` kopiert keine verschachtelten Wertobjekte.
- `max` auf einem leeren Dictionary erzeugt ohne Standardwert `ValueError`.

## Schnellreferenz

| Aufgabe | Methode oder Ausdruck |
| --- | --- |
| Schlüssel / Werte / Paare | `keys()` / `values()` / `items()` |
| Lesen mit Standardwert | `get(schluessel, standardwert)` |
| Fehlenden Eintrag ergänzen | `setdefault(schluessel, standardwert)` |
| Einträge übernehmen | `update(andere_daten)` |
| Schlüssel zum größten Wert | `max(daten, key=daten.get)` |

**Beispiel:** [Dictionary-Methoden](../../tag3/07_dict_methoden.py)  
**Übung:** [Telefonbuch](../../tag3/aufgaben/basic/telefonbuch.md)
