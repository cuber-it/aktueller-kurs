# Lösungsvorschlag · Ist-ein oder braucht-ein?

**Vorbemerkung:** Ein Vorschlag, keine Musterlösung. Bei mehreren Aufgaben sind andere Schnitte vertretbar. Bewertet wird, ob jede Beziehung **die Aussage macht, die zwischen den Klassen tatsächlich besteht**.

---

## 1 · Spezialisierung oder Werkzeugnutzung?

| Klasse | Genutzte Methoden von `BaseTest` | Spezialisierung? |
|---|---|---|
| `AlarmTest` | `setup`, `teardown`, `wait_for_screen`, `write_report`, `driver` | nein, ein Test, der Gerät, Warten und Bericht benutzt |
| `ServiceMenuTest` | `setup`, `teardown`, `login` (überschrieben), `wait_for_screen`, `write_report`, `driver` | nein, und er verweigert zusätzlich `reset_device_database` |
| `ReportExportTest` | `write_report` | nein, er braucht nur den Bericht, erbt aber die Geräteverbindung |

**Was die Tabelle zeigt:** Keine der drei Klassen wird irgendwo als `BaseTest` behandelt, außer im Runner, und der braucht nur `setup`, `run`, `teardown` und `reset_device_database`. Die Vererbung verteilt Werkzeuge. Einen Typ, mit dem Aufrufer arbeiten, modelliert sie kaum.

---

## 2 · `ServiceMenuTest` und der Nachtlauf

`run_nightly()` ruft für jeden Test nacheinander `setup()`, `run()`, `reset_device_database()` und `teardown()` auf. Beim `ServiceMenuTest` wirft der dritte Aufruf `NotImplementedError`:

```
connect to device on test rack
login as service
wait up to 10 s for screen ServiceMenu
click calibration
report: calibration menu reachable
NotImplementedError: service tests must not reset the device
```

**Die Folgen:** Der Nachtlauf bricht ab. `teardown()` wird für diesen Test nicht mehr aufgerufen, das Gerät bleibt verbunden. Alle folgenden Tests laufen nicht.

**Was das über die Beziehung sagt:** `BaseTest` sagt zu: „Jeder Test kann die Gerätedatenbank zurücksetzen." `ServiceMenuTest` hält diese Zusage nicht ein. Er kann deshalb nicht überall stehen, wo ein `BaseTest` erwartet wird, und der Runner braucht eine Sonderbehandlung. Die Aussage „ein `ServiceMenuTest` ist ein `BaseTest`" trifft nicht zu.

Der Grund für die Verweigerung ist fachlich richtig: Der Reset löscht die Kalibrierwerte. Falsch ist die Annahme in `BaseTest`, dass jeder Test zurücksetzen will.

---

## 3 · Die Voraussetzungen von `ScreenshotMixin`

| Voraussetzung | Woher sie kommt | Wo sie sichtbar ist |
|---|---|---|
| `self.report_dir` | `BaseTest.__init__` | nirgends im Mixin |
| `self.driver` mit `save_screenshot()` | `BaseTest.connect_device`, also erst nach `setup()` | nirgends im Mixin |
| `self.log()` | `LoggingMixin` oder `BaseTest`, je nach Reihenfolge | nirgends im Mixin |
| `self.test_id` | `SectionControlTest.__init__`, gebraucht von `LoggingMixin.log` | nirgends in beiden Mixins |

**Vor `setup()`** ist `self.driver` noch `None`. Der Aufruf bricht ab mit:

```
AttributeError: 'NoneType' object has no attribute 'save_screenshot'
```

Die Meldung nennt weder das Mixin noch die fehlende Vorbedingung. Wer sie liest, muss die Klassenhierarchie kennen, um sie zu verstehen.

---

## 4 · `AlarmTest` und `ReportExportTest` mit Kollaborateuren

