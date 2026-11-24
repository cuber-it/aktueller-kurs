# Parameter und Argumente

## Worum geht's

Parameter stehen in der Funktionsdefinition. Argumente sind die Werte eines Aufrufs. Die Zuordnung kann über die Position oder über einen Parameternamen erfolgen.

## Position, Name und Standardwert

```python
def begruesse(name, gruss="Hallo"):
    """Liefert einen Gruß mit optionaler Anrede."""
    return f"{gruss} {name}!"


print(begruesse("Anna"))                         # Hallo Anna!
print(begruesse("Ben", "Moin"))                  # Moin Ben!
print(begruesse(gruss="Servus", name="Cem"))     # Servus Cem!
print(begruesse("Dora", gruss="Guten Morgen"))   # Guten Morgen Dora!
```

| Aufrufart | Zuordnung |
| --- | --- |
| Positionsargument | Über die Reihenfolge |
| Schlüsselwortargument | Über den Parameternamen |
| Weggelassenes optionales Argument | Über den definierten Standardwert |

`name` ist erforderlich. `gruss` besitzt einen Standardwert und darf beim Aufruf fehlen. Schlüsselwortargumente können untereinander in anderer Reihenfolge stehen.

Direkt angegebene Positionsargumente stehen vor den Schlüsselwortargumenten. In der gezeigten Definition stehen Parameter mit Standardwert hinter den erforderlichen Parametern.

## Standardwerte entstehen beim Definieren

Dieses Gegenbeispiel verwendet dieselbe Standardliste bei jedem Aufruf:

```python
def sammle_falsch(element, liste=[]):
    liste.append(element)
    return liste


print(sammle_falsch("Apfel"))    # ['Apfel']
print(sammle_falsch("Birne"))    # ['Apfel', 'Birne']
```

Die Liste wird beim Ausführen der Definition einmal angelegt. Sie wird bei späteren Aufrufen ohne Listenargument weiterverwendet. Dasselbe Problem kann mit einem Dictionary oder Set als veränderlichem Standardwert entstehen.

## Eine neue Liste pro Aufruf

```python
def sammle(element, liste=None):
    """Ergänzt eine vorhandene Liste oder erstellt eine neue."""
    if liste is None:
        liste = []
    liste.append(element)
    return liste


print(sammle("Apfel"))    # ['Apfel']
print(sammle("Birne"))    # ['Birne']
```

`None` bedeutet hier: Es wurde keine Liste bereitgestellt. Erst im Funktionskörper entsteht die neue Liste.

## Eine übergebene Liste wird verändert

```python
def sammle(element, liste=None):
    """Ergänzt eine vorhandene Liste oder erstellt eine neue."""
    if liste is None:
        liste = []
    liste.append(element)
    return liste


obst = ["Kirsche"]
sammle("Orange", obst)
print(obst)    # ['Kirsche', 'Orange']
```

Beim Aufruf wird keine Kopie angelegt. Die Funktion und der Aufrufer greifen auf dieselbe Liste zu. Soll das Original erhalten bleiben, muss die Funktion oder der Aufrufer ausdrücklich eine Kopie erstellen.

## Stolpersteine

- Fehlende Pflichtargumente oder unbekannte Schlüsselwortargumente erzeugen `TypeError`.
- Derselbe Parameter darf nicht zugleich per Position und Schlüsselwort belegt werden.
- `if liste is None:` unterscheidet eine fehlende Liste von einer übergebenen leeren Liste.
- Ein Standardwert macht nur das Argument optional; er prüft nicht dessen Typ.

## Schnellreferenz

| Definition | Möglicher Aufruf |
| --- | --- |
| `def begruesse(name, gruss="Hallo"):` | `begruesse("Anna")` |
| Dieselbe Definition | `begruesse("Anna", gruss="Moin")` |
| `def sammle(element, liste=None):` | `sammle("Apfel")` |

**Beispiel:** [Parameter](../../tag4/02_parameter.py)  
**Übung:** [Begrüßung](../../tag4/aufgaben/basic/begruessung.md)
