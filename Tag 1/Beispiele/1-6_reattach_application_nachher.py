"""1-6 · nachher · reattach_application wirft eine eigene Exception

Eine mögliche Richtung. Ein Fehlschlag wird zur Exception ``AutReattachError``.
Sie trägt die ursprüngliche Exception als ``__cause__``, dadurch bleibt der
vollständige Traceback erhalten. Wer weitermachen kann, fängt sie. Alle anderen
brechen ab, und ``test_wrapper`` meldet den Fehler an einer Stelle.

Offen für die Diskussion: Wie viele eigene Exception-Klassen braucht das
Framework? Eine gemeinsame Basisklasse (hier ``TestAutomationError``) erlaubt es,
Framework-Fehler von Fehlern der AUT zu unterscheiden.
"""
calls = []


class squish:
    @staticmethod
    def attachToApplication(name, timeoutSecs=10):
        raise RuntimeError(f"no AUT named {name} is running")

    @staticmethod
    def snooze(seconds):
        pass


class TimeOut:
    def __init__(self, timeout_sec):
        self._left = 3

    def within_timeout(self):
        self._left -= 1
        return self._left >= 0


class TestAutomationError(Exception):
    """Basis für Fehler des Testframeworks."""


class AutReattachError(TestAutomationError):
    """Die AUT ließ sich nach einem Neustart nicht wieder verbinden."""


class TargetHelper:
    def __init__(self):
        self.application_contexts = {}

    def attach_application(self, application_name):
        self.application_contexts[application_name] = squish.attachToApplication(application_name, timeoutSecs=10)

    def reattach_application(self, application_name: str, timeout_sec: int = 30) -> None:
        """Verbindet eine neu gestartete AUT wieder.

        Raises:
            AutReattachError: wenn das innerhalb von ``timeout_sec`` nicht gelingt.
        """
        timeout = TimeOut(timeout_sec)
        last_exception = None
        while timeout.within_timeout():
            try:
                self.attach_application(application_name)
                return
            except Exception as e:          # wie im Original; welchen Typ attachToApplication
                                            # wirft, steht in der Squish-Dokumentation
                last_exception = e
                squish.snooze(1)
        raise AutReattachError(
            f"could not reattach to {application_name} within {timeout_sec} s") from last_exception


helper = TargetHelper()
try:
    helper.reattach_application("terminalui_launcher")
    calls.append("Test klickt weiter")
except AutReattachError as error:
    calls.append(f"abgebrochen: {error}")
    calls.append(f"Ursache: {error.__cause__!r}")

print("\n".join(calls))
assert "Test klickt weiter" not in calls
print("nachher: alle Beobachtungen bestätigt")
