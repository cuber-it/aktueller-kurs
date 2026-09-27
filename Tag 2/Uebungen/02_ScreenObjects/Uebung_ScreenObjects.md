# Übung · Was bietet ein Menü dem Test an?

Sie untersuchen, wie Testfälle heute durch die Maschineneinstellungen navigieren, und wie die Screen Objects dafür gebaut sind. Der Code funktioniert. Die Frage ist, welche Operationen ein Screen Object anbieten sollte und welches Wissen heute im Testfall steht.

---

## Material A · Navigation in Helper und Testfall

Aus `helper/ui_test_modules/machine_settings_helper.py` (gekürzt):

```python
def open_gnss_source_submenu():
    """ Navigates from the status bar into the Tractor's sub menu "GNSS source"."""
    uih.statusbar.settings_action_btn.click_and_wait(setth.menu_settings.implement_btn)
    setth.menu_settings.implement_btn.click_and_wait(masetth.submenu_machinesettings.title_bar_title)
    masetth.submenu_machinesettings.open_settings_default_tractor()
    masetth.submenu_traction_unit.gnss_btn.set(True)
    masetth.submenu_traction_unit.gnss_gnss_source_btn.click_while_exists()


def close_machine_settings_menus():
    """ Leaves the sub menus "Traction Unit" and Machine Settings, back to the main menu."""
    masetth.submenu_traction_unit.back_btn.click_and_wait(masetth.submenu_machinesettings.title_bar_title)
    masetth.submenu_machinesettings.back_btn.click_while_exists()
    setth.menu_settings.back_btn.click_while_exists()
```

Aus `suite_Machine_Settings/tst_gnss_diagnostics_sae_j1939/test.py` (gekürzt):

```python
masetth.submenu_gnss_source.back_btn.click_and_wait(masetth.submenu_traction_unit.traction_unit_title_txt)
```

---

## Material B · Das Screen Object

`UI/machinesettings_ui.py` (gekürzt)

```python
class SubMenuMachineSettings(ListCtrlMixin):
    def __init__(self):
        super().__init__(container={"container": MACHINESETTINGS_APP, "id": "root", "type": "MainPage",
                                    "unnamed": 1, "visible": True},
                         dialog_name="Sub menu Machine Settings", delegate_type="ItemDelegate",
                         delegate_class=Button, surfaceItemId="surfaceItem",
                         windowId=WINDOW_ID_MACHINESETTINGS_APP, app_name=MACHINESETTINGS_APP_NAME)
        self.title_bar_title = Control(
            {"container": self.container, "objectName": "mainPageTitle", "type": "ListViewTitle", "visible": True},
            "Implement Settings Title", MACHINESETTINGS_APP_NAME)
        self.implement_settings_btn = Button(
            {"container": self.container, "objectName": "image",
             "source": "image://icons/0491_ImplementSettings_settings", "type": "IconImage", "visible": True},
            "Device Settings Button", MACHINESETTINGS_APP_NAME)
        self.tractor_settings_btn = Button(
            {"container": self.container, "objectName": "image",
             "source": "image://icons/0492_TractorSettings_settings", "type": "IconImage", "visible": True},
            "Tractor Settings Button", MACHINESETTINGS_APP_NAME)

    def open_implement_settings_by_text(self, text, quiet=UI_ELEMENTS_QUIET_DEFAULT):
        if not quiet:
            test.log(f"Opening settings of the implement named {text}")
        with self.menu_list.delegate.deviating_text(text):
            with self.implement_settings_btn.deviating_container(self.menu_list.delegate):
                self.implement_settings_btn.wait_for_exists()
                squish.snooze(MENU_ROLL_OUT_TIME)
                self.implement_settings_btn.click(quiet=True)

    def open_settings_default_tractor(self, quiet=UI_ELEMENTS_QUIET_DEFAULT):
        if not quiet:
            test.log("Opening settings of the default Tractor")
        default_tractor_name = "Tractor"
        with self.menu_list.delegate.deviating_text(default_tractor_name):
            with self.tractor_settings_btn.deviating_container(self.menu_list.delegate):
                self.tractor_settings_btn.wait_for_exists()
                squish.snooze(MENU_ROLL_OUT_TIME)
                self.tractor_settings_btn.click(quiet=True)
```

---

## Material C · Zahlen aus dem Bestand

| Was | Anzahl |
|---|---:|
| `squish.snooze` direkt nach einem Klick im aktiven Code | 6 (die eigene Regel ist weitgehend umgesetzt) |
| `back_btn.click_and_wait(<Objekt des Zielmenüs>)` in Tests und Helpern | 58 |
| `deviating_text` / `deviating_container` | 23 |
| Testfälle mit eigenen Real Names | 2 |

Die eigene Regel des Teams (`references/code_patterns.md`): „After a navigation click → never snooze.“

---

## Aufgabe

### Teil 1 · Was ist schon da?

**1.** Welche Ideen des Page-Object-Patterns setzt `SubMenuMachineSettings` bereits um? Welche nicht? Legen Sie eine Tabelle an.

**2.** Welches Wissen über Menüwege steht in Helper und Testfall aus Material A, das ein Screen Object tragen könnte? Nennen Sie für jede Stelle das Screen Object, in das es gehören würde.

**3.** `open_implement_settings_by_text` und `open_settings_default_tractor` sind fast gleich. Was unterscheidet sie? Wie ließen sie sich zusammenführen?

### Teil 2 · Operationen entwerfen

**4.** Entwerfen Sie für `SubMenuGNSSSource` eine Methode `go_back()`. Was klickt sie, worauf wartet sie, was gibt sie zurück? Wie sieht die Zeile aus Material A danach aus?

**5.** `close_machine_settings_menus` kennt drei Menüs und ihre Reihenfolge. Wie sähe die Funktion mit `go_back()`-Methoden der Screen Objects aus? Was ändert sich, wenn ein Menü dazwischen kommt?

**6.** `deviating_text` ändert den Real Name des geteilten Controls. Was passiert, wenn innerhalb des `with`-Blocks eine Exception auftritt? Entwerfen Sie eine Alternative, die kein geteiltes Control verändert.

### Teil 3 · Abwägen

**7.** Sollte `go_back()` auch prüfen, dass das Zielmenü erschienen ist? Was spricht dafür, was dagegen?

**8.** Die Folie zur Einheit sagt: „Page Object ist nicht Object Map.“ Im Framework gibt es keine Object Map, die UI-Module enthalten die Real Names. Ist das ein Problem? Begründen Sie mit einer konkreten Änderung.

---

## Hinweise zur Bearbeitung

- Der Code muss nicht ausgeführt werden.
- Verwenden Sie, wo möglich, die vorhandenen Methoden der Controls (`click_and_wait`, `click_while_exists`, `wait_for_exists`).
- Wenn Sie unsicher sind, ob eine Operation ins Screen Object gehört, fragen Sie: **Muss der Test das wissen, oder das Menü?**
