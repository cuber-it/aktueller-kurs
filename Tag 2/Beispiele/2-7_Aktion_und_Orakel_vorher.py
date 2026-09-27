"""2-7 · vorher · Setzen und Prüfen in einem Aufruf

Ausschnitt aus ui_test_modules/base_ui_test.py, UIElementTest (Testframework des Teams,
gekürzt). Nicht eigenständig lauffähig. UIElementTest wird 148-mal verwendet,
test(..., set_setting=True) 16-mal.

- test(value, set_setting=True) ist Aktion (setzen) und Bewertung (vergleichen) zugleich.
  Scheitert der Vergleich, zeigt die Meldung nicht, ob schon das Setzen gescheitert ist.
- Der gelesene Wert wird mit type(value)(...) in den Typ des Erwartungswerts gewandelt.
  Für Zahlen und Text passend. Bei bool gilt in Python bool("False") == True; harmlos,
  solange get() für Schalter einen bool liefert (bei CheckDelegate und SwitchDelegate der Fall).
- Das Ergebnis steht in self.cur_value, einem Attribut, das erst in test() entsteht.
"""
from contextlib import contextmanager


class UIElementTest:
    FAIL_MESSAGE = "{} was not as expected."
    FAIL_MESSAGE_WITH_RES = FAIL_MESSAGE + " Expected: {}. Found: {}"

    @contextmanager
    def test_wrapper(self, value, deviating_check=False):
        with log_section(self.SECTION_NAME.format(self.display_text)):
            yield
            if (not deviating_check and value != self.cur_value) or \
                    (deviating_check and self.result is not None and not self.result):
                fail_test(self.FAIL_MESSAGE_WITH_RES.format(self.display_text, value, self.cur_value))

    def test(self, value, set_setting=False):
        with self.test_wrapper(value):
            if set_setting:
                self.control.set(value)

            self.cur_value = type(value)(self.control.get())


# Verwendung im Testfall:
tst = UIElementTest(masetth.submenu_gnss_source.sae_j1939_btn)
tst.test(True, set_setting=True)
