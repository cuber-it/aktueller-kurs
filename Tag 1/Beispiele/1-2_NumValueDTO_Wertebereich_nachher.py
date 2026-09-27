"""1-2 · nachher · NumValueDTO: die Klasse schützt ihren Wertebereich

Eine mögliche Richtung. Die Regel „der Wert liegt zwischen min und max“ steht
an genau einer Stelle, im Setter von ``value``. Auch ``input_value`` und der
Konstruktor laufen durch ihn.

Hier ist eine normale Klasse sinnvoller als ``@dataclass``: Eine Property
namens ``value`` und ein gleichnamiges Datenklassenfeld vertragen sich nicht.

Offen für die Diskussion: Gibt es Tests, die bewusst einen ungültigen Wert
eingeben wollen, etwa um die Fehlermeldung des Terminals zu prüfen? Dann
braucht es dafür einen ausdrücklichen Weg, statt die Prüfung zu umgehen.
"""
from enum import Enum
from typing import Optional


class Metric_Units(str, Enum):
    unit_m = "m"


class NumValueDTO:
    """Zahlenwert eines Eingabefelds im Terminal, mit Einheit und Grenzen."""

    def __init__(self, value: Optional[float], precision: float,
                 unit: Optional[Metric_Units], min: float, max: float) -> None:
        self.precision = precision
        self.unit = unit
        self.min = min
        self.max = max
        self.value = value          # läuft durch den Setter

    @property
    def value(self) -> Optional[float]:
        return self._value

    @value.setter
    def value(self, value: Optional[float]) -> None:
        """Setzt den Wert.

        Raises:
            ValueError: wenn der Wert außerhalb von ``min`` bis ``max`` liegt.
        """
        if value is not None and not self.min <= value <= self.max:
            raise ValueError(f"{value} liegt außerhalb von {self.min} bis {self.max}")
        self._value = value

    @property
    def input_value(self) -> Optional[str]:
        if self._value is None:
            return None
        text = str(float(self._value))
        return text[:-2] if text.endswith(".0") else text

    @input_value.setter
    def input_value(self, text: Optional[str]) -> None:
        self.value = float(text) if text is not None else None

    def __repr__(self) -> str:
        return (f"NumValueDTO(value={self._value!r}, precision={self.precision!r}, "
                f"unit={self.unit!r}, min={self.min!r}, max={self.max!r})")


turn_radius = NumValueDTO(0, 0.1, Metric_Units.unit_m, 0, 100)
turn_radius.input_value = "6.5"
assert turn_radius.value == 6.5

for bad in ("150", "-3"):
    try:
        turn_radius.input_value = bad
    except ValueError as error:
        print("abgewiesen:", error)
assert turn_radius.value == 6.5           # der alte, gültige Wert bleibt

# Die Aufrufstellen aus 1-1 (nachher) ändern sich nicht: Der Zugriff bleibt ein Attributzugriff.
print(repr(turn_radius))
print("nachher: alle Beobachtungen bestätigt")
