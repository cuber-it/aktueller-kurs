# Lösungsvorschlag · Wovon hängt dieser Workflow ab?

**Vorbemerkung:** Ein Vorschlag, keine Musterlösung. Welche Abhängigkeit übergeben wird und welche konkret bleibt, ist an mehreren Stellen Ermessenssache. Bewertet wird, ob jede Entscheidung **mit einer Änderung oder einem Testbedarf begründet** ist.

---

## 1 · Die Abhängigkeiten von `execute`

| Abhängigkeit | Wie beschafft | an Signatur oder Konstruktor erkennbar |
|---|---|---|
| Terminal | `TerminalClient.connect(...)` in `execute` | nein |
| Adresse des Terminals | globales `CONFIG["terminal_host"]` | nein |
| Dienst für Aufwandmengen | Singleton `TaskService.instance()` | nein |
| URL des Testbackends | `CONFIG["task_url"]`, beim ersten Zugriff auf das Singleton | nein |
| Reporter | `HtmlReporter(...)` in `execute` | nein |
| Report-Verzeichnis | globales `CONFIG["report_dir"]` | nein |
| aktuelles Datum | `date.today()` | nein |
| Mengenregel | private Methode `_expected_volume` | nein |
| `Decimal`, `max`, `quantize` | Standardbibliothek | nein, muss es auch nicht |
| Feld, Fläche, Produkt | Parameter | ja |

**Nur die fachlichen Eingaben sind sichtbar.** Alles, was der Workflow zum Arbeiten braucht, steht in der Implementierung.

---

## 2 · Was ein Test heute vorbereiten müsste

**Für `_expected_volume` allein:** technisch nichts. `ApplicationWorkflow()._expected_volume(Decimal("5"), Decimal("20"))` läuft ohne Prüfstand, sofern das Modul `environment` importierbar ist. Der Test hängt dann aber an einer privaten Methode und damit an einem Implementierungsdetail. Die Regel ist prüfbar, aber nur über eine Hintertür.

**Für „`execute` meldet ein Fehlergebnis an den Reporter":**

| Zu ersetzen | Warum |
|---|---|
| `TerminalClient.connect` | verbindet sonst mit dem Terminal |
| `TaskService.instance` oder `TaskService._instance` | fragt sonst das Testbackend |
| `HtmlReporter` | schreibt sonst auf die Netzwerkfreigabe; außerdem muss der Test an das erzeugte Objekt herankommen, um die Meldung zu prüfen |
| `date.today` | sonst hängt das Ergebnis vom Wochentag ab |

Alle vier lassen sich nur von außen per `mock.patch` ersetzen, jeweils mit dem Modulpfad als String. Das ist der Test mit 43 Zeilen Vorbereitung aus dem Ticket.

---

## 3 · Die Registry

Sichtbarer ist nichts geworden. `ApplicationWorkflow()` hat weiterhin keinen Parameter. Welche Namen der Workflow aus der Registry holt, steht nur in `execute`.

Hinzu kommen neue Probleme:

- Ein Test muss wissen, dass er `"terminal"`, `"tasks"` und `"reporter"` registrieren muss. Vergisst er einen, gibt es einen `KeyError` mitten im Ablauf.
- `_services` ist ein Klassenattribut. Was ein Test registriert, bleibt für den nächsten Test stehen, bis jemand es entfernt.
- Tippfehler im Namen fallen erst zur Laufzeit auf.

Die Registry macht **austauschbar**, aber nicht **sichtbar**. Sie ist ein Service Locator.

---

## 4 · Der Umbau

