"""1-1 · vorher · NumValueDTO: zwei Darstellungen, Getter und Setter

Quelle: machines_helper/machines_dtos.py (Testframework des Teams, gekürzt auf die Zugriffsmethoden).
Abweichung: pydantic.dataclasses ist durch dataclasses ersetzt. Die Datei läuft
so ohne Zusatzpakete unter Python 3.10. pydantic prüft Zuweisungen an Attribute
standardmäßig nicht, das gezeigte Verhalten ist daher dasselbe.
"""
from dataclasses import dataclass
from enum import Enum
from typing import Optional


class Metric_Units(str, Enum):
    unit_cm = "cm"
    unit_m = "m"


@dataclass
class NumValueDTO:
    value: Optional[float]
    precision: float
    unit: Optional[Metric_Units]
    min: float
    max: float
    input_value: Optional[str] = None

    def __post_init__(self):
        """To be executed after the default dataclass __init__ has been executed."""
        if self.input_value is not None:
            self.value = float(self.input_value)

    def set_value(self, value):
        self.value = value
        self.input_value = str(value)

    def set_input_value(self, value: str):
        self.input_value = value
        self.value = float(value) if value is not None else None

    def get_input_value(self):
        return self.input_value if self.input_value else None if self.value is None else str(self.value).rstrip('0').rstrip(
            '.') if self.value != 0 else "0"


# Verwendung wie in abstract_test_config.read_tractor_settings():
turn_radius = NumValueDTO(0, 0.1, Metric_Units.unit_m, 0, 100)
turn_radius.set_input_value("6.5")
print(turn_radius.get_input_value(), turn_radius.value)

# Drei Wege, den Wert zu ändern. Sie führen zu unterschiedlichen Textdarstellungen:
turn_radius.set_value(7.0)
assert turn_radius.get_input_value() == "7.0"

turn_radius.set_input_value("7")
assert turn_radius.get_input_value() == "7"

turn_radius.value = 9.0                       # öffentliches Attribut, kein Setter
assert turn_radius.get_input_value() == "7"   # Textdarstellung ist veraltet
assert turn_radius.value == 9.0

# Ohne gespeicherten Text wird er abgeleitet – mit einer Überraschung bei ganzen Zahlen:
length = NumValueDTO(0, 0.1, Metric_Units.unit_m, 0, 1000)
length.value = 100
assert length.get_input_value() == "1"        # "100".rstrip("0") ergibt "1"

print("vorher: alle Beobachtungen bestätigt")
