# Lösungsvorschlag · Der Section-Control-Test

**Vorbemerkung:** Ein Vorschlag, keine Musterlösung. Es gibt mehrere tragfähige Entwürfe. Bewertet wird, ob jede Entscheidung **einem Change Request oder einer Beobachtung aus Aufgabe 6 zugeordnet** ist und ob der Entwurf Folgefehler verhindert.

---

## 1 · Markierungen im Ausgangscode

| Stelle | Kategorie | Beobachtung |
|---|---|---|
| `test_config = None`, `get_test_config()` | Abhängigkeit | globale Konfiguration, an keiner Signatur sichtbar |
| `__post_init__`: `global test_config` | Zustand und Lifecycle | das Erzeugen einer Konfiguration verändert globalen Zustand |
| `__post_init__`: `self.data_set = "with_sc_boundary"` | öffentliche API | der Konstruktorparameter `data_set` wird überschrieben |
| `__post_init__`: `self.test_sets = [...]` aus `ROWS` | Verantwortung, technische Kopplung | die Konfiguration liest Testdaten aus einer festen Quelle |
| `TractorDTO`: `NumValueDTO(...)` als Vorgabewert | Zustand und Lifecycle | ein Objekt für alle Instanzen |
| `set_input_value` / `get_input_value` | öffentliche API | Getter und Setter, `value` bleibt öffentlich |
| `NumValueDTO(0, "m", 0, 100)` | Verantwortung | `min`/`max` werden nie geprüft |
| `get_data_value(..., is_bool, cast_type)` | öffentliche API | Schalter-Parameter, keiner wird verwendet |
| `target = Target()` auf Modulebene | Abhängigkeit | globales Target, von `test_wrapper` direkt verwendet |
| `test_wrapper`: Kette im `finally` | Zustand und Lifecycle | scheitert ein Schritt, entfallen die folgenden |

Vererbung kommt im Ausgangscode nicht vor. Das ist eine eigene Beobachtung: Nicht jeder gewachsene Code leidet an Vererbung. Die Konfiguration im Testframework hat eine Hierarchie (siehe 1-3), dieser Ausschnitt zeigt nur ihre unterste Ebene.

---

## 2 · Verantwortlichkeiten von `AbstractSectionControlTest`

| Verantwortung | Änderungsgrund |
|---|---|
| Konfigurationswerte halten | ein neuer Wert für einen Test |
| sich global registrieren | eine andere Art, Konfiguration bereitzustellen |
| den Datensatz festlegen | ein Test braucht einen anderen Datensatz (CR5) |
| Testdaten beschaffen | eine neue Quelle wie JSON aus der CI (CR1) |
| Zeilen in DTOs umwandeln | neue Spalten, andere Prüfregeln (CR3) |
| Texte in Werte umwandeln (`get_data_value`) | ein neues Format in der Datei |

Sechs Änderungsgründe in einer Klasse, deren Name nur „Konfiguration eines Section-Control-Tests" verspricht.

---

## 3 · Wer liest die globale Konfiguration?

Im Ausgangscode liest `test_wrapper` den Datensatz über `get_test_config().data_set`. Die Signatur `test_wrapper()` hat keinen Parameter. Dass der Wrapper eine vorher erzeugte Konfiguration voraussetzt, steht nirgends. Ruft ein Test `test_wrapper()` ohne vorherige Konfiguration auf, endet das mit `AttributeError: 'NoneType' object has no attribute 'data_set'`.

Laut Ticket gibt es 64 solcher Aufrufe in Helpern. Keiner davon ist an einer Signatur erkennbar. Wer wissen will, welche Helper von der Konfiguration abhängen, muss den Code durchsuchen.

---

## 4 · Betroffene Stellen je Change Request

| CR | Betroffene Stellen |
|---|---|
| CR1 JSON aus der CI | `__post_init__` (Quelle `ROWS`), `read_test_set` (Spaltenzugriff) |
| CR2 ohne Squish prüfbar | `__post_init__` (Einlesen beim Erzeugen, globale Registrierung), `read_test_set`, `get_data_value` |
| CR3 Bereich prüfen | `NumValueDTO`, `read_test_set` (Fehlermeldung mit Testsatz und Spalte) |
| CR4 Simulation stoppen | `test_wrapper` (`finally`-Kette) |
| CR5 Datensatz wählbar | `__post_init__` (Überschreiben von `data_set`), `test_wrapper` (liest `data_set` global) |