```python
from datetime import date
from decimal import ROUND_HALF_UP, Decimal
from typing import Callable, Protocol

MIN_VOLUME_L = Decimal("5.00")


def expected_volume(area_ha: Decimal, rate: Decimal) -> Decimal:
    """Erwartete Ausbringmenge in Litern für einen Auftrag.

    area_ha ist die Auftragsfläche in Hektar, rate die Aufwandmenge in Litern je Hektar.
    """
    volume = max(MIN_VOLUME_L, area_ha * rate)
    return volume.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


class TaskForm(Protocol):
    def open_task_form(self) -> None: ...
    def enter_task(self, field_id: str, area_ha: Decimal, product: str) -> None: ...
    def read_volume(self) -> Decimal: ...


class RateSource(Protocol):
    def rate_for(self, product: str) -> Decimal: ...


class ResultReporter(Protocol):
    def record(self, name: str, passed: bool) -> None: ...
    def note(self, text: str) -> None: ...


class ApplicationWorkflow:
    """Legt einen Auftrag an und prüft die angezeigte Ausbringmenge."""

    def __init__(
        self,
        form: TaskForm,
        rates: RateSource,
        reporter: ResultReporter,
        today: Callable[[], date] = date.today,
    ) -> None:
        self._form = form
        self._rates = rates
        self._reporter = reporter
        self._today = today

    def execute(self, field_id: str, area_ha: Decimal, product: str) -> bool:
        expected = expected_volume(area_ha, self._rates.rate_for(product))
        self._form.open_task_form()
        self._form.enter_task(field_id, area_ha, product)
        passed = self._form.read_volume() == expected
        self._reporter.record("application", passed)
        if self._today().weekday() >= 5:
            self._reporter.note("weekend run")
        return passed
```

Zusammengesetzt wird an einer Stelle, und nur dort wird `CONFIG` gelesen:

```python
from environment import CONFIG, HtmlReporter, TaskService, TerminalClient


def build_application_workflow() -> ApplicationWorkflow:
    return ApplicationWorkflow(
        form=TerminalClient.connect(CONFIG["terminal_host"]),
        rates=TaskService(CONFIG["task_url"]),
        reporter=HtmlReporter(CONFIG["report_dir"]),
    )
```

**Die Entscheidungen im Einzelnen:**

| Abhängigkeit | Entscheidung | Begründung |
|---|---|---|
| Terminal | Konstruktor | dauerhaft gebraucht, verbindet mit einem Gerät |
| Dienst für Aufwandmengen | Konstruktor | dauerhaft gebraucht, Netzwerkzugriff |
| Reporter | Konstruktor | dauerhaft gebraucht, schreibt nach außen |
| `CONFIG` | nur in `build_application_workflow` | der Workflow braucht die Objekte, nicht die Konfiguration |
| Singleton `TaskService.instance()` | entfällt | wie viele Instanzen es gibt, entscheidet die Stelle, die zusammensetzt |
| Datum | Default-Parameter `today=date.today` | harmloser Standard, nur Tests ersetzen ihn (siehe Aufgabe 10) |
| Mengenregel | herausgelöst als Funktion `expected_volume` | reine Rechnung auf Werten, braucht keinen Dienst |
| Aufwandmenge für die Regel | als Wert übergeben | `expected_volume` braucht die Aufwandmenge, nicht den Dienst |
| `Decimal`, `max`, `quantize` | bleiben konkret | keine Variante, keine Seiteneffekte |

---

## 5 · Die neue Mengenregel und ihre Tests

```python
THRESHOLD_HA = Decimal("10")


def expected_volume(area_ha: Decimal, rate: Decimal) -> Decimal:
    """Erwartete Ausbringmenge in Litern für einen Auftrag.

    Ab 10 ha Auftragsfläche werden 2 % Randabzug abgezogen, mindestens
    aber 5 l ausgebracht. Kaufmännisch auf 0,01 l gerundet.
    """
    factor = Decimal("0.98") if area_ha >= THRESHOLD_HA else Decimal("1")
    volume = max(MIN_VOLUME_L, area_ha * rate * factor)
    return volume.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
```

```python
from decimal import Decimal


def test_minimum_volume_applies_to_small_tasks():
    assert expected_volume(Decimal("0.2"), Decimal("20")) == Decimal("5.00")


def test_full_rate_below_threshold():
    assert expected_volume(Decimal("5"), Decimal("20")) == Decimal("100.00")


def test_rounds_half_up():
    # 9,95 * 1,5 = 14,925
    assert expected_volume(Decimal("9.95"), Decimal("1.5")) == Decimal("14.93")


def test_edge_deduction_at_threshold():
    assert expected_volume(Decimal("10"), Decimal("20")) == Decimal("196.00")


def test_minimum_compares_total_volume_not_rate():
    # 2 ha zu 3 l/ha sind 6 l, also über der Mindestmenge
    assert expected_volume(Decimal("2"), Decimal("3")) == Decimal("6.00")
```

Der letzte Test hält einen naheliegenden Fehler fest: Wird die Mindestmenge mit der Aufwandmenge je Hektar verglichen statt mit der Gesamtmenge, ergibt sich max(5, 3) × 2 = 10 l statt 6 l.

