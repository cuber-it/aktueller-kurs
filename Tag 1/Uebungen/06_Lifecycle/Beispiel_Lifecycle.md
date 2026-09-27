# Beispiel · Wer räumt auf – in klein

Dieselbe Aufgabe an einem kleineren Gegenstand, vollständig durchgeführt.

---

## Der Gegenstand

Ein Prüfstand für Autobatterien. Ein Skript misst über ein Multimeter an einer seriellen Schnittstelle die Spannung und prüft sie. Es geht um die **Verbindung zum Messgerät**.

```python
class Multimeter:
    def __init__(self, port):
        self.port = port
        self.handle = None

    def open(self):
        print(f"open {self.port}")
        self.handle = f"handle:{self.port}"

    def measure_voltage(self):
        print(f"measure via {self.handle}")
        return 11.98

    def close(self):
        print(f"close {self.handle}")
        self.handle = None


meter = Multimeter("/dev/ttyUSB0")
meter.open()
voltage = meter.measure_voltage()
check_battery(voltage)
meter.close()
```

`check_battery` wirft eine `AssertionError`, wenn die Spannung außerhalb des Sollbereichs liegt. Eine serielle Schnittstelle kann nur von einem Prozess gleichzeitig geöffnet sein.

---

## Schritt 1 · Welche Zustände gibt es?

| Zustand | `handle` | sinnvolle Operationen |
|---|---|---|
| geschlossen | `None` | `open()` |
| geöffnet | gesetzt | `measure_voltage()`, `close()` |

**Heute** prüft `measure_voltage()` den Zustand nicht. Im geschlossenen Zustand gibt der Platzhalter `measure via None` aus und liefert trotzdem einen Wert. Ob eine echte Treiberbibliothek an dieser Stelle abbricht oder einen unsinnigen Wert liefert, hängt von der Bibliothek ab. Beides ist schwer zu diagnostizieren.

---

## Schritt 2 · Der Fehlerpfad

Liegt die Spannung außerhalb des Sollbereichs, wirft `check_battery` eine Exception. `meter.close()` wird nicht erreicht.

**Folge:** Die Schnittstelle bleibt geöffnet. Die nächste Batterie kann erst gemessen werden, wenn der Prozess beendet ist. Der Fehler der ersten Batterie wird zum Fehler der zweiten.

---

## Schritt 3 · Der Context Manager als Klasse

```python
class MeterError(Exception):
    """Basis für Fehler beim Zugriff auf das Messgerät."""


class MeterNotOpen(MeterError):
    """Eine Messung wurde ohne geöffnete Verbindung angefordert."""


class Multimeter:
    """Verbindung zu einem Multimeter an einer seriellen Schnittstelle.

    Die Verbindung ist nur innerhalb eines with-Blocks geöffnet.
    """

    def __init__(self, port: str) -> None:
        self.port = port
        self._handle: str | None = None

    def __enter__(self) -> "Multimeter":
        print(f"open {self.port}")
        self._handle = f"handle:{self.port}"
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        print(f"close {self._handle}")
        self._handle = None
        return False

    def measure_voltage(self) -> float:
        if self._handle is None:
            raise MeterNotOpen(f"{self.port} is not open")
        print(f"measure via {self._handle}")
        return 11.98
```

Verwendung:

```python
with Multimeter("/dev/ttyUSB0") as meter:
    check_battery(meter.measure_voltage())
```

**Was sich geändert hat:**

- Öffnen und Schließen sind an den `with`-Block gebunden. `__exit__` läuft auch, wenn `check_battery` eine Exception wirft.
- `__exit__` gibt `False` zurück. Die Exception aus `check_battery` wird also nicht unterdrückt, der Prüfstand meldet die defekte Batterie weiterhin.
- `measure_voltage()` außerhalb des Blocks wirft `MeterNotOpen` statt einen Wert zu liefern.
- `handle` ist ein Implementierungsdetail geworden: `_handle`.

---

## Schritt 4 · Dasselbe mit `contextlib.contextmanager`

Soll die Klasse ihre Methoden `open()` und `close()` behalten, etwa weil ein anderes Programm sie so verwendet, kann eine Funktion die Lebensdauer übernehmen:

```python
from contextlib import contextmanager


@contextmanager
def open_meter(port):
    meter = Multimeter(port)
    meter.open()
    try:
        yield meter
    finally:
        meter.close()
```

Das `try/finally` um `yield` ist notwendig. Ohne es wird der Code nach `yield` bei einer Exception im `with`-Block nicht ausgeführt, und die Schnittstelle bliebe offen.

---

## Schritt 5 · Fehler an der Grenze übersetzen

Die Treiberbibliothek meldet eine belegte Schnittstelle als `OSError`. Der Prüfstand soll zwischen „Gerät nicht verfügbar" und „Batterie defekt" unterscheiden können.

```python
class MeterUnavailable(MeterError):
    """Die Schnittstelle konnte nicht geöffnet werden."""


class Multimeter:
    # übrige Methoden wie in Schritt 3

    def __enter__(self) -> "Multimeter":
        try:
            self._handle = open_serial_port(self.port)
        except OSError as error:
            raise MeterUnavailable(f"cannot open {self.port}") from error
        return self
```

`open_serial_port` steht für die Funktion der Treiberbibliothek. Durch `from error` bleibt die ursprüngliche `OSError` als `__cause__` erhalten und erscheint im Traceback. Der Aufrufer kann auf `MeterUnavailable` reagieren, die Diagnose sieht die technische Ursache.

Scheitert `__enter__`, wird `__exit__` nicht aufgerufen. Hier ist das unkritisch, weil vor dem Fehler nichts geöffnet wurde.

---

## Was dieses Beispiel zeigt

**Die Lebensdauer gehört zum Objekt, nicht zum Aufrufer.** Mit dem Context Manager muss kein Skript mehr wissen, dass am Ende `close()` kommt.

**Unzulässige Zustände sollten laut scheitern.** Eine Messung ohne Verbindung liefert besser eine Exception als einen Wert.

**Übersetzen heißt nicht verschweigen.** `raise … from error` gibt dem Aufrufer eine verständliche Exception und behält die technische Ursache.

**Nicht jede Klasse braucht `__enter__` und `__exit__`.** Das Messergebnis selbst, eine Zahl mit Einheit, hat keine Lebensdauer. Nur die Verbindung hat eine.
