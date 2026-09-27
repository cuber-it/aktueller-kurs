# Lösungsvorschlag · Wie viel Vertrag braucht diese Grenze?

**Vorbemerkung:** Ein Vorschlag, keine Musterlösung. An mehreren Grenzen sind zwei Formen vertretbar. Bewertet wird, ob der Vertrag **dem Bedarf des Clients** entspricht und ob die gewählte Form begründet ist.

---

## 1 · Was `ResultPublisher` braucht und was `Notifier` verlangt

| Operation | von `Notifier` verlangt | von `ResultPublisher` aufgerufen |
|---|---|---|
| `connect` | ja | nein |
| `send` | ja | **ja** |
| `send_attachment` | ja | nein |
| `set_priority` | ja | nein |
| `disconnect` | ja | nein |

**Eine von fünf.** Die Konsole muss vier Methoden liefern, die sie nicht sinnvoll erfüllen kann, damit ein Client eine Methode aufrufen kann.

Der Vertrag wurde aus Sicht der Implementierung entworfen, die am meisten kann: der Mail-Kanal mit Verbindung und Anhängen.

---

## 2 · `ServiceUnlockFlow` und `UiDriver`

`ServiceUnlockFlow` ruft **zwei** der neun Methoden auf: `type_text` und `click`.

Wer `ServiceUnlockFlow` isoliert testen will, muss trotzdem ein Objekt übergeben, das alle neun Methoden besitzt, jedenfalls wenn ein Type Checker den Test prüft. Sieben davon sind für den Test bedeutungslos. Kommt eine zehnte Methode zu `UiDriver` hinzu, muss auch dieser Fake nachgezogen werden, obwohl `ServiceUnlockFlow` sich nicht geändert hat.

---

## 3 · „Mit Type Hints kann niemand ein falsches Objekt übergeben"

```python
flow = ServiceUnlockFlow("kein Treiber")
flow.unlock("4711")
```

| Zeitpunkt | Was passiert |
|---|---|
| `ServiceUnlockFlow("kein Treiber")` | nichts. Der Konstruktor speichert den String |
| `flow.unlock(...)` | `AttributeError: 'str' object has no attribute 'type_text'` |

Python wertet die Annotation `driver: UiDriver` zur Laufzeit nicht aus. Der Fehler zeigt sich erst beim ersten Zugriff auf eine Methode, die fehlt.

**Wer ihn früher bemerkt:** Ein Type Checker wie mypy meldet die Zeile `ServiceUnlockFlow("kein Treiber")` als `incompatible type "str"; expected "UiDriver"`, und zwar vor dem Lauf. **Voraussetzung:** Er wird ausgeführt, lokal oder in der CI. Im Fallbeispiel geschieht das nicht.

Die Aussage aus dem Team stimmt also nur zusammen mit einem Werkzeug, das die Hints prüft.

---

## 4 · Dieselbe Grenze in drei Formen

**Duck Typing**

```python
class ResultPublisher:
    """Veröffentlicht Suite-Ergebnisse über einen Kanal.

    channel: ein Objekt mit send(message: str) -> None
    """

    def __init__(self, channel) -> None:
        self._channel = channel

    def publish(self, suite_name: str, failed: int, total: int) -> None:
        self._channel.send(f"{suite_name}: {failed} of {total} failed")
```

**Kleine ABC**

```python
from abc import ABC, abstractmethod


class ResultChannel(ABC):
    @abstractmethod
    def send(self, message: str) -> None: ...


class ResultPublisher:
    def __init__(self, channel: ResultChannel) -> None:
        self._channel = channel

    def publish(self, suite_name: str, failed: int, total: int) -> None:
        self._channel.send(f"{suite_name}: {failed} of {total} failed")
```

**Protocol**

```python
from typing import Protocol


class ResultChannel(Protocol):
    def send(self, message: str) -> None: ...


class ResultPublisher:
    def __init__(self, channel: ResultChannel) -> None:
        self._channel = channel

    def publish(self, suite_name: str, failed: int, total: int) -> None:
        self._channel.send(f"{suite_name}: {failed} of {total} failed")
```

**Was sich unterscheidet:**

| | Duck Typing | ABC | Protocol |
|---|---|---|---|
| Vertrag sichtbar | im Docstring | in `ResultChannel`, Implementierungen erben | in `ResultChannel`, Implementierungen erben nicht |
| Type Checker prüft Aufrufer | nein | ja | ja |
| Klasse ohne `send` wird erkannt | beim Aufruf von `publish` | beim Instanziieren, falls sie erbt | durch den Type Checker |

Der Code von `ResultPublisher` selbst ist in allen drei Fassungen gleich.

---

## 5 · `VendorChatClient` als Kanal

| Form | ohne zusätzlichen Code? | Begründung |
|---|---|---|
| Duck Typing | ja | die Klasse besitzt `send(message)` |
| kleine ABC | zur Laufzeit ja, für den Type Checker nein | `ResultPublisher` prüft nichts und ruft nur `send` auf. mypy lehnt die Übergabe ab, weil `VendorChatClient` nicht von `ResultChannel` erbt |
| Protocol | ja | die Struktur passt, mypy akzeptiert die Klasse ohne Vererbung |

Für die ABC-Fassung wäre ein Adapter nötig, der nur weiterreicht:

```python
class VendorChatChannel(ResultChannel):
    def __init__(self, client: VendorChatClient) -> None:
        self._client = client

    def send(self, message: str) -> None:
        self._client.send(message)
```

**Was `register` ändert:**

