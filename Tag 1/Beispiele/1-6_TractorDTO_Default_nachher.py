"""1-6 · nachher · Jede Instanz erzeugt ihren eigenen Vorgabewert

``field(default_factory=...)`` ruft die Fabrik bei jeder Konstruktion auf.
Das funktioniert unter Python 3.10 und 3.12 gleich.
"""
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class NumValueDTO:
    value: Optional[float]
    precision: float
    unit: Optional[str]
    min: float
    max: float

    def set_input_value(self, value: str):
        self.value = float(value) if value is not None else None


@dataclass
class TractorDTO:
    name: Optional[str] = "Tractor"
    turn_radius: NumValueDTO = field(default_factory=lambda: NumValueDTO(0, 0.1, "m", 0, 100))


small = TractorDTO(name="small tractor")
large = TractorDTO(name="large tractor")

small.turn_radius.set_input_value("4.5")
assert large.turn_radius.value == 0
assert small.turn_radius is not large.turn_radius

print("nachher: alle Beobachtungen bestätigt")
