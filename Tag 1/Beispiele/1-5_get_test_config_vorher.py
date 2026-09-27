"""1-5 · vorher · get_test_config: die zuletzt erzeugte Konfiguration gewinnt

Quelle: test_parameters/abstract_test_config.py, init_cleanup_wrapper_helper/
cleanup_helper.py und ein test_config.py aus suite_UT (Testframework des Teams, gekürzt).
Abweichungen: pydantic.dataclasses durch dataclasses ersetzt; ``clean_up_test_data``
löscht nichts, sondern gibt die Muster der zu löschenden Dateien zurück.

Jede Konfiguration trägt sich beim Erzeugen in eine globale Variable ein.
Hilfsfunktionen lesen sie über ``get_test_config()``. Tests lesen dieselbe
Konfiguration über ``from test_config import test_config``. Es gibt also zwei
Wege zum selben Objekt, und welcher Wert gilt, hängt von der Reihenfolge ab.
"""
from dataclasses import dataclass

test_config = None


def get_test_config():
    return test_config


@dataclass
class AbstractTest:
    data_set: str = "clear"

    def __post_init__(self):
        global test_config
        test_config = self


@dataclass
class AbstractTestWithImageComparison(AbstractTest):
    image_comparison_results_path: str = "image_comparison_results"


def clean_up_test_data():
    """Removes most common results from current working directory."""
    removed = ["*.zip", "_*", "*.pdf"]
    if isinstance(get_test_config(), AbstractTestWithImageComparison):
        removed.append(get_test_config().image_comparison_results_path)
    return removed


# test_config.py eines Bildvergleichstests:
@dataclass
class _TestConfig(AbstractTestWithImageComparison):
    data_set: str = "with_gps"


my_config = _TestConfig()
assert "image_comparison_results" in clean_up_test_data()

# Irgendwo im Test wird eine weitere Konfiguration erzeugt, etwa als Vorlage
# für einen Vergleich. Ab jetzt räumt clean_up_test_data die Bildergebnisse nicht mehr auf:
reference = AbstractTest(data_set="clear")
assert get_test_config() is reference
assert "image_comparison_results" not in clean_up_test_data()

# Für einen Test von clean_up_test_data muss man die globale Variable vorbereiten.
print("vorher: alle Beobachtungen bestätigt")
