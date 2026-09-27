"""2-3 · nachher · Die API schließt den Fehler aus, statt ihn per Regel zu verbieten

Eine mögliche Richtung. Ausschnitt, nicht eigenständig lauffähig.

Heute sichern ein Warnabschnitt in den Coding-Regeln und Punkt 6c der Abschlussliste den
Wiederholungsklick bei umschaltenden Quellen ab. Beides muss jeder Aufrufer kennen, Mensch
oder Skill. Klickt click_and_wait genau einmal, entfallen Regel und Checklistenpunkt, und die
„wrong“-Variante aus den Coding-Regeln ist genauso sicher wie die „right“-Variante.

- click_and_wait klickt genau einmal und wartet dann mit squish.waitFor auf das Ziel.
- Wiederholtes Klicken bleibt möglich, aber als eigene Methode mit eigenem Namen. Sie
  beobachtet den geklickten Control selbst: Ist er verschwunden, ist der Klick angekommen.
  Das entspricht click_while_exists() ohne Argument im Bestand.
- Wo der Wiederholungsklick bisher verlorene Klicks auffängt, sollte das Team den Fall
  benennen (welcher Button, welche Bedingung) und dort click_until_gone verwenden.
"""


class Control:
    def click_and_wait(self, wait_object: "Control", timeout_msec=None, quiet=UI_ELEMENTS_QUIET_DEFAULT):
        """Klickt einmal und wartet, bis wait_object existiert.

        Der Test scheitert (fail_test mit raise_exception=True), wenn wait_object nicht
        innerhalb von timeout_msec erscheint.
        """
        timeout_msec = timeout_msec if timeout_msec else self.wait_timeout
        if not quiet:
            test.log(f"Clicking {self.display_name}, then waiting for {wait_object.display_name}")
        self.click(quiet=True)
        if not squish.waitFor(lambda: wait_object.exists(quiet=True), timeout_msec):
            fail_test(f"After clicking {self.display_name}: {wait_object.display_name} did not appear "
                      f"within {timeout_msec} ms. Expected: {wait_object}", raise_exception=True)

    def click_until_gone(self, timeout_sec=None, quiet=UI_ELEMENTS_QUIET_DEFAULT):
        """Klickt wiederholt, bis dieser Control verschwunden ist.

        Nur für Controls, die nach einem angekommenen Klick verschwinden. Ein Klick zu viel
        trifft dann nichts mehr.
        """
        self.click_while_exists(timeout_sec=timeout_sec, quiet=quiet)


# Verwendung: genau ein Klick, auch bei umschaltender Quelle und langsamem Panel.
uih.statusbar.layout_manager_btn.click_and_wait(uih.statusbar.layout_manager_ok_btn)
