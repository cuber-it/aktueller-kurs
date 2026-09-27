# Übung · Prüfskript, KI-Review oder bessere API?

Sie entscheiden, wie Regeln aus Tag 1 und Tag 2 künftig geprüft werden: deterministisch in `check_test.py`, durch einen KI-gestützten Review oder gar nicht mehr, weil das Framework den Fehler ausschließt.

---

## Material A · Das Prüfskript des Teams

`scripts/check_test.py` prüft einen generierten Testfall statisch, ohne Target und ohne Squish-Lizenz. Grundsatz im Docstring: **„never guess“**. Jede Prüfung bleibt still, wenn sie nicht sicher auflösen kann, weil Fehlalarme dazu erziehen, die Ausgabe zu ignorieren. Exit-Code 1 bei Fehlern, geeignet für Commit-Hook oder CI.

| Code | prüft |
|---|---|
| A001 | Attributketten gegen die echten `UI/*.py`: erfundene Attribute |
| B001–B005 | Importe |
| C001 | nicht existierende Prüfmethoden |
| C002 | terminal-spezifische Pfade |
| C003 | `snooze` direkt nach Klick ohne Begründungskommentar (Warnung) |
| C004 | `click_and_wait` auf Controls mit Namensendung `_toggle` oder `_switch` (Warnung) |
| C005 | falsches Lesen eines `NumericTextFieldDelegate` |
| D001 | Testdaten als Literal im Test |
| F004 | `# Expected:` ohne Assertion |

---

## Material B · Prüfung C004

```python
def check_toggle_click_and_wait(tree, path, report):
    for node in ast.walk(tree):
        if not (isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)):
            continue
        if node.func.attr != "click_and_wait":
            continue
        target = node.func.value
        name = target.attr if isinstance(target, ast.Attribute) else getattr(target, "id", "")
        if name.endswith("_toggle") or name.endswith("_switch"):
            report.add(WARN, "C004", path, node.lineno, "...", "checklist 6c")
```

Die Coding-Regeln nennen als Beispiel für eine umschaltende Quelle `layout_manager_btn`.

---

## Material C · Regelkandidaten aus Tag 1 und Tag 2

| Nr. | Regel |
|---|---|
| K1 | `click_and_wait` nicht auf einer umschaltenden Quelle. |
| K2 | Einen Wert direkt nach einer Navigation erst lesen, wenn das Feld existiert. |
| K3 | Setzen und Prüfen nicht in einem Aufruf (`set_setting=True`). |
| K4 | Prüfen mit `UIElementTest` statt `if … test.passes … else test.fail`. |
| K5 | Menüwege über mehrere Screens als Helper, der das Zielmenü zurückgibt. |
| K6 | Keine zwei Testfälle mit identischen Schritten in der Spezifikation. |
| K7 | Aus Text wird ein Wahrheitswert nie mit `bool(...)`. |

---

## Aufgabe

### Teil 1 · Einordnen

**1.** Ordnen Sie jede Regel aus Material C zu: deterministische Prüfung, KI-Review, Änderung am Framework oder keine Prüfung. Begründen Sie kurz.

**2.** Welche Regeln lassen sich statisch prüfen, ohne gegen „never guess“ zu verstoßen?

### Teil 2 · C004

**3.** Warum findet C004 den Fall aus den Coding-Regeln nicht?

**4.** Erweitern Sie C004 so, dass es `layout_manager_btn` erkennt. Wie gehen Sie mit dem Aufruf um, den die Coding-Regeln als „right“ empfehlen?

**5.** Was ist der Nachteil einer Liste bekannter Umschalter? Welche Alternative macht C004 überflüssig?

### Teil 3 · KI-Review

**6.** Für welche Regeln aus Material C braucht es Urteil? Schreiben Sie für eine davon einen Prüfauftrag an Claude Code, der den Teamstandard als Maßstab nennt.

**7.** Wohin gehen die Ergebnisse eines KI-Reviews, damit sie nicht verloren gehen?

---

## Hinweise zur Bearbeitung

- „Deterministisch“ heißt: Gleiche Eingabe, gleiches Ergebnis, ohne Modell.
- Eine Prüfung, die oft falsch anschlägt, schadet mehr, als sie nützt.
- Wenn Sie unsicher sind, fragen Sie: **Kann eine Maschine das sicher entscheiden, oder braucht es Urteil?**
