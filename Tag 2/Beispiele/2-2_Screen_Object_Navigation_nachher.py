"""2-2 · nachher · Jedes Screen Object kennt seine Wege

Eine mögliche Richtung. Ausschnitt, nicht eigenständig lauffähig.

- Navigationsmethoden klicken, warten auf das Ziel und geben dessen Screen Object zurück.
  Verwendet werden die vorhandenen Methoden click_and_wait und click_while_exists.
- Wohin ein Zurück-Button führt, steht genau einmal: in go_back() des Menüs.
- Helper und Tests verketten die Methoden. Ändert sich ein Ziel, ändert sich eine Methode,
  und der Rückgabetyp zeigt, welche Aufrufer davon betroffen sind.

Die Coding-Regeln des Teams verlangen für Wege über mehrere Menüs bereits eine Funktion, die
den erreichten Page Helper zurückgibt. Hier gilt das für jeden einzelnen Schritt.
"""


# ── Screen Objects (UI/machinesettings_ui.py, ergänzt) ─────────────────────────
class SubMenuMachineSettings(ListCtrlMixin):
    def open_default_tractor(self) -> "SubMenuTractionUnit":
        self.open_settings_default_tractor()
        helper.submenu_traction_unit.title_bar_title.wait_for_exists()
        return helper.submenu_traction_unit

    def go_back(self) -> "MenuSettings":
        self.back_btn.click_while_exists()
        return setth.menu_settings


class SubMenuTractionUnit(AnyDeviceSubMenuMixin):
    def open_gnss_source(self) -> "SubMenuGNSSSource":
        self.gnss_btn.set(True)
        self.gnss_gnss_source_btn.click_while_exists()
        return helper.submenu_gnss_source

    def go_back(self) -> "SubMenuMachineSettings":
        self.back_btn.click_and_wait(helper.submenu_machinesettings.title_bar_title)
        return helper.submenu_machinesettings


class SubMenuGNSSSource(ListCtrlMixin):
    def go_back(self) -> "SubMenuTractionUnit":
        self.back_btn.click_and_wait(helper.submenu_traction_unit.traction_unit_title_txt)
        return helper.submenu_traction_unit


# ── Helper ──────────────────────────────────────────────────────────────────────
def open_gnss_source_submenu() -> "SubMenuGNSSSource":
    # open_settings() und open_machine_settings() nach demselben Muster
    settings = uih.statusbar.open_settings()
    return settings.open_machine_settings().open_default_tractor().open_gnss_source()


def close_machine_settings_menus():
    masetth.submenu_traction_unit.go_back().go_back().go_back()


# ── Testfall ────────────────────────────────────────────────────────────────────
def main():
    gnss_source = open_gnss_source_submenu()
    gnss_source.sae_j1939_btn.set(True)
    gnss_source.go_back()
    # …
    close_machine_settings_menus()
