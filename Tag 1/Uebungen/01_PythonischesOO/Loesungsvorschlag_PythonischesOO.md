# Lösungsvorschlag · Pythonisch oder übertragen?

**Vorbemerkung:** Ein Vorschlag, keine Musterlösung. Bei mehreren Aufgaben sind andere Entscheidungen vertretbar. Bewertet wird, ob jede Struktur **ein Problem löst, das in Python besteht**.

---

## 1 · Übertragene Konstrukte

| Konstrukt | Wo | Herkunft | Absicht dahinter |
|---|---|---|---|
| `getTimeout()` / `setTimeout()` usw. | `TestConfiguration`, `TestCase` | Java-Getter/Setter | Aufrufer vor späteren Änderungen am Feld schützen |
| `self.__timeout`, `self.__name` | beide Klassen | `private` | Felder vor fremdem Zugriff verbergen |
| `toString()` | `TestCase` | `Object.toString()` | lesbare Darstellung |
| `equals()` | `TestCase` | `Object.equals()` | fachliche Gleichheit |
| Klasse nur mit `@staticmethod` | `StringUtils` | statische Hilfsklasse | Funktionen unterbringen, weil Java keine freien Funktionen kennt |
| Klasse ohne Zustand, eine Methode | `TimestampFormatter` | Formatter-Objekte, z. B. `SimpleDateFormat` | Formatierung kapseln |

**Jede dieser Absichten ist berechtigt.** Die Frage ist nur, ob die übernommene Struktur sie in Python erreicht.

---

## 2 · Der Zugriff auf `_TestConfiguration__timeout`

Innerhalb der Klasse schreibt Python jeden Namen der Form `__name` in `_Klassenname__name` um (Name Mangling). Das Attribut heißt am Objekt tatsächlich `_TestConfiguration__timeout`. Wer das weiß, kann es lesen und setzen.

```python
config = TestConfiguration()
print(vars(config))
# {'_TestConfiguration__timeout': 20, '_TestConfiguration__can_interface': ..., ...}
```

**Was das über die Aussage „macht die Felder privat" sagt:** Sie trifft nicht zu. Name Mangling verhindert, dass eine Unterklasse mit einem gleichnamigen Attribut versehentlich das der Basisklasse überschreibt. Einen Zugriffsschutz gibt es in Python nicht, und die Sprache versucht auch nicht, einen herzustellen.

**Was der Test zeigt:** Er brauchte einen Weg, einen kurzen Timeout zu setzen. `setTimeout(5)` hätte genügt. Der direkte Zugriff ist ein Hinweis darauf, dass der Autor des Tests die vorgesehene Schnittstelle nicht als solche erkannt oder ihr nicht vertraut hat.

---

## 3 · `StringUtils` und `TimestampFormatter`

| | `StringUtils` | `TimestampFormatter` |
|---|---|---|
| Zustand | keiner | keiner |
| Instanz nötig | nein, nur `@staticmethod` | ja, aber sie trägt nichts bei |
| Rolle der Klasse | Namensraum | Behälter für eine Funktion |

In Python ist das **Modul** der Namensraum. `from text import normalize` leistet dasselbe wie `StringUtils.normalize`, ohne eine Klasse, die nie instanziiert wird.

`TimestampFormatter` wäre als Klasse berechtigt, wenn sie Zustand hätte, zum Beispiel ein konfigurierbares Format, oder wenn sie als austauschbarer Kollaborateur übergeben würde. Beides ist hier nicht der Fall.

---

## 4 · `TestConfiguration` pythonisch

```python
class TestConfiguration:
    """Laufzeiteinstellungen für einen Testlauf.

    Der Timeout gilt für Warteoperationen auf UI-Objekte und liegt
    zwischen 1 und 300 Sekunden.
    """

    def __init__(
        self,
        timeout: int = 20,
        can_interface: str = "can0",
        retries: int = 0,
    ) -> None:
        self.timeout = timeout
        self.can_interface = can_interface
        self.retries = retries

    @property
    def timeout(self) -> int:
        return self._timeout

    @timeout.setter
    def timeout(self, seconds: int) -> None:
        if not 1 <= seconds <= 300:
            raise ValueError(
                f"timeout must be between 1 and 300 seconds, got {seconds}"
            )
        self._timeout = seconds
```

**Welche Einstellung braucht eine Property:**

| Einstellung | Regel | Umsetzung |
|---|---|---|
| `timeout` | 1 bis 300 Sekunden | Property mit Prüfung im Setter |
| `can_interface` | keine genannt | öffentliches Attribut |
| `retries` | keine genannt | öffentliches Attribut |

**Zwei Details:**

- Im Konstruktor wird `self.timeout = timeout` geschrieben, nicht `self._timeout = timeout`. Damit greift die Prüfung auch beim Erzeugen.
- Der Test aus Material C wird zu `TestConfiguration(timeout=5)`. Er braucht keinen Umweg mehr.

Die Aufrufstelle aus Material C:

```python
config = TestConfiguration()
config.timeout = config.timeout * 2
```

---

## 5 · `toString()` und `equals()` als Protokollmethoden

```python
class TestCase:
    """Ein registrierter Testfall. Zwei Testfälle mit gleichem Namen gelten als gleich."""

    def __init__(self, name: str, tags: list[str]) -> None:
        self._name = name
        self.tags = tags

    @property
    def name(self) -> str:
        return self._name

    def __repr__(self) -> str:
        return f"TestCase({self._name!r}, {self.tags!r})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, TestCase):
            return NotImplemented
        return self._name == other._name

    def __hash__(self) -> int:
        return hash(self._name)
```

