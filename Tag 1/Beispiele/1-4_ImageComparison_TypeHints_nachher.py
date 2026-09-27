"""1-4 · nachher · Type Hints, die den Vertrag beschreiben

Die Annotationen sagen jetzt, was die Werte sind. Zur Laufzeit ändert sich
nichts, aber Type Checker und IDE arbeiten mit den richtigen Typen.
"""
from dataclasses import dataclass


@dataclass
class AbstractTestWithImageComparison:
    image_comparison_diff_mask_threshold: int = 15
    image_comparison_threshold: float = 0.9999


config = AbstractTestWithImageComparison()
assert isinstance(config.image_comparison_threshold, float)
assert isinstance(config.image_comparison_diff_mask_threshold, int)
print("nachher: Annotation und Wert passen zusammen")
