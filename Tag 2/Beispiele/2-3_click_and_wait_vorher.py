"""2-3 · vorher · Interaction + Wait mit eingebautem Wiederholungsklick, abgesichert durch eine Regel

Ausschnitt aus UI/controls.py, Control.click_and_wait (Testframework des Teams, gekürzt).
Nicht eigenständig lauffähig. 158 Aufrufe im Bestand, davon 13 auf layout_manager_btn.

Die Methode klickt, wartet 0,5 s (iteration_delay) auf das Ziel und klickt erneut, solange
es fehlt, bis zu 120 s (click_timeout). Die Schleife beobachtet das Ziel, nicht die Quelle.

Das Team kennt die Gefahr. Die Coding-Regeln (controls_and_tests.md) und Punkt 6c der
Abschlussliste sagen: harmlos bei idempotenten Quellen wie dem Statusleisten-Button,
zerstörerisch bei umschaltenden wie layout_manager_btn. Empfohlen wird, auf den OK-Button im
Panel zu warten. Alle 13 Aufrufe halten sich daran.

Die Regel verkürzt den Weg zum Ziel. Erscheint der OK-Button aber nicht innerhalb von 0,5 s,
klickt die Schleife trotzdem erneut und schließt das Panel. Die Sicherheit hängt an einer
Zeitannahme und daran, dass jeder Aufrufer die Regel kennt.
"""


class Control:
    def click_and_wait(self, wait_object: "Control", fail_if_not_exists=True, timeout_sec=None,
                       quiet=UI_ELEMENTS_QUIET_DEFAULT):
        timeout_sec = float(timeout_sec) if timeout_sec else self.click_timeout
        if not quiet:
            test.log(f"Clicking {self.display_name} until {wait_object.display_name} exists")

        timeout = TimeOut(timeout_sec)
        while timeout.within_timeout() and not wait_object.exists(quiet=True):
            try:
                self.click(quiet=True)
                squish.waitFor(lambda: wait_object.exists(quiet=True), int(self.iteration_delay * 1000))
            except (LookupError, RuntimeError):
                pass

        if fail_if_not_exists and not wait_object.exists(quiet=True):
            fail_test(f"While clicking {self.display_name}: {wait_object.display_name} still did not exist "
                      f"after {timeout_sec} seconds")


# Aus den Coding-Regeln des Teams:
# wrong — re-clicks layout_manager_btn on every retry, flickering the panel open/closed
uih.statusbar.layout_manager_btn.click_and_wait(uih.application_launcher.ut_a_lbl)

# right — open once, then wait for the entry to render inside it
uih.statusbar.layout_manager_btn.click_and_wait(uih.statusbar.layout_manager_ok_btn)
uih.application_launcher.ut_a_lbl.wait_for_exists(timeout_msec=90000)
