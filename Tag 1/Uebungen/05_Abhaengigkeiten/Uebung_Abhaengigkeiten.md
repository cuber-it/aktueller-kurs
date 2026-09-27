# Übung · Wovon hängt dieser Workflow ab?

Sie untersuchen einen Workflow aus der GUI-Testsuite eines Landmaschinen-Terminals. Er legt einen Auftrag an und prüft, ob das Terminal die richtige Ausbringmenge anzeigt. Der Code funktioniert auf dem Prüfstand. Die Frage ist, was er zum Arbeiten braucht und wie man das von außen erkennt.

**Es werden keine Squish-Kenntnisse benötigt.** Der Zugriff auf das Terminal ist durch `print`-Platzhalter ersetzt. Die fachliche Regel ist vereinfacht und erhebt keinen Anspruch auf Richtigkeit.

---

## Material A · Der Workflow

```python
from datetime import date
from decimal import ROUND_HALF_UP, Decimal

from environment import CONFIG, HtmlReporter, TaskService, TerminalClient


class ApplicationWorkflow:
    """Legt einen Auftrag an und prüft die angezeigte Ausbringmenge."""

    def execute(self, field_id, area_ha, product):
        terminal = TerminalClient.connect(CONFIG["terminal_host"])
        rate = TaskService.instance().rate_for(product)
        expected = self._expected_volume(area_ha, rate)

        terminal.open_task_form()
        terminal.enter_task(field_id, area_ha, product)
        passed = terminal.read_volume() == expected

        reporter = HtmlReporter(CONFIG["report_dir"])
        reporter.record("application", passed)
        if date.today().weekday() >= 5:
            reporter.note("weekend run")
        return passed

    def _expected_volume(self, area_ha, rate):
        volume = max(Decimal("5.00"), area_ha * rate)
        return volume.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
```

---

## Material B · Das Modul `environment`

```python
CONFIG = {
    "terminal_host": "terminal-01",
    "report_dir": r"\\teststand\reports",
    "task_url": "https://tasks.test.internal/api",
}


class TaskService:
    """Liefert Aufwandmengen je Produkt aus dem Auftragsserver des Testbackends."""

    _instance = None

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls(CONFIG["task_url"])
        return cls._instance

    def __init__(self, url):
        self._url = url

    def rate_for(self, product):
        print(f"GET {self._url}/products/{product}/rate")
        ...


class TerminalClient:
    @classmethod
    def connect(cls, host):
        print(f"attach to terminal on {host}")
        return cls()

    def open_task_form(self):
        print("click: menu 'Auftrag'")

    def enter_task(self, field_id, area_ha, product):
        print(f"type: {field_id}, {area_ha} ha, {product}")

    def read_volume(self):
        print("read: label 'Menge'")
        ...


class HtmlReporter:
    def __init__(self, directory):
        self._directory = directory

    def record(self, name, passed):
        print(f"{self._directory}: {name} -> {passed}")

    def note(self, text):
        print(f"{self._directory}: note {text}")
```

---

## Material C · Ein zweiter Vorschlag aus dem Team

Ein Kollege hat eine Variante mit einer zentralen Registry gebaut, „damit man alles austauschen kann":

```python
class Registry:
    _services = {}

    @classmethod
    def register(cls, name, service):
        cls._services[name] = service

    @classmethod
    def get(cls, name):
        return cls._services[name]


class ApplicationWorkflow:
    def execute(self, field_id, area_ha, product):
        terminal = Registry.get("terminal")
        rate = Registry.get("tasks").rate_for(product)
        reporter = Registry.get("reporter")
        ...
```

---

## Material D · Eine neue Mengenregel und ein Entwurf dazu

Neue Regel: **Ab einer Auftragsfläche von 10 ha zieht das Terminal 2 % Randabzug von der Menge ab.** Die Mindestmenge von 5 l bleibt.