---

## 5 · Hotspots

| Stelle | CRs |
|---|---|
| `AbstractSectionControlTest.__post_init__` | CR1, CR2, CR5 |
| `read_test_set` | CR1, CR2, CR3 |
| `test_wrapper` | CR4, CR5 |
| `NumValueDTO` | CR3 |

`__post_init__` und `read_test_set` tragen je drei Änderungsgründe. Dort kommen Konfiguration, Datenquelle und Umwandlung zusammen. Ein Entwurf, der CR1 bis CR3 trägt, trennt diese Aufgaben.

---

## 6 · Die zwei Beobachtungen

**150 m Wenderadius für `narrow`.** `TractorDTO` hat `turn_radius: NumValueDTO = NumValueDTO(0, "m", 0, 100)`. Der Vorgabewert wird einmal beim Laden der Klasse erzeugt. Beide Traktoren teilen sich dieses Objekt.

```text
read_test_set(narrow)  -> turn_radius.set_input_value("6.5")   geteiltes Objekt: 6.5
read_test_set(wide)    -> turn_radius.set_input_value("150")   geteiltes Objekt: 150
drive narrow r=150.0
```

Dasselbe betrifft `wheelbase`. `wide` hat eine leere Spalte. `get_data_value` liefert dann den Vorgabewert `tractor.wheelbase.get_input_value()`, und das ist der Wert, den `narrow` gerade gesetzt hat: 2,8. Ein leerer Eintrag übernimmt damit den Wert eines anderen Testsatzes.

Unter Python 3.12 würde der Fehler gar nicht erst auftreten: Die Klassendefinition bricht dort mit `ValueError: mutable default ... use default_factory` ab.

**Die Simulation lief weiter.** Der Test bricht mit `AssertionError` ab. `test_wrapper` fängt ihn und setzt `failed = True`. Im `finally` ruft er `target.backup_data_set(...)` auf, das mit `PermissionError` scheitert. Die Exception verlässt das `finally` sofort. `target.cleanup()` und das Stoppen der Simulation werden nicht mehr erreicht. Der nächste Test findet eine laufende Simulation vor.

---

## 7 · Zwei Zielentwürfe

### Entwurf A · Funktionen und ein Context Manager

Vollständig in `Tag 1/Beispiele/1-8_Design_Challenge_nachher.py`. Der Kern:

```python
import json
from contextlib import ExitStack, contextmanager
from dataclasses import dataclass, field
from typing import Iterable, List, Mapping, Optional

calls = []


class NumValueDTO:                                        # CR3: Bereich an einer Stelle
    def __init__(self, value: Optional[float], unit: str, min: float, max: float) -> None:
        self.unit, self.min, self.max = unit, min, max
        self.value = value

    @property
    def value(self) -> Optional[float]:
        return self._value

    @value.setter
    def value(self, value: Optional[float]) -> None:
        if value is not None and not self.min <= value <= self.max:
            raise ValueError(f"{value} {self.unit} outside {self.min}..{self.max}")
        self._value = value

    @property
    def input_value(self) -> Optional[str]:
        if self._value is None:
            return None
        text = str(float(self._value))
        return text[:-2] if text.endswith(".0") else text

    @input_value.setter
    def input_value(self, text: Optional[str]) -> None:
        self.value = float(text) if text is not None else None


@dataclass
class TractorDTO:                                         # eigener Vorgabewert je Instanz
    name: str = "Tractor"
    turn_radius: NumValueDTO = field(default_factory=lambda: NumValueDTO(0, "m", 0, 100))
    wheelbase: NumValueDTO = field(default_factory=lambda: NumValueDTO(0, "m", 0, 10))


def read_tractor(record: Mapping[str, str]) -> TractorDTO:   # CR2: ohne Squish prüfbar
    tractor = TractorDTO(name=record.get("name") or "Tractor")
    for column, dto in (("tr_turn_radius", tractor.turn_radius), ("tr_wheelbase", tractor.wheelbase)):
        text = record.get(column, "").strip()
        if text:
            try:
                dto.input_value = text
            except ValueError as error:
                raise ValueError(f"{tractor.name}: {column}: {error}") from error
    return tractor


def records_from_json(text: str) -> List[Mapping[str, str]]:  # CR1: zweite Quelle
    return json.loads(text)


@dataclass
class SectionControlConfig:                               # CR5: Datensatz frei wählbar
    test_sets: List[TractorDTO]
    data_set: str = "with_sc_boundary"


@contextmanager
def test_wrapper(target, simulation, config: SectionControlConfig):   # CR4
    failed = False

    def save_evidence_if_failed():
        if failed:
            target.backup_data_set("_backup_after_fail")

    with ExitStack() as cleanup:
        cleanup.callback(simulation.stop)
        cleanup.callback(target.cleanup)
        cleanup.callback(save_evidence_if_failed)
        target.replace_data_set(config.data_set)
        try:
            yield
        except Exception as e:
            failed = True
            calls.append(f"FAIL {e}")
```

