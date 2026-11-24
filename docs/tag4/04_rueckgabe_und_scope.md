# Rückgabewerte und Gültigkeitsbereiche

## Worum geht's

Eine Funktion kann mehrere Ergebnisse als Tupel liefern und sich mit `return` früh beenden. Ihre lokalen Namen gehören zum jeweiligen Aufruf. Das hilft, Berechnungen von Änderungen am übrigen Programmzustand zu trennen.

## Mehrere Ergebnisse zurückgeben

```python
def min_max(werte):
    """Liefert Minimum und Maximum einer nicht leeren Sammlung."""
    if not werte:
        raise ValueError("Mindestens ein Wert ist erforderlich.")
    return min(werte), max(werte)


kleinste, groesste = min_max([7, 2, 9, 4])
print(kleinste, groesste)    # 2 9

ergebnis = min_max([5, 1, 8])
print(ergebnis)             # (1, 8)
```

Es wird ein Wert zurückgegeben: ein Tupel mit zwei Elementen. Der Aufrufer kann es entpacken oder als Ganzes speichern.

Die Prüfung am Anfang weist eine leere Sammlung ab, bevor `min` und `max` aufgerufen werden. Der Fehler ist Teil des beschriebenen Funktionsverhaltens.

## Frühes `return`

```python
def vorzeichen(zahl):
    """Liefert die Bezeichnung des Vorzeichens."""
    if zahl > 0:
        return "positiv"
    if zahl < 0:
        return "negativ"
    return "null"


print(vorzeichen(-3))    # negativ
```

Nach einem ausgeführten `return` wird der restliche Funktionskörper nicht mehr durchlaufen. Ein zusätzliches `else` ist hier nicht nötig.

## Lokale Namen

```python
def erhoehe(stand):
    """Liefert den nächsten Stand."""
    stand += 1
    return stand


stand = 10
naechster_stand = erhoehe(stand)
print(stand)             # 10
print(naechster_stand)   # 11
```

Der Parameter `stand` ist lokal. Die Zuweisung im Funktionskörper bindet diesen lokalen Namen neu. Der gleichnamige Name außerhalb der Funktion bleibt unverändert.

Das unterscheidet sich vom Ändern einer übergebenen Liste mit `append`: Dabei verändert sich ein gemeinsam verwendetes Objekt.

## Äußere Namen und `global`

Eine Funktion kann auf Namen ihres Moduls lesend zugreifen. Eine Zuweisung an einen Namen im Funktionskörper macht ihn normalerweise lokal:

```python
stand = 10

def fehlerhaft():
    stand += 1


try:
    fehlerhaft()
except UnboundLocalError:
    print("Lokaler stand wurde noch nicht belegt.")
```

`global stand` würde die Zuweisung ausdrücklich auf den Namen im Modul beziehen. Beim gezeigten Zähler machen ein Parameter und ein Rückgabewert den Datenfluss deutlicher.

## Kurze Funktion als Sortierschlüssel: `lambda`

```python
datensaetze = [{"name": "Apfel", "menge": 3}, {"name": "Birne", "menge": 1}]
nach_menge = sorted(datensaetze, key=lambda eintrag: eintrag["menge"])
print(nach_menge)
# [{'name': 'Birne', 'menge': 1}, {'name': 'Apfel', 'menge': 3}]
```

`lambda eintrag: eintrag["menge"]` erzeugt eine Funktion mit einem Ausdruck als Rückgabewert. Für mehrere Arbeitsschritte eignet sich eine benannte Funktion mit `def`.

## Stolpersteine

- Lokal neu zuweisen und ein übergebenes Objekt verändern sind verschiedene Vorgänge.
- Die Anzahl beim Entpacken muss zu den zurückgegebenen Elementen passen.
- Fehlende Daten nicht durch eine scheinbar gültige Kennzahl wie `0` ersetzen.
- `return` in einer Schleife beendet die Funktion, nicht nur die Schleife.

## Schnellreferenz

| Aufgabe | Mittel |
| --- | --- |
| Mehrere Ergebnisse | `return minimum, maximum` |
| Ungültige Eingabe abweisen | `raise ValueError(...)` |
| Aufruf früh beenden | `return wert` |
| Kurzes Sortierkriterium | `key=lambda eintrag: eintrag["menge"]` |

**Beispiel:** [Rückgabe und Scope](../../tag4/04_rueckgabe_und_scope.py)  
**Übungen:** [Statistik](../../tag4/aufgaben/erfahren/statistik.md), [Lottofunktionen](../../tag4/aufgaben/basic/lottobude.md)
