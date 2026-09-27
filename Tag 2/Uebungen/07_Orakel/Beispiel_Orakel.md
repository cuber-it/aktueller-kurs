# Beispiel · Wer handelt, wer beobachtet, wer urteilt? – in klein

Dieselbe Aufgabe an einem kleineren Gegenstand, vollständig durchgeführt.

---

## Der Gegenstand

GUI-Tests für einen Heizungsregler. Ein Hilfsobjekt setzt den Sollwert und prüft ihn:

```python
class SetpointCheck:
    def __init__(self, field):
        self.field = field

    def test(self, value, set_first=False):
        if set_first:
            self.field.set(value)
        actual = type(value)(self.field.get())
        if actual != value:
            test.fail(f"Setpoint: expected {value}, found {actual}")


SetpointCheck(panel.setpoint).test(21.5, set_first=True)
SetpointCheck(panel.eco_mode).test(True)
```

`panel.eco_mode.get()` liefert den Text `"off"`.

---

## Schritt 1 · Unterscheiden

| Teil | Art |
|---|---|
| `field.set(value)` | Aktion |
| `field.get()` | Beobachtung |
| `type(value)(…)` | Umwandlung, versteckt |
| `actual != value` | Bewertung |

`bool("off")` ist `True`. Die Prüfung auf `True` besteht, obwohl der Eco-Modus aus ist.

---

## Schritt 2 · Trennen

```python
def parse_on_off(text):
    return {"on": True, "off": False}[text.strip().lower()]


def expect(control, expected, parse=None):
    raw = control.get()
    actual = parse(raw) if parse else raw
    if actual != expected:
        test.fail(f"{control}: expected {expected!r}, found {actual!r} (raw {raw!r})")


panel.setpoint.set("21.5")
expect(panel.setpoint, 21.5, parse=float)
expect(panel.eco_mode, True, parse=parse_on_off)
```

---

## Schritt 3 · Wenn die Aktion scheitert

`set()` meldet selbst, wenn die Eingabe nicht angekommen ist, etwa weil die Tastatur nicht öffnet. Dann steht im Protokoll zuerst „Setpoint: keyboard did not open“ und danach die Abweichung.

---

## Was dieses Beispiel zeigt

**Aktion und Prüfung getrennt, Meldungen getrennt.** Ein Fehler der Aktion steht als solcher im Protokoll.

**Umwandlung ausdrücklich.** `parse=parse_on_off` sagt, wie Text zu `bool` wird.

**Rohwert in der Meldung.** „raw 'off'“ zeigt, was das Control geliefert hat.
