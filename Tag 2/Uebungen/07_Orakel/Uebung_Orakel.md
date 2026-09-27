# Übung · Wer handelt, wer beobachtet, wer urteilt?

Sie untersuchen das Verifikationsobjekt Ihres Frameworks und die Art, wie Prüfungen Fehler melden. Der Code funktioniert. Die Frage ist, ob Aktion, Beobachtung und Bewertung unterscheidbar bleiben und was ein roter Test aussagt.

---

## Material A · Das Verifikationsobjekt

`ui_test_modules/base_ui_test.py`, `UIElementTest` (gekürzt)

```python
class UIElementTest:
    FAIL_MESSAGE = "{} was not as expected."
    FAIL_MESSAGE_WITH_RES = FAIL_MESSAGE + " Expected: {}. Found: {}"

    def __init__(self, control, dev_display_text=None, display_text_addition=None):
        self.result = None
        self.control = control
        self.display_text = dev_display_text if dev_display_text else control.display_name

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
```

---

## Material B · Wie Fehler gemeldet werden

- Squish: `test.compare`, `test.verify` und `test.fail` schreiben einen Eintrag ins Protokoll und brechen den Test **nicht** ab, außer `testSettings.throwOnFailure` ist gesetzt.
- Framework: `fail_test(message, raise_exception=False)` ruft `test.fail`, schreibt den Traceback ins Log und wirft nur mit `raise_exception=True`.
- Framework: `test_wrapper` um jeden Test fängt Exceptions, meldet sie mit `fail_test` und räumt im `finally` auf.

---

## Material C · Zahlen aus dem Bestand

| Was | Anzahl |
|---|---:|
| `UIElementTest(...)` | 148 |
| `.test(..., set_setting=True)` | 16 |
| Testfälle mit `test_wrapper` | 978 von 983 |

---

## Material D · Ein Beispielprotokoll

```text
FAIL  Keyboard didn't open while clicking Turning Radius
FAIL  Turn Radius (Tractor) was not as expected. Expected: 6.5. Found: 5.0
FAIL  Min. Turn Radius (Tractor) was not as expected. Expected: 4.0. Found: 5.0
FAIL  Headland Width was not as expected. Expected: 12. Found: 24
FAIL  Implement Width was not as expected. Expected: 12. Found: 24
```

Der Test setzt vier Werte mit `test(..., set_setting=True)`. `set()` läuft über `click_with_entry`, das meldet, wenn die Tastatur nicht öffnet, und trägt dafür einen FAIL ein. Der Test läuft weiter. Die Tastatur blieb für alle vier Felder geschlossen.

---

## Aufgabe

### Teil 1 · Unterscheiden

**1.** Welche Teile von `UIElementTest.test` sind Aktion, welche Beobachtung, welche Bewertung?

**2.** Was sagt eine Meldung „Expected: 6.5. Found: 5.0“ aus, wenn `set_setting=True` war? Was sagt sie nicht?

**3.** Was passiert mit `type(value)(self.control.get())`, wenn `value` ein `bool` und `get()` ein Text ist? Für welche Controls ist das harmlos?

**4.** Warum stehen in Material D fünf FAILs statt einem? Welcher davon nennt die Ursache?

### Teil 2 · Trennen

**5.** Entwerfen Sie eine Prüfung, die nur beobachtet und bewertet. Wie wird der gelesene Wert in den Typ der Erwartung gewandelt?

**6.** Schreiben Sie die Verwendung aus Material D neu: erst setzen, dann prüfen. Was steht im Protokoll, wenn die Tastatur nicht öffnet?

**7.** Wann sollte ein Fehler den Test abbrechen, wann nur einen FAIL eintragen? Formulieren Sie ein Kriterium.

### Teil 3 · Diagnose

**8.** Ein roter Test kann ein AUT-Fehler, ein Testfehler, ein Umgebungsfehler oder ein Synchronisationsproblem sein. Welche Information in der Meldung hilft, das zu unterscheiden?

**9.** Formulieren Sie zwei Regelkandidaten für Prüfungen im Teamstandard.

---

## Hinweise zur Bearbeitung

- Der Code muss nicht ausgeführt werden.
- `UIElementTest` bleibt bestehen. Es geht um die Stellen mit `set_setting=True` und um Meldungen.
- Wenn Sie unsicher sind, fragen Sie: **Was sagt dieser rote Test, und was nicht?**
