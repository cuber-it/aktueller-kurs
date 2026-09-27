"""2-5 · vorher · Eine Klasse, drei Abläufe, per Schalter gewählt

Ausschnitt aus helper/ui_test_modules/machine_settings_helper.py, Klasse
MachineSettingsParameterTests (Testframework des Teams, gekürzt). Nicht eigenständig lauffähig.

Jede Methode process_<Control-Typ> verzweigt nach self.action in drei Abläufe:
auslesen und sammeln, mit Referenz vergleichen, auf Referenz setzen. Es gibt fünf solcher
Methoden (TextFieldDelegate, ItemDelegateWithValue, …Toggle, CheckDelegate, SwitchDelegate).
Der Weg durch die Menüs (iterate_through_implement_settings) ruft sie auf. Zustand wird als
Text in Attributen gesammelt.
"""


class MachineSettingsParameterTests:
    def __init__(self):
        self.action = None
        self.reference_value_dict = None
        self.names = ""
        self.default_values = ""

    def process_text_field_delegate(self, gui_element):
        if self.action == TestAction.readout_and_dump:
            str_text = gui_element.get()
            test.log(f"Logging {gui_element.display_name} : {str_text}")
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
        else:
            test.log(f"Action {self.action} unknown for text_field_delegate!!!")

    def process_check_delegate(self, gui_element):
        gui_element.wait_for_exists()
        checked_state = gui_element.get_state()
        if self.action == TestAction.readout_and_dump:
            self.names += ";" + gui_element.display_name
            self.default_values += ";" + str(checked_state)
        elif self.action == TestAction.compare_with_ref:
            if str(checked_state) == self.reference_value_dict[gui_element.display_name]:
                test.passes(f"Read out {gui_element.display_name} : {checked_state}, OK")
            else:
                test.fail(f"Element {gui_element.display_name} current value : {checked_state}, "
                          f"reference : {self.reference_value_dict[gui_element.display_name]}")
        elif self.action == TestAction.set_to_ref:
            if str(checked_state) != self.reference_value_dict[gui_element.display_name]:
                gui_element.switch_state()
                checked_state = gui_element.get_state()
        else:
            test.log(f"Action {self.action} unknown for check_delegate!!!")
        return checked_state

    # … process_item_delegate_with_value, …_toggle, process_switch_delegate nach demselben Muster

    def iterate_through_implement_settings(self, implement_name, action, reference_file, row):
        self.action = action
        # … Navigation durch General, Geometry, … und je Parameter:
        self.process_text_field_delegate(masetth.submenu_implement.general_manufacturer_btn)
