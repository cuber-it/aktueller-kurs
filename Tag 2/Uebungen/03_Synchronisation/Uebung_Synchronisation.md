# Übung · Worauf wartet dieser Code?

Sie untersuchen, wie die Control-Schicht Ihres Frameworks klickt, wartet und liest. Der Code funktioniert in den meisten Läufen. Die Frage ist, worauf genau gewartet wird, und was passiert, wenn die AUT langsamer ist als erwartet.

---

## Material A · Klicken und warten

`UI/controls.py`, `Control.click_and_wait` (gekürzt)

```python
def click_and_wait(self, wait_object, fail_if_not_exists=True, timeout_sec=None, quiet=UI_ELEMENTS_QUIET_DEFAULT):
    timeout_sec = float(timeout_sec) if timeout_sec else self.click_timeout          # 120 s
    timeout = TimeOut(timeout_sec)
    while timeout.within_timeout() and not wait_object.exists(quiet=True):
        try:
            self.click(quiet=True)
            squish.waitFor(lambda: wait_object.exists(quiet=True), int(self.iteration_delay * 1000))   # 500 ms
        except (LookupError, RuntimeError):
            pass
    if fail_if_not_exists and not wait_object.exists(quiet=True):
        fail_test(f"While clicking {self.display_name}: {wait_object.display_name} still did not exist "
                  f"after {timeout_sec} seconds")
```

Aus den Coding-Regeln des Teams (`controls_and_tests.md`, gekürzt): `click_and_wait` klickt die Quelle bei jeder Wiederholung erneut. Das ist richtig, wenn die Quelle idempotent ist (Statusleisten-Button, Listeneintrag), aber zerstörerisch, wenn sie umschaltet:

```python
# wrong — re-clicks layout_manager_btn on every retry, flickering the panel open/closed
uih.statusbar.layout_manager_btn.click_and_wait(uih.application_launcher.ut_a_lbl)

# right — open once, then wait for the entry to render inside it
uih.statusbar.layout_manager_btn.click_and_wait(uih.statusbar.layout_manager_ok_btn)
uih.application_launcher.ut_a_lbl.wait_for_exists(timeout_msec=90000)
```

Die Abschlussliste des Skills enthält dazu Punkt 6c: `click_and_wait` nicht mit einer umschaltenden Quelle verwenden.

---

## Material B · Lesen

`UI/controls.py` (gekürzt)

```python
def get_property_value(self, prop, quiet=UI_ELEMENTS_QUIET_DEFAULT):
    if self.exists(quiet=True):                      # object.exists: prüft sofort, wartet nicht
        value = getattr(self.wait_for_exists(), prop, None)
        return value

def get(self, quiet=UI_ELEMENTS_QUIET_DEFAULT):
    text = self.get_property_value("text", quiet=True)
    if text is None or text == "":
        text = self.get_property_value("displayText", quiet=True)
    if text is None or text == "":
        text = self.get_property_value("value", quiet=True)
    return str(text)
```

---

## Material C · Zahlen und eine Regel

| Was | Anzahl |
|---|---:|
| `click_and_wait(...)` | 158 |
| davon auf `layout_manager_btn` (schaltet das Panel auf und zu) | 13, alle mit Ziel `layout_manager_ok_btn` |
| `click_while_exists(...)` | 84 |
| `squish.snooze(...)` im aktiven Code | 51, davon 6 direkt nach einem Klick |
| `UIElementTest(...)`, liest über `get()` | 148 |

Aus den Coding-Regeln des Teams: „After a navigation click → never snooze. Use `click_and_wait(target)`.“ Begründete Ausnahmen stehen in einer Tabelle, etwa 2 s nach dem Schließen des Layout-Managers.

---

## Material D · Zwei erwartbare Fehlerbilder

Angenommen, ein langsameres Terminal kommt in den Nachtlauf. Nach Material A und B sind zwei Fehlerbilder zu erwarten:

- Nach `layout_manager_btn.click_and_wait(layout_manager_ok_btn)` ist der Layout-Manager beim nächsten Schritt wieder geschlossen. Der Aufruf folgt der „right“-Variante aus den Coding-Regeln.
- Direkt nach dem Öffnen eines Menüs meldet `UIElementTest`: „Turn Radius was not as expected. Expected: 6.5. Found: None“. Mit einem `snooze(1)` davor ist der Test grün.

---

## Aufgabe

### Teil 1 · Lesen

**1.** Was tut `click_and_wait`, wenn das Zielobjekt erst 0,7 s nach dem Klick erscheint? Spielen Sie die Schleife Schritt für Schritt durch.

**2.** Unter welcher Bedingung ist ein zweiter Klick harmlos, unter welcher nicht? Ordnen Sie `settings_action_btn` und `layout_manager_btn` ein. Warum schützt die „right“-Variante aus den Coding-Regeln nicht in jedem Fall?

**3.** Was liefert `get()`, wenn das Objekt in dem Moment der Abfrage noch nicht existiert? Was steht im Protokoll?

**4.** Erklären Sie mit Material A und B beide Beobachtungen aus Material D.

### Teil 2 · Umbauen

**5.** Die Gefahr ist heute durch eine Regel in der Dokumentation und Punkt 6c der Abschlussliste abgesichert. Entwerfen Sie stattdessen eine API, die den Fehler nicht zulässt: `click_and_wait` klickt genau einmal. Wie meldet die Methode, dass das Ziel nicht erschienen ist?

**6.** Wo im Bestand ist ein Wiederholungsklick sicher? Welche vorhandene Methode leistet das bereits?

**7.** Entwerfen Sie `get_property_value` so, dass es auf das Objekt wartet. Wie lange, und was passiert, wenn es nicht erscheint?

### Teil 3 · Abwägen

**8.** Im aktiven Bestand stehen noch 51 `snooze` und Parameter wie `snooze_time=8`. Könnte eine dieser Wartezeiten die zweite Beobachtung aus Material D verdecken? Wie würden Sie das prüfen, bevor Sie sie entfernen?

**9.** Regel in der Checkliste oder sichere API: Was spricht jeweils dafür? Formulieren Sie zwei Regelkandidaten für den Teamstandard und ordnen Sie sie als MUST, SHOULD, MAY oder DON'T ein.

---

## Hinweise zur Bearbeitung

- Der Code muss nicht ausgeführt werden.
- Squish-Verhalten: `waitForObject` und `waitForObjectExists` warten und werfen bei Zeitablauf `LookupError`, `object.exists` prüft sofort, `waitFor` wiederholt eine Bedingung und liefert `True` oder `False`.
- Wenn Sie unsicher sind, fragen Sie: **Worauf genau wird hier gewartet, und wer kennt diesen Zustand?**
