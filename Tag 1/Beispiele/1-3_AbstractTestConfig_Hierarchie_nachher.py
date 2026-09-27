"""1-3 · nachher · Testkonfiguration aus Bausteinen zusammengesetzt

Eine mögliche Richtung. Ein Test besitzt Einstellungen für GPS, Testdaten oder
Section Control, statt von entsprechenden Klassen zu erben. Welche Bausteine
vorhanden sind, steht am Objekt und nicht in der Klassenhierarchie.

Die Fabrikfunktion ``section_control_config`` setzt den üblichen Datensatz als
Vorgabe, lässt ihn aber überschreiben.

Kosten dieser Richtung: Zugriffe werden länger (``config.gps.start_position``
statt ``config.start_position``), und Code, der heute mit ``isinstance`` fragt,
fragt künftig nach vorhandenen Bausteinen.
"""
from dataclasses import dataclass, field
from typing import Optional, Type


@dataclass(frozen=True)
class GPSPosition:
    lat: float
    lon: float


class AbstractTestSetDTO: ...
class TestSetWithSectionControlDTO(AbstractTestSetDTO): ...


@dataclass
class GpsSettings:
    start_position: GPSPosition = GPSPosition(50, 12)


@dataclass
class TestDataSettings:
    test_data_file_name: str = "data.tsv"
    test_set_type: Type[AbstractTestSetDTO] = AbstractTestSetDTO


@dataclass
class SectionControlSettings:
    terminal_processing_time_sec: float = 0.0
    area_error_tolerance_qm: float = 0.0


@dataclass
class TestConfig:
    data_set: str = "clear"
    gps: Optional[GpsSettings] = None
    test_data: Optional[TestDataSettings] = None
    section_control: Optional[SectionControlSettings] = None


def section_control_config(data_set: str = "with_sc_boundary", **settings) -> TestConfig:
    """Konfiguration für Section-Control-Tests mit den dafür üblichen Bausteinen."""
    return TestConfig(
        data_set=data_set,
        gps=GpsSettings(),
        test_data=TestDataSettings(test_set_type=TestSetWithSectionControlDTO),
        section_control=SectionControlSettings(**settings),
    )


default = section_control_config()
assert default.data_set == "with_sc_boundary"

custom = section_control_config("sc_set_3", area_error_tolerance_qm=2.5)
assert custom.data_set == "sc_set_3"
assert custom.section_control is not None
assert custom.section_control.area_error_tolerance_qm == 2.5

# Aus  isinstance(get_test_config(), AbstractTestWithImageComparison)  wird z. B.
#      config.image_comparison is not None
assert TestConfig().gps is None

print(custom)
print("nachher: alle Beobachtungen bestätigt")
