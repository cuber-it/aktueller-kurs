# Beispiel · Abhängigkeiten sichtbar machen – in klein

Dieselbe Aufgabe an einem kleineren Gegenstand, vollständig durchgeführt.

---

## Der Gegenstand

Eine private Wetterstation. Sie soll morgens vor 9 Uhr eine SMS schicken, wenn die Temperatur bei oder unter 0 °C liegt.

```python
from datetime import datetime

SETTINGS = {
    "sensor_port": "/dev/ttyUSB0",
    "sms_url": "https://sms.test.internal",
    "phone": "PHONE-TEST",
}


class FrostWarning:
    def check(self):
        sensor = Sensor(SETTINGS["sensor_port"])
        temperature = sensor.read_celsius()
        if temperature <= 0.0 and datetime.now().hour < 9:
            SmsGateway.instance().send(SETTINGS["phone"], f"Frost: {temperature} °C")
            return True
        return False
```

Die Regel ist klein. Prüfen lässt sie sich trotzdem nur mit angeschlossenem Sensor, erreichbarem SMS-Dienst und zur richtigen Uhrzeit.

---

## Schritt 1 · Wovon hängt `check` ab?

| Abhängigkeit | Wie beschafft | an der Signatur erkennbar |
|---|---|---|
| Sensor | in `check` erzeugt | nein |
| Port des Sensors | globales `SETTINGS` | nein |
| SMS-Dienst | Singleton `SmsGateway.instance()` | nein |
| Telefonnummer | globales `SETTINGS` | nein |
| Uhrzeit | `datetime.now()` | nein |
| Frostgrenze 0 °C | Literal im Code | nein, muss es auch nicht |

**Sechs Abhängigkeiten, keine davon sichtbar.** `FrostWarning()` hat einen Konstruktor ohne Parameter.

---

## Schritt 2 · Für jede Abhängigkeit entscheiden

| Abhängigkeit | Entscheidung | Begründung |
|---|---|---|
| Sensor | Konstruktor | dauerhaft gebraucht, externe Hardware |
| SMS-Dienst | Konstruktor | dauerhaft gebraucht, Seiteneffekt nach außen |
| Port des Sensors | entfällt | gehört zum Sensor, nicht zur Warnung |
| Telefonnummer | Konstruktor, als Wert | Konfiguration, kein Dienst |
| Uhrzeit | Default-Parameter `now=datetime.now` | der Standard ist harmlos, nur Tests brauchen einen anderen Wert |
| Frostgrenze | bleibt konkret, als Konstante | eine fachliche Festlegung ohne bekannte Variante |

Die Frostgrenze bleibt im Code. Sollte sie einmal je Standort verschieden sein, wird sie zum Parameter. Heute kann niemand eine zweite Grenze nennen.

---

## Schritt 3 · Der Umbau

```python
from collections.abc import Callable
from datetime import datetime

FROST_LIMIT = 0.0


class FrostWarning:
    """Warnt morgens vor 9 Uhr per SMS, wenn die Temperatur bei oder unter 0 °C liegt."""

    def __init__(
        self,
        sensor,
        gateway,
        phone: str,
        now: Callable[[], datetime] = datetime.now,
    ) -> None:
        self._sensor = sensor
        self._gateway = gateway
        self._phone = phone
        self._now = now

    def check(self) -> bool:
        temperature = self._sensor.read_celsius()
        if temperature <= FROST_LIMIT and self._now().hour < 9:
            self._gateway.send(self._phone, f"Frost: {temperature} °C")
            return True
        return False
```

`now=datetime.now` übergibt die Funktion selbst, nicht ihr Ergebnis. Aufgerufen wird sie erst in `check`. Hier zeigt sich, dass Funktionen in Python Objekte sind (Einheit 1-1).

---

## Schritt 4 · Zusammensetzen an einer Stelle

```python
def build_frost_warning(settings: dict) -> FrostWarning:
    return FrostWarning(
        sensor=Sensor(settings["sensor_port"]),
        gateway=SmsGateway(settings["sms_url"]),
        phone=settings["phone"],
    )
```

Nur hier steht, welche konkreten Objekte die Station verwendet. `FrostWarning` kennt weder `SETTINGS` noch das Singleton.

---

## Schritt 5 · Die Tests

```python
from datetime import datetime


class FixedSensor:
    """Stub: liefert immer denselben Messwert."""

    def __init__(self, celsius: float) -> None:
        self._celsius = celsius

    def read_celsius(self) -> float:
        return self._celsius


class RecordingGateway:
    """Spy: merkt sich jede gesendete Nachricht."""

    def __init__(self) -> None:
        self.sent: list[tuple[str, str]] = []

    def send(self, phone: str, text: str) -> None:
        self.sent.append((phone, text))


def at(hour):
    return lambda: datetime(2026, 1, 15, hour, 0)


def test_warns_at_zero_degrees_in_the_morning():
    gateway = RecordingGateway()
    warning = FrostWarning(FixedSensor(0.0), gateway, "PHONE-TEST", now=at(6))
    assert warning.check() is True
    assert gateway.sent == [("PHONE-TEST", "Frost: 0.0 °C")]


def test_no_warning_above_zero():
    gateway = RecordingGateway()
    warning = FrostWarning(FixedSensor(0.1), gateway, "PHONE-TEST", now=at(6))
    assert warning.check() is False
    assert gateway.sent == []


def test_no_warning_after_nine():
    gateway = RecordingGateway()
    warning = FrostWarning(FixedSensor(-3.0), gateway, "PHONE-TEST", now=at(9))
    assert warning.check() is False
    assert gateway.sent == []
```

Drei Tests, beide Grenzen der Regel abgedeckt: genau 0 °C und genau 9 Uhr. Kein Sensor, kein SMS-Dienst, kein `mock.patch`.

---

## Was dieses Beispiel zeigt

**Die Abhängigkeiten stehen jetzt im Konstruktor.** Wer `FrostWarning` verwenden will, sieht an der Signatur, was gebraucht wird.

**Nicht alles wird injiziert.** Die Frostgrenze bleibt eine Konstante, der Port wandert zum Sensor. Übergeben wird, was sich unabhängig ändert oder im Test ersetzt werden muss.

**Ein Wert ist oft besser als ein Dienst.** Die Warnung braucht die Telefonnummer, nicht das ganze `SETTINGS`.

**Test Doubles entstehen fast von selbst.** `FixedSensor` und `RecordingGateway` sind wenige Zeilen lang und brauchen keine Bibliothek.

---

## Zum Vergleich: zu viel des Guten

```python
class FrostWarning:
    def __init__(self, sensor, gateway, phone, clock, limit_provider, comparator):
        ...

    def check(self):
        temperature = self._sensor.read_celsius()
        if self._comparator.at_or_below(temperature, self._limit_provider.limit()):
            ...
```

`limit_provider` und `comparator` lassen sich mit keiner Änderung und keinem Test begründen. Sie machen die Regel `temperature <= 0.0` schwerer lesbar, ohne etwas austauschbar zu machen, das ausgetauscht werden müsste.
