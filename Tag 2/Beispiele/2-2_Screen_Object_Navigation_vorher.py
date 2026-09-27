"""2-2 · vorher · Helper und Tests kennen die Wege zwischen den Menüs

Ausschnitte aus helper/ui_test_modules/machine_settings_helper.py und
suite_Machine_Settings/tst_gnss_diagnostics_sae_j1939/test.py (Testframework des Teams,
gekürzt). Nicht eigenständig lauffähig.

Die Screen Objects beschreiben Menüs und ihre Controls. Wohin ein Zurück-Button führt und
in welcher Reihenfolge Menüs geschlossen werden, steht in Helpern und Testfällen: 58-mal
back_btn.click_and_wait(<Objekt des Zielmenüs>). Ändert sich das Ziel eines Zurück-Buttons,
ändern sich alle Stellen, die es kennen.

Die Snooze-Regel des Teams ist dabei eingehalten: gewartet wird auf ein Objekt, nicht auf Zeit.
"""
from UI.generic_ui import helper as uih
from UI.machinesettings_ui import helper as masetth
from UI.terminalui_settings import helper as setth


# ── helper/ui_test_modules/machine_settings_helper.py ─────────────────────────
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


# ── Testfall ────────────────────────────────────────────────────────────────────
def main():
    open_gnss_source_submenu()
    masetth.submenu_gnss_source.sae_j1939_btn.set(True)
    masetth.submenu_gnss_source.back_btn.click_and_wait(masetth.submenu_traction_unit.traction_unit_title_txt)
    # …
    close_machine_settings_menus()
