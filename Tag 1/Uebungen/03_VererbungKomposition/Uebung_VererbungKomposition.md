# Übung · Ist-ein oder braucht-ein?

Sie untersuchen die Testklassen eines GUI-Testprojekts. Alle Tests erben von einer gemeinsamen Basisklasse, einige zusätzlich von Mixins. Der Code funktioniert. Die Frage ist, welche dieser Vererbungsbeziehungen einen Typ modellieren und welche nur Werkzeuge verteilen.

**Es werden keine Squish-Kenntnisse benötigt.** Gerätezugriffe sind durch `print`-Ausgaben ersetzt. Die fachlichen Details sind vereinfacht und erheben keinen Anspruch auf Richtigkeit.

---

## Material A · Die Basisklasse und drei Testklassen

```python
class DeviceDriver:
    """Technischer Zugriff auf die Bedienoberfläche eines Geräts."""

    def click(self, target):
        print(f"click {target}")

    def type_text(self, target, text):
        print(f"type {text!r} into {target}")

    def save_screenshot(self, path):
        print(f"screenshot -> {path}")


class BaseTest:
    """Gemeinsame Basis aller GUI-Tests."""

    def __init__(self):
        self.report_dir = "/var/testreports"
        self.driver = None

    def setup(self):
        self.connect_device()
        self.login()

    def teardown(self):
        self.disconnect_device()

    def connect_device(self):
        print("connect to device on test rack")
        self.driver = DeviceDriver()

    def disconnect_device(self):
        print("disconnect device")

    def login(self, role="operator"):
        print(f"login as {role}")

    def wait_for_screen(self, name, timeout=10):
        print(f"wait up to {timeout} s for screen {name}")

    def log(self, message):
        print(message)

    def reset_device_database(self):
        print("reset device database")

    def write_report(self, message):
        print(f"report: {message}")


class AlarmTest(BaseTest):
    def run(self):
        self.wait_for_screen("WorkScreen")
        self.driver.click("simulateGnssLoss")
        self.wait_for_screen("AlarmGnssLost")
        self.write_report("gnss loss alarm shown")


class ServiceMenuTest(BaseTest):
    def login(self, role="service"):
        super().login(role)

    def reset_device_database(self):
        raise NotImplementedError("service tests must not reset the device")

    def run(self):
        self.wait_for_screen("ServiceMenu")
        self.driver.click("calibration")
        self.write_report("calibration menu reachable")


class ReportExportTest(BaseTest):
    def run(self):
        self.write_report("stored task data export checked")


def run_nightly(tests):
    for test in tests:
        test.setup()
        test.run()
        test.reset_device_database()
        test.teardown()
```

---

## Material B · Die Ergebnisklassen

```python
class TestResult:
    """Ergebnis eines einzelnen Testlaufs."""

    label = "?"

    def __init__(self, test_name, duration):
        self.test_name = test_name
        self.duration = duration

    def is_success(self):
        return False

    def summary(self):
        return f"{self.label:<7} {self.test_name} ({self.duration:.1f} s)"


class PassedResult(TestResult):
    label = "PASSED"

    def is_success(self):
        return True


class FailedResult(TestResult):
    label = "FAILED"

    def __init__(self, test_name, duration, reason):
        super().__init__(test_name, duration)
        self.reason = reason

    def summary(self):
        return f"{super().summary()}: {self.reason}"


# aus dem Nachtbericht
def nightly_summary(results):
    failed = [r for r in results if isinstance(r, FailedResult)]
    for result in results:
        print(result.summary())
    print(f"{len(failed)} failed, all green: {all(r.is_success() for r in results)}")
```

Ein Vorschlag aus dem Team für Tests, die erst im zweiten Versuch bestehen:

```python
class RetriedResult(FailedResult):
    label = "RETRIED"

    def is_success(self):
        return True
```

---

## Material C · Zwei Mixins

```python
class LoggingMixin:
    def log(self, message):
        print(f"[{self.test_id}] {message}")


class ScreenshotMixin:
    def capture(self, name):
        path = f"{self.report_dir}/{name}.png"
        self.driver.save_screenshot(path)
        self.log(f"screenshot {path}")


class SectionControlTest(ScreenshotMixin, LoggingMixin, BaseTest):
    def __init__(self):
        super().__init__()
        self.test_id = "SC-017"

    def run(self):
        self.wait_for_screen("ImplementSelection")
        self.driver.click("startSectionControl")
        self.capture("section-control-started")
```

---

## Material D · Eine neue Anforderung

Für die Konformitätsprüfung soll **jede Bedienaktion am Gerät protokolliert** werden: Klicks und Texteingaben, mit dem Ziel der Aktion. Die Testklassen sollen dafür nicht geändert werden.

---

## Aufgabe

### Teil 1 · Lesen und einordnen

**1.** Legen Sie eine Tabelle an: Ist `AlarmTest`, `ServiceMenuTest` und `ReportExportTest` jeweils eine Spezialisierung von `BaseTest`, oder benutzt die Klasse nur einen Teil seiner Werkzeuge? Welche Methoden von `BaseTest` braucht jede Klasse tatsächlich?

**2.** `ServiceMenuTest` überschreibt `reset_device_database()` mit einer Exception. Was passiert in `run_nightly()`? Was sagt das über die Beziehung „ein `ServiceMenuTest` ist ein `BaseTest`"?

**3.** Welche Voraussetzungen stellt `ScreenshotMixin.capture()` an `self`? Wo im Code sind diese Voraussetzungen sichtbar, und was passiert, wenn `capture()` vor `setup()` aufgerufen wird?

### Teil 2 · Umbauen

**4.** Schreiben Sie `AlarmTest` und `ReportExportTest` so um, dass sie nicht mehr von `BaseTest` erben, sondern die benötigten Fähigkeiten als Kollaborateure erhalten. Wie sieht die Stelle aus, an der ein Test zusammengesetzt wird?

**5.** Setzen Sie die Anforderung aus Material D um, ohne `DeviceDriver` und die Testklassen zu ändern. Warum ist Ihre Lösung keine Unterklasse von `DeviceDriver`, oder warum doch?

**6.** Prüfen Sie die Ergebnisklassen aus Material B. Trägt hier die Vererbung? Passt der Vorschlag `RetriedResult(FailedResult)` in diese Hierarchie? Was würde `nightly_summary()` für einen `RetriedResult` ausgeben?

### Teil 3 · Abwägen

**7.** Welche Kosten hat Ihre Lösung aus Aufgabe 4 gegenüber der Basisklasse? Nennen Sie mindestens zwei.

**8.** `SectionControlTest` erbt von `ScreenshotMixin`, `LoggingMixin` und `BaseTest`, und sowohl `LoggingMixin` als auch `BaseTest` definieren `log()`. Welche Methode wird in `capture()` aufgerufen? Was ändert sich, wenn die Reihenfolge der Basisklassen umgedreht wird?

**9.** Nennen Sie einen Fall aus Ihrem eigenen Testcode, in dem Vererbung die passende Beziehung ist. Woran machen Sie das fest?

---

## Hinweise zur Bearbeitung

- Der Code muss nicht ausgeführt werden. Er sollte aber so geschrieben sein, dass er lauffähig wäre.
- Wer die Kollaborateure erzeugt und übergibt, ist Thema der Einheit 1-5. Hier genügt eine einfache Zusammensetzung von Hand.
- Wenn Sie unsicher sind, ob eine Vererbung bleiben sollte, fragen Sie: **Kann die Unterklasse überall dort stehen, wo die Basisklasse erwartet wird?**
- Für die Aufgaben 1 bis 3 genügen Stichpunkte.