```python
ResultChannel.register(VendorChatClient)
isinstance(VendorChatClient("qa"), ResultChannel)   # True
```

Für `Notifier.register(VendorChatClient)` aus der Aufgabenstellung gilt dasselbe. `isinstance` stimmt danach zu. Geprüft wird dabei nichts: Auch eine registrierte Klasse ohne `send` würde als `ResultChannel` gelten. Type Checker wie mypy berücksichtigen die Registrierung nicht und lehnen die Übergabe weiterhin ab.

---

## 6 · Ein Vertrag für `ServiceUnlockFlow`

```python
from typing import Protocol


class PinInput(Protocol):
    """Was ServiceUnlockFlow von der UI-Steuerung braucht."""

    def type_text(self, target: str, text: str) -> None: ...
    def click(self, target: str) -> None: ...


class ServiceUnlockFlow:
    def __init__(self, ui: PinInput) -> None:
        self._ui = ui

    def unlock(self, pin: str) -> None:
        self._ui.type_text("pinField", pin)
        self._ui.click("unlockButton")
```

Ein Test-Double braucht jetzt zwei Methoden:

```python
class RecordingInput:
    """Zeichnet Eingaben auf, statt eine Oberfläche zu bedienen."""

    def __init__(self) -> None:
        self.actions: list[tuple[str, ...]] = []

    def type_text(self, target: str, text: str) -> None:
        self.actions.append(("type", target, text))

    def click(self, target: str) -> None:
        self.actions.append(("click", target))


def test_unlock_enters_pin_and_confirms() -> None:
    ui = RecordingInput()
    ServiceUnlockFlow(ui).unlock("4711")
    assert ui.actions == [
        ("type", "pinField", "4711"),
        ("click", "unlockButton"),
    ]
```

**Muss die echte Treiberimplementierung geändert werden?** Nein. Sie besitzt `type_text` und `click` mit passenden Signaturen und erfüllt `PinInput` strukturell, obwohl sie davon nichts weiß. Das andere Team muss nichts anpassen.

`UiDriver` kann für Clients bestehen bleiben, die tatsächlich viele Operationen brauchen, etwa eine Klasse, die die Anwendung startet und stoppt.

---

## 7 · `ReportRenderer`

**Entfernen**, solange diese Umstände gelten:

- Es gibt seit Jahren genau eine Implementierung.
- Kein weiteres Format ist konkret beauftragt.
- Tests brauchen keinen Ersatz, weil `HtmlReportRenderer` schnell ist und keine externen Ressourcen braucht.
- Es gibt einen Client. Wer die Stelle liest, springt heute von `ReportRenderer` zu `HtmlReportRenderer`, um zu erfahren, was passiert.

**Behalten** oder wieder einführen, wenn:

- ein zweites Format beauftragt ist, etwa JSON für die CI,
- der Renderer in Tests ersetzt werden soll, weil er langsam wird oder Dateien schreibt,
- mehrere Renderer gemeinsame Logik teilen, die in eine Basisklasse gehört.

Wird die ABC entfernt, bleibt `HtmlReportRenderer` unverändert. Der Client verwendet ihn direkt. Kommt ein zweites Format, ergibt sich der Vertrag aus dem, was der Client aufruft: `render(results)`.

---

## 8 · „Wir sollten alle ABCs durch Protocols ersetzen"

Eine ABC leistet mehr als ein Protocol, wenn:

| Situation | Warum die ABC |
|---|---|
| Implementierungen teilen Code oder einen festen Ablauf | die ABC trägt konkrete Methoden, Unterklassen füllen nur die Lücken |
| die Familie bewusst geschlossen ist | Zugehörigkeit soll erklärt werden, nicht zufällig entstehen |
| Vollständigkeit früh geprüft werden soll | eine Unterklasse ohne abstrakte Methode lässt sich nicht instanziieren |
| zur Laufzeit zuverlässig unterschieden werden soll | `isinstance` gegen eine ABC ist ohne Zusatz möglich |

Ein Protocol leistet mehr, wenn fremde oder unabhängig entstandene Klassen passen sollen oder wenn ein Client einen kleinen Ausschnitt eines größeren Objekts braucht.

**Die Aussage verwechselt Alter mit Eignung.** Protocols kamen mit Python 3.8 hinzu. Sie ergänzen ABCs für strukturelle Grenzen, sie ersetzen sie nicht.

---

## 9 · `isinstance` mit einem Protocol

Ohne weitere Angabe schlägt die Prüfung fehl:

```python
isinstance(channel, ResultChannel)
# TypeError: Instance and class checks can only be used with @runtime_checkable protocols
```

Nötig ist der Dekorator:

```python
from typing import Protocol, runtime_checkable


@runtime_checkable
class ResultChannel(Protocol):
    def send(self, message: str) -> None: ...
```

**Was dann geprüft wird:** nur, ob das Objekt ein Attribut `send` besitzt. Parameter, Rückgabetyp und Aufrufbarkeit mit einem String werden nicht geprüft. Eine Klasse mit `def send(self): ...` gilt ebenfalls als `ResultChannel`.

`isinstance` gegen ein Protocol ist damit eine grobe Plausibilitätsprüfung. Die genaue Prüfung der Signaturen leistet der Type Checker vor dem Lauf.

---

## Diskussionsanschluss

Nach dem Umbau gibt es mehr Verträge als vorher, aber jeder ist kleiner. Was passiert jetzt, wenn eine Methode `set_priority` hinzukommt, und wo stünde sie?
