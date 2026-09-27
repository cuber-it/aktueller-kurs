# Lösungsvorschlag · Wo landet jeder Schritt?

**Vorbemerkung:** Ein Vorschlag, keine Musterlösung. Bewertet wird, ob **jede Zeile einem vorhandenen Aufruf oder einer benannten Lücke** zugeordnet ist und **kein Name geraten** wird.

---

## 1 · Abbildung

| Zeile | Aufruf |
|---|---|
| Given nur Standardtraktor | Datensatz über `test_wrapper(replace_data=True)` (Standard) |
| When neuen Traktor anlegen | Weg: Statusleiste → Geräte → Zugfahrzeug; Anlegen: **fehlt** |
| Then Liste enthält beide | Geräteliste in `SubMenuMachineSettings.menu_list` (ein `ListCtrl`, dort sucht auch `open_settings_default_tractor()` den Eintrag „Tractor“): `UIElementTest(… .get_delegate_by_text(name)).test_existence(True)` |
| And ausgewählt | **offen:** Die Einträge sind `Button`-Controls, `get()` liefert den Text. Woran „ausgewählt“ sichtbar ist (Eigenschaft, Symbol), zeigt erst ein Spy-Dump |

---

## 2 · Given

`test_wrapper` ersetzt den Datensatz vor jedem Test (`replace_data=True` ist Standard). Ob der Standarddatensatz nur „Tractor“ enthält, ist mit dem Team zu klären; die Datensätze liegen unter `data/backups/`.

---

## 3 · Was der Agent darf

| darf | darf nicht |
|---|---|
| im Framework suchen (Übersicht, Quellcode) | einen Namen nach Muster bilden |
| nach Rückfrage einen Spy-Dump machen | ohne Rückfrage spähen |
| `# TODO: [helper-missing]` setzen und fragen | das Element im Test überbrücken |
| nach Bestätigung den Button im UI-Modul ergänzen | ohne Bestätigung Framework-Dateien ändern |

---

## 4 · Der fehlende Button

Ort: `UI/machinesettings_ui.py`, im Screen Object des Menüs, in dem der Eintrag „Neuen Traktor hinzufügen“ erscheint. Form nach Muster von `add_new_implement_btn`, aber `objectName` und `type` aus einem Spy-Dump oder dem QML-Quellcode:

```python
self.add_new_tractor_btn = Button(
    {"container": self.container, "objectName": "<aus Spy-Dump>", "type": "<aus Spy-Dump>", "visible": True},
    "Add New Tractor Button", MACHINESETTINGS_APP_NAME)
```

---

## 5 · Prüfung mit Routing

```python
UIElementTest(masetth.submenu_any_implement.menu_list.get_delegate_by_text(option_text_front)).test(True)
```

Statt `if … get_by_text(…): test.passes(…) else: test.fail(…)`. Meldung und Log-Abschnitt kommen aus `UIElementTest`.

---

## 6 · Dünne Step-Funktionen

```python
@When("I add a new tractor named |any|")
def step(context, name):
    open_traction_unit()      # neu anzulegen: Weg ins Menü Zugfahrzeug, als Funktion in machine_settings_helper.py (Schritt 4b)
    # TODO: [helper-missing] add-new-tractor button - spy run pending
    masetth.submenu_traction_unit.add_new_tractor_btn.click_with_entry(name)


@Then("the tractor list contains |any|")
def step(context, name):
    UIElementTest(masetth.submenu_machinesettings.menu_list.get_delegate_by_text(name)).test_existence(True)


@Step("|any| is selected")
def step(context, name):
    # TODO: [object-map] how "selected" shows on a device entry - spy run pending
    ...
```

Der Code, der heute in `test.py` stünde, steht in Helpern und Screen Objects. Drei Dinge sind offen: `open_traction_unit()` gibt es noch nicht, der Button zum Anlegen fehlt, und woran „ausgewählt“ auf einem Geräteeintrag sichtbar ist, weiß erst ein Spy-Dump. `SubMenuTractionUnit` ist übrigens die Einstellungsseite eines einzelnen Traktors, keine Liste; die Liste steckt in `SubMenuMachineSettings`. Alle drei Punkte gehören vor der Umsetzung geklärt, nicht geraten.

---

## 7 · Step Definitions und Routing-Tabelle

Sie würden sie ergänzen, nicht ersetzen: Die Routing-Tabelle entscheidet, welcher Aufruf in eine Step-Funktion gehört. Ohne ausführbare Szenarien ist die Schicht verzichtbar; der Skill schreibt `test.py` direkt.

---

## Diskussionsanschluss

Wie viele `[helper-missing]`-Markierungen hat Ihr Skill schon erzeugt, und wer arbeitet sie ab?
