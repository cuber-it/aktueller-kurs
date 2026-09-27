"""1-3 · nachher · Kontextverwaltung als eigener Kollaborateur

Eine mögliche Richtung. ``ApplicationContexts`` verwaltet die
Squish-Anwendungskontexte und ist ohne Target prüfbar. Ein Target besitzt eine
Instanz davon (Komposition) und reicht ``start`` und
``switch_application_context`` an sie weiter (Delegation).

Die Vererbung bleibt dort, wo sie eine Typbeziehung ausdrückt: Lokales Target
und Terminal sind beide Targets mit denselben Geräteoperationen.

Nebenbei ist ``application_contexts`` jetzt ein Instanzattribut. Warum das
wichtig ist, zeigt 1-6.
"""
from abc import ABC, abstractmethod
from enum import Enum
from typing import Callable, Dict, Optional


class ApplicationName(Enum):
    terminalui_launcher = "terminalui_launcher"
    vtserver = "vtserver"


class ApplicationContexts:
    """Hält je Anwendung den Squish-Kontext und schaltet zwischen ihnen um."""

    def __init__(self, attach: Callable[[str], object], activate: Callable[[object], None]) -> None:
        self._attach = attach
        self._activate = activate
        self._contexts: Dict[ApplicationName, object] = {}

    def attach_all(self) -> None:
        for name in ApplicationName:
            self._contexts[name] = self._attach(name.value)

    def switch_to(self, name: ApplicationName = ApplicationName.terminalui_launcher) -> None:
        self._activate(self._contexts[name])


class TargetHelper(ABC):
    """Geräteoperationen eines Targets. Die Kontextverwaltung wird übergeben."""

    def __init__(self, contexts: ApplicationContexts) -> None:
        self._contexts = contexts

    def start(self) -> None:
        self._contexts.attach_all()

    def switch_application_context(self, name: ApplicationName = ApplicationName.terminalui_launcher) -> None:
        self._contexts.switch_to(name)

    @abstractmethod
    def start_aut_docker(self) -> None: ...

    @abstractmethod
    def replace_data_set(self, data_set: str, data_set_path: Optional[str] = None) -> None: ...


class TerminalTargetHelper(TargetHelper):
    def start_aut_docker(self) -> None:
        print("terminal: ssh ... systemctl start")

    def replace_data_set(self, data_set: str, data_set_path: Optional[str] = None) -> None:
        print(f"terminal: scp {data_set}")


# Die Kontextverwaltung lässt sich ohne Squish und ohne Target prüfen:
activated: list = []
contexts = ApplicationContexts(attach=lambda name: f"<context {name}>", activate=activated.append)
contexts.attach_all()
contexts.switch_to(ApplicationName.vtserver)
assert activated == ["<context vtserver>"]

# Im Kurs mit Squish sähe die Zusammensetzung so aus:
#   contexts = ApplicationContexts(squish.attachToApplication, squish.setApplicationContext)
terminal = TerminalTargetHelper(contexts)
terminal.switch_application_context()
assert activated[-1] == "<context terminalui_launcher>"

print("nachher: alle Beobachtungen bestätigt")
