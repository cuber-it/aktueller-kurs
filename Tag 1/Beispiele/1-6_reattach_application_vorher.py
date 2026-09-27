"""1-6 · vorher · reattach_application: Rückgabewert und Testfehler zugleich

Quelle: target_helper/abstract_target_helper.py (Testframework des Teams, gekürzt).
Abweichungen: ``squish``, ``test`` und ``TimeOut`` durch Platzhalter ersetzt;
der Platzhalter scheitert bei jedem Versuch. Gezeigt wird der Fehlerpfad.

Die Methode meldet einen Fehlschlag auf zwei Wegen: ``test.fail`` im
Squish-Protokoll und ``False`` als Rückgabewert. Der Aufrufer entscheidet selbst,
ob er den Rückgabewert beachtet. Die ursprüngliche Exception steht nur als Text
in der Meldung.
"""
calls = []


class test:
    @staticmethod
    def log(message):
        calls.append(f"LOG {message}")

    @staticmethod
    def fail(message):
        calls.append(f"FAIL {message}")


class squish:
    @staticmethod
    def attachToApplication(name, timeoutSecs=10):
        raise RuntimeError(f"no AUT named {name} is running")

    @staticmethod
    def snooze(seconds):
        pass


class TimeOut:
    def __init__(self, timeout_sec):
        self._left = 3                    # drei Versuche statt einer Zeitspanne

    def within_timeout(self):
        self._left -= 1
        return self._left >= 0


class TargetHelper:
    def __init__(self):
        self.application_contexts = {}

    def attach_application(self, application_name):
        self.application_contexts[application_name] = squish.attachToApplication(application_name, timeoutSecs=10)

    def reattach_application(self, application_name, timeout_sec=30):
        """
        Re-establishes the application context of an AUT that was restarted.

        Returns:
            bool: Indicates if the AUT could be reattached.
        """
        test.log(f"Reattaching to {application_name}")
        timeout = TimeOut(timeout_sec)
        last_exception = None
        while timeout.within_timeout():
            try:
                self.attach_application(application_name)
                return True
            except Exception as e:
                last_exception = e
                squish.snooze(1)

        test.fail(f"Could not reattach to {application_name} within {timeout_sec} seconds: {last_exception}")
        return False


# Ein Aufrufer, der den Rückgabewert nicht prüft, macht weiter:
helper = TargetHelper()
helper.reattach_application("terminalui_launcher")
calls.append("Test klickt weiter in einer Anwendung ohne Kontext")

print("\n".join(calls))
print("vorher: läuft weiter")
