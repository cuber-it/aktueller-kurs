"""1-6 · nachher · Zustand gehört der Instanz

Jede Instanz bekommt im Konstruktor ihr eigenes Dictionary. Klassenattribute
bleiben für Werte, die wirklich für alle Instanzen gleich sind und nicht
verändert werden, etwa Konstanten.
"""
from abc import ABC
from typing import Dict


class squish:
    @staticmethod
    def attachToApplication(name, timeoutSecs=10):
        return f"<context {name}>"


class AbstractTargetHelper(ABC):
    def __init__(self) -> None:
        self._application_contexts: Dict[str, object] = {}

    def attach_application(self, application_name: str) -> None:
        self._application_contexts[application_name] = squish.attachToApplication(application_name, timeoutSecs=10)

    def detach_all_applications(self) -> None:
        self._application_contexts.clear()

    def is_attached(self, application_name: str) -> bool:
        return application_name in self._application_contexts


class _LocalTargetHelper(AbstractTargetHelper): ...
class _TerminalTargetHelper(AbstractTargetHelper): ...


local_target_helper = _LocalTargetHelper()
terminal_target_helper = _TerminalTargetHelper()

terminal_target_helper.attach_application("terminalui_launcher")
assert not local_target_helper.is_attached("terminalui_launcher")

local_target_helper.detach_all_applications()
assert terminal_target_helper.is_attached("terminalui_launcher")

print("nachher: alle Beobachtungen bestätigt")
