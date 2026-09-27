"""2-3 · vorher · Lesen ohne Synchronisation

Ausschnitt aus UI/controls.py (Control.get_property_value, Control.get), Testframework des
Teams, gekürzt. Nicht eigenständig lauffähig.

get_property_value fragt zuerst self.exists(), also object.exists. Laut Squish-Doku prüft
object.exists sofort und wartet nicht. Existiert das Objekt in diesem Moment nicht, liefert
die Methode None, ohne Wartezeit und ohne Protokolleintrag. get() macht daraus den Text
"None". Eine Prüfung meldet dann etwa "Expected: 6.5. Found: None", egal ob das Feld noch
nicht da war oder gar nicht existiert. Über get() lesen unter anderem alle 148 UIElementTest.
"""


class Control:
    def get_property_value(self, prop, quiet=UI_ELEMENTS_QUIET_DEFAULT):
        if self.exists(quiet=True):
            value = getattr(self.wait_for_exists(), prop, None)

            if value and not quiet:
                test.log(f"The property {prop} of {self.display_name} is {value}")
            return value

    def get(self, quiet=UI_ELEMENTS_QUIET_DEFAULT):
        text = self.get_property_value("text", quiet=True)
        if text is None or text == "":
            text = self.get_property_value("displayText", quiet=True)
        if text is None or text == "":
            text = self.get_property_value("value", quiet=True)
        if not quiet:
            test.log(f"The current text of {self.display_name} is {text}")
        return str(text)