Die Fähigkeiten aus `BaseTest` werden eigene Objekte. `DeviceDriver` bleibt unverändert.

```python
class DeviceSession:
    """Verbindung zu einem Gerät auf dem Testrack mit einer angemeldeten Rolle."""

    def __init__(self, role: str) -> None:
        self._role = role

    def connect(self) -> DeviceDriver:
        print("connect to device on test rack")
        print(f"login as {self._role}")
        return DeviceDriver()

    def disconnect(self) -> None:
        print("disconnect device")


class ScreenWaiter:
    """Wartet auf Bildschirme. Der Timeout gilt für alle Wartevorgänge dieser Instanz."""

    def __init__(self, timeout: float) -> None:
        self.timeout = timeout

    def wait_for(self, screen: str) -> None:
        print(f"wait up to {self.timeout} s for screen {screen}")


class Reporter:
    def write(self, message: str) -> None:
        print(f"report: {message}")


class AlarmTest:
    """Prüft, dass ein simulierter Verschluss den Verschlussalarm auslöst."""

    def __init__(
        self, session: DeviceSession, waiter: ScreenWaiter, reporter: Reporter
    ) -> None:
        self._session = session
        self._waiter = waiter
        self._reporter = reporter
        self._driver: DeviceDriver | None = None

    def setup(self) -> None:
        self._driver = self._session.connect()

    def run(self) -> None:
        self._waiter.wait_for("WorkScreen")
        self._driver.click("simulateGnssLoss")
        self._waiter.wait_for("AlarmGnssLost")
        self._reporter.write("gnss loss alarm shown")

    def teardown(self) -> None:
        self._session.disconnect()


class ReportExportTest:
    """Prüft einen gespeicherten TaskData-Export. Braucht kein Gerät."""

    def __init__(self, reporter: Reporter) -> None:
        self._reporter = reporter

    def setup(self) -> None:
        pass

    def run(self) -> None:
        self._reporter.write("stored task data export checked")

    def teardown(self) -> None:
        pass
```

**Die Stelle, an der zusammengesetzt wird:**

```python
def run_nightly(tests):
    for test in tests:
        test.setup()
        test.run()
        test.teardown()


reporter = Reporter()
run_nightly([
    AlarmTest(DeviceSession("operator"), ScreenWaiter(timeout=5), reporter),
    ReportExportTest(reporter),
])
```

**Was sich geändert hat:**

| Kriterium | Vorher | Nachher |
|---|---|---|
| Was ein Test braucht | nur durch Lesen von `run()` erkennbar | am Konstruktor ablesbar |
| Geräteverbindung für den Exporttest | über `setup()` geerbt | keine, er erhält keine `DeviceSession` |
| Timeout der Alarmtests | Default der Basisklasse oder an jeder Aufrufstelle | einmal am `ScreenWaiter` der Alarmtests |
| Reset der Gerätedatenbank | Pflicht im Runner für alle | nur für Tests, die einen Reset-Kollaborateur erhalten |

Der Runner ruft den Reset nicht mehr auf. Damit entfällt der Konflikt mit `ServiceMenuTest`: Ein Servicetest erhält schlicht keinen Kollaborateur für den Reset.

`setup()` und `teardown()` des Exporttests sind leer, weil der Runner sie verlangt. Sie machen sichtbar, dass dieser Test keinen Lebenszyklus hat. Wie sich `setup` und `teardown` im Fehlerfall verhalten, ist Thema der Einheit 1-6.

---

## 5 · Protokollierung der Bedienaktionen durch Delegation

```python
class RecordingDriver:
    """Protokolliert jede Bedienaktion und reicht sie an den eigentlichen Treiber weiter.

    Eingegebene Texte werden nicht protokolliert, nur ihr Ziel.
    """

    def __init__(self, driver: DeviceDriver, audit_log: list[str]) -> None:
        self._driver = driver
        self._audit_log = audit_log

    def click(self, target: str) -> None:
        self._audit_log.append(f"click {target}")
        self._driver.click(target)

    def type_text(self, target: str, text: str) -> None:
        self._audit_log.append(f"type into {target}")
        self._driver.type_text(target, text)

    def save_screenshot(self, path: str) -> None:
        self._driver.save_screenshot(path)
```

