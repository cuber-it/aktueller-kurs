"""1-1 · vorher · NumValueDTO: Magic Methods für Rechnen, Vergleichen und Text

Quelle: machines_helper/machines_dtos.py (Testframework des Teams, gekürzt).
Abweichung: pydantic.dataclasses durch dataclasses ersetzt (siehe 1-1 Getter_Setter).
"""
import operator
import sys
from dataclasses import dataclass
from enum import Enum
from typing import Optional


class Metric_Units(str, Enum):
    unit_m = "m"
    unit_degree = "degrees"  # we don't want to deal with the symbol °


@dataclass
class NumValueDTO:
    value: Optional[float]
    precision: float
    unit: Optional[Metric_Units]
    min: float
    max: float
    input_value: Optional[str] = None

    def get_input_value(self):
        return self.input_value if self.input_value else None if self.value is None else str(self.value).rstrip('0').rstrip(
            '.') if self.value != 0 else "0"

    def _coerce(self, other):
        return other.value if isinstance(other, NumValueDTO) else float(other)

    def _binary(self, other, op):
        return op(self.value, self._coerce(other))

    def __iadd__(self, other):
        self.value += self._coerce(other)
        return self

    def __add__(self, o):
        return self._binary(o, operator.add)

    def __eq__(self, o):
        return self._binary(o, operator.eq)

    def __lt__(self, o):
        return self._binary(o, operator.lt)

    def __float__(self):
        return self.value

    def __str__(self):
        return f"{self.get_input_value()}" + (f" {self.unit}" if self.unit != Metric_Units.unit_degree else "°") if self.unit else ""


width = NumValueDTO(2.5, 0.1, Metric_Units.unit_m, 0, 100)

# + und += liefern verschiedene Typen:
assert type(width + 1) is float
width += 1
assert type(width) is NumValueDTO

# += verändert das Objekt selbst. Wer eine zweite Referenz hält, sieht die Änderung:
same = width
width += 1
assert same.value == 4.5

# __eq__ vergleicht mit Zahlen, dadurch ist das Objekt nicht hashbar:
assert width == 4.5
try:
    {width}
except TypeError as error:
    print("set:", error)

# __str__ ohne Einheit liefert einen leeren Text. Der bedingte Ausdruck bindet schwächer als "+":
count = NumValueDTO(3, 1, None, 0, 10)
assert str(count) == ""

# Einheit im f-String: Python 3.10 liefert den Wert, ab 3.11 den Namen des Enum-Mitglieds.
print(f"Python {sys.version_info.major}.{sys.version_info.minor}:", str(width))
# 3.10: "4.5 m"      3.12: "4.5 Metric_Units.unit_m"

print("vorher: alle Beobachtungen bestätigt")
