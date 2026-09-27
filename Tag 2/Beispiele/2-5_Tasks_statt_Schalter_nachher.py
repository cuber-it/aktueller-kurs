"""2-5 · nachher · Zugriff je Control-Typ, drei Tasks, ein Workflow

Eine mögliche Richtung. Ausschnitt, nicht eigenständig lauffähig.

- ParameterAccess beschreibt je Control-Typ, wie ein Wert gelesen und gesetzt wird. Das ist
  der Teil, der sich mit einem neuen Control-Typ ändert.
- Drei Tasks tun je eine Sache: auslesen, vergleichen, setzen. Das ist der Teil, der sich mit
  einer neuen Aktion ändert.
- Der Workflow kennt nur den Weg durch die Menüs und wendet einen Task auf jeden Parameter an.

Eine neue Aktion ist ein neuer Task, ein neuer Control-Typ ein neuer Eintrag in ACCESS.
Vorher bedeutete jede neue Aktion eine Änderung in fünf Methoden.
"""
from dataclasses import dataclass
from typing import Callable, Dict


@dataclass(frozen=True)
class ParameterAccess:
    read: Callable[["Control"], str]
    write: Callable[["Control", str], None]


def _write_check(control, value):
    if control.get_state() != value.upper():
        control.switch_state()


ACCESS: Dict[type, ParameterAccess] = {
    TextFieldDelegate: ParameterAccess(read=lambda c: c.get(), write=lambda c, v: c.set(v)),
    CheckDelegate: ParameterAccess(read=lambda c: c.get_state(), write=_write_check),
    SwitchDelegate: ParameterAccess(read=lambda c: c.get_state(), write=_write_check),
    # ItemDelegateWithValue, … entsprechend
}


def access_for(control) -> ParameterAccess:
    return ACCESS[type(control)]


# ── Tasks ───────────────────────────────────────────────────────────────────────
def read_parameter(control, readings: Dict[str, str]) -> None:
    readings[control.display_name] = access_for(control).read(control)


def compare_parameter(control, reference: Dict[str, str]) -> None:
    expected = reference[control.display_name]
    actual = access_for(control).read(control)
    if actual == expected:
        test.passes(f"{control.display_name}: {actual}")
    else:
        test.fail(f"{control.display_name}: expected {expected}, found {actual}")


def set_parameter(control, reference: Dict[str, str]) -> None:
    access_for(control).write(control, reference[control.display_name])


# ── Workflow ────────────────────────────────────────────────────────────────────
def for_each_implement_parameter(implement_name: str, task: Callable[["Control"], None]) -> None:
    """Geht durch die Menüs eines Geräts und wendet task auf jeden Parameter an."""
    masetth.submenu_machinesettings.open_implement_settings_by_text(implement_name)
    with log_section("General"):
        masetth.submenu_implement.general_btn.set(True)
        task(masetth.submenu_implement.general_manufacturer_btn)
        masetth.submenu_implement.general_btn.set(False)
    # … Geometry, … nach demselben Muster


# ── Verwendung ──────────────────────────────────────────────────────────────────
reference = read_reference_row("implement_reference.csv", row="Sprayer 24m")   # neu: liest eine Zeile der Referenz-CSV
for_each_implement_parameter("Sprayer 24m", lambda c: compare_parameter(c, reference))
