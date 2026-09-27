# Übung · Der Section-Control-Test

Sie untersuchen gewachsenen Testcode für die Section-Control-Tests eines Landmaschinen-Terminals und entwickeln einen Zielentwurf. Der Code funktioniert. Er ist über Jahre entstanden, jede einzelne Entscheidung war zu ihrer Zeit naheliegend.

Die Übung verbindet die Themen des Tages. Es geht nicht darum, möglichst viele Techniken einzubauen, sondern darum, Entscheidungen zu begründen.

**Es werden keine Squish-Kenntnisse benötigt.** Squish, Testdaten, Target und Simulation sind durch Platzhalter ersetzt. Der Code liegt auch als `Tag 1/Beispiele/1-8_Design_Challenge_vorher.py` vor und läuft unter Python 3.10. Die fachlichen Details sind vereinfacht und erheben keinen Anspruch auf Richtigkeit.

---

## Material A · Der Ausgangscode

```python
"""Section-Control-Test, gewachsener Stand."""
from contextlib import contextmanager
from dataclasses import dataclass
from typing import Optional

calls = []
ROWS = [{"name": "narrow", "tr_turn_radius": "6.5", "tr_wheelbase": "2.8"},   # Platzhalter für
        {"name": "wide", "tr_turn_radius": "150", "tr_wheelbase": ""}]         # testData.dataset()

test_config = None


def get_test_config():
    return test_config


@dataclass
class NumValueDTO:
    value: Optional[float]
    unit: str
    min: float
    max: float
    input_value: Optional[str] = None

    def set_input_value(self, value):
        self.input_value = value
        self.value = float(value) if value is not None else None

    def get_input_value(self):
        return self.input_value


@dataclass
class TractorDTO:
    name: str = "Tractor"
    turn_radius: NumValueDTO = NumValueDTO(0, "m", 0, 100)
    wheelbase: NumValueDTO = NumValueDTO(0, "m", 0, 10)


@dataclass
class AbstractSectionControlTest:
    data_set: str = "clear"

    def __post_init__(self):
        global test_config
        test_config = self
        self.data_set = "with_sc_boundary"
        self.test_sets = [self.read_test_set(r) for r in ROWS]

    def read_test_set(self, record):
        tractor = TractorDTO(name=self.get_data_value(record, "name", "Tractor"))
        tractor.turn_radius.set_input_value(
            self.get_data_value(record, "tr_turn_radius", tractor.turn_radius.get_input_value()))
        tractor.wheelbase.set_input_value(
            self.get_data_value(record, "tr_wheelbase", tractor.wheelbase.get_input_value()))
        return tractor

    @staticmethod
    def get_data_value(record, column, def_val, is_bool=False, cast_type=None):
        value = record.get(column, "").strip()
        if not value:
            return def_val
        if is_bool:
            return value in ("true", "t", "v")
        return cast_type(value) if cast_type else value


class Target:
    def replace_data_set(self, name): calls.append(f"replace {name}")
    def backup_data_set(self, name): calls.append("backup"); raise PermissionError("backup dir")
    def cleanup(self): calls.append("target cleanup")


target = Target()


@contextmanager
def test_wrapper():
    failed = False
    try:
        target.replace_data_set(get_test_config().data_set)
        yield
    except Exception as e:
        failed = True
        calls.append(f"FAIL {e}")
    finally:
        if failed:
            target.backup_data_set("_backup_after_fail")
        target.cleanup()
        calls.append("stop simulation")


def main():
    config = AbstractSectionControlTest(data_set="sc_set_3")
    with test_wrapper():
        for tractor in config.test_sets:
            calls.append(f"drive {tractor.name} r={tractor.turn_radius.value}")
            assert tractor.turn_radius.value <= 100, "turn radius out of range"


if __name__ == "__main__":
    try:
        main()
    except PermissionError as error:
        calls.append(f"propagiert: {error!r}")
    print("\n".join(calls))
```

Die Ausgabe eines Laufs:

```text
replace with_sc_boundary
drive narrow r=150.0
FAIL turn radius out of range
backup
propagiert: PermissionError('backup dir')
```

---

## Material B · Die Change Requests