**Eine fachliche Auffälligkeit:** Bei 9,99 ha und 20 l/ha erwartet die Regel 199,80 l, bei 10 ha nur 196,00 l. Mehr Fläche, weniger Menge. Das ist keine Frage an den Code, sondern an die Applikationstechnik. Die Tests an der Grenze machen sie sichtbar.

---

## 6 · Der Workflow-Test

```python
from datetime import date
from decimal import Decimal
from typing import Optional, Tuple


class FixedRates:
    """Stub: liefert für jedes Produkt dieselbe Aufwandmenge."""

    def __init__(self, rate: Decimal) -> None:
        self._rate = rate

    def rate_for(self, product: str) -> Decimal:
        return self._rate


class StubTaskForm:
    """Stub: zeigt eine vorgegebene Menge an und merkt sich die Eingabe."""

    def __init__(self, shown_volume: Decimal) -> None:
        self._shown_volume = shown_volume
        self.entered: Optional[Tuple[str, Decimal, str]] = None

    def open_task_form(self) -> None:
        pass

    def enter_task(self, field_id: str, area_ha: Decimal, product: str) -> None:
        self.entered = (field_id, area_ha, product)

    def read_volume(self) -> Decimal:
        return self._shown_volume


class RecordingReporter:
    """Spy: zeichnet Ergebnisse und Notizen auf."""

    def __init__(self) -> None:
        self.records: list = []
        self.notes: list = []

    def record(self, name: str, passed: bool) -> None:
        self.records.append((name, passed))

    def note(self, text: str) -> None:
        self.notes.append(text)


MONDAY = date(2026, 9, 21)
SATURDAY = date(2026, 9, 19)


def test_reports_mismatch_when_terminal_shows_volume_without_deduction():
    reporter = RecordingReporter()
    workflow = ApplicationWorkflow(
        StubTaskForm(shown_volume=Decimal("200.00")),
        FixedRates(Decimal("20")),
        reporter,
        today=lambda: MONDAY,
    )

    assert workflow.execute("field-7", Decimal("10"), "product-a") is False
    assert reporter.records == [("application", False)]
    assert reporter.notes == []


def test_notes_weekend_run():
    reporter = RecordingReporter()
    workflow = ApplicationWorkflow(
        StubTaskForm(shown_volume=Decimal("196.00")),
        FixedRates(Decimal("20")),
        reporter,
        today=lambda: SATURDAY,
    )

    assert workflow.execute("field-7", Decimal("10"), "product-a") is True
    assert reporter.notes == ["weekend run"]
```

| Kollaborateur | Test Double | Warum diese Art |
|---|---|---|
| Aufwandmengen | Stub `FixedRates` | der Test braucht eine feste Antwort |
| Terminal | Stub `StubTaskForm` | der Test braucht eine vorgegebene angezeigte Menge; `entered` erlaubt bei Bedarf eine Prüfung der Eingabe |
| Reporter | Spy `RecordingReporter` | geprüft wird, was gemeldet wurde |
| Datum | Funktion `lambda: MONDAY` | eine Funktion genügt, kein eigenes Objekt |

Kein `mock.patch`, kein Modulpfad. Die Doubles sind kleine Klassen, die nur die Methoden des jeweiligen Vertrags haben.

---

## 7 · `reporter or HtmlReporter(...)`

```python
class ApplicationWorkflow:
    def __init__(self, form, rates, reporter=None):
        self._reporter = reporter or HtmlReporter(CONFIG["report_dir"])
```

**Folgen:**

- `ApplicationWorkflow` importiert wieder `HtmlReporter` und `CONFIG`. AK3 ist verletzt. Die Abhängigkeit ist nur noch „manchmal" versteckt.
- Wer den Parameter vergisst, schreibt still auf die Netzwerkfreigabe. Auf einem Entwicklerrechner scheitert das erst beim ersten `record`.
- `or` prüft Wahrheitswerte, nicht `None`. Jedes Objekt, das als falsch gilt, wird ersetzt:

```python
class RecordingReporter:
    def __init__(self):
        self.records = []

    def __len__(self):
        return len(self.records)


spy = RecordingReporter()
chosen = spy or HtmlReporter(CONFIG["report_dir"])
# chosen ist der HtmlReporter: ein leerer Spy hat die Länge 0 und gilt als falsch
```

