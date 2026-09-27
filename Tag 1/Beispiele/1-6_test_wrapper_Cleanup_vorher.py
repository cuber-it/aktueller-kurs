"""1-6 · vorher · test_wrapper: Cleanup-Schritte in einer Kette

Quelle: init_cleanup_wrapper_helper/test_wrapper.py (Testframework des Teams, gekürzt).
Abweichung: Squish-Log, Target und Simulation sind durch Platzhalter ersetzt,
die jeden Aufruf in ``calls`` protokollieren.

Der Wrapper ist bereits ein Context Manager und garantiert, dass ``finally``
erreicht wird. Innerhalb von ``finally`` laufen die Schritte aber nacheinander:
Wirft einer, entfallen alle folgenden.
"""
from contextlib import contextmanager

calls = []
errors = 0


# --- Platzhalter --------------------------------------------------------------
def fail_test(message, exception=None):
    global errors
    errors += 1
    calls.append(f"FAIL {message}")


def cur_error_count():
    return errors


class _TargetHelper:
    def replace_data_set(self, data_set):
        calls.append(f"replace_data_set {data_set}")

    def start(self):
        calls.append("start")

    def backup_data_set(self, name, path):
        calls.append("backup_data_set")
        raise PermissionError("backup directory not writable")

    def cleanup(self):
        calls.append("target cleanup")


class Simulation_Helper:
    @staticmethod
    def stop_docker():
        calls.append("stop_docker")


target_helper = _TargetHelper()


def collect_and_zip(name):
    calls.append("collect_and_zip")


def clean_up_test_data():
    calls.append("clean_up_test_data")
# ------------------------------------------------------------------------------


@contextmanager
def test_wrapper(test_set_name=None, replace_data=True):
    try:
        issue_count = cur_error_count()
        clean_up_test_data()
        if replace_data:
            target_helper.replace_data_set("with_gps")
        target_helper.start()
        yield
    except Exception as e:
        fail_test(f"Test execution failed: {e}", exception=e)
    finally:
        if cur_error_count() > issue_count:
            target_helper.backup_data_set("_backup_after_fail", ".")
            collect_and_zip(test_set_name)
        clean_up_test_data()
        target_helper.cleanup()
        Simulation_Helper.stop_docker()


try:
    with test_wrapper("sc_set_3"):
        raise AssertionError("area differs by 3.1 qm")
except PermissionError as error:
    calls.append(f"propagiert: {error!r}")

print("\n".join(calls))
assert "target cleanup" not in calls
assert "stop_docker" not in calls        # die Simulation läuft weiter, der nächste Test findet sie vor

# Zweiter Fall: Schlägt schon cur_error_count() fehl, ist issue_count im finally
# nicht gesetzt. Geworfen wird dann ein UnboundLocalError, die eigentliche Ursache
# steht nur noch als Kontext darunter im Traceback.
print("vorher: alle Beobachtungen bestätigt")
