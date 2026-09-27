"""1-6 · vorher · TractorDTO: ein veränderliches Objekt als Vorgabewert

Quelle: machines_helper/machines_dtos.py (Testframework des Teams, gekürzt auf ein Feld).
Abweichung: pydantic.dataclasses durch dataclasses ersetzt.

Der Vorgabewert ``NumValueDTO(...)`` wird einmal erzeugt, beim Laden der Klasse.
Alle ``TractorDTO``-Instanzen teilen sich dieses eine Objekt.

Unter Python 3.10 läuft das ohne Meldung. Ab Python 3.11 lehnt ``dataclasses``
nicht hashbare Vorgabewerte ab. Das Originalmodul lässt sich dann nicht mehr
importieren (geprüft mit Python 3.12 und pydantic 2.12):
``ValueError: mutable default <class 'NumValueDTO'> for field turn_radius is not allowed``
"""
import sys
from dataclasses import dataclass
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


try:
    @dataclass
    class TractorDTO:
        name: Optional[str] = "Tractor"
        turn_radius: Optional[NumValueDTO] = NumValueDTO(0, 0.1, "m", 0, 100)
except ValueError as error:
    print(f"Python {sys.version_info.major}.{sys.version_info.minor}: {error}")
    raise SystemExit(0)


small = TractorDTO(name="small tractor")
large = TractorDTO(name="large tractor")

small.turn_radius.set_input_value("4.5")
assert large.turn_radius.value == 4.5          # der große Traktor hat jetzt denselben Wenderadius
assert small.turn_radius is large.turn_radius

print("vorher: alle Beobachtungen bestätigt")