Der Test übergibt einen Spy, der Workflow verwendet trotzdem den echten Reporter, und der Test prüft eine leere Liste.

**Wenn ein Default gewollt ist,** dann mit `is None`:

```python
self._reporter = reporter if reporter is not None else HtmlReporter(CONFIG["report_dir"])
```

Das behebt die Falle, nicht die Kopplung. Für den Reporter schlägt dieses Papier deshalb **keinen** Default vor. Er hat einen Seiteneffekt nach außen, und sein Standard braucht Konfiguration.

---

## 8 · Der Vertrag zum Terminal

Der Workflow braucht vom Terminal genau drei Operationen: `open_task_form`, `enter_task`, `read_volume`. Das beschreibt `TaskForm` in Aufgabe 4.

```
vorher:   ApplicationWorkflow ──────────────▶ TerminalClient

nachher:  ApplicationWorkflow ──▶ TaskForm (Protocol)
                                       ▲
                                       │ erfüllt strukturell
                                 TerminalClient
```

**Wem der Vertrag gehört:** dem Workflow. Er beschreibt, was der Workflow braucht, nicht, was der Terminal-Client alles kann. `TaskForm` liegt deshalb im Modul des Workflows. `TerminalClient` muss es nicht erben: Als `Protocol` wird der Vertrag über die vorhandenen Methoden erfüllt.

Das ist Dependency Inversion ohne großen Aufwand. Der fachlich höherliegende Workflow hängt von einem schmalen Vertrag ab, den er selbst festlegt. Das technische Detail richtet sich danach.

---

## 9 · Der Entwurf `VolumeCalculator`

| Strategie | Begründbar mit | Einschätzung |
|---|---|---|
| `rounding_strategy` | – | Die Rundung auf 0,01 l ist Teil der Regel. Eine zweite Rundungsart ist nicht bekannt. |
| `minimum_provider` | – | Die Mindestmenge ist ein fester Wert. Ändert er sich, ändert sich die Regel, und dann ändert sich der Code mit Test. |
| `factor_strategy` | vielleicht | nur, wenn mehrere Abzugsmodelle gleichzeitig gelten, etwa je Gerätetyp. Davon ist nichts bekannt. |

**Keine der drei Strategien lässt sich heute mit einer Änderung oder einem Test begründen.** Der Test der Regel braucht keine Ersatzobjekte, er braucht nur Zahlen. Der Entwurf verteilt eine Regel aus drei Zeilen auf vier Klassen und macht sie dadurch schwerer lesbar.

Gäbe es später tatsächlich Abzugsmodelle je Gerätetyp, wäre eine Funktion je Modell, übergeben als `Callable[[Decimal, Decimal], Decimal]`, eine kleine Erweiterung von Aufgabe 4.

---

## 10 · `date.today()`

Zwei vertretbare Antworten:

| Antwort | Begründung |
|---|---|
| **Injizieren, mit Default** | Das Verhalten am Wochenende ist eine Regel des Workflows. Ohne Steuerung der Zeit ist sie nur samstags und sonntags prüfbar, und Tests liefern je nach Wochentag verschiedene Ergebnisse. |
| **Konkret lassen** | Die Notiz ist nur ein Hinweis im Report und kein Prüfergebnis. Wenn niemand sie testen will, ist ein zusätzlicher Parameter nicht gerechtfertigt. |

Der Vorschlag in Aufgabe 4 wählt die erste Antwort mit `today=date.today` als Default. Der Standard ist harmlos: kein Netz, keine Datei, kein Prozess. Übergeben wird die Funktion selbst, nicht ihr Ergebnis. Das Datum wird so bei jedem Aufruf von `execute` neu bestimmt.

**Was dagegen spräche:** Ein Parameter mehr an der öffentlichen API, den jeder Leser verstehen muss. Und wer ihn einmal hat, ist versucht, auch `datetime.now` in allen anderen Workflows zu injizieren, ohne dass es dort eine Regel gibt.

---

## Diskussionsanschluss

Der umgebaute Workflow hat drei Pflichtparameter statt keinem. Jede Stelle, die ihn erzeugt, muss jetzt wissen, was er braucht. Ist das ein Nachteil – oder genau das, was vorher gefehlt hat?
