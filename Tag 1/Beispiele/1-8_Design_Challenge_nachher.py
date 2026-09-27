"""1-8 · nachher · Design Challenge: ein möglicher Entwurf

Einer von mehreren tragfähigen Entwürfen. Jede Änderung ist einem Change Request
zugeordnet (CR-Nummern aus der vorher-Datei). Bewusst nicht eingeführt: eigene
Protocols für Target und Simulation, eine Klassenhierarchie für Testkonfigurationen.
Beides löst hier keinen der fünf Change Requests.
"""
import json
from contextlib import ExitStack, contextmanager
from dataclasses import dataclass, field
from typing import Iterable, List, Mapping, Optional

calls = []


class NumValueDTO:                                        # CR3: Bereich an einer Stelle
    def __init__(self, value: Optional[float], unit: str, min: float, max: float) -> None:
        self.unit, self.min, self.max = unit, min, max
        self.value = value

    @property
    def value(self) -> Optional[float]:
        return self._value

    @value.setter
    def value(self, value: Optional[float]) -> None:
        if value is not None and not self.min <= value <= self.max:
            raise ValueError(f"{value} {self.unit} outside {self.min}..{self.max}")
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


@dataclass
class TractorDTO:                                         # eigener Vorgabewert je Instanz
    name: str = "Tractor"
    turn_radius: NumValueDTO = field(default_factory=lambda: NumValueDTO(0, "m", 0, 100))
    wheelbase: NumValueDTO = field(default_factory=lambda: NumValueDTO(0, "m", 0, 10))


def read_tractor(record: Mapping[str, str]) -> TractorDTO:   # CR2: ohne Squish prüfbar
    tractor = TractorDTO(name=record.get("name") or "Tractor")
    for column, dto in (("tr_turn_radius", tractor.turn_radius), ("tr_wheelbase", tractor.wheelbase)):
        text = record.get(column, "").strip()
        if text:
            try:
                dto.input_value = text
            except ValueError as error:
                raise ValueError(f"{tractor.name}: {column}: {error}") from error
    return tractor


def records_from_json(text: str) -> List[Mapping[str, str]]:  # CR1: zweite Quelle
    return json.loads(text)


@dataclass
class SectionControlConfig:                               # CR5: Datensatz frei wählbar
    test_sets: List[TractorDTO]
    data_set: str = "with_sc_boundary"


@contextmanager
def test_wrapper(target, simulation, config: SectionControlConfig):   # CR4
    failed = False

    def save_evidence_if_failed():
        if failed:
            target.backup_data_set("_backup_after_fail")

    with ExitStack() as cleanup:
        cleanup.callback(simulation.stop)
        cleanup.callback(target.cleanup)
        cleanup.callback(save_evidence_if_failed)
        target.replace_data_set(config.data_set)
        try:
            yield
        except Exception as e:
            failed = True
            calls.append(f"FAIL {e}")


# --- Prüfung ohne Squish -------------------------------------------------------
tsv_rows = [{"name": "narrow", "tr_turn_radius": "6.5", "tr_wheelbase": "2.8"},
            {"name": "wide", "tr_turn_radius": "12", "tr_wheelbase": ""}]
tractors = [read_tractor(r) for r in tsv_rows]
assert [t.turn_radius.value for t in tractors] == [6.5, 12.0]
assert tractors[1].wheelbase.value == 0

json_rows = records_from_json('[{"name": "ci", "tr_turn_radius": "8"}]')
assert read_tractor(json_rows[0]).turn_radius.input_value == "8"

try:
    read_tractor({"name": "huge", "tr_turn_radius": "150"})
except ValueError as error:
    calls.append(f"abgewiesen: {error}")


# --- Zusammensetzen, im Kurs mit echten Squish-Objekten -----------------------
class Target:
    def replace_data_set(self, name): calls.append(f"replace {name}")
    def backup_data_set(self, name): calls.append("backup"); raise PermissionError("backup dir")
    def cleanup(self): calls.append("target cleanup")


class Simulation:
    def stop(self): calls.append("stop simulation")


config = SectionControlConfig(tractors, data_set="sc_set_3")
try:
    with test_wrapper(Target(), Simulation(), config):
        raise AssertionError("area differs by 3.1 qm")
except PermissionError as error:
    calls.append(f"propagiert: {error!r}")

print("\n".join(calls))
assert "stop simulation" in calls and "target cleanup" in calls
