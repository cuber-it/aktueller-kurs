"""1-6 · nachher · test_wrapper mit ExitStack

Eine mögliche Richtung. Jeder Aufräumschritt wird mit ``ExitStack.callback``
registriert, sobald es etwas aufzuräumen gibt. Beim Verlassen laufen alle
registrierten Schritte in umgekehrter Reihenfolge, auch wenn einer davon wirft.
Wirft mehr als einer, bleiben die früheren Fehler als ``__context__`` der
zuletzt geworfenen Exception erhalten.

Target und Simulation werden übergeben (siehe 1-5). ``fail_test`` und das
Zählen der Fehler bleiben wie im Testframework.
"""
from contextlib import ExitStack, contextmanager

calls = []
errors = 0


# --- Platzhalter wie in der vorher-Datei --------------------------------------
def fail_test(message, exception=None):
    global errors
    errors += 1
    calls.append(f"FAIL {message}")


def cur_error_count():
    return errors


class TargetHelper:
    def replace_data_set(self, data_set):
        calls.append(f"replace_data_set {data_set}")

    def start(self):
        calls.append("start")

    def backup_data_set(self, name, path):
        calls.append("backup_data_set")
        raise PermissionError("backup directory not writable")

    def cleanup(self):
        calls.append("target cleanup")


class Simulation:
    def stop_docker(self):
        calls.append("stop_docker")


def collect_and_zip(name):
    calls.append("collect_and_zip")


def clean_up_test_data():
    calls.append("clean_up_test_data")
# ------------------------------------------------------------------------------


@contextmanager
def test_wrapper(target, simulation, data_set, test_set_name=None):
    issue_count = cur_error_count()

    def save_evidence_if_failed():
        if cur_error_count() > issue_count:
            target.backup_data_set("_backup_after_fail", ".")
            collect_and_zip(test_set_name)

    with ExitStack() as cleanup:
        cleanup.callback(simulation.stop_docker)
        cleanup.callback(target.cleanup)
        cleanup.callback(clean_up_test_data)
        cleanup.callback(save_evidence_if_failed)   # läuft als erster Schritt

        clean_up_test_data()
        target.replace_data_set(data_set)
        target.start()
        try:
            yield
        except Exception as e:
            fail_test(f"Test execution failed: {e}", exception=e)


try:
    with test_wrapper(TargetHelper(), Simulation(), "with_gps", "sc_set_3"):
        raise AssertionError("area differs by 3.1 qm")
except PermissionError as error:
    calls.append(f"propagiert: {error!r}")

print("\n".join(calls))
assert "target cleanup" in calls
assert "stop_docker" in calls
print("nachher: alle Beobachtungen bestätigt")
