"""1-8 · vorher · Design Challenge: Section-Control-Test, gewachsener Stand

Zusammengesetzt aus Mustern des Testframeworks (abstract_test_config.py,
machines_dtos.py, test_wrapper.py), stark gekürzt. Squish, testData, Target und
Simulation sind Platzhalter. Der Code läuft unter Python 3.10 (wie Squish 9.2).
Erst analysieren, dann ändern.
"""
from contextlib import contextmanager
from dataclasses import dataclass
from typing import Optional

calls = []
ROWS = [{"name": "narrow", "tr_turn_radius": "6.5", "tr_wheelbase": "2.8"},   # Platzhalter für
        {"name": "wide", "tr_turn_radius": "150", "tr_wheelbase": ""}]         # testData.dataset()

test_config = None


def get_test_config():
    return test_config


@dataclass
class NumValueDTO:
    value: Optional[float]
    unit: str
    min: float
    max: float
    input_value: Optional[str] = None

    def set_input_value(self, value):
        self.input_value = value
        self.value = float(value) if value is not None else None

    def get_input_value(self):
        return self.input_value


@dataclass
class TractorDTO:
    name: str = "Tractor"
    turn_radius: NumValueDTO = NumValueDTO(0, "m", 0, 100)
    wheelbase: NumValueDTO = NumValueDTO(0, "m", 0, 10)


@dataclass
class AbstractSectionControlTest:
    data_set: str = "clear"

    def __post_init__(self):
        global test_config
        test_config = self
        self.data_set = "with_sc_boundary"
        self.test_sets = [self.read_test_set(r) for r in ROWS]

    def read_test_set(self, record):
        tractor = TractorDTO(name=self.get_data_value(record, "name", "Tractor"))
        tractor.turn_radius.set_input_value(
            self.get_data_value(record, "tr_turn_radius", tractor.turn_radius.get_input_value()))
        tractor.wheelbase.set_input_value(
            self.get_data_value(record, "tr_wheelbase", tractor.wheelbase.get_input_value()))
        return tractor

    @staticmethod
    def get_data_value(record, column, def_val, is_bool=False, cast_type=None):
        value = record.get(column, "").strip()
        if not value:
            return def_val
        if is_bool:
            return value in ("true", "t", "v")
        return cast_type(value) if cast_type else value


class Target:
    def replace_data_set(self, name): calls.append(f"replace {name}")
    def backup_data_set(self, name): calls.append("backup"); raise PermissionError("backup dir")
    def cleanup(self): calls.append("target cleanup")


target = Target()


@contextmanager
def test_wrapper():
    failed = False
    try:
        target.replace_data_set(get_test_config().data_set)
        yield
    except Exception as e:
        failed = True
        calls.append(f"FAIL {e}")
    finally:
        if failed:
            target.backup_data_set("_backup_after_fail")
        target.cleanup()
        calls.append("stop simulation")


def main():
    config = AbstractSectionControlTest(data_set="sc_set_3")
    with test_wrapper():
        for tractor in config.test_sets:
            calls.append(f"drive {tractor.name} r={tractor.turn_radius.value}")
            assert tractor.turn_radius.value <= 100, "turn radius out of range"


if __name__ == "__main__":
    try:
        main()
    except PermissionError as error:
        calls.append(f"propagiert: {error!r}")
    print("\n".join(calls))

# Change Requests
#  CR1  Testsätze kommen zusätzlich aus einer JSON-Datei der CI.
#  CR2  Einlesen und Aufbereiten der Testsätze soll ohne Squish und Target prüfbar sein.
#  CR3  Ein Wenderadius außerhalb des erlaubten Bereichs soll beim Einlesen auffallen.
#  CR4  Die Simulation wird auch gestoppt, wenn das Sichern nach einem Fehler scheitert.
#  CR5  Ein Test soll mit einem anderen Datensatz als "with_sc_boundary" laufen können.
