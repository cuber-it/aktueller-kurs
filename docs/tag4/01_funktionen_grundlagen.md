# Funktionen – Grundlagen

## Worum geht's

Eine Funktion bündelt einen benannten Ablauf. Sie kann Eingaben über Parameter erhalten und ein Ergebnis zurückgeben. Dadurch lassen sich Berechnungen mehrfach verwenden und getrennt prüfen.

## Definieren und aufrufen

```python
def begruesse(name):
    """Liefert eine Begrüßung als Text."""
    return f"Hallo {name}!"


nachricht = begruesse("Anna")
print(nachricht)    # Hallo Anna!
```

- `def` legt die Funktion an und bindet sie an den Namen `begruesse`.
- `name` ist ein Parameter der Definition.
- `"Anna"` ist das Argument dieses Aufrufs.
- Der eingerückte Funktionskörper wird erst beim Aufruf ausgeführt.

Die Definition muss ausgeführt worden sein, bevor die Funktion aufgerufen wird. Üblich sind zwei Leerzeilen zwischen eigenständigen Funktionsdefinitionen.

## Ein Ergebnis weiterverwenden

```python
def quadrat(zahl):
    """Liefert das Quadrat einer Zahl."""
    return zahl * zahl


ergebnis = quadrat(3) + quadrat(4)
print(ergebnis)    # 25
```

Der Aufruf ist ein Ausdruck: Sein Rückgabewert kann gespeichert, verrechnet oder an eine andere Funktion übergeben werden. `return` beendet den aktuellen Funktionsaufruf und liefert den angegebenen Wert.

## `return` und `print` unterscheiden

```python
def zeige_doppeltes(zahl):
    """Gibt den doppelten Wert aus."""
    print(zahl * 2)


rueckgabe = zeige_doppeltes(10)    # Ausgabe: 20
print(rueckgabe)                  # None
```

`print` erzeugt eine Ausgabe auf dem Ausgabekanal. Es liefert selbst `None`. Auch eine Funktion ohne ausgeführtes `return` mit Wert liefert `None`.

Eine Berechnungsfunktion sollte ihr Ergebnis normalerweise zurückgeben. Das aufrufende Programm entscheidet dann, ob es den Wert ausgibt, speichert oder weiterverarbeitet. Funktionen dürfen bewusst Ausgaben oder andere Nebenwirkungen haben; der Name sollte ihre Aufgabe erkennen lassen.

## Docstrings

```python
def quadrat(zahl):
    """Liefert das Quadrat einer Zahl."""
    return zahl * zahl


print(quadrat.__doc__)    # Liefert das Quadrat einer Zahl.
```

Ein Docstring ist der erste String im Funktionskörper. Er beschreibt den Zweck; bei Bedarf auch Eingaben, Rückgabe und mögliche Fehler. `help(quadrat)` zeigt diese Beschreibung zusammen mit der Aufrufsignatur.

## Stolpersteine

- `quadrat` bezeichnet die Funktion; `quadrat(5)` ruft sie auf.
- `return` außerhalb einer Funktion erzeugt `SyntaxError`.
- `begruesse()` ohne das erforderliche Argument `name` erzeugt `TypeError`.
- Ein berechneter Wert wird nicht automatisch zurückgegeben: Dafür braucht es `return`.
- Ein `return` ohne nachfolgenden Wert liefert ebenfalls `None`.

## Schnellreferenz

| Bestandteil | Bedeutung |
| --- | --- |
| `def name(parameter):` | Funktion definieren |
| `name(argument)` | Funktion aufrufen |
| `return ergebnis` | Aufruf beenden und Wert liefern |
| Docstring | Zweck und Verhalten dokumentieren |
| `print(ergebnis)` | Ergebnis ausgeben |

**Beispiel:** [Funktionen-Grundlagen](../../tag4/01_funktionen_grundlagen.py)  
**Übungen:** [Begrüßung](../../tag4/aufgaben/basic/begruessung.md), [Temperatur](../../tag4/aufgaben/basic/temperatur.md), [Würfeln](../../tag4/aufgaben/basic/wuerfeln.md)
