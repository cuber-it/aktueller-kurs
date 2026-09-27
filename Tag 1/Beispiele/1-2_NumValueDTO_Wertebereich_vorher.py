"""1-2 · vorher · NumValueDTO: Grenzen, die niemand prüft

Quelle: machines_helper/machines_dtos.py (Testframework des Teams, gekürzt).
Abweichung: pydantic.dataclasses durch dataclasses ersetzt (siehe 1-1).

``min`` und ``max`` beschreiben den zulässigen Bereich des Eingabefelds.
Keine Methode der Klasse verwendet sie.
"""
from dataclasses import dataclass
from enum import Enum
from typing import Optional


class Metric_Units(str, Enum):
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
        if self.input_value is not None:
            self.value = float(self.input_value)

    def set_value(self, value):
        self.value = value
        self.input_value = str(value)

    def set_input_value(self, value: str):
        self.input_value = value
        self.value = float(value) if value is not None else None


# Ein Wenderadius von 150 m bei erlaubten 0 bis 100 m wird ohne Einwand übernommen:
turn_radius = NumValueDTO(0, 0.1, Metric_Units.unit_m, 0, 100, input_value="150")
assert turn_radius.value == 150.0

turn_radius.set_value(-3)
assert turn_radius.value == -3

# Wer prüfen will, muss die Regel an der Aufrufstelle selbst kennen:
if not turn_radius.min <= turn_radius.value <= turn_radius.max:
    print(f"ungültig: {turn_radius.value}, erlaubt {turn_radius.min} bis {turn_radius.max}")

print("vorher: alle Beobachtungen bestätigt")
