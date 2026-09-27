"""1-4 · vorher · AbstractTest: eine ABC ohne abstrakte Methode

Quelle: test_parameters/abstract_test_config.py (Testframework des Teams, gekürzt).
Abweichung: pydantic.dataclasses durch dataclasses ersetzt.

Name und Basisklasse versprechen einen Vertrag. ``ABC`` verhindert aber nur
die Instanziierung von Klassen, die noch abstrakte Methoden haben, und hier
gibt es keine.
"""
from abc import ABC
from dataclasses import dataclass


@dataclass
class AbstractTest(ABC):
    """
    The minimal parameters and methods any test should have.

    The test config class of any test should implement this class or any of it's derivatives
    and either overwrite or keep the default parameters.
    """
    data_set: str = "clear"


config = AbstractTest()          # „abstrakt“, trotzdem instanziierbar
assert config.data_set == "clear"
print("vorher: AbstractTest() ließ sich erzeugen")
