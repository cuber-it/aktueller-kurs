"""3-5 · nachher · Die Prüfung kennt die dokumentierten Umschalter

Eine mögliche Richtung. Ausschnitt, nicht eigenständig lauffähig.

Zusätzlich zur Namensendung gibt es eine Liste bekannter umschaltender Quellen. Für jede ist
festgehalten, welche Ziele die Coding-Regeln als „right“ empfehlen. Ein Aufruf mit anderem Ziel
ist ein Fehler, ein Aufruf mit empfohlenem Ziel bleibt eine Warnung: Auch dort klickt
click_and_wait erneut, wenn das Ziel nicht innerhalb von 0,5 s erscheint.

Die Liste ist ein neuer Ort, an dem eine Regel gepflegt werden muss. Nach der eigenen Regel des
Teams („say it once“) gehört sie an genau eine Stelle; check_references.py könnte prüfen, dass
die Dokumentation dieselben Namen nennt.

Die Alternative ohne Liste: click_and_wait klickt nur noch einmal (Tag 2, Beispiel 2-3). Dann
entfallen Prüfung, Checklistenpunkt 6c und der Warnabschnitt in den Coding-Regeln.
"""
import ast

# Quelle: controls_and_tests.md, Abschnitt "click_and_wait re-clicks the source on every retry"
KNOWN_TOGGLING_SOURCES = {
    "layout_manager_btn": {"layout_manager_ok_btn"},       # empfohlene Ziele ("right")
}


def check_toggle_click_and_wait(tree: ast.Module, path: Path, report: Report):
    for node in ast.walk(tree):
        if not (isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)):
            continue
        if node.func.attr != "click_and_wait":
            continue
        source = node.func.value
        name = source.attr if isinstance(source, ast.Attribute) else getattr(source, "id", "")
        wait_target = node.args[0] if node.args else None
        target_name = wait_target.attr if isinstance(wait_target, ast.Attribute) else ""

        if name.endswith(("_toggle", "_switch")):
            report.add(WARN, "C004", path, node.lineno,
                       f"click_and_wait() on the toggling control '{name}' - it re-clicks on every retry; "
                       "use click() + UIElementTest(...).test(...)", "checklist 6c")
        elif name in KNOWN_TOGGLING_SOURCES:
            if target_name in KNOWN_TOGGLING_SOURCES[name]:
                report.add(WARN, "C004", path, node.lineno,
                           f"click_and_wait() on '{name}' toggles a panel; waiting for '{target_name}' is the "
                           "documented pattern but still re-clicks if it takes longer than iteration_delay",
                           "checklist 6c")
            else:
                report.add(ERROR, "C004", path, node.lineno,
                           f"click_and_wait() on '{name}' waits for '{target_name}' inside the panel it toggles - "
                           f"wait for one of {sorted(KNOWN_TOGGLING_SOURCES[name])} first", "checklist 6c")
