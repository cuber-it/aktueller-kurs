"""1-1 · nachher · NumValueDTO: nur die Protokolle, die das Objekt tatsächlich erfüllt

Eine mögliche Richtung. ``NumValueDTO`` beschreibt ein Eingabefeld mit Wert,
Einheit und Grenzen. Es ist kein Zahlentyp. Wer rechnen will, rechnet mit
``float(dto)`` und schreibt das Ergebnis zurück. Dafür bleiben:

- ``__float__``: das Objekt lässt sich in eine Zahl umwandeln,
- ``__str__``: Text für Protokolle, mit Einheit, unabhängig von der Python-Version,
- ``__eq__`` und ``__repr__`` aus ``@dataclass``: Vergleich aller Felder, lesbare Ausgabe.

Veränderliche Objekte mit ``__eq__`` sind in Python nicht hashbar. Das ist hier gewollt.
"""
from dataclasses import dataclass
from enum import Enum
from typing import Optional


class Metric_Units(str, Enum):
    unit_m = "m"
    unit_degree = "degrees"


@dataclass
class NumValueDTO:
    value: Optional[float]
    precision: float
    unit: Optional[Metric_Units]
    min: float
    max: float

    @property
    def input_value(self) -> Optional[str]:
        if self.value is None:
            return None
        text = str(float(self.value))
        return text[:-2] if text.endswith(".0") else text

    def __float__(self) -> float:
        if self.value is None:
            raise ValueError("NumValueDTO has no value")
        return float(self.value)

    def __str__(self) -> str:
        if self.unit is None:
            return f"{self.input_value}"
        if self.unit is Metric_Units.unit_degree:
            return f"{self.input_value}°"
        return f"{self.input_value} {self.unit.value}"


width = NumValueDTO(2.5, 0.1, Metric_Units.unit_m, 0, 100)

# Rechnen ist sichtbar eine Umwandlung in float:
width.value = float(width) + 1
assert width.value == 3.5

assert str(width) == "3.5 m"
assert str(NumValueDTO(3, 1, None, 0, 10)) == "3"
assert str(NumValueDTO(45, 1, Metric_Units.unit_degree, 0, 90)) == "45°"

# Vergleich über alle Felder, nicht mit nackten Zahlen:
assert width == NumValueDTO(3.5, 0.1, Metric_Units.unit_m, 0, 100)
assert width.value == 3.5

print(repr(width))
print("nachher: alle Beobachtungen bestätigt")
