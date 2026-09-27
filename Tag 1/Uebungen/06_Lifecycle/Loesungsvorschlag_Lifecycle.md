# Lösungsvorschlag · Wer räumt auf, wenn der Test scheitert?

**Vorbemerkung:** Ein Vorschlag, keine Musterlösung. Bei den Aufgaben 7, 8 und 10 sind andere Entscheidungen vertretbar. Bewertet wird, ob für jede Ressource **klar ist, wer sie beendet und welcher Fehler den Aufrufer erreicht**.

---

## 1 · Der Zustand nach einer Exception in `check_alarm_list`

| Ressource | Zustand danach | Folge |
|---|---|---|
| Anwendung | läuft weiter, Prozess 4711 | der nächste Test kann keine zweite Instanz starten |
| Testdatenbank | bleibt geöffnet, Fixture `section_valve_failure` geladen | der nächste Test sieht fremde Daten, falls er dieselbe Datenbank öffnet |
| Objekte `app`, `database` | werden nach dem Ende der Funktion unerreichbar | niemand hat mehr eine Referenz, um aufzuräumen |

Das ist genau Nacht 1 aus Material C: ein echter Fehler in Test 312, danach 548 Folgefehler. Die Ursache liegt nicht in Test 313, sondern in dem, was Test 312 hinterlassen hat.

---

## 2 · Die Zustände von `TerminalApp`

| Zustand | Kennzeichen | sinnvolle Operationen |
|---|---|---|
| erzeugt, ohne Datenbank | `database is None` | `configure()` |
| konfiguriert | `database` gesetzt, `process_id is None` | `start()` |
| laufend | `process_id` gesetzt | `send()`, `stop()` |
| beendet | `process_id is None` | im Grunde keine; `start()` ist technisch möglich |

**`send()` vor `start()`:** Die Methode gibt `send 'acknowledge_alarm SV-3' to process None` aus und kehrt normal zurück. Kein Fehler, keine Wirkung. Der Test läuft weiter und scheitert erst an einer späteren Prüfung mit einer Meldung, die nichts mit der Ursache zu tun hat.

---

## 3 · Das Objekt zwischen Konstruktor und `configure()`

- `start()` bricht mit `AttributeError: 'NoneType' object has no attribute 'connection'` ab. Die Meldung nennt die Datenbank nicht.
- Wird `configure()` nach `start()` aufgerufen, läuft die Anwendung mit einer anderen Datenbank, als das Objekt behauptet.
- Wer den Code liest, erkennt am Konstruktor nicht, dass eine Datenbank Pflicht ist.

Die Invariante „eine laufende Anwendung hat eine Datenbank" ist nirgends geschützt. Sie hängt davon ab, dass jeder Aufrufer die Reihenfolge kennt.

---

## 4 · Was `return False` verschweigt

`socket.create_connection` kann unter anderem so scheitern:

| Ursache | Exception | Was der Aufrufer tun könnte |
|---|---|---|
| Simulator antwortet nicht rechtzeitig | `TimeoutError` | später erneut versuchen |
| Simulator nicht gestartet | `ConnectionRefusedError` | Simulator starten oder den Lauf abbrechen |
| Hostname unbekannt | `socket.gaierror` | Konfiguration korrigieren, ein neuer Versuch hilft nicht |

`except Exception` fängt außerdem Programmierfehler, etwa einen `TypeError`, wenn `host` versehentlich `None` ist.

**Nach `return False` hat der Aufrufer nur noch eine Information:** Es hat nicht geklappt. Welche der drei Reaktionen passt, kann er nicht entscheiden. Genau das zeigen die 41 Tickets.

---

## 5 · `try/finally`

```python
def run_alarm_test():
    database = TestDatabase("alarm.db")
    database.open()
    try:
        database.load_fixture("section_valve_failure")
        app = TerminalApp()
        app.configure(database)
        app.start()
        try:
            app.send("acknowledge_alarm SV-3")
            check_alarm_list(app)
        finally:
            app.stop()
    finally:
        database.close()
```

Jede Ressource bekommt ihr eigenes `try`, und zwar erst **nach** dem erfolgreichen Öffnen. Scheitert `app.start()`, wird `app.stop()` nicht aufgerufen, die Datenbank aber geschlossen.

**Warum das an einer Stelle nicht reicht:** Die Struktur muss in allen 860 Tests stehen und in jedem neuen Test richtig wiederholt werden. Die Verschachtelung ist leicht falsch zu machen, etwa mit einem gemeinsamen `finally`, das `stop()` auch nach einem gescheiterten `start()` aufruft. Das Wissen, wie aufgeräumt wird, gehört zu den Klassen, nicht zu jedem Test.

