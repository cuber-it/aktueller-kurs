"""1-7 · nachher · Eine Funktion je Umwandlung, ein dokumentierter Vertrag

Eine mögliche Richtung. Der gemeinsame Teil (Spalte fehlt, ist leer oder
enthält ``<none>``) steht einmal in ``_raw``. Für jede Umwandlung gibt es eine
eigene Funktion, deren Name sagt, was sie liefert. Unbekannte Wahrheitswerte
führen zu einer Exception statt zu ``False``.
"""
from typing import Callable, List, Mapping, Optional, TypeVar

T = TypeVar("T")
NONE_MARKER = "<none>"
_TRUE = {"true", "t", "v"}
_FALSE = {"false", "f", "x"}


def _raw(record: Mapping[str, str], column: str) -> Optional[str]:
    """Der getrimmte Text der Spalte, oder None, wenn sie fehlt oder leer ist."""
    value = record.get(column, "").strip()
    return value or None


def read_text(record: Mapping[str, str], column: str, default: Optional[str]) -> Optional[str]:
    value = _raw(record, column)
    if value is None:
        return default
    return None if value == NONE_MARKER else value


def read_as(record: Mapping[str, str], column: str, convert: Callable[[str], T], default: T) -> Optional[T]:
    value = read_text(record, column, None)
    return default if value is None else convert(value)


def read_bool(record: Mapping[str, str], column: str, default: Optional[bool]) -> Optional[bool]:
    """Liest true/false, t/f oder v/x, ohne Rücksicht auf Groß- und Kleinschreibung.

    Raises:
        ValueError: bei jedem anderen Text.
    """
    value = read_text(record, column, None)
    if value is None:
        return default
    if value.lower() in _TRUE:
        return True
    if value.lower() in _FALSE:
        return False
    raise ValueError(f"{column}: {value!r} is not a boolean")


def read_list(record: Mapping[str, str], column: str, default: List[Optional[str]]) -> List[Optional[str]]:
    value = _raw(record, column)
    if value is None:
        return default
    return [None if e.strip() == NONE_MARKER else e.strip() for e in value.split(",")]


record = {"i_is_virtual": "True", "i_working_width": "12.5", "tags": "smoke, <none>",
          "tr_clothoid": "", "i_is_simulated": "ja"}

assert read_as(record, "i_working_width", float, None) == 12.5
assert read_list(record, "tags", []) == ["smoke", None]
assert read_as(record, "tr_clothoid", int, 0) == 0
assert read_bool(record, "i_is_virtual", None) is True
try:
    read_bool(record, "i_is_simulated", False)
except ValueError as error:
    print("abgewiesen:", error)

print("nachher: alle Beobachtungen bestätigt")
