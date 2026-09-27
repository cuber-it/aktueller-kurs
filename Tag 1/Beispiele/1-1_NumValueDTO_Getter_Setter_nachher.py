"""1-1 · nachher · NumValueDTO: ein gespeicherter Wert, Text als Property

Eine mögliche Richtung. Gespeichert wird nur ``value``. Die Textdarstellung
``input_value`` wird daraus abgeleitet und beim Setzen in ``value`` umgerechnet.
Getter und Setter entfallen, der Zugriff sieht aus wie ein Attributzugriff.

Die Konstruktion mit ``input_value=...`` entfällt dabei. Wer von Text ausgeht,
setzt nach der Konstruktion ``dto.input_value = "..."``.
"""
from dataclasses import dataclass
from enum import Enum
from typing import Optional


class Metric_Units(str, Enum):
    unit_cm = "cm"
    unit_m = "m"


@dataclass
class NumValueDTO:
    """Zahlenwert eines Eingabefelds im Terminal, mit Einheit und Grenzen."""

    value: Optional[float]
    precision: float
    unit: Optional[Metric_Units]
    min: float
    max: float

    @property
    def input_value(self) -> Optional[str]:
        """Der Wert so, wie er in das Eingabefeld getippt wird: ohne ``.0`` am Ende."""
        if self.value is None:
            return None
        text = str(float(self.value))
        return text[:-2] if text.endswith(".0") else text

    @input_value.setter
    def input_value(self, text: Optional[str]) -> None:
        self.value = float(text) if text is not None else None


turn_radius = NumValueDTO(0, 0.1, Metric_Units.unit_m, 0, 100)
turn_radius.input_value = "6.5"
print(turn_radius.input_value, turn_radius.value)

# Jeder Weg führt zu derselben Darstellung, weil es nur eine gespeicherte Angabe gibt:
turn_radius.value = 7.0
assert turn_radius.input_value == "7"
turn_radius.input_value = "7"
assert turn_radius.input_value == "7"
turn_radius.value = 9.0
assert turn_radius.input_value == "9"

length = NumValueDTO(0, 0.1, Metric_Units.unit_m, 0, 1000)
length.value = 100
assert length.input_value == "100"

# Aufrufstelle in read_tractor_settings(), vorher:
#   tractor.turn_radius.set_input_value(
#       self.get_data_value(record, "tr_turn_radius", tractor.turn_radius.get_input_value()))
# nachher:
#   tractor.turn_radius.input_value = self.get_data_value(
#       record, "tr_turn_radius", tractor.turn_radius.input_value)

print("nachher: alle Beobachtungen bestätigt")