---

## 6 und 7 · Context Manager und zulässige Zustände

Die Aufgaben 6 und 7 hängen zusammen und werden gemeinsam gelöst.

```python
import logging

# terminate_process und _running_processes wie in Material A

log = logging.getLogger(__name__)


class TestEnvironmentError(Exception):
    """Basis für Fehler der Testumgebung."""


class TerminalAppNotRunning(TestEnvironmentError):
    """Eine Operation erfordert eine laufende Anwendung."""


class CleanupFailed(TestEnvironmentError):
    """Eine Ressource der Testumgebung konnte nicht beendet werden."""


class TestDatabase:
    """Testdatenbank mit definiertem Maschinenzustand.

    Die Datenbank ist nur innerhalb eines with-Blocks geöffnet.
    """

    def __init__(self, path: str) -> None:
        self.path = path
        self._connection: str | None = None

    def __enter__(self) -> "TestDatabase":
        print(f"open test database {self.path}")
        self._connection = f"connection:{self.path}"
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        print(f"close {self._connection}")
        self._connection = None
        return False

    @property
    def connection(self) -> str:
        if self._connection is None:
            raise TestEnvironmentError(f"test database {self.path} is not open")
        return self._connection

    def load_fixture(self, name: str) -> None:
        print(f"load fixture {name} via {self.connection}")


class TerminalApp:
    """Instanz der Terminal-Anwendung für einen Test.

    Die Anwendung läuft nur innerhalb eines with-Blocks und braucht eine
    geöffnete Testdatenbank. Nach dem Block ist der Prozess beendet oder
    ein Fehler beim Beenden gemeldet.
    """

    def __init__(self, database: TestDatabase) -> None:
        self._database = database
        self._process_id: int | None = None

    def __enter__(self) -> "TerminalApp":
        print(f"start terminal app with {self._database.connection}")
        self._process_id = 4711  # Platzhalter für die ID des gestarteten Prozesses
        _running_processes.add(self._process_id)
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        self._stop(pending=exc_value)
        return False

    def send(self, command: str) -> None:
        if self._process_id is None:
            raise TerminalAppNotRunning(f"cannot send {command!r}: terminal app is not running")
        print(f"send {command!r} to process {self._process_id}")

    def _stop(self, pending: BaseException | None) -> None:
        # Siehe Aufgabe 9.
        process_id, self._process_id = self._process_id, None
        print(f"stop terminal app process {process_id}")
        try:
            terminate_process(process_id)
        except OSError as error:
            if pending is None:
                raise CleanupFailed(
                    f"stopping terminal app process {process_id} failed"
                ) from error
            log.error(
                "cleanup failed as well: stopping terminal app process %s: %r", process_id, error
            )
```

Der Test:

```python
def run_alarm_test():
    with TestDatabase("alarm.db") as database:
        database.load_fixture("section_valve_failure")
        with TerminalApp(database) as app:
            app.send("acknowledge_alarm SV-3")
            check_alarm_list(app)
```

**Reihenfolge des Aufräumens:** Die Blöcke werden von innen nach außen verlassen. Zuerst endet die Anwendung, dann die Datenbank. Das entspricht der Abhängigkeit, denn die Anwendung braucht die Datenbank.

**Was aus Aufgabe 3 und 7 geworden ist:**

| Problem | Lösung |
|---|---|
| Anwendung ohne Datenbank | die Datenbank ist Konstruktorparameter, `configure()` entfällt |
| Start mit geschlossener Datenbank | `connection` wirft `TestEnvironmentError` mit Pfad |
| `send()` vor dem Start oder nach dem Ende | `TerminalAppNotRunning` mit dem Befehl in der Meldung |
| `stop()` vergessen | nicht mehr möglich, der Block endet immer |

**Welche der vier Richtungen gewählt wurde:**

| Richtung | verwendet |
|---|---|
| Methode prüft den Zustand | ja, `send()` |
| Konstruktor liefert nur verwendbare Objekte | teilweise, die Datenbank ist Pflicht, der Start erfolgt aber erst in `__enter__` |
| Getrennte Objekte je Zustand | nein |
| Context Manager kapselt Aufbau und Abbau | ja |

Getrennte Objekte wären die strengere Variante:

