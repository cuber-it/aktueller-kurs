# Übung · Wie viel Vertrag braucht diese Grenze?

Sie untersuchen vier Stellen aus einem Testframework, an denen ein Objekt mit einem anderen zusammenarbeitet, ohne dessen konkrete Klasse zu kennen. An jeder Stelle wurde eine Abstraktion eingeführt oder vermisst. Die Frage ist, welche Form von Vertrag die jeweilige Grenze tatsächlich braucht.

**Es werden keine Squish-Kenntnisse benötigt.** Technische Aufrufe sind durch `print` ersetzt.

---

## Material A · Die Benachrichtigung über Testergebnisse

```python
from abc import ABC, abstractmethod


class Notifier(ABC):
    @abstractmethod
    def connect(self): ...

    @abstractmethod
    def send(self, message): ...

    @abstractmethod
    def send_attachment(self, path): ...

    @abstractmethod
    def set_priority(self, level): ...

    @abstractmethod
    def disconnect(self): ...


class ConsoleNotifier(Notifier):
    def connect(self):
        pass

    def send(self, message):
        print(message)

    def send_attachment(self, path):
        raise NotImplementedError

    def set_priority(self, level):
        pass

    def disconnect(self):
        pass


class ResultPublisher:
    def __init__(self, notifier):
        self.notifier = notifier

    def publish(self, suite_name, failed, total):
        self.notifier.send(f"{suite_name}: {failed} of {total} failed")
```

Es gibt vier Implementierungen von `Notifier`: Konsole, Datei, Mail und Teams-Kanal. Alle sind nach demselben Muster gebaut. Die Mail-Implementierung nutzt Verbindung, Versand und Anhänge, die Konsole nur den Versand.

---

## Material B · Eine Klasse aus einer fremden Bibliothek

```python
# aus der Bibliothek eines Drittanbieters, nicht änderbar
class VendorChatClient:
    def __init__(self, channel):
        self.channel = channel

    def send(self, message):
        print(f"[{self.channel}] {message}")
```

Das Team möchte Testergebnisse künftig auch über diesen Chat-Client veröffentlichen.

---

## Material C · Der Vertrag für die UI-Steuerung

```python
from typing import Protocol


class UiDriver(Protocol):
    def start_application(self, path: str) -> None: ...
    def stop_application(self) -> None: ...
    def click(self, target: str) -> None: ...
    def type_text(self, target: str, text: str) -> None: ...
    def read_text(self, target: str) -> str: ...
    def select_item(self, target: str, item: str) -> None: ...
    def wait_for(self, target: str, timeout: int) -> None: ...
    def screenshot(self, name: str) -> None: ...
    def drag(self, source: str, destination: str) -> None: ...


class ServiceUnlockFlow:
    def __init__(self, driver: UiDriver) -> None:
        self._driver = driver

    def unlock(self, pin: str) -> None:
        self._driver.type_text("pinField", pin)
        self._driver.click("unlockButton")
```

Für Unit-Tests von `ServiceUnlockFlow` gibt es einen `FakeDriver`, der alle neun Methoden implementiert, sieben davon mit `pass`.

---

## Material D · Eine Abstraktion mit einer Implementierung

```python
from abc import ABC, abstractmethod


class ReportRenderer(ABC):
    @abstractmethod
    def render(self, results): ...


class HtmlReportRenderer(ReportRenderer):
    def render(self, results):
        rows = "".join(f"<tr><td>{result}</td></tr>" for result in results)
        return f"<table>{rows}</table>"
```

`ReportRenderer` wurde 2021 eingeführt. `HtmlReportRenderer` ist bis heute die einzige Implementierung. Es gibt eine Stelle, an der ein Renderer verwendet wird.

---

## Material E · Drei Aussagen aus dem Team

Aus dem Architekturteam:

> „Wir programmieren gegen Interfaces. Deshalb bekommt jede Komponente eine abstrakte Basisklasse."

Ein Entwickler:

> „Protocols sind der moderne Weg. Wir sollten alle ABCs durch Protocols ersetzen."

Aus der Testautomatisierung:

> „Seit wir Type Hints verwenden, kann niemand mehr ein falsches Objekt übergeben."

---

## Aufgabe

### Teil 1 · Verträge lesen

**1.** Welche Operationen von `Notifier` verwendet `ResultPublisher` tatsächlich? Welche verlangt die ABC von jeder Implementierung? Stellen Sie beides in einer Tabelle gegenüber.

**2.** `ServiceUnlockFlow` hängt von `UiDriver` ab. Wie viele der neun Methoden ruft `ServiceUnlockFlow` auf? Was bedeutet das für jeden, der einen `FakeDriver` für `ServiceUnlockFlow` schreibt?

**3.** Prüfen Sie die dritte Aussage aus Material E. Was passiert zur Laufzeit, wenn jemand `ServiceUnlockFlow("kein Treiber")` erzeugt und `unlock()` aufruft? Wer würde den Fehler früher bemerken, und unter welcher Voraussetzung?

### Teil 2 · Drei Formen derselben Grenze

**4.** Formulieren Sie die Grenze zwischen `ResultPublisher` und seinem Benachrichtigungskanal dreimal: mit Duck Typing, mit einer kleinen ABC und mit einem Protocol. Jede Variante soll nur verlangen, was `ResultPublisher` braucht.

**5.** `VendorChatClient` aus Material B soll als Kanal verwendet werden. Prüfen Sie für jede Ihrer drei Varianten: Funktioniert das ohne zusätzlichen Code? Wenn nicht, was ist nötig? Was ändert `Notifier.register(VendorChatClient)` daran, und was nicht?

**6.** Schneiden Sie den Vertrag für `ServiceUnlockFlow` auf das zu, was die Klasse braucht. Muss die vorhandene Implementierung von `UiDriver` für das echte GUI-Werkzeug dafür geändert werden?

### Teil 3 · Abwägen

**7.** Soll `ReportRenderer` aus Material D bleiben? Nennen Sie Umstände, unter denen Sie die ABC behalten würden, und Umstände, unter denen Sie sie entfernen würden.

**8.** Prüfen Sie die zweite Aussage aus Material E. Nennen Sie mindestens zwei Situationen, in denen eine ABC mehr leistet als ein Protocol.

**9.** Ein Kollege möchte zur Laufzeit prüfen, ob ein übergebenes Objekt Ihr Protocol aus Aufgabe 4 erfüllt: `isinstance(channel, ResultChannel)`. Was ist dafür nötig, und was genau prüft `isinstance` dann?

---

## Hinweise zur Bearbeitung

- Der Code muss nicht ausgeführt werden. Er sollte aber so geschrieben sein, dass er lauffähig wäre.
- Keine der drei Formen aus Aufgabe 4 ist grundsätzlich die richtige. Begründen Sie Ihre Wahl mit der Grenze, nicht mit der Form.
- Wenn Sie unsicher sind, ob eine Operation in einen Vertrag gehört, fragen Sie: **Ruft der Client sie auf?**
- Wer einen Type Checker wie mypy zur Hand hat, kann die Aufgaben 3, 5 und 6 damit überprüfen. Nötig ist das nicht.
