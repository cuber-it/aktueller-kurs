# Flexible Argumentlisten – `*args` und `**kwargs`

## Worum geht's

Eine Funktion kann beliebig viele Positionsargumente oder Schlüsselwortargumente entgegennehmen. Umgekehrt lassen sich vorhandene Sammlungen beim Aufruf in einzelne Argumente zerlegen.

## Positionsargumente sammeln: `*`

```python
def summe(*zahlen):
    """Liefert die Summe aller übergebenen Zahlen."""
    return sum(zahlen)


print(summe(1, 2, 3))    # 6
print(summe())           # 0
```

`zahlen` ist innerhalb der Funktion ein **Tupel** mit allen übergebenen Positionsargumenten. Ohne Argumente ist das Tupel leer.

`args` ist nur ein üblicher Name. `*zahlen` funktioniert nach derselben Regel und beschreibt hier den Inhalt genauer.

## Schlüsselwortargumente sammeln: `**`

```python
def beschreibe(**daten):
    """Verbindet Feldnamen und Werte zu einer Beschreibung."""
    beschreibungen = [f"{feld}: {wert}" for feld, wert in daten.items()]
    return ", ".join(beschreibungen)


print(beschreibe(name="Anna", stadt="Hamburg"))
# name: Anna, stadt: Hamburg
```

`daten` ist ein **Dictionary**. Die Namen der übergebenen Schlüsselwortargumente werden zu seinen Schlüsseln. Ohne solche Argumente ist es leer; `beschreibe()` liefert hier einen leeren String.

`kwargs` steht für „keyword arguments“ und ist ebenfalls eine Namenskonvention.

## Vorhandene Werte beim Aufruf entpacken

```python
def summe(*zahlen):
    """Liefert die Summe aller übergebenen Zahlen."""
    return sum(zahlen)


werte = [1, 2, 3]
print(summe(*werte))    # 6
```

`*werte` übergibt die drei Listenelemente als einzelne Positionsargumente. `summe(werte)` würde dagegen eine einzige Liste übergeben. Die gezeigte Funktion erwartet einzelne Zahlen und könnte diese Liste nicht mit `sum` verarbeiten.

Für benannte Argumente:

```python
def begruesse(name, gruss="Hallo"):
    """Liefert einen Gruß."""
    return f"{gruss} {name}!"


aufruf = {"name": "Ben", "gruss": "Moin"}
print(begruesse(**aufruf))    # Moin Ben!
```

`**aufruf` verteilt die Dictionary-Einträge auf die gleichnamigen Parameter. Die Schlüssel müssen Strings sein. Ohne einen `**`-Sammelparameter müssen sie außerdem zu den Parametern der aufgerufenen Funktion passen.

## Definition und Aufruf auseinanderhalten

| Stelle | `*` | `**` |
| --- | --- | --- |
| Definition | Positionsargumente als Tupel sammeln | Schlüsselwortargumente als Dictionary sammeln |
| Aufruf | Iterable in Positionsargumente entpacken | Zuordnung in Schlüsselwortargumente entpacken |

## Stolpersteine

- Die Sterne gehören zur Definition oder zum Aufruf, nicht zum gespeicherten Variablennamen.
- Derselbe Parameter darf beim Entpacken und durch ein weiteres Argument nicht doppelt belegt werden.
- `*` auf einem Dictionary entpackt dessen Schlüssel als Positionsargumente.
- `**daten` übergibt keine automatisch geprüften Optionen; die Funktion muss zulässige Inhalte selbst festlegen.

## Schnellreferenz

| Schreibweise | Verwendung |
| --- | --- |
| `def summe(*zahlen):` | Viele Zahlen entgegennehmen |
| `def beschreibe(**daten):` | Benannte Angaben entgegennehmen |
| `summe(*werte)` | Vorhandene Folge entpacken |
| `begruesse(**aufruf)` | Vorhandene Zuordnung entpacken |

**Beispiel:** [Flexible Argumentlisten](../../tag4/03_args_kwargs.py)  
**Übung:** [Statistik](../../tag4/aufgaben/erfahren/statistik.md)
