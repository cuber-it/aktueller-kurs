# Übung · Wer tut hier was?

Sie untersuchen eine Klasse, die alle Parameter der Maschineneinstellungen ausliest, vergleicht oder setzt. Sie funktioniert. Die Frage ist, welche Verantwortungen in ihr stecken und wie sie sich trennen ließen.

---

## Material A · Die Klasse

`helper/ui_test_modules/machine_settings_helper.py`, Klasse `MachineSettingsParameterTests` (gekürzt)

```python
class MachineSettingsParameterTests:
    """ This class offers functions for testing the parameters of Machine Settings. """

    def __init__(self):
        self.action = None
        self.reference_value_dict = None
        self.names = ""
        self.default_values = ""

    def process_text_field_delegate(self, gui_element):
        if self.action == TestAction.readout_and_dump:
            str_text = gui_element.get()
            self.names += ";" + gui_element.display_name
            self.default_values += ";" + str_text
        elif self.action == TestAction.compare_with_ref:
            reference = append_missing_zeros(self.reference_value_dict[gui_element.display_name],
                                             self.resolution_dict[gui_element.display_name])
            str_text = gui_element.get()
            if str_text == reference:
                test.passes(f"Read out {gui_element.display_name} : {str_text}, OK")
            else:
                test.fail(f"Element {gui_element.display_name} current value : {str_text}, reference : {reference}")
        elif self.action == TestAction.set_to_ref:
            reference = self.reference_value_dict[gui_element.display_name]
            if reference == "Off":
                reference = "0.00"
            gui_element.wait_for_exists()
            squish.snooze(MENU_ROLL_OUT_TIME)
            gui_element.set(reference)

    def process_check_delegate(self, gui_element):
        gui_element.wait_for_exists()
        checked_state = gui_element.get_state()
        if self.action == TestAction.readout_and_dump:
            self.names += ";" + gui_element.display_name
            self.default_values += ";" + str(checked_state)
        elif self.action == TestAction.compare_with_ref:
            ...
        elif self.action == TestAction.set_to_ref:
            if str(checked_state) != self.reference_value_dict[gui_element.display_name]:
                gui_element.switch_state()
        return checked_state

    # … process_item_delegate_with_value, process_item_delegate_with_value_toggle, process_switch_delegate

    def iterate_through_implement_settings(self, implement_name, action, reference_file, row):
        self.action = action
        self.handle_reference_file()
        uih.statusbar.settings_action_btn.click_and_wait(setth.menu_settings.implement_btn)
        setth.menu_settings.implement_btn.click_and_wait(masetth.submenu_machinesettings.title_bar_title)
        with log_section("General"):
            masetth.submenu_machinesettings.open_implement_settings_by_text(implement_name)
            masetth.submenu_implement.general_btn.set(True)
            self.process_text_field_delegate(masetth.submenu_implement.general_manufacturer_btn)
            masetth.submenu_implement.general_btn.set(False)
        # … Geometry, … für alle Untermenüs
```

---

## Material B · Eine angekündigte Änderung

Die Applikationstechnik möchte eine vierte Aktion: **Jeden Parameter auf seinen Werkswert zurücksetzen.** Die Werkswerte stehen in einer eigenen CSV-Datei.

---

## Aufgabe

### Teil 1 · Verantwortungen

**1.** Welche Verantwortungen stecken in `MachineSettingsParameterTests`? Nennen Sie für jede einen Änderungsgrund.

**2.** Die Klasse hat zwei Dimensionen: Aktionen und Control-Typen. Legen Sie eine Tabelle an. Wie viele Stellen müssen Sie für die Aktion aus Material B ändern? Wie viele für einen neuen Control-Typ?

**3.** Was ist hier Task, was Workflow, was Orakel? Ordnen Sie Methoden und Zweige zu.

### Teil 2 · Trennen

**4.** Entwerfen Sie je Control-Typ einen Zugriff: wie ein Wert gelesen und gesetzt wird. Wo liegt er?

**5.** Entwerfen Sie die drei vorhandenen Aktionen als Tasks, die einen Parameter bearbeiten.

**6.** Entwerfen Sie den Workflow, der durch die Menüs eines Geräts geht und einen Task auf jeden Parameter anwendet.

**7.** Wie viele Stellen ändern Sie jetzt für die Aktion aus Material B?

### Teil 3 · Abwägen

**8.** Der Zustand wird heute als Text in Attributen gesammelt (`self.names += ";" + …`). Was spricht dagegen, was dafür? Was würden Sie stattdessen sammeln?

**9.** Lohnt sich der Umbau jetzt, oder erst mit der vierten Aktion? Begründen Sie.

---

## Hinweise zur Bearbeitung

- Der Code muss nicht ausgeführt werden.
- Die Controls (`TextFieldDelegate`, `CheckDelegate`, …) bleiben unverändert.
- Wenn Sie unsicher sind, fragen Sie: **Welche Änderung trifft diese Stelle, und trifft sie auch die anderen?**
