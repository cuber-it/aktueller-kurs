"""1-4 · vorher · AbstractTargetHelper: ein Vertrag mit 14 Pflichtmethoden

Quelle: target_helper/abstract_target_helper.py (Testframework des Teams, nur die Signaturen
der abstrakten Methoden) und der Testfall
suite_UT/tst_1_2_TC_1010_Store_function_instance_and_isobus_address (gekürzt).

Die Prüffunktion unten liest nur Dateien vom Gerät. Ein Test Double für sie muss
trotzdem alle 14 abstrakten Methoden implementieren, sonst lässt es sich nicht
erzeugen.
"""
from abc import ABC, abstractmethod
from datetime import datetime


class AbstractTargetHelper(ABC):
    @abstractmethod
    def stop_aut_docker(self): ...
    @abstractmethod
    def start_aut_docker(self): ...
    @abstractmethod
    def initial_maintenance(self): ...
    @abstractmethod
    def replace_data_set(self, data_set, data_set_path=None): ...
    @abstractmethod
    def backup_data_set(self, data_set, data_set_path=None, restart_docker=True): ...
    @abstractmethod
    def simulate_usb(self): ...
    @abstractmethod
    def get_system_time(self) -> datetime: ...
    @property
    @abstractmethod
    def data_root_path(self) -> str: ...
    @abstractmethod
    def path_exists(self, path) -> bool: ...
    @abstractmethod
    def list_files(self, pattern) -> list: ...
    @abstractmethod
    def read_file(self, path) -> str: ...
    @abstractmethod
    def count_lines(self, path) -> int: ...
    @abstractmethod
    def search_lines(self, path, substrings, since_line=0) -> list: ...
    @abstractmethod
    def read_aut_os_release(self) -> str: ...


def settings_file_has_fields(target: AbstractTargetHelper, path: str, *fields: str) -> bool:
    """Prüft, ob die Einstellungsdatei auf dem Gerät alle Felder enthält."""
    if not target.path_exists(path):
        return False
    content = target.read_file(path)
    return all(f in content for f in fields)


class FakeFiles(AbstractTargetHelper):
    def __init__(self, files):
        self._files = files

    def path_exists(self, path):
        return path in self._files

    def read_file(self, path):
        return self._files[path]


try:
    FakeFiles({"gen3_vtserver_service_0.json": '{"function_instance": 0}'})
except TypeError as error:
    print("Test Double abgewiesen:", str(error)[:80], "...")

print("vorher: alle Beobachtungen bestätigt")
