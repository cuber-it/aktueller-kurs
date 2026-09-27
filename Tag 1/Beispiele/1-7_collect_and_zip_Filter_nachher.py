"""1-7 · nachher · Die Bedingung bekommt einen Namen und einen Vertrag

Eine mögliche Richtung. Was ins Ergebnisarchiv gehört, steht in einer eigenen
Funktion mit sprechendem Namen und Docstring. Ein Fehler wie die fehlenden
Klammern an ``lower`` fällt in einer kleinen, benannten Funktion eher auf, und
sie lässt sich einzeln prüfen.

Ob Target-Verzeichnisse wirklich ausgeschlossen werden sollen, müsste das Team
bestätigen. Der Docstring macht die Absicht überprüfbar.
"""
from pathlib import Path
from typing import Iterable

TARGETS = {"local": ..., "terminal": ..., "tr_terminal": ...}


def belongs_in_result_archive(name: str, target_names: Iterable[str]) -> bool:
    """True für Dateien und Verzeichnisse, die ins Ergebnisarchiv eines Testlaufs gehören.

    Ausgeschlossen sind Python-Quelltexte und Verzeichnisse, die wie ein Target heißen
    (ohne Rücksicht auf Groß- und Kleinschreibung).
    """
    if Path(name).suffix == ".py":
        return False
    return name.lower() not in target_names


files_in_cwd = ["test.py", "test_config.py", "results.json", "Terminal", "screenshot_area.png"]
copied = [f for f in files_in_cwd if belongs_in_result_archive(f, TARGETS)]

print(copied)
assert copied == ["results.json", "screenshot_area.png"]
print("nachher: alle Beobachtungen bestätigt")
