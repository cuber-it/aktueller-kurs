"""1-5 · nachher · Ausführungskontext wird ermittelt und übergeben

Eine mögliche Richtung.

- ``determine_target`` ist eine Funktion ohne Seiteneffekt. Sie bekommt IP und
  Target-Tabelle und liefert eine Kopie mit fester IP. ``TARGETS`` bleibt unverändert.
- ``ExecutionContext`` entsteht einmal, dort, wo die Suite startet (im Testframework
  etwa in ``suite_init``), und wird an die Stellen übergeben, die ihn brauchen.
- ``result_zip_path`` bekommt alles, was sie braucht, als Parameter.

Kosten: Der Kontext muss durchgereicht werden. Das macht Abhängigkeiten sichtbar,
bedeutet aber zusätzliche Parameter an Stellen, die heute ohne auskommen.
"""
import os
from dataclasses import dataclass, replace
from fnmatch import fnmatch
from typing import Dict, List


@dataclass(frozen=True)
class TargetDTO:
    name: str
    ip: str
    can: str
    terminal_processing_time_sec: float


TARGETS = {"local": TargetDTO("local", "127.0.*", "can0", 0.125),
           "terminal": TargetDTO("terminal", "192.168.*", "can1", 0.05)}


def determine_target(ip_address: str, targets: Dict[str, TargetDTO]) -> TargetDTO:
    """Liefert das Target, dessen IP-Muster passt, mit eingesetzter IP.

    Raises:
        LookupError: wenn kein Muster passt.
    """
    for target in targets.values():
        if fnmatch(ip_address, target.ip):
            return replace(target, ip=ip_address)
    raise LookupError(f"no target matches {ip_address}")


@dataclass(frozen=True)
class ExecutionContext:
    target: TargetDTO
    tags: List[str]


def result_zip_path(results_dir: str, timestamp: str, target_name: str, test_set_name: str = "") -> str:
    suffix = f"_{test_set_name}" if test_set_name else ""
    return os.path.join(results_dir, f"_{timestamp}{suffix}-{target_name}")


# In suite_init, mit Squish:  ip = str(squish.currentApplicationContext().host)
context = ExecutionContext(determine_target("192.168.3.17", TARGETS), ["full"])

assert result_zip_path("/results", "20260922-1014", context.target.name, "sc_set_3") \
    == "/results/_20260922-1014_sc_set_3-terminal"

# TARGETS bleibt ein Muster, ein zweites Terminal wird erkannt:
assert TARGETS["terminal"].ip == "192.168.*"
assert determine_target("192.168.4.20", TARGETS).ip == "192.168.4.20"

print("nachher: alle Beobachtungen bestätigt")
