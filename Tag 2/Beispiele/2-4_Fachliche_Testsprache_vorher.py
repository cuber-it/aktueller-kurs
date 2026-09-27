"""2-4 · vorher · Ein Test auf drei Ebenen

suite_Machine_Settings/tst_1_9_TC_1009_gnss_diagnostics_sae_j1939/test.py (Testframework des
Teams, gekürzt). Nicht eigenständig lauffähig.

Der Test wechselt zwischen fachlichen Helpern (open_gnss_source_submenu), Controls über Screen
Objects (masetth.submenu_gnss_source.sae_j1939_btn) und Navigation mit Wissen über das
Zielmenü (traction_unit_title_txt). Die Positionsargumente von test_wrapper bedeuten
test_set_name=None, replace_data=False.
"""
from UI.machinesettings_ui import helper as masetth
from general.squish_helper import bug_workaround
from init_cleanup_wrapper_helper.test_wrapper import test_wrapper
from simulation_helper.simulation_helper import Simulation_Helper, GpsProtocol
from ui_test_modules.base_ui_test import UIElementTest
from ui_test_modules.machine_settings_helper import (
    assert_gnss_diagnostics_values, close_machine_settings_menus, open_gnss_diagnostics_submenu,
    open_gnss_source_submenu, read_gnss_diagnostics_reference)


def main():
    with test_wrapper(None, False):
        gnss_ref = read_gnss_diagnostics_reference("sae_j1939")

        simulation = Simulation_Helper()
        nmea_path = "gps_traces/Esch_6m.nmea"
        simulation.configure_gps_drive_via_isobus(nmea_path, protocol=GpsProtocol.sae_j1939)

        open_gnss_source_submenu()
        tst = UIElementTest(masetth.submenu_gnss_source.sae_j1939_btn)
        tst.test(True, set_setting=True)

        masetth.submenu_gnss_source.back_btn.click_and_wait(masetth.submenu_traction_unit.traction_unit_title_txt)

        simulation.start_docker()

        open_gnss_diagnostics_submenu(snooze_time=8)
        assert_gnss_diagnostics_values(gnss_ref)
        with bug_workaround("BUG-1001 - [Implement Settings:] display issues in menu Diagnostics"):
            pass

        masetth.submenu_gnss_diagnostics.back_btn.click_while_exists()
        close_machine_settings_menus()