| Nr. | Änderung |
|---|---|
| **CR1** | Testsätze kommen zusätzlich aus einer JSON-Datei der CI. |
| **CR2** | Einlesen und Aufbereiten der Testsätze soll ohne Squish und Target prüfbar sein. |
| **CR3** | Ein Wenderadius außerhalb des erlaubten Bereichs soll beim Einlesen auffallen. |
| **CR4** | Die Simulation wird auch gestoppt, wenn das Sichern nach einem Fehler scheitert. |
| **CR5** | Ein Test soll mit einem anderen Datensatz als `with_sc_boundary` laufen können. |

---

## Material C · Aussagen aus dem Team

Ein Testautomatisierer, seit Beginn im Projekt:

> „Die globale Konfiguration hat uns viel Arbeit erspart. Jeder Helper kommt über `get_test_config()` an alles heran, niemand muss Parameter durchreichen. Wenn ich das jetzt überall übergebe, werden die Signaturen endlos."

Die Leiterin der Testautomatisierung:

> „Im letzten Nachtlauf fuhr der Traktor `narrow` laut Protokoll mit 150 m Wenderadius. In den Testdaten stehen 6,5 m. Danach liefen 38 Tests nicht mehr an, weil die Simulation noch lief."

---

## Aufgabe

### Teil 1 · Analysieren, ohne zu ändern

**1.** Ändern Sie noch nichts. Lassen Sie den Code einmal laufen. Markieren Sie im Code alle Stellen, an denen Sie eine Designentscheidung sehen, und ordnen Sie jede einer Kategorie zu: *Verantwortung*, *Abhängigkeit*, *Zustand und Lifecycle*, *Vererbung*, *öffentliche API*, *technische Kopplung*.

**2.** Welche Verantwortlichkeiten hat `AbstractSectionControlTest`? Formulieren Sie für jede einen Änderungsgrund.

**3.** `AbstractSectionControlTest` trägt sich in `__post_init__` in die globale Variable `test_config` ein. Welche Stellen lesen die Konfiguration darüber, und was davon ist an ihren Signaturen zu erkennen?

### Teil 2 · Change Requests als Hotspot-Suche

**4.** Tragen Sie für jeden Change Request aus Material B ein, welche Methoden oder Stellen im Ausgangscode Sie ändern müssten.

**5.** Welche Stellen tauchen bei mehreren Change Requests auf? Was sagt das über die Kopplung im Code?

**6.** Die Leiterin der Testautomatisierung nennt zwei Beobachtungen. Welche Stelle im Code erklärt den Wenderadius von 150 m für `narrow`? Welche erklärt, dass die Simulation weiterlief? Spielen Sie beide Abläufe durch.

### Teil 3 · Zielentwurf

**7.** Entwickeln Sie einen Zielentwurf, der alle fünf Change Requests trägt. Es genügt Code für die Section-Control-Tests, Skizzen für den Rest sind erlaubt.

**8.** Nennen Sie für jede neue Klasse, jedes Protocol, jede ABC, jede Funktion und jeden Context Manager in Ihrem Entwurf:
- welches konkrete Problem sie löst (Change Request oder Aufgabe 6),
- was schlechter wäre, wenn Sie sie wieder entfernen.

Streichen Sie, was Sie nicht begründen können.

### Teil 4 · Entwürfe vergleichen

**9.** Stellen Sie Ihren Entwurf einem zweiten gegenüber, dem einer anderen Gruppe oder einer Variante, die Sie selbst verworfen haben. Füllen Sie die Tabelle aus:

| Frage | Entwurf A | Entwurf B |
|---|---|---|
| Welche Änderung wird leichter? | | |
| Welche Kopplung sinkt? | | |
| Welche neue Komplexität entsteht? | | |
| Wie testbar ist der Entwurf? | | |
| Welche Annahmen macht er? | | |
| Welche Teamregel steckt dahinter? | | |

**10.** Formulieren Sie aus Ihren Entscheidungen drei bis fünf Kandidaten für den Teamstandard. Ordnen Sie jeden ein: **MUST**, **SHOULD**, **MAY**, **DON'T** oder **noch offen**.

---

## Hinweise zur Bearbeitung

- **Teil 1 zuerst.** Wer sofort Klassen extrahiert, löst Probleme, die er noch nicht benannt hat.
- Der Entwurf muss nicht ausgeführt werden. Er sollte aber so geschrieben sein, dass er lauffähig wäre.
- Es gibt keinen vorgegebenen Zielentwurf. Mehrere Lösungen sind tragfähig, wenn ihre Entscheidungen begründet sind.
- Wenn Sie unsicher sind, ob eine Abstraktion bleiben soll, fragen Sie: **Welcher Change Request braucht sie?**
