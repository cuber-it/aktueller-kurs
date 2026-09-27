# Lösungsvorschlag · Was erzählt dieser Test?

**Vorbemerkung:** Ein Vorschlag, keine Musterlösung. Bewertet wird, ob **die Aussage des Tests sichtbar** ist und ob **fachliche Operationen Absichten benennen**.

---

## 1 · Ebenen

| Zeile | Ebene |
|---|---|
| `test_wrapper(None, False)` | Infrastruktur |
| `read_gnss_diagnostics_reference("sae_j1939")` | Testdaten |
| `Simulation_Helper()`, `configure_gps_drive_via_isobus(…)` | Infrastruktur |
| `open_gnss_source_submenu()` | Navigation |
| `UIElementTest(…sae_j1939_btn).test(True, set_setting=True)` | UI-Bedienung und Prüfung |
| `back_btn.click_and_wait(…traction_unit_title_txt)` | Navigation |
| `simulation.start_docker()` | Infrastruktur |
| `open_gnss_diagnostics_submenu(snooze_time=8)` | Navigation mit Wartezeit |
| `assert_gnss_diagnostics_values(gnss_ref)` | Prüfung |
| `bug_workaround(…)` | Infrastruktur (Protokoll) |
| `back_btn.click_while_exists()`, `close_machine_settings_menus()` | Navigation |

---

## 2 · Was die Fachabteilung lesen muss

Quelle wählen, Fahrt simulieren, Diagnose prüfen. Alles andere ist Bedienung oder Infrastruktur.

---

## 3 · `test_wrapper(None, False)`

`test_set_name=None, replace_data=False`: kein eigener Name, Datensatz nicht ersetzen. Lesbarer: `test_wrapper(replace_data=False)`.

---

## 4 · `select_gnss_source`

```python
_SOURCE_BUTTONS = {
    GnssSource.nmea_2000: lambda: masetth.submenu_gnss_source.nmea_2000_btn,
    GnssSource.sae_j1939: lambda: masetth.submenu_gnss_source.sae_j1939_btn,
    GnssSource.rs232_nmea_0183: lambda: masetth.submenu_gnss_source.rs232_nmea_0183_btn,
}


def select_gnss_source(source: GnssSource) -> None:
    """Wählt im Traktor die GNSS-Quelle und kehrt ins Menü Zugfahrzeug zurück."""
    open_gnss_source_submenu()
    _SOURCE_BUTTONS[source]().set(True)
    masetth.submenu_gnss_source.back_btn.click_and_wait(masetth.submenu_traction_unit.traction_unit_title_txt)
```

Hinein wandern: Navigation hin, Auswahl, Navigation zurück. Im Test bleiben: welche Quelle, und die Prüfung.

---

## 5 · Prüfen in `select_gnss_source`?

Vorschlag: nicht. Die Einstellung ist Aktion. Ob sie angekommen ist, prüft der Test:

```python
assert_selected_gnss_source(GnssSource.sae_j1939)
```

Das hält die Prüfung sichtbar und erlaubt Tests, die bewusst eine ungültige Auswahl versuchen.

---

## 6 · `main()` neu

```python
def main():
    with test_wrapper(replace_data=False):
        reference = read_gnss_diagnostics_reference("sae_j1939")

        simulation = Simulation_Helper()
        simulation.configure_gps_drive_via_isobus("gps_traces/Esch_6m.nmea", protocol=GpsProtocol.sae_j1939)

        select_gnss_source(GnssSource.sae_j1939)
        assert_selected_gnss_source(GnssSource.sae_j1939)

        simulation.start_docker()

        show_gnss_diagnostics()
        assert_gnss_diagnostics_values(reference)
        leave_gnss_diagnostics()
```

---

## 7 · Die drei Aussagen

| Aussage | Stellungnahme |
|---|---|
| „Wir haben schon eine fachliche API“ | für Wege und Prüfungen ja, für Einstellungen nein |
| „Fluent API am lesbarsten“ | liest sich gut, aber wo ist der Zustand nach `.select()`? Welche Methode meldet einen Fehler? Für 14 Tests mehr Konzept als Nutzen |
| „Ich will sehen, was geklickt wird“ | im Test nicht nötig, in der Fehlermeldung schon (AK5) |

---

## 8 · Direkter Control-Zugriff

Wenn die Bedienung selbst die Aussage ist, etwa „Der Button SAE J1939 ist ausgegraut, solange keine ISOBUS-Verbindung besteht“. Dann ist das Control der Prüfgegenstand.

---

## 9 · `snooze_time=8`

In `show_gnss_diagnostics()`, begründet mit „Satellitenwerte eingependelt“. Besser noch ein Warten auf einen Zustand im Diagnosemenü, sofern er abfragbar ist.

---

## Diskussionsanschluss

Wer im Team entscheidet, welche Begriffe eine fachliche Operation verwendet: die Testautomatisierung oder die Applikationstechnik?