### Entwurf B · Datenquelle, Leser und Sitzung als Objekte

```python
import csv
import io
import json
from contextlib import ExitStack
from dataclasses import dataclass
from typing import Iterable, List, Mapping, Protocol

# NumValueDTO und TractorDTO wie in Entwurf A


class TestDataSource(Protocol):
    def records(self) -> Iterable[Mapping[str, str]]: ...


class TsvSource:
    def __init__(self, text: str) -> None:
        self._text = text

    def records(self) -> Iterable[Mapping[str, str]]:
        return csv.DictReader(io.StringIO(self._text), delimiter="\t")


class JsonSource:
    def __init__(self, text: str) -> None:
        self._text = text

    def records(self) -> Iterable[Mapping[str, str]]:
        return json.loads(self._text)


class TractorReader:
    """Macht aus den Datensätzen einer Quelle Traktoren."""

    COLUMNS = {"tr_turn_radius": "turn_radius", "tr_wheelbase": "wheelbase"}

    def __init__(self, source: TestDataSource) -> None:
        self._source = source

    def read(self) -> List[TractorDTO]:
        return [self._read_one(r) for r in self._source.records()]

    def _read_one(self, record: Mapping[str, str]) -> TractorDTO:
        tractor = TractorDTO(name=record.get("name") or "Tractor")
        for column, attribute in self.COLUMNS.items():
            text = (record.get(column) or "").strip()
            if text:
                try:
                    getattr(tractor, attribute).value = float(text)
                except ValueError as error:
                    raise ValueError(f"{tractor.name}: {column}: {error}") from error
        return tractor


class Target(Protocol):
    def replace_data_set(self, name: str) -> None: ...
    def backup_data_set(self, name: str) -> None: ...
    def cleanup(self) -> None: ...


class Simulation(Protocol):
    def stop(self) -> None: ...


@dataclass
class SectionControlConfig:
    test_sets: List[TractorDTO]
    data_set: str = "with_sc_boundary"


class TestSession:
    """Lebenszyklus eines Tests: Datensatz, Target, Simulation."""

    def __init__(self, target: Target, simulation: Simulation, config: SectionControlConfig) -> None:
        self._target = target
        self._simulation = simulation
        self._config = config
        self._stack = ExitStack()

    def __enter__(self) -> "TestSession":
        self._stack.callback(self._simulation.stop)
        self._stack.callback(self._target.cleanup)
        self._target.replace_data_set(self._config.data_set)
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        if exc_value is not None:
            self._stack.callback(self._target.backup_data_set, "_backup_after_fail")
        return self._stack.__exit__(exc_type, exc_value, traceback)
```

### Was beide gemeinsam haben

- `NumValueDTO` prüft seinen Bereich im Setter (CR3).
- `TractorDTO` erzeugt seine Vorgabewerte mit `default_factory` (Aufgabe 6).
- Die Konfiguration ist ein Datenhalter ohne `__post_init__`, `data_set` ist ein normaler Parameter mit Vorgabe (CR5).
- Das Aufräumen läuft über `ExitStack`, jeder Schritt einzeln registriert (CR4).
- Keine globale Konfiguration, kein globales Target. Beides wird übergeben.

### Die Change Requests in beiden Entwürfen

