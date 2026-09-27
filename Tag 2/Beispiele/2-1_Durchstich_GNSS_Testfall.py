"""2-1 · Durchstich: eine Testzeile durch alle Schichten

Ausschnitte aus dem Testframework des Teams, gekürzt. Nicht eigenständig lauffähig.

Ausgangspunkt ist eine Zeile aus
suite_Machine_Settings/tst_1_9_TC_1009_gnss_diagnostics_sae_j1939/test.py:

    open_gnss_source_submenu()

Die Kommentare zeigen, in welcher Schicht der Code liegt und welche Verantwortung er trägt.
"""

# ── Schicht 1 · Testfall (test.py) ──────────────────────────────────────────────
# Verantwortung: Testablauf und Testaussage.
def main():
    with test_wrapper(None, False):                                   # Lifecycle, siehe Schicht 6
        open_gnss_source_submenu()                                     # → Schicht 2
        tst = UIElementTest(masetth.submenu_gnss_source.sae_j1939_btn)  # Verifikation, siehe Schicht 7
        tst.test(True, set_setting=True)


# ── Schicht 2 · Helper (helper/ui_test_modules/machine_settings_helper.py) ──────
# Verantwortung: ein wiederkehrender Weg durch mehrere Menüs, mit fachlichem Namen.
def open_gnss_source_submenu():
    """ Navigates from the status bar into the Tractor's sub menu "GNSS source"."""
    uih.statusbar.settings_action_btn.click_and_wait(setth.menu_settings.implement_btn)          # → Schicht 3
    setth.menu_settings.implement_btn.click_and_wait(masetth.submenu_machinesettings.title_bar_title)
    masetth.submenu_machinesettings.open_settings_default_tractor()
    masetth.submenu_traction_unit.gnss_btn.set(True)
    masetth.submenu_traction_unit.gnss_gnss_source_btn.click_while_exists()


# ── Schicht 3 · UI-Modul / Screen Object (UI/machinesettings_ui.py) ─────────────
# Verantwortung: Wissen über ein Menü, seine Controls und ihre Real Names.
class SubMenuGNSSSource(ListCtrlMixin):
    def __init__(self):
        super().__init__(container={"container": MACHINESETTINGS_APP, "id": "root", "type": "GNSSSourcePage",
                                    "visible": True}, dialog_name="Sub menu GNSS Source", options_enum=GnssSource,
                         surfaceItemId="surfaceItem", windowId=WINDOW_ID_MACHINESETTINGS_APP,
                         app_name=MACHINESETTINGS_APP_NAME)
        self.sae_j1939_btn = CheckDelegate(                             # → Schicht 4
            {"container": self.container, "objectName": "itemGnssSourceJ1939", "type": "CheckDelegate", "visible": True},
            f"{GnssSource.sae_j1939} (GPS source) Button", MACHINESETTINGS_APP_NAME)


helper = _GenericMachineSettingsUi()     # Modul-Singleton, im Test importiert als masetth


# ── Schicht 4 · Control (UI/controls.py) ────────────────────────────────────────
# Verantwortung: ein UI-Element bedienen, warten, lesen.
class Control:
    def click(self, quiet=UI_ELEMENTS_QUIET_DEFAULT):
        if not quiet:
            test.log(f"Clicking on {self.display_name}")
        squish.mouseClick(self.wait(quiet=True))                        # → Schicht 5

    def wait(self, fail_if_not_exists=True, timeout_msec=None, quiet=UI_ELEMENTS_QUIET_DEFAULT):
        timeout_msec = timeout_msec if timeout_msec else self.wait_timeout
        test_exec_helper.target.helper.switch_application_context(self.application_name)   # → Schicht 8
        ...
        return squish.waitForObject(self.name, timeout_msec)


# ── Schicht 5 · Squish API ──────────────────────────────────────────────────────
# waitForObject, mouseClick, object.exists, setApplicationContext, test.*
# Einziger Ort mit direktem Squish-Zugriff: kein Testfall im aktiven Bestand (983) ruft Squish selbst auf
# (abgesehen von squish.snooze).


# ── Schicht 6 · Lifecycle (init_cleanup_wrapper_helper/test_wrapper.py) ─────────
# Verantwortung: vor und nach jedem Test Zustand herstellen und aufräumen.
@contextmanager
def test_wrapper(test_set_name=None, replace_data=True, start_mockbackend=False, dev_data_set=None):
    ...


# ── Schicht 7 · Verifikation (ui_test_modules/base_ui_test.py) ──────────────────
# Verantwortung: Wert lesen, mit Erwartung vergleichen, Abweichung melden.
class UIElementTest:
    ...


# ── Schicht 8 · Target (target_helper/) ─────────────────────────────────────────
# Verantwortung: Gerät oder lokale Umgebung, Squish-Anwendungskontexte, Dateien auf dem Gerät.
class _TerminalTargetHelper(AbstractTargetHelper):
    ...
