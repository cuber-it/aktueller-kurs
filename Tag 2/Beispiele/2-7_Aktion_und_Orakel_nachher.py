"""2-7 · nachher · Aktion im Test, Bewertung im Orakel

Eine mögliche Richtung. Ausschnitt, nicht eigenständig lauffähig.

- Die Aktion steht im Test: control.set(...).
- Das Orakel beobachtet und bewertet: expect_value(control, expected, parse=...).
  parse ist ausdrücklich: Wer Text liest und einen bool erwartet, sagt, wie Text zu bool wird.
- Die Meldung nennt Control, Real Name, Erwartung und gelesenen Rohwert.
- UIElementTest bleibt für die übrigen Prüfarten bestehen. Neu ist nur die Trennung dort,
  wo heute set_setting=True steht.
"""
from typing import Any, Callable


def parse_bool(text: str) -> bool:
    """'true'/'false' ohne Rücksicht auf Groß- und Kleinschreibung, sonst ValueError."""
    lowered = str(text).strip().lower()
    if lowered in ("true", "1"):
        return True
    if lowered in ("false", "0"):
        return False
    raise ValueError(f"not a boolean: {text!r}")


def expect_value(control, expected: Any, parse: Callable[[Any], Any] = None) -> bool:
    """Liest den Wert eines Controls und vergleicht ihn mit expected.

    parse wandelt den gelesenen Rohwert, bevor verglichen wird. Ohne parse wird der
    Rohwert direkt verglichen. Liefert True bei Übereinstimmung; sonst fail_test.
    """
    raw = control.get()
    actual = parse(raw) if parse else raw
    if actual == expected:
        test.passes(f"{control.display_name}: {actual}")
        return True
    fail_test(f"{control.display_name} was not as expected. Expected: {expected!r}. "
              f"Found: {actual!r} (raw {raw!r}). Object: {control}")
    return False


# Verwendung im Testfall:
sae_j1939 = masetth.submenu_gnss_source.sae_j1939_btn
sae_j1939.set(True)                       # Aktion
expect_value(sae_j1939, True)             # Bewertung; CheckDelegate.get() liefert bereits bool

expect_value(masetth.submenu_implement.turning_radius_btn, 6.5, parse=float)
