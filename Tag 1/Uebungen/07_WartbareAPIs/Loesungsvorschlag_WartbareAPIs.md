# Lösungsvorschlag · Was dürfen andere Teams benutzen?

**Vorbemerkung:** Ein Vorschlag, keine Musterlösung. Namen, Modulschnitt und Einordnung der Regeln sind Ermessenssache. Bewertet wird, ob die Schnittstelle **den Gebrauch durch die vier Teams trägt** und ob klar ist, was sich ohne Ankündigung ändern darf.

---

## 1 · Wer verwendet was?

| Name | öffentlich nach Konvention | Team | Ziel |
|---|---|---|---|
| `add` | ja | A | Ergebnis erfassen |
| `results` (schreibend) | ja | A | Test nachträglich als instabil markieren |
| `_write_json` | nein | B | JSON an einen eigenen Ort schreiben |
| `_format_duration` | nein | B | Laufzeit lesbar ausgeben |
| `_failed` | nein | C | fehlgeschlagene Tests ermitteln |
| `get_results` | ja | D | alle Ergebnisse auswerten |

**Drei von sechs Zugriffen gehen auf Namen mit Unterstrich.** Jeder davon hat ein nachvollziehbares Ziel, für das es keinen öffentlichen Weg gibt.

**Zwei der öffentlichen Zugriffe legen den inneren Zustand offen.** `results` ist das Dictionary, in dem gesammelt wird. `get_results()` gibt genau dieses Dictionary zurück. Team Section Control könnte darüber ebenso schreiben wie Team UT.

---

## 2 · Namen

| Vorher | Problem | Vorschlag |
|---|---|---|
| `add(n, s, d, msg)` | Abkürzungen, drei Positionsparameter ohne erkennbare Bedeutung | `record(result)` |
| `get_results()` | Java-Getter, gibt interne Struktur heraus | Property `results` |
| `export(fmt="html")` | ein String wählt zwischen zwei Verhalten | `export_html()`, `export_json(path)` |
| `_write_json(path)` | beschreibt Technik, wird von außen gebraucht | `export_json(path)` |
| `_format_duration(seconds)` | braucht kein `self`, wird von außen gebraucht | Modulfunktion `format_duration(seconds)` |
| `_failed()` | wird von außen gebraucht | Property `failed` |

`ResultCollector` bleibt. Der Name beschreibt, was die Klasse tut.

---

## 3 · Die Docstrings

| Methode | Docstring | Beurteilung |
|---|---|---|
| `add` | „Adds a result." | wiederholt den Namen |
| `get_results` | „Returns the results." | wiederholt den Namen |
| `export` | Formate, Überschreiben vorhandener Dateien, `ValueError` bei unbekanntem Format | beschreibt einen Vertrag |

Der Docstring von `export` sagt drei Dinge, die ein Aufrufer wissen muss und nicht aus dem Namen ableiten kann. Die beiden anderen würden beim nächsten Umbau vermutlich nicht angepasst und sagen schon heute nichts.

---

## 4 · Die öffentliche API

