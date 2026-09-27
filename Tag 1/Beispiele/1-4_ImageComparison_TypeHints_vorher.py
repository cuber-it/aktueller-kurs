"""1-4 · vorher · Type Hints, die dem Wert widersprechen

Quelle: test_parameters/abstract_test_config.py, AbstractTestWithImageComparison
(Testframework des Teams, gekürzt). Abweichung: pydantic.dataclasses durch dataclasses ersetzt.

Python prüft Type Hints zur Laufzeit nicht. Auch pydantic prüft nur übergebene
Werte, nicht die Vorgabewerte (geprüft mit pydantic 2.12: ``str = 0.9999`` bleibt
ein float).
"""
from dataclasses import dataclass


@dataclass
class AbstractTestWithImageComparison:
    image_comparison_diff_mask_threshold: str = 15
    image_comparison_threshold: str = 0.9999


config = AbstractTestWithImageComparison()
assert isinstance(config.image_comparison_threshold, float)   # annotiert als str
assert isinstance(config.image_comparison_diff_mask_threshold, int)

# Ein Type Checker (mypy, pyright) meldet beide Zeilen der Klasse. Die IDE
# schlägt für config.image_comparison_threshold String-Methoden vor.
print("vorher: Annotation und Wert passen nicht zusammen")