```python
class TerminalInstallation:
    """Startbare, noch nicht laufende Anwendung."""

    def __init__(self, database: TestDatabase) -> None:
        self._database = database

    def start(self) -> "RunningTerminalApp":
        print(f"start terminal app with {self._database.connection}")
        return RunningTerminalApp(process_id=4711)


class RunningTerminalApp:
    """Laufende Anwendung. Nur dieses Objekt kann Befehle senden."""

    def __init__(self, process_id: int) -> None:
        self._process_id = process_id

    def send(self, command: str) -> None:
        print(f"send {command!r} to process {self._process_id}")
```

Ein nicht gestartetes Objekt hat dann gar kein `send()`. Nach dem Beenden existiert `RunningTerminalApp` aber weiterhin, und das Problem verschiebt sich auf „Senden nach dem Ende". Bei zwei Zuständen ist das mehr Struktur als Gewinn. Bei vier oder fünf Zuständen kann sich das Verhältnis umkehren.

**Die Variante mit `contextlib.contextmanager`:** Sollen die Klassen aus Material A mit `open()`/`close()` und `start()`/`stop()` unverändert bleiben, übernehmen zwei Funktionen die Lebensdauer:

```python
from contextlib import contextmanager


@contextmanager
def open_database(path):
    database = TestDatabase(path)
    database.open()
    try:
        yield database
    finally:
        database.close()


@contextmanager
def running_terminal_app(database):
    app = TerminalApp()
    app.configure(database)
    app.start()
    try:
        yield app
    finally:
        app.stop()


def run_alarm_test():
    with open_database("alarm.db") as database:
        database.load_fixture("section_valve_failure")
        with running_terminal_app(database) as app:
            app.send("acknowledge_alarm SV-3")
            check_alarm_list(app)
```

Das `try/finally` um `yield` ist notwendig. Ohne es laufen `close()` und `stop()` bei einer Exception im `with`-Block nicht.

Diese Variante sichert das Aufräumen, lässt aber die Probleme aus den Aufgaben 3 und 7 bestehen: `send()` vor `start()` bleibt möglich, und `configure()` bleibt ein eigener Schritt. Sie verdeckt sie nur, solange alle Tests die Funktionen verwenden.

---

## 8 · Exceptions statt `return False`

```python
import socket


class SimulatorUnavailable(TestEnvironmentError):
    """Die ECU-Simulation nimmt keine Verbindung an."""


class SimulatorTimeout(SimulatorUnavailable):
    """Der Simulator antwortet nicht rechtzeitig. Ein erneuter Versuch kann helfen."""


class ConfigurationError(TestEnvironmentError):
    """Die Konfiguration der Testumgebung ist fehlerhaft."""


def ensure_simulation_reachable(host: str, port: int = 5020) -> None:
    """Prüft, ob die ECU-Simulation Verbindungen annimmt.

    Raises:
        SimulatorTimeout: keine Antwort innerhalb von 5 Sekunden.
        SimulatorUnavailable: Verbindung abgewiesen.
        ConfigurationError: Hostname nicht auflösbar.
    """
    try:
        connection = socket.create_connection((host, port), timeout=5)
    except TimeoutError as error:
        raise SimulatorTimeout(f"{host}:{port} did not answer within 5 s") from error
    except ConnectionRefusedError as error:
        raise SimulatorUnavailable(f"{host}:{port} refused the connection") from error
    except socket.gaierror as error:
        raise ConfigurationError(f"simulator host {host!r} is unknown") from error
    connection.close()
```

**Wie viele Klassen:** drei neue, dazu die gemeinsame Basis `TestEnvironmentError` aus Aufgabe 6. Das richtet sich nach den Reaktionen aus Aufgabe 4, nicht nach der Zahl der möglichen Ursachen.

| Aufrufer fängt | reagiert auf |
|---|---|
| `SimulatorTimeout` | erneuter Versuch |
| `SimulatorUnavailable` | Timeout und Abweisung, etwa um den Lauf abzubrechen |
| `ConfigurationError` | Konfigurationsfehler, sofortiger Abbruch |
| `TestEnvironmentError` | alle Fehler der Testumgebung |

**Was nicht mehr gefangen wird:** Programmierfehler wie ein `TypeError` laufen ungehindert durch. Andere `OSError`-Fälle, etwa ein unerreichbares Netz, ebenfalls. Sie sind selten und sollten mit ihrer eigenen Meldung sichtbar werden.

**Warum `from error`:** Die ursprüngliche Exception bleibt als `__cause__` erhalten und steht im Traceback. Der Aufrufer bekommt eine Exception der Testumgebung, die Diagnose die technische Ursache.

