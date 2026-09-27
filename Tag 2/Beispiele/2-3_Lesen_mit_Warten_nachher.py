"""2-3 · nachher · Lesen wartet auf das Objekt

Eine mögliche Richtung. Ausschnitt, nicht eigenständig lauffähig.

get_property_value wartet mit der vorhandenen Methode wait_for_exists (darunter
squish.waitForObjectExists) auf das Objekt. Erscheint es nicht, bricht der Test mit einer
Meldung ab, die Control und Real Name nennt. Wer wissen will, ob etwas fehlt, verwendet
weiterhin exists().

Die Lesezeit ist kürzer als der allgemeine Timeout: Wer liest, erwartet ein vorhandenes
Objekt. Der Wert 5000 ms ist ein Vorschlag.
"""


class Control:
    READ_TIMEOUT_MSEC = 5000

    def get_property_value(self, prop, quiet=UI_ELEMENTS_QUIET_DEFAULT):
        obj = self.wait_for_exists(fail_if_not_exists=False, timeout_msec=self.READ_TIMEOUT_MSEC, quiet=True)
        if obj is None:
            fail_test(f"Cannot read {prop}: {self.display_name} did not appear within "
                      f"{self.READ_TIMEOUT_MSEC} ms.{self}", raise_exception=True)
        value = getattr(obj, prop, None)
        if value and not quiet:
            test.log(f"The property {prop} of {self.display_name} is {value}")
        return value

    def get(self, quiet=UI_ELEMENTS_QUIET_DEFAULT):
        for prop in ("text", "displayText", "value"):
            value = self.get_property_value(prop, quiet=True)
            if value not in (None, ""):
                break
        if not quiet:
            test.log(f"The current text of {self.display_name} is {value}")
        return "" if value is None else str(value)
