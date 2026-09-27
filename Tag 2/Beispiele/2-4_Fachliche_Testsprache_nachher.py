"""2-4 · nachher · Der Test spricht in Begriffen der Maschineneinstellungen

Eine mögliche Richtung. Ausschnitt, nicht eigenständig lauffähig.

Eine Facade (gnss_settings.py) fasst zusammen, was der Test über GNSS-Einstellungen wissen
muss. Sie verwendet die vorhandenen Screen Objects, Controls und Helper. Der Test enthält
keine Controls und keine Menüwege mehr. GnssSource gibt es bereits in
machines_helper/machines_dtos.py.

Die Facade verbirgt Wege und Controls, nicht die Prüfung: Die Assertion bleibt im Test
sichtbar (assert_gnss_diagnostics_values).
"""
from machines_helper.machines_dtos import GnssSource


# ── gnss_settings.py (neu, im Helper-Paket) ─────────────────────────────────────
_SOURCE_BUTTONS = {
    GnssSource.nmea_2000: lambda: masetth.submenu_gnss_source.nmea_2000_btn,
    GnssSource.sae_j1939: lambda: masetth.submenu_gnss_source.sae_j1939_btn,
    GnssSource.rs232_nmea_0183: lambda: masetth.submenu_gnss_source.rs232_nmea_0183_btn,
}


def select_gnss_source(source: GnssSource) -> None:
    """Wählt im Traktor die GNSS-Quelle und kehrt in das Menü Zugfahrzeug zurück."""
    open_gnss_source_submenu()
    button = _SOURCE_BUTTONS[source]()
    button.set(True)
    UIElementTest(button).test(True)
    masetth.submenu_gnss_source.back_btn.click_and_wait(masetth.submenu_traction_unit.traction_unit_title_txt)


def show_gnss_diagnostics() -> None:
    """Öffnet die GNSS-Diagnose und wartet, bis sich die Satellitenwerte eingependelt haben."""
    open_gnss_diagnostics_submenu(snooze_time=8)


def leave_gnss_diagnostics() -> None:
    masetth.submenu_gnss_diagnostics.back_btn.click_while_exists()
    close_machine_settings_menus()


# ── Testfall ────────────────────────────────────────────────────────────────────
def main():
    with test_wrapper(replace_data=False):
        reference = read_gnss_diagnostics_reference("sae_j1939")

        simulation = Simulation_Helper()
        simulation.configure_gps_drive_via_isobus("gps_traces/Esch_6m.nmea", protocol=GpsProtocol.sae_j1939)

        select_gnss_source(GnssSource.sae_j1939)
        simulation.start_docker()

        show_gnss_diagnostics()
        assert_gnss_diagnostics_values(reference)
        leave_gnss_diagnostics()