| CR | Entwurf A | Entwurf B |
|---|---|---|
| CR1 | `records_from_json` liefert Datensätze, `read_tractor` verarbeitet sie | `JsonSource` neben `TsvSource`, beide über `TestDataSource` |
| CR2 | `read_tractor(record)` ist eine Funktion ohne Umgebung | `TractorReader(source).read()` mit einer Quelle aus Text |
| CR3 | `NumValueDTO`, Fehlermeldung mit Name und Spalte in `read_tractor` | ebenso, in `TractorReader._read_one` |
| CR4 | `test_wrapper` mit `ExitStack` | `TestSession` mit `ExitStack` |
| CR5 | `SectionControlConfig(data_set=...)` | ebenso |

---

## 8 · Begründung jeder neuen Abstraktion

### Entwurf A

| Neu | Löst | Wenn wieder entfernt |
|---|---|---|
| `read_tractor` | CR2, CR3 | Einlesen wieder nur über die Konfiguration prüfbar |
| `records_from_json` | CR1 | JSON-Testsätze bräuchten einen eigenen Weg |
| `SectionControlConfig` | CR5 | Datensatz wieder fest verdrahtet |
| `ExitStack` in `test_wrapper` | CR4 | Folgefehler nach gescheitertem Aufräumen |

### Entwurf B

| Neu | Löst | Wenn wieder entfernt |
|---|---|---|
| `TestDataSource`, `TsvSource`, `JsonSource` | CR1 | wie Entwurf A: eine Funktion je Format |
| `TractorReader` | CR2, CR3 | wie Entwurf A: eine Funktion |
| `Target`, `Simulation` (Protocols) | keiner der CRs | nichts, außer Typprüfung durch mypy |
| `TestSession` | CR4 | wie Entwurf A: ein `@contextmanager` |
| `SectionControlConfig` | CR5 | Datensatz wieder fest verdrahtet |

Die Protocols `Target` und `Simulation` lösen keinen Change Request. Nach AK7 gehören sie gestrichen, solange niemand einen Test oder eine zweite Implementierung benennt, die sie braucht.

---

## 9 · Vergleich

| Frage | Entwurf A | Entwurf B |
|---|---|---|
| Welche Änderung wird leichter? | ein neues Format: eine Funktion, die Datensätze liefert | ein neues Format: eine Klasse mit `records()` |
| Welche Kopplung sinkt? | keine globale Konfiguration, kein globales Target | ebenso, zusätzlich explizite Verträge für Quellen |
| Welche neue Komplexität entsteht? | vier Bausteine | acht Bausteine, davon zwei ohne CR |
| Wie testbar ist der Entwurf? | Funktionen mit Werten, Doubles für Target und Simulation | ebenso, Quellen lassen sich aus Text erzeugen |
| Welche Annahmen macht er? | Formate liefern Datensätze als Dictionaries | es kommen weitere Quellen mit eigenem Zustand hinzu |
| Welche Teamregel steckt dahinter? | „Funktionen, bis ein Objekt Zustand braucht" | „Grenzen bekommen einen expliziten Vertrag" |

Für die fünf Change Requests reicht Entwurf A. Entwurf B lohnt sich, wenn Quellen eigenen Zustand bekommen, etwa eine Verbindung zu einem Server der CI, oder wenn mehrere Teams eigene Quellen beisteuern.

---

## 10 · Kandidaten für das Rule Board

| Kandidat | Einordnung |
|---|---|
| Veränderliche Objekte werden nicht als Vorgabewerte von Datenklassen verwendet, sondern über `default_factory` erzeugt. | **MUST**, von Python ab 3.11 teilweise erzwungen |
| Cleanup-Schritte werden einzeln registriert (`ExitStack` oder Context Manager je Ressource), nicht als Kette in einem `finally`. | **SHOULD** |
| Konfiguration wird übergeben und nicht beim Erzeugen global eingetragen. | **SHOULD**, Übergang für die 64 vorhandenen Aufrufe offen |
| Wertebereiche prüft das Objekt, das sie kennt. | **SHOULD** |
| Protocols werden eingeführt, wenn ein Test oder eine zweite Implementierung sie braucht. | **noch offen** |

---

## Diskussionsanschluss

Beide Entwürfe beheben den geteilten Vorgabewert und die Folgefehler beim Aufräumen. Welcher der beiden würde bei Ihnen die Umstellung der übrigen 45 Konfigurationen leichter machen, und warum?
