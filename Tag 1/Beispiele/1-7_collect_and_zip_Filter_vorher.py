"""1-7 · vorher · collect_and_zip: eine Bedingung ohne Namen

Quelle: init_cleanup_wrapper_helper/cleanup_helper.py, collect_and_zip
(Testframework des Teams, gekürzt auf die Auswahl der Dateien).
Abweichung: ``glob("*")`` durch eine feste Liste ersetzt, Kopieren durch Sammeln.

Die Bedingung soll Python-Dateien und Target-Verzeichnisse ausschließen,
vermutlich. ``file.lower`` ohne Klammern ist die Methode selbst, kein Text.
Sie ist nie Schlüssel in ``TARGETS``, der zweite Teil der Bedingung ist also
immer False.
"""
TARGETS = {"local": ..., "terminal": ..., "tr_terminal": ...}

files_in_cwd = ["test.py", "test_config.py", "results.json", "Terminal", "screenshot_area.png"]

copied = []
for file in files_in_cwd:
    if not (".py" in file or file.lower in TARGETS):
        copied.append(file)

print(copied)
assert "Terminal" in copied               # Target-Verzeichnis wird mitkopiert
print("vorher: alle Beobachtungen bestätigt")
