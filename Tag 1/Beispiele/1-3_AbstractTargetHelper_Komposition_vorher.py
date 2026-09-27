"""1-3 · vorher · AbstractTargetHelper: gemeinsamer Squish-Code in der Basisklasse

Quelle: target_helper/abstract_target_helper.py, local_target_helper.py,
terminal_target_helper.py (Testframework des Teams, stark gekürzt).
Abweichung: ``squish.attachToApplication`` und ``squish.setApplicationContext``
sind durch Platzhalter ersetzt.

Die Basisklasse enthält zwei Dinge: den für alle Targets gleichen Umgang mit
Squish-Anwendungskontexten und die abstrakten Geräteoperationen, in denen sich
die Targets unterscheiden. Wer die Kontextverwaltung ändern will, ändert die
Basis aller Targets.
"""
from abc import ABC, abstractmethod
from enum import Enum


# --- Platzhalter für Squish ---------------------------------------------------
class squish:
    current = None

    @staticmethod
    def attachToApplication(name, timeoutSecs=10):
        return f"<context {name}>"

    @staticmethod
    def setApplicationContext(ctx):
        squish.current = ctx
# ------------------------------------------------------------------------------


class ApplicationName(Enum):
    terminalui_launcher = "terminalui_launcher"
    vtserver = "vtserver"


class AbstractTargetHelper(ABC):
    """The abstract class for all target helpers."""
    application_contexts = {}

    def start(self):
        self.attach_all_applications()

    def attach_all_applications(self, timeout_sec=60):
        for application_name in ApplicationName:
            self.application_contexts[application_name] = squish.attachToApplication(application_name.value)

    def switch_application_context(self, application_name=ApplicationName.terminalui_launcher):
        squish.setApplicationContext(self.application_contexts[application_name])

    @abstractmethod
    def start_aut_docker(self): ...

    @abstractmethod
    def replace_data_set(self, data_set, data_set_path=None): ...


class _LocalTargetHelper(AbstractTargetHelper):
    def start_aut_docker(self):
        print("local: docker compose up")

    def replace_data_set(self, data_set, data_set_path=None):
        print(f"local: copy {data_set}")


class _TerminalTargetHelper(AbstractTargetHelper):
    def start_aut_docker(self):
        print("terminal: ssh ... systemctl start")

    def replace_data_set(self, data_set, data_set_path=None):
        print(f"terminal: scp {data_set}")


terminal_target_helper = _TerminalTargetHelper()
terminal_target_helper.start()
terminal_target_helper.switch_application_context()
print(squish.current)

# Ein Test der Kontextverwaltung braucht ein konkretes Target, weil die Logik
# nur als Teil einer Target-Klasse existiert.
print("vorher: läuft")