**Was sich ändert:**

| Stelle | Vorher | Nachher |
|---|---|---|
| `print(first)` | `<TestCase object at 0x…>` | `TestCase('select_implement', ['smoke'])` |
| `first == second` | `False` (Identitätsvergleich) | `True` (Name gleich) |
| `{first, second}` | zwei Elemente | ein Element |
| Meldung im Squish-Testprotokoll | Speicheradresse | lesbarer Testfall |

**Warum `__hash__` dazugehört:** Wer `__eq__` definiert, setzt `__hash__` implizit auf `None`. Ohne eigenes `__hash__` wäre `TestCase` nicht mehr in Sets verwendbar, und `{first, second}` würde mit `TypeError: unhashable type` abbrechen.

**Warum `name` eine Property ohne Setter ist:** Der Hash beruht auf dem Namen. Ändert sich der Name eines Testfalls, der bereits in einem Set liegt, findet das Set ihn nicht mehr. Der Name ist deshalb nur lesbar. Die Tags gehen nicht in Gleichheit und Hash ein und dürfen sich ändern.

**Warum kein `__str__`:** Ohne `__str__` verwendet `print()` die Ausgabe von `__repr__`. Für Testcode genügt das in der Regel.

**Eine fachliche Frage bleibt:** Sind zwei Testfälle mit gleichem Namen und verschiedenen Tags wirklich gleich? Das alte `equals()` sagte ja. Der Vorschlag übernimmt diese Bedeutung, ändert sie aber nicht stillschweigend.

---

## 6 · `StringUtils` und `TimestampFormatter` als Funktionen

```python
from datetime import datetime


def normalize(text: str) -> str:
    """Fasst Leerraum zusammen und wandelt in Kleinbuchstaben um."""
    return " ".join(text.split()).lower()


def is_blank(text: str | None) -> bool:
    return text is None or text.strip() == ""


def format_timestamp(moment: datetime) -> str:
    return moment.strftime("%Y-%m-%d %H:%M:%S")
```

Die Aufrufstellen:

```python
label = normalize("  Select   Implement ")
stamp = format_timestamp(datetime.now())
```

Liegen die Funktionen in einem Modul `text.py`, bleibt der Namensraum erhalten: `text.normalize(...)`.

---

## 7 · Die Begründung „damit wir später Validierung einbauen können"

Mit der Property-Variante:

| Zeitpunkt | Aufrufstelle |
|---|---|
| vor der Validierung (Attribut) | `config.timeout = 40` |
| nach der Validierung (Property) | `config.timeout = 40` |

**Kein Aufrufer ändert sich.** Die Absicht des Teams war richtig: Aufrufer sollen von einer späteren Regel nicht betroffen sein. In Java braucht es dafür Getter von Anfang an, weil ein Feldzugriff später nicht in einen Methodenaufruf umgewandelt werden kann. In Python übernimmt die Property genau diese Umwandlung.

Die Getter waren eine Vorleistung für einen Fall, der in sieben Jahren bei keinem der 29 logikfreien Paare eingetreten ist. In Python ist diese Vorleistung nicht nötig.

---

## 8 · Wann eine Methode besser ist als eine Property

Eine Methode wie `load_timeout()` ist in der Regel angemessen, wenn der Zugriff

| Kriterium | Beispiel |
|---|---|
| Parameter braucht | `timeout_for(screen_name)` |
| spürbar Zeit kostet | Wert wird aus Datei oder Konfigurationsdienst gelesen |
| Seiteneffekte hat | Zugriff protokolliert, zählt oder cached |
| fehlschlagen kann, ohne dass der Aufrufer damit rechnet | Netzwerkfehler, fehlende Datei |
| bei jedem Aufruf etwas anderes liefert | aktuelle Zeit, nächster freier Port |

Der Name der Methode sollte dann ausdrücken, was passiert: `load_`, `fetch_`, `compute_`.

---

## 9 · Eine Methode übergeben statt eines Interfaces

```python
from collections.abc import Callable


class Scheduler:
    def __init__(self) -> None:
        self._jobs: list[Callable[[], None]] = []

    def schedule(self, job: Callable[[], None]) -> None:
        self._jobs.append(job)

    def run_all(self) -> None:
        for job in self._jobs:
            job()


scheduler = Scheduler()
scheduler.schedule(smoke_suite.run)
```

**Was übergeben wird:** `smoke_suite.run` ohne Klammern ist eine **gebundene Methode**. Sie ist ein Objekt, das die Funktion `run` und die Instanz `smoke_suite` zusammenhält. Beim Aufruf `job()` wird `self` automatisch mitgegeben.

Braucht der Job Argumente, genügt eine Funktion, ein `lambda` oder `functools.partial`:

```python
from functools import partial

scheduler.schedule(partial(smoke_suite.run_tagged, "smoke"))
```

Ein Interface `Runnable` wäre hier eine zusätzliche Klasse ohne zusätzliche Aussage. Soll der Vertrag für Werkzeuge sichtbar werden, leistet das die Annotation `Callable[[], None]`.

---

## Diskussionsanschluss

`TestConfiguration` ist nach dem Umbau nicht kürzer als vorher. Welche der Änderungen verhindert einen Timeout von 0 in der gemeinsamen Konfiguration, und welche erleichtert nur die Analyse?
