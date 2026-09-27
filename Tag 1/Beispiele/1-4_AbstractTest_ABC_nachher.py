"""1-4 · nachher · Basisklasse ohne ABC, abstrakt nur mit echtem Vertrag

Eine mögliche Richtung. ``TestConfig`` ist eine gewöhnliche Datenklasse mit
Vorgabewerten. Sie braucht weder ``ABC`` noch „Abstract“ im Namen.

``ABC`` lohnt sich, wo Unterklassen etwas liefern müssen. Im Testframework wäre das
etwa ``_provide_test_set``: Jede datengetriebene Konfiguration muss sagen, welche
Art Testsatz sie erzeugt. Mit ``@abstractmethod`` meldet Python eine vergessene
Implementierung beim Erzeugen, nicht erst beim ersten Lesen der Testdaten.
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class TestConfig:
    data_set: str = "clear"


class TestSet: ...
class MachineTestSet(TestSet): ...


class DataDrivenTestConfig(TestConfig, ABC):
    @abstractmethod
    def provide_test_set(self) -> TestSet:
        """Liefert einen leeren Testsatz der passenden Art."""


@dataclass
class MachineTestConfig(DataDrivenTestConfig):
    def provide_test_set(self) -> TestSet:
        return MachineTestSet()


@dataclass
class ForgottenConfig(DataDrivenTestConfig):
    pass


assert TestConfig().data_set == "clear"
assert isinstance(MachineTestConfig().provide_test_set(), MachineTestSet)
try:
    ForgottenConfig()  # type: ignore[abstract]  # absichtlich: zeigt die Prüfung
except TypeError as error:
    print("abgewiesen:", error)

print("nachher: alle Beobachtungen bestätigt")
