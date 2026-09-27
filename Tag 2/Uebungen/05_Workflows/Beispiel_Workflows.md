# Beispiel · Wer tut hier was? – in klein

Dieselbe Aufgabe an einem kleineren Gegenstand, vollständig durchgeführt.

---

## Der Gegenstand

GUI-Tests für die Kalibrierparameter einer Laborwaage. Zwei Control-Typen (Zahlenfeld, Auswahlliste), zwei Aktionen (auslesen, prüfen):

```python
class ScaleParameterRunner:
    def process_number(self, field):
        if self.action == "read":
            self.values[field.name] = field.get()
        elif self.action == "check":
            assert field.get() == self.expected[field.name]

    def process_choice(self, choice):
        if self.action == "read":
            self.values[choice.name] = choice.selected()
        elif self.action == "check":
            assert choice.selected() == self.expected[choice.name]

    def run(self, action):
        self.action = action
        self.process_number(screens.calibration.reference_weight)
        self.process_choice(screens.calibration.unit)
```

Neue Aktion: **auf Werkseinstellung setzen.**

---

## Schritt 1 · Zwei Dimensionen

| | read | check | reset (neu) |
|---|---|---|---|
| Zahlenfeld | ✓ | ✓ | neu |
| Auswahl | ✓ | ✓ | neu |

Eine neue Aktion: zwei Stellen. Ein neuer Typ: zwei Stellen, künftig drei.

---

## Schritt 2 · Trennen

```python
ACCESS = {
    NumberField: (lambda c: c.get(), lambda c, v: c.set(v)),
    ChoiceField: (lambda c: c.selected(), lambda c, v: c.select(v)),
}


def read(control):
    return ACCESS[type(control)][0](control)


def write(control, value):
    ACCESS[type(control)][1](control, value)


def check(control, expected):
    assert read(control) == expected[control.name]


def reset(control, factory):
    write(control, factory[control.name])


def for_each_calibration_parameter(task):
    task(screens.calibration.reference_weight)
    task(screens.calibration.unit)
```

Aufruf: `for_each_calibration_parameter(lambda c: reset(c, factory_values))`.

---

## Was dieses Beispiel zeigt

**Zwei Dimensionen, zwei Orte.** Zugriff je Typ in `ACCESS`, Aktionen als Funktionen.

**Der Weg kennt keine Aktion.** `for_each_calibration_parameter` nimmt irgendeine Funktion.

**Eine neue Aktion ist eine neue Funktion.** Keine bestehende Zeile ändert sich.