Eingesetzt wird der Wrapper an der Stelle, die den Treiber erzeugt, also in `DeviceSession`:

```python
class DeviceSession:
    """Verbindung zu einem Gerät auf dem Testrack. Jede Bedienaktion wird protokolliert."""

    def __init__(self, role: str, audit_log: list[str]) -> None:
        self._role = role
        self._audit_log = audit_log

    def connect(self) -> RecordingDriver:
        print("connect to device on test rack")
        print(f"login as {self._role}")
        return RecordingDriver(DeviceDriver(), self._audit_log)

    def disconnect(self) -> None:
        print("disconnect device")


audit_log: list[str] = []
test = AlarmTest(DeviceSession("operator", audit_log), ScreenWaiter(timeout=5), Reporter())
```

Die Testklassen rufen weiter `click()` auf. `DeviceDriver` bleibt unverändert. Geändert haben sich nur die Session und die Stelle, an der sie erzeugt wird.

Für einen Typprüfer passt die Annotation `DeviceDriver` in `AlarmTest` danach nicht mehr, weil `RecordingDriver` keine Unterklasse ist. Zur Laufzeit genügt, dass beide dieselben Methoden anbieten. Wie man diesen Vertrag ausdrücklich beschreibt, ist Thema der Einheit 1-4.

**Warum keine Unterklasse von `DeviceDriver`?** Eine Unterklasse `RecordingDriver(DeviceDriver)` würde für genau diesen Treiber funktionieren. Zwei Punkte sprechen dagegen:

| | Unterklasse | Wrapper |
|---|---|---|
| Andere Treiber, etwa ein Simulator | eigene Unterklasse je Treiber | derselbe Wrapper um jeden Treiber |
| Neue Methode im Treiber, z. B. `swipe()` | wird geerbt und ohne Protokoll ausgeführt | fehlt im Wrapper, Aufruf bricht mit `AttributeError` ab |

Die zweite Zeile ist eine Abwägung. Für ein Konformitätsprotokoll ist ein lauter Abbruch besser als eine stille Lücke. Ein `__getattr__`, das unbekannte Methoden automatisch weiterreicht, würde die Lücke wieder still machen.

---

## 6 · Die Ergebnisklassen

**Die Vererbung trägt.** `nightly_summary()` arbeitet mit dem Basistyp: Es ruft `summary()` und `is_success()` für jedes Ergebnis auf, ohne zu wissen, welches es ist. `PassedResult` und `FailedResult` halten den Vertrag von `TestResult` ein und können überall stehen, wo ein Ergebnis erwartet wird.

**`RetriedResult(FailedResult)` passt nicht.** Die Klasse erbt „ist ein Fehlschlag" und sagt zugleich mit `is_success()`, sie sei erfolgreich. Beide Aussagen gelten gleichzeitig:

```python
nightly_summary([
    PassedResult("alarm_gnss_lost", 1.4),
    RetriedResult("section_control_start", 9.1, "first attempt timeout"),
])
```

```
PASSED  alarm_gnss_lost (1.4 s)
RETRIED section_control_start (9.1 s): first attempt timeout
1 failed, all green: True
```

Der Bericht meldet einen Fehlschlag und zugleich „alles grün". Die Ursache ist die Typprüfung `isinstance(r, FailedResult)`, die sich auf die Hierarchie verlässt, während `is_success()` etwas anderes sagt.

**Ein Vorschlag:** Ein wiederholter Test ist bestanden. Er gehört unter `PassedResult` und trägt den ersten Fehlschlag als Information mit. Der Bericht zählt über den Vertrag statt über den Typ.

