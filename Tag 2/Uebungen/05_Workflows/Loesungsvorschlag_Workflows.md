# Lösungsvorschlag · Wer tut hier was?

**Vorbemerkung:** Ein Vorschlag, keine Musterlösung. Bewertet wird, ob **jede Änderungsrichtung einen Ort** hat.

---

## 1 · Verantwortungen

| Verantwortung | Änderungsgrund |
|---|---|
| Weg durch die Menüs eines Geräts | neues Untermenü, geänderte Reihenfolge |
| Zugriff je Control-Typ | neuer Control-Typ, anderes Lesen |
| Aktion: auslesen | anderes Ausgabeformat |
| Aktion: vergleichen | andere Vergleichsregel (Nullen, „Off“) |
| Aktion: setzen | anderes Setzverhalten |
| Referenzdatei lesen | anderes Dateiformat |
| Ergebnisse sammeln | anderer Bericht |

---

## 2 · Zwei Dimensionen

| | auslesen | vergleichen | setzen | Werkswerte (neu) |
|---|---|---|---|---|
| TextFieldDelegate | ✓ | ✓ | ✓ | neu |
| ItemDelegateWithValue | ✓ | ✓ | ✓ | neu |
| …Toggle | ✓ | ✓ | ✓ | neu |
| CheckDelegate | ✓ | ✓ | ✓ | neu |
| SwitchDelegate | ✓ | ✓ | ✓ | neu |

Neue Aktion: 5 Stellen. Neuer Control-Typ: eine Methode mit 3 Zweigen.

---

## 3 · Task, Workflow, Orakel

| Teil | Art |
|---|---|
| `iterate_through_implement_settings` | Workflow |
| Zweig „vergleichen“ | Task mit Orakel |
| Zweige „auslesen“, „setzen“ | Tasks |
| Lesen/Setzen je Typ innerhalb der Zweige | technischer Helper |

---

## 4 · Zugriff je Control-Typ

```python
@dataclass(frozen=True)
class ParameterAccess:
    read: Callable[["Control"], str]
    write: Callable[["Control", str], None]


def _write_check(control, value):
    if control.get_state() != value.upper():
        control.switch_state()


ACCESS: Dict[type, ParameterAccess] = {
    TextFieldDelegate: ParameterAccess(read=lambda c: c.get(), write=lambda c, v: c.set(v)),
    CheckDelegate: ParameterAccess(read=lambda c: c.get_state(), write=_write_check),
    SwitchDelegate: ParameterAccess(read=lambda c: c.get_state(), write=_write_check),
}
```

Ort: neben den Controls, etwa `ui_test_modules/parameter_access.py`.

---

## 5 · Tasks

```python
def read_parameter(control, readings):
    readings[control.display_name] = ACCESS[type(control)].read(control)


def compare_parameter(control, reference):
    expected = reference[control.display_name]
    actual = ACCESS[type(control)].read(control)
    if actual == expected:
        test.passes(f"{control.display_name}: {actual}")
    else:
        test.fail(f"{control.display_name}: expected {expected}, found {actual}")


def set_parameter(control, reference):
    ACCESS[type(control)].write(control, reference[control.display_name])
```

---

## 6 · Workflow

```python
def for_each_implement_parameter(implement_name, task):
    masetth.submenu_machinesettings.open_implement_settings_by_text(implement_name)
    with log_section("General"):
        masetth.submenu_implement.general_btn.set(True)
        masetth.submenu_implement.enforceFocus()
        task(masetth.submenu_implement.general_manufacturer_btn)
        masetth.submenu_implement.general_btn.set(False)
    # … weitere Untermenüs
```

`enforceFocus()` läuft immer. Braucht nur das Setzen den Fokus, kostet der Aufruf beim Lesen wenig und macht den Weg unabhängig von der Aktion.

---

## 7 · Die vierte Aktion

```python
factory = read_reference_csv("factory_values.csv")
for_each_implement_parameter("Sprayer 24m", lambda c: set_parameter(c, factory))
```

Keine neue Funktion nötig: Werkswerte zu setzen ist `set_parameter` mit anderer Referenz. Null Stellen im Bestand ändern sich.

---

## 8 · Zustand als Text

Dagegen: Für Bericht und Vergleich muss der Text wieder zerlegt werden, ein Semikolon im Namen zerstört die Spalten. Dafür: das CSV-Format ist sofort da. Stattdessen ein Dictionary `{display_name: value}`, das CSV entsteht beim Schreiben.

---

## 9 · Jetzt oder später?

Mit der vierten Aktion. Dann zeigt der Umbau seinen Nutzen an einer konkreten Änderung, und die drei vorhandenen Aktionen lassen sich gegen die alte Klasse prüfen.

---

## Diskussionsanschluss

Welche andere Klasse in Ihrem Framework wächst in zwei Richtungen zugleich?