```python
"""Testergebnisse eines Laufs sammeln und als Bericht exportieren."""

import json
import warnings
from collections.abc import Mapping
from dataclasses import asdict, dataclass
from pathlib import Path
from types import MappingProxyType

__all__ = ["ResultCollector", "TestResult", "format_duration"]


@dataclass(frozen=True)
class TestResult:
    """Ergebnis eines einzelnen Tests. Nach dem Erzeugen unveränderlich."""

    name: str
    status: str
    duration: float
    message: str | None = None


def format_duration(seconds: float) -> str:
    """Laufzeit in der Form, in der sie in Berichten erscheint, z. B. ``12.5 s``."""
    return f"{seconds:.1f} s"


class ResultCollector:
    """Sammelt die Ergebnisse eines Testlaufs und exportiert sie als Bericht."""

    def __init__(self, output_dir: Path) -> None:
        self._output_dir = output_dir
        self._results: dict[str, TestResult] = {}

    def record(self, result: TestResult) -> None:
        """Erfasst ein Ergebnis.

        Ein weiteres Ergebnis mit demselben Testnamen ersetzt das vorherige,
        etwa wenn ein Test nach einer Wiederholung als ``"flaky"`` gilt.
        """
        self._results[result.name] = result

    @property
    def results(self) -> Mapping[str, TestResult]:
        """Nur lesbare Sicht auf alle Ergebnisse, Schlüssel ist der Testname.

        Die Sicht zeigt auch Ergebnisse, die nach dem Abruf erfasst werden.
        """
        return MappingProxyType(self._results)

    @property
    def failed(self) -> tuple[TestResult, ...]:
        return tuple(r for r in self._results.values() if r.status == "failed")

    def export_json(self, path: Path | None = None) -> Path:
        """Schreibt alle Ergebnisse als JSON und gibt den Zielpfad zurück.

        Ohne ``path`` wird ``results.json`` im Ausgabeverzeichnis geschrieben.
        Eine vorhandene Datei wird überschrieben.
        """
        target = path if path is not None else self._output_dir / "results.json"
        data = [asdict(result) for result in self._results.values()]
        target.write_text(json.dumps(data, indent=2), encoding="utf-8")
        return target

    def export_html(self) -> Path:
        """Schreibt den HTML-Bericht ins Ausgabeverzeichnis und gibt den Pfad zurück.

        Eine vorhandene Datei wird überschrieben.
        """
        target = self._output_dir / "results.html"
        print(f"write HTML report to {target}")
        return target

    def get_results(self) -> Mapping[str, TestResult]:
        """Veraltet. Stattdessen ``results`` verwenden."""
        warnings.warn(
            "get_results() is deprecated, use results",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.results
```

**Die Aufrufstellen der vier Teams:**

```python
# Team UT
collector.record(TestResult("select_implement", "passed", 3.2))
collector.record(TestResult("select_implement", "flaky", 3.2))

# Team AEF
collector.export_json(Path("/shared/nightly/aef.json"))
print(format_duration(12.5))

# Team Einstellungen
if collector.failed:
    print(f"{len(collector.failed)} tests failed")

# Team Section Control
for name, result in collector.results.items():
    print(name, result.status)
```

**Entscheidungen im Einzelnen:**

- **`record` ersetzt bei gleichem Namen.** Team UT erreicht sein Ziel über einen dokumentierten Weg. Ein bereits erfasstes Ergebnis wird nicht verändert, sondern durch ein neues ersetzt. Die Position in der Reihenfolge bleibt dabei die der ersten Erfassung.
- **`results` liefert eine nur lesbare Sicht.** `MappingProxyType` verhält sich beim Lesen wie ein Dictionary und weist Zuweisungen mit `TypeError` ab.
- **`failed` hat keinen Docstring.** Name und Rückgabetyp sagen, was herauskommt.
- **`export_json` gibt den Pfad zurück.** Aufrufer, die ohne `path` exportieren, erfahren so, wo die Datei liegt.
- **`get_results` bleibt vorerst.** Sie verweist auf `results` und löst eine `DeprecationWarning` aus. Team Section Control kann umstellen, wenn es die neue Version übernimmt.
- **`started` gehört nicht zur Schnittstelle.** Kein Team verwendet es. Wird es intern gebraucht, heißt es `_started`.
- **`__all__` nennt drei Namen.** `from reporting import *` liefert genau diese. Direkte Importe anderer Namen bleiben technisch möglich, sind aber als nicht angeboten erkennbar.

---

## 5 · Ein Datentyp für das Ergebnis

`TestResult` ist eine `@dataclass(frozen=True)` (siehe Aufgabe 4). Die Dataclass erzeugt `__init__`, `__repr__` und `__eq__` aus den Feldern. Mit `frozen=True` kommt ein `__hash__` dazu, und jede Zuweisung an ein Feld bricht ab.

**Was das bei Team UT verhindert:**

