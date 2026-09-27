# Lösungsvorschlag · Wer handelt, wer beobachtet, wer urteilt?

**Vorbemerkung:** Ein Vorschlag, keine Musterlösung. Bewertet wird, ob **eine Meldung auf ihre Ursache zeigt**.

---

## 1 · Teile von `test()`

| Teil | Art |
|---|---|
| `self.control.set(value)` | Aktion |
| `self.control.get()` | Beobachtung |
| `type(value)(…)` | Umwandlung |
| `value != self.cur_value` in `test_wrapper` | Bewertung |
| `fail_test(...)` | Meldung |

---

## 2 · „Expected: 6.5. Found: 5.0“

Sagt: Nach dem Setzen stand 5.0 im Feld. Sagt nicht: ob das Setzen gelang, ob die AUT den Wert verworfen hat oder ob 5.0 der alte Wert ist.

---

## 3 · `bool` aus Text

`bool("False")` ist `True`, jeder nicht leere Text ergibt `True`. Harmlos, wo `get()` bereits einen `bool` liefert: `CheckDelegate` und `SwitchDelegate` lesen `checked`.

---

## 4 · Fünf FAILs

`click_with_entry` trägt „Keyboard didn't open“ ein und lässt den Test weiterlaufen. Die vier Vergleiche melden danach Abweichungen, die nur Folgen sind. Die Ursache nennt der erste FAIL.

---

## 5 · Nur beobachten und bewerten

```python
def expect_value(control, expected, parse=None):
    raw = control.get()
    actual = parse(raw) if parse else raw
    if actual == expected:
        test.passes(f"{control.display_name}: {actual}")
        return True
    fail_test(f"{control.display_name} was not as expected. Expected: {expected!r}. "
              f"Found: {actual!r} (raw {raw!r}). Object: {control}")
    return False
```

---

## 6 · Neu geschrieben

```python
turn_radius = masetth.submenu_traction_unit.turning_radius_btn
turn_radius.set("6.5")                                    # meldet, wenn die Tastatur nicht öffnet
expect_value(turn_radius, 6.5, parse=float)
```

`set()` meldet über `click_with_entry` bereits „Keyboard didn't open while clicking Turning Radius“. Ruft es dabei `fail_test(..., raise_exception=True)`, endet der Testschritt dort, und die Abweichungen folgen nicht.

---

## 7 · Abbrechen oder weiterlaufen

Abbrechen, wenn die folgenden Schritte vom Ergebnis abhängen: Ist die Eingabe gescheitert, sind alle weiteren Eingaben in diesem Menü fraglich. Weiterlaufen, wenn die Prüfungen unabhängig sind, etwa bei reinem Auslesen.

Konkret: Scheitert eine Aktion, `raise_exception=True`. Scheitert eine Prüfung, FAIL und weiter.

---

## 8 · Diagnose

| Information | unterscheidet |
|---|---|
| Aktion gelungen oder nicht | Testfehler/Umgebung gegen AUT |
| Rohwert | Umwandlungsfehler gegen falschen Wert |
| Real Name | Objekt fehlt gegen falscher Wert |
| Wartezeit | Synchronisation |

---

## 9 · Regelkandidaten

| Regel | Einordnung |
|---|---|
| Aktion und Prüfung in getrennten Aufrufen | SHOULD für neue Tests |
| Scheitert eine Aktion, bricht der Testschritt ab | SHOULD |
| Umwandlung aus Text nach `bool` ausdrücklich | MUST |

---

## Diskussionsanschluss

Welche Aktionen in Ihrem Framework können scheitern, ohne es zu melden?
