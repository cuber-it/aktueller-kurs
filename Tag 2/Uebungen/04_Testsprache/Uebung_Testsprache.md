# Übung · Was erzählt dieser Test?

Sie untersuchen einen Testfall für die GNSS-Diagnose. Er funktioniert. Die Frage ist, ob ein Leser aus dem Test erkennt, was geprüft wird, und welche Zeilen stattdessen erzählen, wie das Terminal bedient wird.

---

## Material A · Der Testfall

`suite_Machine_Settings/tst_gnss_diagnostics_sae_j1939/test.py` (gekürzt)

```python
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
```

---

## Material B · Vorhandene Helper

`helper/ui_test_modules/machine_settings_helper.py` (gekürzt)

```python
def open_gnss_source_submenu():
    """ Navigates from the status bar into the Tractor's sub menu "GNSS source"."""
    ...

def open_gnss_diagnostics_submenu(snooze_time=7):
    """ Opens the sub menu "GNSS Diagnostics" and waits for the satellite parameter values to settle."""
    ...

def assert_gnss_diagnostics_values(gnss_ref):
    """ Checks the displayed values in sub menu "GNSS Diagnostics" against the given reference row."""
    ...

def close_machine_settings_menus():
    """ Leaves the sub menus "Traction Unit" and Machine Settings, back to the main menu."""
    ...
```

Signatur des Wrappers: `test_wrapper(test_set_name=None, replace_data=True, start_mockbackend=False, dev_data_set=None)`

Vorhandenes Enum in `machines_helper/machines_dtos.py`:

```python
class GnssSource(str, Enum):
    nmea_2000 = "NMEA 2000"
    sae_j1939 = "SAE J1939"
    rs232_nmea_0183 = "RS232 - serial"
    # … weitere Einträge
```

---

## Material C · Drei Aussagen aus dem Team

> „Wir haben doch schon eine fachliche API. Die Helper heißen `open_gnss_source_submenu` und `assert_gnss_diagnostics_values`.“

> „Eine Fluent API wäre am lesbarsten: `terminal.gnss().source(J1939).select().diagnostics().verify(ref)`.“

> „Je mehr wir verstecken, desto schwerer finden wir Fehler. Ich will im Test sehen, was geklickt wird.“

---

## Aufgabe

### Teil 1 · Ebenen erkennen

**1.** Ordnen Sie jede Zeile von `main()` einer Ebene zu: fachliche Absicht, UI-Bedienung über Screen Objects, Navigation, Infrastruktur, Prüfung.

**2.** Welche Zeilen müsste ein Leser aus der Fachabteilung verstehen, um den Test zu beurteilen? Welche nicht?

**3.** Was bedeutet `test_wrapper(None, False)`? Wie könnte der Aufruf lesbarer werden, ohne die Signatur zu ändern?

### Teil 2 · Fachliche Operationen entwerfen

**4.** Entwerfen Sie `select_gnss_source(source: GnssSource)`. Welche Zeilen aus `main()` wandern hinein? Was bleibt im Test?

**5.** Sollte `select_gnss_source` prüfen, dass die Quelle gewählt ist? Wenn ja: Wie bleibt im Test sichtbar, dass geprüft wird?

**6.** Schreiben Sie `main()` mit Ihren Operationen neu.

### Teil 3 · Abwägen

**7.** Nehmen Sie Stellung zu den drei Aussagen aus Material C.

**8.** Wo ist direkter Zugriff auf ein Control im Test besser als eine fachliche Operation? Nennen Sie ein Kriterium.

**9.** `snooze_time=8` steht im Test. Wohin gehört diese Information in Ihrem Entwurf?

---

## Hinweise zur Bearbeitung

- Der Code muss nicht ausgeführt werden.
- Verwenden Sie vorhandene Helper, Screen Objects und das Enum `GnssSource`.
- Wenn Sie unsicher sind, fragen Sie: **Welche Information verschwindet, und ist genau diese für den Test wichtig?**
