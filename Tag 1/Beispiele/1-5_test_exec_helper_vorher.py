"""1-5 · vorher · test_exec_helper: ein Singleton, das beim Import Squish befragt

Quelle: test_parameters/test_exec_helper.py, target_helper/targets.py,
init_cleanup_wrapper_helper/cleanup_helper.py (Testframework des Teams, gekürzt).
Abweichung: ``squish.currentApplicationContext`` und die Target-Helper sind
durch Platzhalter ersetzt, ``fail_test(..., raise_exception=True)`` durch
``LookupError``, der Zeitstempel ist fest.

Jedes Modul, das ``test_exec_helper`` importiert, hängt davon ab, dass beim
Import eine Squish-Verbindung besteht. An den Funktionen, die es verwenden, ist
das nicht zu sehen.
"""
import os
from fnmatch import fnmatch


# --- Platzhalter für Squish ---------------------------------------------------
class _Context:
    host = "192.168.3.17"


class squish:
    @staticmethod
    def currentApplicationContext():
        return _Context()
# ------------------------------------------------------------------------------


class TargetDTO:
    def __init__(self, name, ip, can, terminal_processing_time_sec, target_helper):
        self.name = name
        self.ip = ip
        self.can = can
        self.terminal_processing_time_sec = terminal_processing_time_sec
        self.helper = target_helper

    def set_ip(self, ip):
        if "*" in self.ip:
            self.ip = ip
        if "*" in self.can:
            self.can = "can" + str(self.ip).split(".")[2]


TARGETS = {"local": TargetDTO("local", "127.0.*", "can0", 0.125, None),
           "terminal": TargetDTO("terminal", "192.168.*", "can1", 0.05, None)}


class _TestExecHelper:
    def __init__(self):
        self.target = self.determine_target()
        self.tags = [e.strip() for e in os.getenv("SQUISH_TAGS", "full").split(",")]

    def determine_target(self):
        ip_address = str(squish.currentApplicationContext().host)
        for target in TARGETS.values():
            if fnmatch(ip_address, target.ip):
                if "*" in target.ip:
                    target.set_ip(ip_address)
                return target
        raise LookupError("Unknown IP format, can't determine target")


test_exec_helper = _TestExecHelper()          # läuft beim Import


def _get_res_zip_path(test_set_name):
    if len(test_set_name) > 0:
        test_set_name = "_" + test_set_name
    results_name = f"_20260922-1014{test_set_name}-{test_exec_helper.target.name}"
    return os.path.join("/results", results_name)


print(_get_res_zip_path("sc_set_3"))

# Das Singleton verändert die gemeinsame Tabelle TARGETS: Aus dem Muster wird eine feste IP.
assert TARGETS["terminal"].ip == "192.168.3.17"

# Ein zweites Terminal im selben Prozess passt danach nicht mehr auf das Muster:
_Context.host = "192.168.4.20"
try:
    _TestExecHelper()
except LookupError as error:
    print("zweites Terminal:", error)

print("vorher: alle Beobachtungen bestätigt")