Der Name der Funktion hat sich geändert. Sie liefert kein Ergebnis mehr, sie stellt etwas sicher oder wirft.

---

## 9 · Der verdrängte Fehler

**Wie es zustande kommt:** In Test 97 stürzte die Anwendung ab. `check_alarm_list` warf deshalb eine Exception. Im `finally` rief der Test `app.stop()` auf, und `terminate_process` (im Original `os.kill`) warf `ProcessLookupError`, weil der Prozess nicht mehr existierte.

Eine Exception, die im `finally` entsteht, **ersetzt** die gerade laufende. Die ursprüngliche hängt nur noch als `__context__` an der neuen. Der vollständige Traceback zeigt beide, mit dem Satz „During handling of the above exception, another exception occurred". Das Protokoll des Nachtlaufs gab aber nur Typ und Meldung der letzten Exception aus.

**Die Gestaltung in `_stop`:**

| Situation | Verhalten |
|---|---|
| Test erfolgreich, Beenden erfolgreich | nichts |
| Test erfolgreich, Beenden scheitert | `CleanupFailed` wird geworfen, mit der technischen Ursache als `__cause__` |
| Test scheitert, Beenden erfolgreich | die ursprüngliche Exception läuft weiter |
| Test scheitert, Beenden scheitert | die ursprüngliche Exception läuft weiter, der Cleanup-Fehler wird zusätzlich protokolliert |

Mit `add_note()` ließe sich der Cleanup-Fehler direkt an die ursprüngliche Exception hängen, er stünde dann im Traceback unter deren Meldung. `add_note()` gibt es aber erst ab Python 3.11, Squish 9.2 bringt Python 3.10 mit. Der Vorschlag protokolliert den Cleanup-Fehler deshalb über `logging`. In einem Squish-Test wäre `test.log` die naheliegende Alternative.

**Was dabei offen bleibt:** Scheitert das Beenden, läuft die Anwendung vielleicht noch. Der Protokolleintrag macht das sichtbar, er räumt aber nicht auf. Ob der nächste Test starten darf, entscheidet damit eine andere Stelle, etwa ein Start, der vorher auf eine übriggebliebene Instanz prüft.

---

## 10 · `TestReport` als Context Manager?

| Dafür | Dagegen |
|---|---|
| Der Bericht würde auch geschrieben, wenn der Lauf abbricht | `TestReport` besitzt während des Sammelns keine Ressource, nur eine Liste |
| Der Aufrufer kann `write()` nicht vergessen | Die Datei ist nur in `write()` geöffnet, und dort reicht ein `with open(...)` |
| | Das Ende des Berichts ist das Ende des Laufs, und das gehört dem Testrunner |

**Vorschlag:** `TestReport` bleibt eine gewöhnliche Klasse. `write()` öffnet die Datei selbst mit `with`. Dass der Bericht auch nach einem Abbruch geschrieben wird, garantiert der Testrunner, etwa mit `try/finally` um den gesamten Lauf.

Das Bedürfnis hinter dem Vorschlag ist berechtigt: Teilergebnisse sollen nicht verloren gehen. Es gehört nur an eine andere Stelle.

---

## 11 · Die Aussage „Aufräumen ist Sache des Tests"

Die Aussage verteilt eine Verantwortung auf 860 Stellen. Ihre Einhaltung lässt sich im Review kaum prüfen, und ein einziger Verstoß genügt für eine Kaskade.

**Vorschlag für eine Teamregel:**

> **MUST:** Ressourcen der Testumgebung, die geöffnet oder gestartet werden, werden über einen Context Manager oder eine Fixture mit `yield` verwaltet. Tests rufen kein `start()`/`stop()` direkt auf.
>
> **MUST:** Ein Fehler beim Aufräumen verdrängt nicht den ursprünglichen Fehler und geht nicht verloren.
>
> **DON'T:** `except Exception` mit `return False` oder `pass` in Code der Testumgebung.

Die zweite Regel ist schwerer zu prüfen als die erste. Sie verlangt einen Test, der beide Fehler gleichzeitig auslöst.

---

## Diskussionsanschluss

Der Umbau verhindert Kaskaden und macht Abstürze sichtbar. Eine Frage beantwortet er nicht: Soll ein Test, dessen Aufräumen scheitert, den nächsten Test verhindern – oder soll der nächste Test selbst prüfen, ob er eine saubere Umgebung vorfindet?
