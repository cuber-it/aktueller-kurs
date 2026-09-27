"""1-5 · nachher · Die Konfiguration wird übergeben

Eine mögliche Richtung. Die Konfiguration trägt sich nirgends ein. Wer sie
braucht, bekommt sie als Parameter, im Testframework etwa
``test_wrapper(test_config)`` und von dort ``clean_up_test_data(config)``.

Die Abhängigkeit steht jetzt in der Signatur. Ein Test von
``clean_up_test_data`` übergibt einfach ein passendes Objekt.
"""
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class TestConfig:
    data_set: str = "clear"
    image_comparison_results_path: Optional[str] = None


def clean_up_test_data(config: TestConfig) -> List[str]:
    """Liefert die Muster der Dateien, die nach einem Test entfernt werden."""
    removed = ["*.zip", "_*", "*.pdf"]
    if config.image_comparison_results_path is not None:
        removed.append(config.image_comparison_results_path)
    return removed


my_config = TestConfig(data_set="with_gps", image_comparison_results_path="image_comparison_results")
reference = TestConfig(data_set="clear")          # stört niemanden

assert "image_comparison_results" in clean_up_test_data(my_config)
assert "image_comparison_results" not in clean_up_test_data(reference)

print("nachher: alle Beobachtungen bestätigt")
