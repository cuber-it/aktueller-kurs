"""1-3 · vorher · Testkonfigurationen als Vererbungshierarchie

Quelle: test_parameters/abstract_test_config.py (Testframework des Teams, stark gekürzt:
nur Felder und Verknüpfungen, keine Lese-Logik).
Abweichung: pydantic.dataclasses durch dataclasses ersetzt.

Jede neue Fähigkeit eines Tests (GPS, Testdaten, Maschinen, Section Control)
wird eine weitere Ebene. Eine zweite, parallele Hierarchie für Testsätze hängt
über ``_provide_test_set`` an der ersten.
"""
from abc import ABC
from dataclasses import dataclass, fields


@dataclass(frozen=True)
class GPSPosition:
    lat: float
    lon: float


# Parallele Hierarchie der Testsätze (abstract_test_set.py)
class AbstractTestSetDTO: ...
class AbstractTestSetWithMachinesDTO(AbstractTestSetDTO): ...
class TestSetWithSectionControlDTO(AbstractTestSetWithMachinesDTO): ...
class TestSetWithSectionControlBoundaryDTO(TestSetWithSectionControlDTO): ...


@dataclass
class AbstractTest(ABC):
    data_set: str = "clear"

    def __post_init__(self):
        pass


@dataclass
class AbstractTestWithGPS(AbstractTest):
    start_position: GPSPosition = GPSPosition(50, 12)


@dataclass
class AbstractDataDrivenTest(AbstractTest):
    test_data_file_name: str = "data.tsv"

    def _provide_test_set(self):
        return AbstractTestSetDTO()


@dataclass
class AbstractDataDrivenTestWithMachines(AbstractDataDrivenTest):
    def _provide_test_set(self):
        return AbstractTestSetWithMachinesDTO()


@dataclass
class AbstractSectionControlTest(AbstractDataDrivenTestWithMachines, AbstractTestWithGPS):
    terminal_processing_time_sec: float = 0.0
    area_error_tolerance_qm: float = 0.0

    def __post_init__(self):
        self.data_set = "with_sc_boundary"
        super().__post_init__()

    def _provide_test_set(self):
        return TestSetWithSectionControlDTO()


@dataclass
class AbstractSectionControlTestBoundary(AbstractSectionControlTest):
    def _provide_test_set(self):
        return TestSetWithSectionControlBoundaryDTO()


# Die MRO umfasst acht Klassen, sechs davon liegen zwischen dem Test und object:
print([c.__name__ for c in AbstractSectionControlTestBoundary.__mro__])

# Die Reihenfolge der Konstruktorparameter ergibt sich aus der MRO, nicht aus dem Code:
print([f.name for f in fields(AbstractSectionControlTestBoundary)])

# Der Konstruktor nimmt data_set an und verwirft es in __post_init__:
config = AbstractSectionControlTestBoundary(data_set="sc_set_3")
assert config.data_set == "with_sc_boundary"

# Eine Frage an die Hierarchie: Ist ein Section-Control-Test „ein GPS-Test“ und
# „ein datengetriebener Test mit Maschinen“, oder benutzt er GPS, Testdaten und Maschinen?
print("vorher: alle Beobachtungen bestätigt")
