"""2-2 · nachher · Varianten eines Locators als neue Controls

Eine mögliche Richtung. Ausschnitt, nicht eigenständig lauffähig.

with_text() und inside() ändern das Control nicht, sie liefern ein neues Control mit
angepasstem Real Name. Das geteilte Control im Screen Object bleibt unverändert, auch wenn
im Ablauf eine Exception auftritt. Ein with-Block ist nicht mehr nötig.

Kleinste mögliche Korrektur des Bestands: try/finally in deviating_name_value. Sie verhindert
das Zurückbleiben, der geteilte Zustand bleibt aber bestehen.
"""
from copy import copy


class Control:
    def _variant(self, name, display_name):
        variant = copy(self)                       # übernimmt application_name, Timeouts, …
        variant.name = name
        variant.display_name = display_name
        return variant

    def with_text(self, text) -> "Control":
        """Dasselbe Control mit anderem Text im Real Name."""
        return self._variant({**self.name, "text": text}, f"{self.display_name} '{text}'")

    def inside(self, container: "Control") -> "Control":
        """Dasselbe Control innerhalb eines anderen Containers."""
        return self._variant({**self.name, "container": dict(container.name)},
                             f"{self.display_name} in {container.display_name}")


class SubMenuMachineSettings(ListCtrlMixin):
    def open_implement_settings_by_text(self, text, quiet=UI_ELEMENTS_QUIET_DEFAULT):
        if not quiet:
            test.log(f"Opening settings of the implement named {text}")

        entry = self.menu_list.delegate.with_text(text)
        button = self.implement_settings_btn.inside(entry)
        button.wait_for_exists()
        squish.snooze(MENU_ROLL_OUT_TIME)  # Give the menu Time to roll out all options
        button.click(quiet=True)
