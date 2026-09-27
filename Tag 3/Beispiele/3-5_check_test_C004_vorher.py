"""3-5 · vorher · Eine Regel aus der Checkliste als deterministische Prüfung

Ausschnitt aus scripts/check_test.py des Teams (Prüfung C004, unverändert). Nicht eigenständig
lauffähig.

Die Coding-Regeln des Teams warnen: click_and_wait klickt die Quelle bei jeder Wiederholung
erneut, zerstörerisch bei umschaltenden Quellen. Als Beispiel nennen sie layout_manager_btn.
Die Abschlussliste (Punkt 6c) verbietet click_and_wait auf umschaltenden Quellen.

C004 erkennt einen Umschalter nur an der Endung des Namens: _toggle oder _switch.
layout_manager_btn endet auf _btn und wird nicht erkannt. Der Fall, den die eigene
Dokumentation als Beispiel nennt, fällt durch.
"""
import ast


def check_toggle_click_and_wait(tree: ast.Module, path: Path, report: Report):
    for node in ast.walk(tree):
        if not (isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)):
            continue
        if node.func.attr != "click_and_wait":
            continue
        target = node.func.value
        name = target.attr if isinstance(target, ast.Attribute) else getattr(target, "id", "")
        if name.endswith("_toggle") or name.endswith("_switch"):
            report.add(WARN, "C004", path, node.lineno,
                       f"click_and_wait() on the toggling control '{name}' - it re-clicks on every retry; "
                       "use click() + UIElementTest(...).test(...)", "checklist 6c")
