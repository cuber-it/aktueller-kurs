# Übung · Wo landet diese Änderung?

Sie untersuchen einen Ausschnitt aus Ihrem Testframework: einen Testfall, den Helper, den er aufruft, ein Screen Object und die Control-Schicht darunter. Der Code funktioniert. Die Frage ist, welche Schicht welches Wissen trägt und wo eine bestimmte Änderung landen würde.

Bewertet wird in dieser Übung nichts. Es geht darum, die vorhandene Architektur sichtbar zu machen.

---

## Material A · Der Testfall

`suite_Machine_Settings/tst_1_9_TC_1009_gnss_diagnostics_sae_j1939/test.py` (gekürzt)

```python
def main():
    with test_wrapper(None, False):
        gnss_ref = read_gnss_diagnostics_reference("sae_j1939")

        simulation = Simulation_Helper()
        simulation.configure_gps_drive_via_isobus("gps_traces/Esch_6m.nmea", protocol=GpsProtocol.sae_j1939)

        open_gnss_source_submenu()
        tst = UIElementTest(masetth.submenu_gnss_source.sae_j1939_btn)
        tst.test(True, set_setting=True)

        masetth.submenu_gnss_source.back_btn.click_and_wait(masetth.submenu_traction_unit.traction_unit_title_txt)

        simulation.start_docker()

        open_gnss_diagnostics_submenu(snooze_time=8)
        assert_gnss_diagnostics_values(gnss_ref)

        masetth.submenu_gnss_diagnostics.back_btn.click_while_exists()
        close_machine_settings_menus()
```

---

## Material B · Zwei Helper

`helper/ui_test_modules/machine_settings_helper.py` (gekürzt)

```python
def open_gnss_source_submenu():
    """ Navigates from the status bar into the Tractor's sub menu "GNSS source"."""
    uih.statusbar.settings_action_btn.click_and_wait(setth.menu_settings.implement_btn)
    setth.menu_settings.implement_btn.click_and_wait(masetth.submenu_machinesettings.title_bar_title)
    masetth.submenu_machinesettings.open_settings_default_tractor()
    masetth.submenu_traction_unit.gnss_btn.set(True)
    masetth.submenu_traction_unit.gnss_gnss_source_btn.click_while_exists()


def open_gnss_diagnostics_submenu(snooze_time=7):
    """ Opens the sub menu "GNSS Diagnostics" and waits for the satellite parameter values to settle."""
    masetth.submenu_traction_unit.gnss_diagnostics_btn.click_and_wait(masetth.submenu_gnss_diagnostics.title_bar_title)
    squish.snooze(snooze_time)
```

---

## Material C · Screen Object und Control

`UI/machinesettings_ui.py` und `UI/controls.py` (gekürzt)

```python
class SubMenuGNSSSource(ListCtrlMixin):
    def __init__(self):
        super().__init__(container={"container": MACHINESETTINGS_APP, "id": "root", "type": "GNSSSourcePage",
                                    "visible": True}, dialog_name="Sub menu GNSS Source", options_enum=GnssSource,
                         surfaceItemId="surfaceItem", windowId=WINDOW_ID_MACHINESETTINGS_APP,
                         app_name=MACHINESETTINGS_APP_NAME)
        self.sae_j1939_btn = CheckDelegate(
            {"container": self.container, "objectName": "itemGnssSourceJ1939", "type": "CheckDelegate", "visible": True},
            f"{GnssSource.sae_j1939} (GPS source) Button", MACHINESETTINGS_APP_NAME)


helper = _GenericMachineSettingsUi()          # im Test importiert als masetth


class Control:
    def wait(self, fail_if_not_exists=True, timeout_msec=None, quiet=UI_ELEMENTS_QUIET_DEFAULT):
        timeout_msec = timeout_msec if timeout_msec else self.wait_timeout
        test_exec_helper.target.helper.switch_application_context(self.application_name)
        ret = None
        try:
            ret = squish.waitForObject(self.name, timeout_msec)
            ...
        except (LookupError, RuntimeError) as e:
            if fail_if_not_exists:
                fail_test(f"{self.display_name} did not become accessible within {timeout_msec} milliseconds.{self}",
                          exception=e)
        return ret
```

---

## Material D · Fünf Änderungen

| Nr. | Änderung |
|---|---|
| D1 | Die AUT benennt den Eintrag für SAE J1939 um: `objectName` wird `itemGnssSourceSaeJ1939`. |
| D2 | Die GNSS-Quelle wird künftig direkt im Menü Zugfahrzeug gewählt, das Untermenü entfällt. |
| D3 | Die Einstellungs-App läuft künftig in einem eigenen Prozess mit eigenem Anwendungsnamen. |
| D4 | Ein zweiter Target-Typ kommt hinzu: ein Terminal mit anderem Displayformat. |
| D5 | Für die GNSS-Diagnose soll statt 8 s Wartezeit auf die Anzahl sichtbarer Satelliten gewartet werden. |

---

## Aufgabe

### Teil 1 · Schichten zuordnen

**1.** Legen Sie eine Tabelle an: Welche Schichten erkennen Sie in Material A bis C? Nennen Sie für jede Schicht eine Datei oder Klasse und die Verantwortung in einem Satz.

**2.** Welches Wissen steckt im Testfall aus Material A, das nicht zur Testaussage gehört? Nennen Sie mindestens drei Stellen.

**3.** Welche Aufgaben erledigt `Control.wait()` außer dem Warten? Woran sieht ein Testfall, dass sie passieren?

### Teil 2 · Änderungen verfolgen

**4.** Tragen Sie für jede Änderung aus Material D ein, welche Dateien oder Klassen Sie anfassen müssten. Welche Änderung bleibt in einer Schicht, welche zieht durch mehrere?

**5.** Für D1: Wie viele Stellen im gesamten Framework kennen den Real Name des Eintrags? Wie würden Sie das prüfen?

**6.** Für D5: Wer kennt heute die Wartezeit von 8 s, und wer müsste die neue Bedingung kennen?

### Teil 3 · Einordnen

**7.** Welche Kopplungen in Material A bis C sind notwendig, weil ein GUI-Test von Squish und AUT abhängen muss? Welche könnten an einer anderen Stelle liegen?

**8.** Nennen Sie zwei Architekturentscheidungen aus dem Material, die Sie ausdrücklich beibehalten würden, und begründen Sie sie.

---

## Hinweise zur Bearbeitung

- Keine Verbesserungsvorschläge in Teil 1 und 2. Erst beschreiben, dann einordnen.
- Für Aufgabe 1 und 4 genügen Tabellen.
- Wenn Sie unsicher sind, wohin etwas gehört, fragen Sie: **Welche Änderung würde genau hier landen?**
