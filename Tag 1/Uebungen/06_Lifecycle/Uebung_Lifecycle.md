# Übung · Wer räumt auf, wenn der Test scheitert?

Sie untersuchen die Testumgebung einer Terminal-Software. Jeder Test öffnet eine Testdatenbank, startet die Anwendung und beendet beides am Ende wieder. Der Code funktioniert, solange kein Test fehlschlägt.

**Es werden keine Squish-Kenntnisse benötigt.** Die Anwendung wird durch `print`-Ausgaben vertreten, es zählt nur die Objektstruktur. Die fachlichen Details sind vereinfacht und erheben keinen Anspruch auf Richtigkeit.

---

## Material A · Die Klassen der Testumgebung

```python
_running_processes = set()  # Platzhalter für die Prozesstabelle des Betriebssystems


def terminate_process(process_id):
    """Platzhalter für os.kill(process_id, signal.SIGTERM).

    Wirft wie os.kill einen ProcessLookupError, wenn der Prozess nicht mehr läuft.
    """
    if process_id not in _running_processes:
        raise ProcessLookupError(3, "No such process")
    _running_processes.discard(process_id)


class TestDatabase:
    def __init__(self, path):
        self.path = path
        self.connection = None

    def open(self):
        print(f"open test database {self.path}")
        self.connection = f"connection:{self.path}"

    def load_fixture(self, name):
        print(f"load fixture {name} via {self.connection}")

    def close(self):
        print(f"close {self.connection}")
        self.connection = None


class TerminalApp:
    def __init__(self):
        self.process_id = None
        self.database = None

    def configure(self, database):
        self.database = database

    def start(self):
        print(f"start terminal app with {self.database.connection}")
        self.process_id = 4711  # Platzhalter für die ID des gestarteten Prozesses
        _running_processes.add(self.process_id)

    def send(self, command):
        print(f"send {command!r} to process {self.process_id}")

    def stop(self):
        print(f"stop terminal app process {self.process_id}")
        terminate_process(self.process_id)
        self.process_id = None
```

---

## Material B · Ein typischer Test und eine Hilfsfunktion

```python
import socket


def run_alarm_test():
    database = TestDatabase("alarm.db")
    database.open()
    database.load_fixture("section_valve_failure")

    app = TerminalApp()
    app.configure(database)
    app.start()

    app.send("acknowledge_alarm SV-3")
    check_alarm_list(app)

    app.stop()
    database.close()


def connect_to_simulation(host):
    try:
        connection = socket.create_connection((host, 5020), timeout=5)
        connection.close()
        return True
    except Exception:
        return False
```

---

## Material C · Zwei Auszüge aus Protokollen von Nachtläufen

**Nacht 1.** `run_alarm_test` läuft als Test 312 von 860.

```text
test 312 alarm_acknowledge ........ FAILED
  AssertionError: alarm SV-3 not acknowledged
test 313 alarm_history ............ FAILED
  terminal app already running, cannot start second instance
test 314 section_overview ......... FAILED
  terminal app already running, cannot start second instance
...
test 860 task_report .............. FAILED
  terminal app already running, cannot start second instance
```

**Nacht 2.** Einige Tests wurden inzwischen mit `try/finally` abgesichert. Test 97 ist einer davon.

```text
test 97 section_control ........... FAILED
  ProcessLookupError: [Errno 3] No such process
test 98 section_history ........... PASSED
```

In Test 97 war die Anwendung während der Prüfung abgestürzt. Der Absturz selbst steht nicht im Protokoll.

---

## Material D · Eine Aussage aus dem Team

Aus dem Team, verantwortlich für die Testinfrastruktur:

> „Aufräumen ist Sache des Tests. Wer `start()` aufruft, weiß, dass er `stop()` aufrufen muss. Das steht so im Wiki."

---

## Aufgabe

### Teil 1 · Zustand und Fehlerpfade lesen

**1.** Nehmen Sie an, `check_alarm_list(app)` wirft eine Exception. In welchem Zustand bleiben Datenbank und Anwendung zurück? Was bedeutet das für den nächsten Test? Vergleichen Sie mit Material C, Nacht 1.

**2.** Welche Zustände kann ein `TerminalApp`-Objekt annehmen? Welche Operationen sind in welchem Zustand sinnvoll? Was passiert heute bei `send()` vor `start()`?

**3.** Zwischen `TerminalApp()` und `configure(database)` existiert ein Objekt ohne Datenbank. Was kann in diesem Zeitraum schiefgehen?

**4.** `connect_to_simulation` liefert `False`. Welche verschiedenen Ursachen kann das haben? Welche Information hat der Aufrufer danach noch?

### Teil 2 · Umbauen

**5.** Sichern Sie `run_alarm_test` mit `try/finally` ab. Warum reicht es nicht, das nur an dieser einen Stelle zu tun?

**6.** Machen Sie `TestDatabase` und `TerminalApp` zu Context Managern, einmal als Klasse mit `__enter__`/`__exit__`, einmal mit `contextlib.contextmanager`. Wie sieht der Test danach aus, und in welcher Reihenfolge wird aufgeräumt?

**7.** Entscheiden Sie, wie `TerminalApp` mit `send()` vor `start()` umgehen soll, und setzen Sie es um. Beziehen Sie Aufgabe 3 mit ein.

**8.** Ersetzen Sie das `return False` in `connect_to_simulation` durch Exceptions, auf die ein Aufrufer sinnvoll reagieren kann. Wie viele eigene Exception-Klassen brauchen Sie dafür?

### Teil 3 · Abwägen

**9.** Material C, Nacht 2, zeigt: Der Fehler beim Aufräumen hat den eigentlichen Fehler verdrängt. Erklären Sie, wie das in Python zustande kommt, und gestalten Sie `stop()` bzw. `__exit__` so, dass der ursprüngliche Fehler sichtbar bleibt.

**10.** Ein Kollege schlägt vor, auch `TestReport` zum Context Manager zu machen. `TestReport` sammelt Ergebnisse in einer Liste und schreibt sie am Ende mit `write()` in eine Datei. Was spricht dafür, was dagegen?

**11.** Prüfen Sie die Aussage aus Material D. Welche Cleanup-Garantie würden Sie stattdessen als Teamregel formulieren?

---

## Hinweise zur Bearbeitung

- Der Code muss nicht ausgeführt werden. Er sollte aber so geschrieben sein, dass er lauffähig wäre.
- `check_alarm_list` ist eine vorhandene Prüffunktion. Sie müssen sie nicht schreiben.
- Für jede Ressource hilft die Frage: **Wer beendet diesen Zustand – und was passiert, wenn zwischen Start und Ende ein Fehler auftritt?**
- Für die Aufgaben 1 bis 4 genügen Stichpunkte.
