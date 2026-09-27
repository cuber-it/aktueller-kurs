"""2-2 · vorher · Ein Control wird für einen Listeneintrag umgebaut

Ausschnitt aus UI/controls.py und UI/machinesettings_ui.py (Testframework des Teams,
gekürzt). Nicht eigenständig lauffähig. deviating_text und deviating_container werden im
Bestand 23-mal aufgerufen.

Die Controls gehören zu Screen Objects, die als Modul-Singletons (masetth, setth, uih) von
allen Tests eines Laufs geteilt werden. deviating_name_value ändert den Real Name des
geteilten Controls und stellt ihn nach dem Block wieder her, ohne try/finally. Wirft der
Block, bleibt der geänderte Real Name stehen. Der nächste Aufruf merkt sich den falschen Wert
als "vorher" und stellt diesen wieder her.
"""
from contextlib import contextmanager


class Control:
    @contextmanager
    def deviating_name_value(self, key, value):
        cur_value = self.name.get(key, None)
        if value is None:
            self.name.pop(key, None)
        else:
            self.name[key] = value
        yield
        if cur_value is None:
            self.name.pop(key, None)
        else:
            self.name[key] = cur_value

    @contextmanager
    def deviating_text(self, text):
        with self.deviating_name_value("text", text):
            yield

    @contextmanager
    def deviating_container(self, container):
        if isinstance(container, Control):
            container = container.name
        with self.deviating_name_value("container", container):
            yield


class SubMenuMachineSettings(ListCtrlMixin):
    def open_implement_settings_by_text(self, text, quiet=UI_ELEMENTS_QUIET_DEFAULT):
        if not quiet:
            test.log(f"Opening settings of the implement named {text}")

        with self.menu_list.delegate.deviating_text(text):
            with self.implement_settings_btn.deviating_container(self.menu_list.delegate):
                self.implement_settings_btn.wait_for_exists()
                squish.snooze(MENU_ROLL_OUT_TIME)  # Give the menu Time to roll out all options
                self.implement_settings_btn.click(quiet=True)
