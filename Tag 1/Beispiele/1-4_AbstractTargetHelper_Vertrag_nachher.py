"""1-4 · nachher · Kleine Verträge aus Sicht der Aufrufer

Eine mögliche Richtung. Jeder Aufrufer beschreibt mit einem ``Protocol``, was er
vom Target braucht. Die vorhandenen Target-Klassen bleiben unverändert: Sie
erfüllen die Protocols strukturell, ohne sie zu erben.

Mögliche Aufteilung nach den Aufrufstellen im Testframework:

- Dateien auf dem Gerät: path_exists, read_file, list_files, count_lines, search_lines
- Datensätze: replace_data_set, backup_data_set (test_wrapper)
- Lebenszyklus der AUT: start, cleanup (test_wrapper)

Die Prüffunktion unten braucht davon nur path_exists und read_file. Genau das
beschreibt ``DeviceFiles``.

Die ABC der Targets kann bleiben, wenn sie eine bewusst modellierte Typfamilie
beschreibt. Die Frage ist nur, wovon ein Aufrufer abhängt.
"""
from typing import Protocol


class DeviceFiles(Protocol):
    """Lesender Zugriff auf Dateien des Geräts."""

    def path_exists(self, path: str) -> bool: ...
    def read_file(self, path: str) -> str: ...


def settings_file_has_fields(files: DeviceFiles, path: str, *fields: str) -> bool:
    """Prüft, ob die Einstellungsdatei auf dem Gerät alle Felder enthält."""
    if not files.path_exists(path):
        return False
    content = files.read_file(path)
    return all(f in content for f in fields)


class FakeFiles:
    """Test Double: implementiert nur, was DeviceFiles verlangt."""

    def __init__(self, files: dict) -> None:
        self._files = files

    def path_exists(self, path: str) -> bool:
        return path in self._files

    def read_file(self, path: str) -> str:
        return self._files[path]


device = FakeFiles({"gen3_vtserver_service_0.json":
                    '{"function_instance": 0, "last_used_isobus_source_address": 38}'})

assert settings_file_has_fields(device, "gen3_vtserver_service_0.json",
                                "function_instance", "last_used_isobus_source_address")
assert not settings_file_has_fields(device, "gen3_vtserver_service_1.json", "function_instance")

print("nachher: alle Beobachtungen bestätigt")