| Versuch | Ergebnis |
|---|---|
| `collector.results["select_implement"]["status"] = "flaky"` | `TypeError`: `TestResult` unterstützt keine Zuweisung per Index |
| `collector.results["select_implement"].status = "flaky"` | `FrozenInstanceError` |
| `collector.results["select_implement"] = ...` | `TypeError`: die Sicht ist nur lesbar |

Der offizielle Weg ist `record` mit einem neuen Ergebnis.

**Ist `ResultCollector` ein Kandidat für `@dataclass`?** Nein. Die Klasse hat Verhalten, und ihr Zustand ist ein Implementierungsdetail. Eine Dataclass würde `_results` zu einem Konstruktorparameter machen, es in `__repr__` ausgeben und in `__eq__` vergleichen. Keines davon ist gewollt.

**Eine mögliche Ergänzung:** Soll ein leerer Testname abgewiesen werden, lässt sich das in `__post_init__` prüfen, auch bei `frozen=True`:

```python
@dataclass(frozen=True)
class TestResult:
    name: str
    status: str
    duration: float
    message: str | None = None

    def __post_init__(self) -> None:
        if not self.name:
            raise ValueError("test result needs a name")
```

---

## 6 · Modulstruktur nach Verantwortung

```text
testframework/
    reporting.py        ResultCollector, TestResult, format_duration, JSON-Export
    configuration.py    Konfiguration laden
    retry.py            Retry-Dekorator
    testdata.py         Testdaten erzeugen
    workflows.py        Freischaltung, Anbaugeräte anlegen
    assertions.py       Asserts für Tabellen
    ui/
        waiting.py      Warten auf Dialoge
        screenshots.py  Screenshot-Ablage, Vergleich von Screenshots
        screens/        Bildschirmelemente, je Bereich ein Modul
```

**Zuordnung der Inhalte aus Material A:**

| Inhalt | bisher | neu |
|---|---|---|
| ResultCollector | `common.py` | `reporting.py` |
| Konfiguration laden | `common.py` | `configuration.py` |
| Retry-Dekorator | `common.py` | `retry.py` |
| Zeitformatierung | `utils.py` | `reporting.py` (`format_duration`) |
| Screenshot-Ablage | `utils.py` | `ui/screenshots.py` |
| Warten auf Dialoge | `utils.py` | `ui/waiting.py` |
| JSON-Hilfen | `utils.py` | `reporting.py`, sofern sie nur dem Export dienen, sonst beim jeweiligen Verwender |
| Freischaltung, Anbaugeräte anlegen | `helpers.py` | `workflows.py` |
| Testdaten erzeugen | `helpers.py` | `testdata.py` |
| Asserts für Tabellen | `test_helpers.py` | `assertions.py` |
| Vergleich von Screenshots | `test_helpers.py` | `ui/screenshots.py` |
| Bildschirmelemente | `screens.py` | `ui/screens/`, je Bereich ein Modul |

**Ein Nebeneffekt:** `test_helpers.py` entspricht dem Standardmuster `test_*.py`, nach dem pytest Testdateien sammelt. Liegt die Datei in einem Pfad, den pytest durchsucht, wird sie als Testmodul importiert.

Die Struktur ist ein Vorschlag. Wie die UI-Schicht geschnitten wird, ist Thema von Tag 2.

---

## 7 · Regelkandidaten einordnen