Eine Entwicklerin möchte die neue Regel prüfen, bevor sie in den Nachtlauf geht. Auf ihrem Rechner gibt es weder ein Terminal noch Zugang zum Testbackend oder zur Netzwerkfreigabe für Reports.

Ein anderer Kollege schlägt für die Mengenberechnung folgenden Entwurf vor:

```python
class VolumeCalculator:
    def __init__(self, rounding_strategy, minimum_provider, factor_strategy):
        self._rounding = rounding_strategy
        self._minimum = minimum_provider
        self._factor = factor_strategy

    def volume(self, area_ha, rate):
        raw = max(self._minimum.get(), area_ha * rate * self._factor.for_area(area_ha))
        return self._rounding.apply(raw)
```

---

## Aufgabe

### Teil 1 · Abhängigkeiten sichtbar machen

**1.** Legen Sie eine Tabelle an: Von welchen Objekten, Werten und Funktionen hängt `ApplicationWorkflow.execute` ab? Geben Sie für jede Abhängigkeit an, wie sie beschafft wird und ob sie an der Signatur von `execute` oder am Konstruktor erkennbar ist.

**2.** Was müsste vorbereitet oder ersetzt werden, um nur die Methode `_expected_volume` zu prüfen? Was, um zu prüfen, dass `execute` ein fehlgeschlagenes Ergebnis an den Reporter meldet?

**3.** Ist die Abhängigkeit in der Registry-Variante aus Material C sichtbarer geworden? Woran erkennt ein Aufrufer, was `ApplicationWorkflow` braucht?

### Teil 2 · Umbauen

**4.** Bauen Sie `ApplicationWorkflow` so um, dass die wesentlichen Kollaborateure von außen übergeben werden. Entscheiden Sie für jede Abhängigkeit aus Aufgabe 1: über den Konstruktor, über die Methode, als Wert statt als Dienst, oder bleibt sie konkret?

**5.** Setzen Sie die neue Mengenregel aus Material D um. Schreiben Sie Tests für die Regel, die ohne Terminal, Backend und Netzwerkfreigabe laufen. Berücksichtigen Sie die Grenze bei 10 ha und die Mindestmenge.

**6.** Schreiben Sie einen Test, der prüft, dass `execute` bei abweichender Menge `False` zurückgibt und das Ergebnis an den Reporter meldet. Welche Art von Test Double verwenden Sie für welchen Kollaborateur?

**7.** Jemand schlägt vor, den Reporter optional zu machen: `def __init__(self, ..., reporter=None)` und im Konstruktor `self._reporter = reporter or HtmlReporter(CONFIG["report_dir"])`. Welche Folgen hat das? Prüfen Sie auch, was passiert, wenn ein Test-Reporter `__len__` definiert und noch keine Einträge hat.

### Teil 3 · Abwägen

**8.** Der Workflow braucht vom Terminal drei Operationen. Beschreiben Sie den Vertrag, den der Workflow tatsächlich benötigt. Wem gehört dieser Vertrag – dem Workflow oder dem Terminal-Client?

**9.** Bewerten Sie den Entwurf `VolumeCalculator` aus Material D. Welche der drei injizierten Strategien lässt sich mit einer realen Änderung oder einem Testbedarf begründen?

**10.** `date.today()` entscheidet, ob eine Notiz geschrieben wird. Würden Sie diese Abhängigkeit injizieren? Begründen Sie Ihre Entscheidung und nennen Sie, was dagegen spräche.

---

## Hinweise zur Bearbeitung

- Der Code muss nicht ausgeführt werden. Er sollte aber so geschrieben sein, dass er lauffähig wäre.
- Ein DI-Framework oder Container wird nicht benötigt. Konstruktor- und Methodenparameter genügen.
- Nicht jede Abhängigkeit muss injiziert werden. Fragen Sie für jede: **Welche Änderung oder welcher Test rechtfertigt die Übergabe von außen?**
- Für die Aufgaben 1 bis 3 genügen Stichpunkte und eine Tabelle.