```python
class RetriedResult(PassedResult):
    label = "RETRIED"

    def __init__(self, test_name, duration, first_failure):
        super().__init__(test_name, duration)
        self.first_failure = first_failure

    def summary(self):
        return f"{super().summary()} after: {self.first_failure}"


def nightly_summary(results):
    failed = [r for r in results if not r.is_success()]
    for result in results:
        print(result.summary())
    print(f"{len(failed)} failed, all green: {not failed}")
```

Ob ein wiederholter Test als bestanden gelten soll, ist eine fachliche Entscheidung des Teams. Die Hierarchie sollte sie abbilden, nicht offenlassen.

---

## 7 · Die Kosten der Komposition

| Kosten | Konkret |
|---|---|
| Mehr Objekte | `DeviceSession`, `ScreenWaiter`, `Reporter` statt einer Basisklasse |
| Zusammensetzung muss irgendwo stattfinden | jemand erzeugt für 212 Tests die passenden Kollaborateure |
| Weniger Entdeckbarkeit | `self.` plus Autovervollständigung zeigt nicht mehr alle Werkzeuge |
| Runner-Vertrag wird explizit | Tests ohne Lebenszyklus brauchen leere `setup()`/`teardown()` |
| Delegationscode | Wrapper müssen jede Methode einzeln weiterreichen |
| Übergangszeit | alte und neue Tests existieren nebeneinander |

Die Zusammensetzung übernimmt in pytest-basierten Suiten meist eine Fixture. Wie Abhängigkeiten übergeben werden, vertieft die Einheit 1-5.

---

## 8 · Welche `log()`-Methode gilt?

Python sucht Methoden entlang der Method Resolution Order (MRO) der Klasse:

```python
print([cls.__name__ for cls in SectionControlTest.__mro__])
# ['SectionControlTest', 'ScreenshotMixin', 'LoggingMixin', 'BaseTest', 'object']
```

`capture()` ruft `self.log()` auf. Gefunden wird zuerst `LoggingMixin.log`, die Ausgabe lautet:

```
[SC-017] screenshot /var/testreports/section-control-started.png
```

**Mit umgekehrter Reihenfolge** `class SectionControlTest(BaseTest, LoggingMixin, ScreenshotMixin)` lautet die MRO `SectionControlTest, BaseTest, LoggingMixin, ScreenshotMixin, object`. Jetzt gilt `BaseTest.log`, und die Ausgabe enthält keine Test-ID mehr:

```
screenshot /var/testreports/section-control-started.png
```

**Was das zeigt:** Welche Methode ausgeführt wird, entscheidet die Reihenfolge in der Klassendeklaration. An der Aufrufstelle `self.log(...)` ist das nicht zu sehen. Mit einem übergebenen Logger stünde am Konstruktor, welcher Logger benutzt wird.

---

## 9 · Vererbung im eigenen Testcode

Die Antworten sind individuell. Beispiele, bei denen Vererbung in der Regel trägt:

| Fall | Warum die Typbeziehung besteht |
|---|---|
| Ergebnistypen wie in Material B | Aufrufer arbeiten mit dem Basistyp |
| Eigene Exception-Hierarchie, z. B. `UIObjectNotFound(TestAutomationError)` | `except TestAutomationError` fängt alle Untertypen, das ist der Zweck der Hierarchie |
| Varianten eines Kommunikationsprotokolls mit gemeinsamem Vertrag | der Aufrufer kennt nur den Vertrag |

Der Prüfstein in allen drei Fällen: Es gibt einen Aufrufer, der mit dem Basistyp arbeitet und die Unterklasse nicht kennen muss.

---

## Diskussionsanschluss

Der Umbau hat die Vererbung bei den Tests entfernt und bei den Ergebnissen behalten. Welche Regel für den Teamstandard würden Sie aus dieser Unterscheidung ableiten?