| Regel | Vorschlag | Prüfbar durch |
|---|---|---|
| Öffentliche Funktionen und Methoden des Frameworks sind typannotiert. | **MUST** für das Framework, **SHOULD** für Testcode der Suite-Teams | Type Checker, z. B. mypy mit `--disallow-untyped-defs`, oder Linter-Regeln für fehlende Annotationen |
| Code wird mit einem automatischen Formatter formatiert. | **MUST** | Formatter im Prüfmodus in der CI |
| Module heißen `utils`, `helpers` oder `common`. | **DON'T** | Review; mit gängigen Linter-Regeln nicht abgedeckt |
| Testcode greift auf `_`-Namen aus dem Framework zu. | **DON'T** | Linter mit Regel für Zugriffe auf private Member, z. B. Ruff `SLF001` |
| Jede Methode hat einen Docstring. | **so nicht übernehmen**; stattdessen **SHOULD:** Öffentliche API hat einen Docstring, wenn der Vertrag nicht aus Name und Typen hervorgeht | Vorhandensein per Linter, Inhalt nur im Review |
| Reine Datenträger werden als `dataclass` geschrieben. | **MAY** | Review |
| Jedes Modul des Frameworks deklariert `__all__`. | **SHOULD** | Review oder eigener Check |

**Zur Docstring-Regel:** „Jede Methode hat einen Docstring" ist prüfbar und erzeugt genau die Docstrings aus Material B. Ein Linter stellt fest, ob ein Docstring da ist, nicht, ob er etwas sagt.

**Zur DON'T-Regel für `_`-Namen:** Sie ist erst tragfähig, wenn die öffentliche Schnittstelle die berechtigten Bedürfnisse bedient. Vorher erzwingt sie Umwege.

---

## 8 · `results` schützen, ohne lesende Aufrufer zu ändern

Aus dem öffentlichen Attribut wird eine Property mit demselben Namen (siehe Aufgabe 4):

```python
@property
def results(self) -> Mapping[str, TestResult]:
    return MappingProxyType(self._results)
```

| Aufrufstelle | vorher | nachher |
|---|---|---|
| `collector.results["select_implement"]` | liefert den Eintrag | liefert den Eintrag |
| `collector.results.items()` | funktioniert | funktioniert |
| `name in collector.results` | funktioniert | funktioniert |
| `collector.results["select_implement"] = ...` | verändert den Collector | `TypeError` |

**Lesende Aufrufer merken nichts, schreibende scheitern sichtbar.** Das ist dieselbe Eigenschaft, die in Einheit 1-1 bei der Validierung gezeigt wurde: Die Syntax an der Aufrufstelle bleibt, das Verhalten dahinter ändert sich.

**Eine Einschränkung:** Waren die Einträge vorher Dictionaries, schützt die Sicht nur die oberste Ebene. `collector.results["select_implement"]["status"] = "flaky"` würde weiterhin funktionieren. Erst mit `TestResult` als unveränderlichem Datentyp aus Aufgabe 5 ist auch der Eintrag selbst geschützt. Dann ändern sich allerdings lesende Zugriffe von `result["status"]` zu `result.status`.

---

## 9 · Werkzeug oder Mensch?

| Nr. | Kommentar | Entscheidet |
|---|---|---|
| 1 | Zeile länger als 88 Zeichen | Formatter bzw. Linter |
| 2 | Imports sortieren | Linter oder Import-Sortierer |
| 3 | fehlender Type Hint | Linter oder Type Checker (ob der Hint *richtig* ist, prüft der Type Checker nur teilweise) |
| 4 | Was verarbeitet `proc`? | Mensch |
| 5 | Warum öffentlich? | Mensch |
| 6 | Zwei Leerzeilen vor der Klasse | Formatter |
| 7 | Gehört das nach `utils.py`? | Mensch |
| 8 | `json` importiert, nicht verwendet | Linter |
| 9 | Docstring sagt nicht, was bei unbekanntem Format passiert | Mensch |
| 10 | `camelCase` statt `snake_case` | Linter mit Naming-Regeln |

**Sechs von zehn Kommentaren kann ein Werkzeug entscheiden.** Die vier übrigen betreffen Namen, Sichtbarkeit, Modulschnitt und Vertrag. Genau diese Fragen hatten im Fallbeispiel keinen Platz im Review.

---

## Diskussionsanschluss

Die neue Schnittstelle bedient alle vier Teams. Welche der 87 Zugriffe aus dem Ticket würden Sie **nicht** bedienen, und wie teilen Sie das dem betroffenen Team mit?
