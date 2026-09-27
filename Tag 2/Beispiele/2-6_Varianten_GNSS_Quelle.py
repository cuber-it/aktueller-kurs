"""2-6 · Ein Szenario, vier Architekturvarianten

Szenario aus dem Testframework des Teams: "GNSS-Quelle SAE J1939 wählen und prüfen, dass sie
ausgewählt ist." Die Varianten sind Skizzen, nicht eigenständig lauffähig. Variante 3
entspricht weitgehend dem heutigen Stand des Kunden.

Zum Vergleich je ein Change Case: "Die GNSS-Quelle wird künftig im Menü Zugfahrzeug über eine
Auswahlliste statt über ein eigenes Untermenü gewählt."
"""

# ── Variante 1 · Direkter Testcode ──────────────────────────────────────────────
# Alles im Test: Real Names, Squish-Aufrufe, Warten.
def test_direct():
    squish.mouseClick(squish.waitForObject(STATUSBAR_SETTINGS_BUTTON))   # Real Name als Dictionary im Test
    # … weitere Klicks bis ins Untermenü GNSS-Quelle …
    button = squish.waitForObject({"objectName": "itemGnssSourceJ1939", "type": "CheckDelegate", "visible": True})
    squish.mouseClick(button)
    test.compare(button.checked, True)
# Change Case: jeder Test, der die GNSS-Quelle wählt, ändert seine Klickfolge.


# ── Variante 2 · Screen Objects ─────────────────────────────────────────────────
# Der Test navigiert über Screen Objects, kennt aber jedes Menü auf dem Weg.
def test_screen_objects():
    uih.statusbar.settings_action_btn.click_and_wait(setth.menu_settings.implement_btn)
    setth.menu_settings.implement_btn.click_and_wait(masetth.submenu_machinesettings.title_bar_title)
    masetth.submenu_machinesettings.open_settings_default_tractor()
    masetth.submenu_traction_unit.gnss_gnss_source_btn.click_while_exists()
    masetth.submenu_gnss_source.sae_j1939_btn.set(True)
    UIElementTest(masetth.submenu_gnss_source.sae_j1939_btn).test(True)
# Change Case: Screen Objects ändern sich, dazu jeder Test, der den Weg selbst geht.


# ── Variante 3 · Screen Objects + Tasks (heutiger Stand) ────────────────────────
# Ein Task kennt den Weg, der Test nutzt ihn.
def test_screen_objects_and_tasks():
    open_gnss_source_submenu()
    masetth.submenu_gnss_source.sae_j1939_btn.set(True)
    UIElementTest(masetth.submenu_gnss_source.sae_j1939_btn).test(True)
# Change Case: open_gnss_source_submenu und das Screen Object ändern sich; Tests, die das
# Control direkt ansprechen, ebenfalls.


# ── Variante 4 · Screenplay ─────────────────────────────────────────────────────
# Ein Actor mit Fähigkeiten führt Tasks aus; Tasks bestehen aus Interactions.
class BrowseTheTerminal:                       # Fähigkeit
    def __init__(self, target):
        self.target = target


class Actor:
    def __init__(self, name, *abilities):
        self.name = name
        self.abilities = {type(a): a for a in abilities}

    def attempts_to(self, *tasks):
        for task in tasks:
            task.perform_as(self)

    def should_see(self, question, expected):
        test.compare(question.answered_by(self), expected, f"{self.name} sees {question}")


class SelectGnssSource:                        # Task
    def __init__(self, source):
        self.source = source

    def perform_as(self, actor):
        open_gnss_source_submenu()                             # Interactions: vorhandene Controls
        _SOURCE_BUTTONS[self.source]().set(True)


class SelectedGnssSource:                      # Question
    def answered_by(self, actor):
        return next(s for s, b in _SOURCE_BUTTONS.items() if b().get())


def test_screenplay():
    driver = Actor("Fahrer", BrowseTheTerminal(test_exec_helper.target))
    driver.attempts_to(SelectGnssSource(GnssSource.sae_j1939))
    driver.should_see(SelectedGnssSource(), GnssSource.sae_j1939)
# Change Case: SelectGnssSource ändert sich; Tests bleiben unverändert.
# Kosten: Actor, Fähigkeit, Task, Question als neue Konzepte neben den vorhandenen.
