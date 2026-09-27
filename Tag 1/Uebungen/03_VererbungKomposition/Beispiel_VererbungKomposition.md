# Beispiel · Ist-ein oder braucht-ein – in klein

Dieselbe Aufgabe an einem kleineren Gegenstand, vollständig durchgeführt.

---

## Der Gegenstand

Eine Heizungssteuerung für ein Mehrfamilienhaus. Es gibt eine Basisklasse für alles, was die Steuerung regelt.

```python
class Controller:
    """Basis aller Regelkreise der Heizungssteuerung."""

    def __init__(self, name):
        self.name = name

    def read_temperature(self, sensor):
        print(f"read sensor {sensor}")
        return 21.0

    def open_valve(self, valve, percent):
        print(f"valve {valve} -> {percent} %")

    def show_on_display(self, text):
        print(f"display: {text}")

    def log(self, message):
        print(f"[{self.name}] {message}")


class FloorHeatingZone(Controller):
    def regulate(self, target):
        current = self.read_temperature("floor")
        self.open_valve("floor", 80 if current < target else 0)
        self.log(f"{current} -> {target}")


class SolarYieldCounter(Controller):
    def record(self, kilowatt_hours):
        self.show_on_display(f"solar yield {kilowatt_hours} kWh")
        self.log(f"yield {kilowatt_hours}")
```

Neue Anforderung: **Jede Ventilbewegung soll für die Wartungsfirma protokolliert werden.** Die Regelkreise sollen dafür nicht geändert werden.

---

## Schritt 1 · Ist-ein oder braucht-ein?

| Klasse | Nutzt von `Controller` | Spezialisierung? |
|---|---|---|
| `FloorHeatingZone` | Temperatur lesen, Ventil stellen, protokollieren | ja: ein Regelkreis, der einen Sollwert hält |
| `SolarYieldCounter` | Anzeige, protokollieren | nein: zählt Erträge, regelt nichts |

`SolarYieldCounter` kann Ventile öffnen, obwohl er nie eines öffnen darf. Das ist der Hinweis: Er ist kein Regelkreis, er braucht zwei Werkzeuge eines Regelkreises.

---

## Schritt 2 · Komposition für den Ertragszähler

```python
class Display:
    def show(self, text):
        print(f"display: {text}")


class Logbook:
    def __init__(self, source):
        self._source = source

    def write(self, message):
        print(f"[{self._source}] {message}")


class SolarYieldCounter:
    """Zeigt den Solarertrag an und protokolliert ihn."""

    def __init__(self, display, logbook):
        self._display = display
        self._logbook = logbook

    def record(self, kilowatt_hours):
        self._display.show(f"solar yield {kilowatt_hours} kWh")
        self._logbook.write(f"yield {kilowatt_hours}")


counter = SolarYieldCounter(Display(), Logbook("solar"))
counter.record(12.5)
```

Am Konstruktor steht jetzt, was der Zähler braucht. Ventile gehören nicht dazu.

---

## Schritt 3 · Delegation für das Ventilprotokoll

Die Ventile werden über ein eigenes Objekt gestellt. Für das Protokoll kommt ein zweites Objekt davor, das dieselbe Methode anbietet.

```python
class Valves:
    def open(self, valve, percent):
        print(f"valve {valve} -> {percent} %")


class RecordingValves:
    """Protokolliert jede Ventilbewegung und reicht sie weiter."""

    def __init__(self, valves, logbook):
        self._valves = valves
        self._logbook = logbook

    def open(self, valve, percent):
        self._logbook.write(f"valve {valve} set to {percent} %")
        self._valves.open(valve, percent)
```

Wer bisher `Valves()` erhielt, erhält jetzt `RecordingValves(Valves(), Logbook("maintenance"))`. Der Regelkreis ruft weiter `open(...)` auf und merkt keinen Unterschied.

---

## Schritt 4 · Wo die Vererbung bleibt

`FloorHeatingZone` ist ein Regelkreis. Gäbe es weitere, etwa `RadiatorZone` oder `HotWaterTank`, hätten alle denselben Vertrag: `regulate(target)`. Die Steuerung ruft ihn für jede Zone auf, ohne zu wissen, welche es ist.

```python
class Zone:
    """Ein Regelkreis, der einen Sollwert hält."""

    def regulate(self, target):
        raise NotImplementedError


def regulate_all(zones, target):
    for zone in zones:
        zone.regulate(target)
```

Hier trägt die Vererbung: Jede Zone kann überall stehen, wo eine Zone erwartet wird. Ob die Zonen ihre Werkzeuge erben oder übergeben bekommen, ist eine zweite, unabhängige Frage.

`NotImplementedError` in der Basisklasse ist hier etwas anderes als in einer Unterklasse: Die Basisklasse sagt „jede Zone muss das können", eine Unterklasse, die es wirft, sagt „ich kann es nicht".

---

## Was dieses Beispiel zeigt

**Die Frage ist nicht, ob Code wiederverwendet wird, sondern welche Beziehung besteht.** `SolarYieldCounter` hat Code aus `Controller` genutzt, ohne ein Controller zu sein.

**Komposition macht den Bedarf sichtbar.** Am Konstruktor steht, womit ein Objekt zusammenarbeitet. Bei der Vererbung steht dort nur der Name der Basisklasse.

**Delegation ergänzt Verhalten, ohne Klassen zu ändern.** Das Ventilprotokoll kam ohne Eingriff in `Valves` oder die Regelkreise dazu.

**Vererbung bleibt, wo eine Typfamilie besteht.** Die Zonen teilen einen Vertrag, den ein Aufrufer benutzt, ohne die einzelne Zone zu kennen.
