# Beispiel · Wie viel Vertrag braucht diese Grenze – in klein

Dieselbe Aufgabe an einem kleineren Gegenstand, vollständig durchgeführt.

---

## Der Gegenstand

Eine Büroanwendung verteilt Druckaufträge auf Ausgabegeräte. Es geht um die Grenze zwischen der **Druckwarteschlange** und den **Geräten**.

```python
from abc import ABC, abstractmethod


class OutputDevice(ABC):
    @abstractmethod
    def power_on(self): ...

    @abstractmethod
    def power_off(self): ...

    @abstractmethod
    def print_page(self, page): ...

    @abstractmethod
    def set_duplex(self, enabled): ...

    @abstractmethod
    def status(self): ...


class PrintQueue:
    def __init__(self, device):
        self.device = device

    def print_document(self, pages):
        for page in pages:
            self.device.print_page(page)
```

Es gibt zwei eigene Geräte, `LaserPrinter` und `PdfExporter`. Neu hinzukommen soll ein Etikettendrucker, dessen Hersteller eine Python-Klasse mitliefert:

```python
# aus dem SDK des Herstellers, nicht änderbar
class LabelPrinter:
    def print_page(self, page):
        print(f"label: {page}")
```

---

## Schritt 1 · Was braucht der Client?

| Operation | verlangt von `OutputDevice` | aufgerufen von `PrintQueue` |
|---|---|---|
| `power_on` | ja | nein |
| `power_off` | ja | nein |
| `print_page` | ja | **ja** |
| `set_duplex` | ja | nein |
| `status` | ja | nein |

**Eine von fünf.** `PdfExporter` muss trotzdem `set_duplex` und `power_on` liefern, die für eine PDF-Datei keine Bedeutung haben.

---

## Schritt 2 · Drei Formen derselben Grenze

**Duck Typing**

```python
class PrintQueue:
    def __init__(self, device):
        """device: ein Objekt mit print_page(page: str)."""
        self._device = device

    def print_document(self, pages: list[str]) -> None:
        for page in pages:
            self._device.print_page(page)
```

**Kleine ABC**

```python
from abc import ABC, abstractmethod


class PageOutput(ABC):
    @abstractmethod
    def print_page(self, page: str) -> None: ...


class PrintQueue:
    def __init__(self, device: PageOutput) -> None:
        self._device = device

    def print_document(self, pages: list[str]) -> None:
        for page in pages:
            self._device.print_page(page)
```

**Protocol**

```python
from typing import Protocol


class PageOutput(Protocol):
    def print_page(self, page: str) -> None: ...


class PrintQueue:
    def __init__(self, device: PageOutput) -> None:
        self._device = device

    def print_document(self, pages: list[str]) -> None:
        for page in pages:
            self._device.print_page(page)
```

**Der Code von `PrintQueue` ist in allen drei Fassungen gleich.** Der Unterschied liegt darin, wo der Vertrag steht und wer ihn prüft.

---

## Schritt 3 · Der Etikettendrucker

| Form | `LabelPrinter` verwendbar? |
|---|---|
| Duck Typing | ja, er besitzt `print_page` |
| kleine ABC | nicht direkt, er erbt nicht von `PageOutput`. Ein Type Checker lehnt ihn ab, ein Adapter wäre nötig |
| Protocol | ja, seine Struktur passt. Ein Type Checker akzeptiert ihn ohne Vererbung |

Ein Adapter für die ABC-Fassung sähe so aus:

```python
class LabelPrinterAdapter(PageOutput):
    def __init__(self, printer: LabelPrinter) -> None:
        self._printer = printer

    def print_page(self, page: str) -> None:
        self._printer.print_page(page)
```

Er ergänzt kein Verhalten. Er existiert nur, damit die Typbeziehung formal stimmt.

---

## Schritt 4 · Und die große ABC?

`OutputDevice` hat eine Berechtigung, aber an anderer Stelle. Die Geräteverwaltung schaltet Geräte ein und aus und fragt ihren Status ab. Für sie ist ein Vertrag mit `power_on`, `power_off` und `status` angemessen.

**Zwei Clients, zwei Verträge.** Die Warteschlange braucht `print_page`, die Geräteverwaltung braucht den Lebenszyklus. Ein Gerät, das beides kann, erfüllt beide Verträge.

---

## Schritt 5 · Die Entscheidung

Gewählt wird das **Protocol** `PageOutput`:

- Es gibt drei Implementierungen, eine davon fremd.
- Die Grenze ist eine öffentliche Stelle der Anwendung, an der ein Type Checker helfen soll.
- Die Implementierungen teilen keinen Code, der in eine Basisklasse gehörte.

Duck Typing wäre ebenfalls vertretbar gewesen. Es hätte den Vertrag nur im Docstring festgehalten.

---

## Zum Vergleich: wann die ABC gewonnen hätte

Angenommen, jeder Drucker muss vor dem ersten Blatt aufgewärmt werden, und diese Logik ist für alle eigenen Drucker gleich:

```python
from abc import ABC, abstractmethod


class Printer(ABC):
    """Gemeinsamer Ablauf für eigene Drucker: erst aufwärmen, dann drucken."""

    def __init__(self) -> None:
        self._warm = False

    def print_page(self, page: str) -> None:
        if not self._warm:
            self._warm_up()
            self._warm = True
        self._output(page)

    @abstractmethod
    def _warm_up(self) -> None: ...

    @abstractmethod
    def _output(self, page: str) -> None: ...
```

Hier trägt die ABC eine gemeinsame Implementierung und eine bewusst modellierte Familie. Ein Protocol könnte beides nicht leisten. `Printer` erfüllt trotzdem das Protocol `PageOutput`, die Warteschlange bleibt unverändert.

---

## Was dieses Beispiel zeigt

**Der Vertrag gehört zum Client, nicht zum Gerät.** `PrintQueue` braucht eine Operation, also verlangt sie eine.

**Strukturelle Typisierung nimmt fremde Klassen auf.** Der Etikettendrucker passt zum Protocol, ohne davon zu wissen.

**Die Form folgt der Grenze.** Gemeinsame Implementierung spricht für eine ABC, fremde Implementierungen sprechen für ein Protocol oder Duck Typing.

**Mehrere kleine Verträge können nebeneinander stehen.** Ein Gerät erfüllt den Vertrag der Warteschlange und den der Geräteverwaltung.
