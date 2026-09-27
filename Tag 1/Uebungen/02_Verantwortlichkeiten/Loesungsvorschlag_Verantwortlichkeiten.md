# Lösungsvorschlag · Wer ist hier wofür zuständig?

**Vorbemerkung:** Ein Vorschlag, keine Musterlösung. Schnitte nach Verantwortung lassen mehrere vertretbare Varianten zu. Bewertet wird, ob jede Klasse **einen Änderungsgrund** hat und ob jede Regel über Zustand **einen Ort**.

---

## 1 · Methoden und Änderungsgründe

| Methode | D1 JSON | D2 Lizenzstick | D3 Umgebungsvariablen | D4 Statusleiste | D5 REST-Reset | D6 Überlappung je Teilbreite |
|---|---|---|---|---|---|---|
| `load_config` | | | ja | | | |
| `unlock_service_menu` | | ja | indirekt | | | |
| `enter_section` | | | | | | |
| `set_overlap` | | | | | | ja |
| `wait_for_confirmation_dialog` | | | | ja | | |
| `compute_expected_working_width` | | | | | | ja |
| `take_screenshot` | | | | | | |
| `write_html_report` | ja | | indirekt | | | |
| `reset_database` | | | indirekt | | ja | |

„Indirekt" heißt: Die Methode ändert sich nicht selbst, bricht aber, wenn `load_config` sich ändert. Genau das ist das Risiko bei `load_config`.

**Sechs voneinander unabhängige Änderungsgründe**, angestoßen von vier verschiedenen Stellen: Teamleitung Qualitätssicherung, Produktmanagement, Betrieb der Testinfrastruktur, Fachbereich Applikationstechnik.

---

## 2 · Die Verantwortung in einem Satz

Ein zutreffender Satz lautet etwa:

> „`ImplementTestHelper` lädt die Konfiguration **und** bedient das Terminal **und** berechnet erwartete Breiten **und** erstellt Berichte **und** setzt die Datenbank zurück."

Das ist eine Aufzählung. Ein Satz ohne „und" gelingt nur auf einer Ebene, die nichts mehr aussagt: „hilft den Tests".

---

## 3 · Gruppen nach Zusammengehörigkeit

| Gruppe | Methoden | ändert sich bei | Verantwortung in einem Satz |
|---|---|---|---|
| Konfiguration | `load_config` | D3 | stellt die Einstellungen eines Testlaufs bereit |
| Freischaltung | `unlock_service_menu` | D2 | schaltet das Servicemenü frei |
| Geräteeinstellung | `enter_section`, `set_overlap`, `wait_for_confirmation_dialog` | D4, D6 (Bedienung) | bedient die Einstellungsseite eines Anbaugeräts |
| Erwartete Breiten | `compute_expected_working_width` | D6 (Regel) | kennt die Regel, gegen die geprüft wird |
| Berichte | `write_html_report`, `take_screenshot` | D1 | hält Ergebnis und Belege eines Tests fest |
| Testumgebung | `reset_database` | D5 | bringt die Datenbank in einen definierten Ausgangszustand |

**Zwei Abwägungen:**

- `unlock_service_menu` könnte zur Geräteeinstellung gehören, weil beides das Terminal bedient. D2 betrifft aber nur die Freischaltung, D4 nur die Einstellungsseite. Getrennt bleibt eine Umstellung auf den Lizenzstick auf eine Klasse beschränkt.
- D6 betrifft zwei Gruppen: die Bedienung (wo wird die Überlappung eingegeben) und die Regel (wie wird die Breite gerechnet). Das ist kein Widerspruch. Eine fachliche Änderung kann Oberfläche und Erwartung zugleich betreffen, aber jede an ihrem eigenen Ort.

Eine Skizze der neuen Aufteilung:

```text
implement_tests/
    configuration.py     load_config()
    service_menu.py      class ServiceMenu
    implement_page.py    class ImplementSettingsPage
    geometry.py          class Section, class Implement
    reporting.py         class HtmlReport, take_screenshot()
    environment.py       reset_database()
```

Wie Tests diese Teile erhalten, ist Thema von 1-3 und 1-5.

---

## 4 · Ungültige Zustände von `Implement`

| Stelle in Material B | Zustand | Warum ungültig |
|---|---|---|
| erster Builder | `status = "saved"`, `saved_at = None` | gespeichert ohne Zeitpunkt |
| erster Builder | eine Teilbreite mit 300 cm, `working_width_cm = 0` | Arbeitsbreite widerspricht den Teilbreiten |
| zweiter Test | `working_width_cm = 300`, danach zweite Teilbreite hinzugefügt | Arbeitsbreite veraltet |
| zweiter Test | `saved_at` gesetzt, `status = "draft"` | Zeitpunkt ohne Speichern |

**Die Regeln für ein gültiges Anbaugerät:**

1. Die Arbeitsbreite ist die Summe der Teilbreiten.
2. Ein Anbaugerät ist genau dann gespeichert, wenn es einen Speicherzeitpunkt hat.
3. Einem gespeicherten Anbaugerät werden keine Teilbreiten mehr hinzugefügt.
4. Ein Anbaugerät ohne Teilbreiten wird nicht gespeichert.

---

## 5 · `Implement` mit geschützten Regeln

```python
from datetime import datetime
from typing import Optional, Tuple


class Section:
    """Eine Teilbreite. Alle Längen in Zentimetern."""

    def __init__(self, name: str, nozzle_count: int, nozzle_spacing_cm: int, overlap_cm: int = 0) -> None:
        self.name = name
        self.nozzle_count = nozzle_count
        self.nozzle_spacing_cm = nozzle_spacing_cm
        self.overlap_cm = overlap_cm

    @property
    def width_cm(self) -> int:
        return self.nozzle_count * self.nozzle_spacing_cm - self.overlap_cm


class Implement:
    """Ein Anbaugerät, das als Entwurf bearbeitet wird, bis es gespeichert ist."""

    def __init__(self) -> None:
        self._sections: list = []
        self._saved_at: Optional[datetime] = None

    @property
    def sections(self) -> Tuple[Section, ...]:
        return tuple(self._sections)

    @property
    def working_width_cm(self) -> int:
        return sum(section.width_cm for section in self._sections)

    @property
    def saved_at(self) -> Optional[datetime]:
        return self._saved_at

    @property
    def is_saved(self) -> bool:
        return self._saved_at is not None

    def add(self, section: Section) -> None:
        if self.is_saved:
            raise ValueError("cannot add sections to a saved implement")
        self._sections.append(section)

    def save(self, timestamp: datetime) -> None:
        if self.is_saved:
            raise ValueError("implement is already saved")
        if not self._sections:
            raise ValueError("cannot save an implement without sections")
        self._saved_at = timestamp
```

**Wie jede Regel geschützt ist:**

| Regel | Mittel |
|---|---|
| 1 · Arbeitsbreite stimmt | `working_width_cm` wird berechnet, nicht gespeichert. Es gibt nichts, was veralten kann. |
| 2 · gespeichert genau mit Zeitpunkt | `is_saved` wird aus `saved_at` abgeleitet. Es gibt kein zweites Attribut `status`. |
| 3 · keine Teilbreiten nach dem Speichern | `add` prüft den Zustand. `sections` liefert ein Tupel, `append` von außen ist nicht möglich. |
| 4 · nicht leer speichern | `save` prüft die Teilbreiten. |

Die Builder aus Material B werden zu:

```python
implement = Implement()
implement.add(Section("section 1", 6, 50))
implement.save(datetime(2026, 9, 22, 10, 14))
```

Längen stehen hier als ganze Zentimeter. Mit `float` in Metern kann die Summe von Teilbreiten um Rundungsreste von der erwarteten Arbeitsbreite abweichen. Das ist nicht Thema dieser Einheit, verhindert aber eine zweite Fehlerquelle.

---

## 6 · Reicht ein Unterstrich?

Nein. Aus `implement.status = "saved"` würde `implement._status = "saved"`. Der Builder könnte dasselbe tun wie vorher, nur mit einem Zeichen mehr.

Der Unterstrich sagt: „Darauf soll fremder Code sich nicht verlassen." Er sagt nicht, **wie** ein Anbaugerät korrekt gespeichert wird. Das sagt erst `save()`. Erst wenn es einen offiziellen Weg gibt, hat der Builder keinen Grund mehr, das Attribut zu setzen.

In der Lösung aus Aufgabe 5 fällt außerdem ein Attribut ganz weg. `status` und `working_width_cm` existieren nicht mehr als gespeicherte Werte. Was nicht gespeichert ist, kann nicht falsch gesetzt werden.

---

## 7 · Tell, don't ask für C1

```python
from datetime import datetime
from typing import Optional


class TerminalNotReadyError(Exception):
    """Das Terminal kann in seinem aktuellen Zustand keine Teilbreite schalten."""


class Terminal:
    def __init__(self) -> None:
        self._state = "starting"
        self._implement: Optional[object] = None
        self._last_action: Optional[datetime] = None

    def switch_section(self, section_no: int) -> None:
        if self._state != "ready" or self._implement is None:
            raise TerminalNotReadyError(
                f"cannot switch section in state {self._state!r} without implement"
            )
        self._last_action = datetime.now()
        print(f"click: section {section_no}")
```

Der Test wird zu:

```python
terminal.switch_section(section_no)
```

**Die Prüfung** wandert in `switch_section`, weil nur das Terminal weiß, in welchen Zuständen es Teilbreiten schaltet. Kommt ein Zustand „Straßenfahrt" hinzu, ändert sich `switch_section` und kein Test.

**Die Aktualisierung von `last_action`** wandert ebenfalls in `switch_section`. Sie ist eine Folge des Schaltens und kein eigener Schritt des Tests.

Ein Test, der prüfen will, dass ein Terminal in Straßenfahrt nicht schaltet, erwartet jetzt die Exception (`test` ist das Squish-Modul):

```python
def check_road_mode_rejects_switch(terminal):
    try:
        terminal.switch_section(3)
    except TerminalNotReadyError:
        test.passes("section switch rejected in road mode")
    else:
        test.fail("section switch accepted in road mode")
```

---

## 8 · Feature Envy in `ReportWriter`

`section_width` verwendet `nozzle_count`, `nozzle_spacing_cm` und `overlap_cm` der Teilbreite und nichts vom `ReportWriter`. Die Berechnung gehört zur Teilbreite, in der Lösung aus Aufgabe 5 als `Section.width_cm`.

```python
class ReportWriter:
    def write_line(self, section: Section) -> None:
        print(f"{section.name}: {section.width_cm} cm")
```

**Was D6 ändert:** Wird die Überlappung künftig je Teilbreite eingestellt, ändert sich `Section` an einer Stelle. `ReportWriter`, `Implement.working_width_cm` und alle Builder, die `Section` verwenden, bleiben unverändert. Vorher stand die Rechnung an vier Stellen.

---

## 9 · Legitime Abfragen

| Stelle | Beispiel | Warum legitim |
|---|---|---|
| Prüfung | `test.compare(implement.working_width_cm, 1800)` | der Test prüft ein Ergebnis, er bedient das Objekt nicht |
| Bericht | `print(f"saved: {implement.saved_at}")` | Anzeige eines Zustands, keine Entscheidung über das Objekt |
| Testauswahl | `if not terminal_has_license_stick: return` | Entscheidung über den Test, nicht über das Terminal |

Die Grenze: Tell, don't ask betrifft Code, der Zustand abfragt, **um zu entscheiden, wie er das Objekt korrekt bedient**. Eine Prüfung entscheidet nichts am Objekt.

---

## 10 · „Das ist nur Testcode"

| Teil | Benutzt von | Lebensdauer |
|---|---|---|
| `load_config`, `unlock_service_menu`, `enter_section` | fast allen 412 Tests | seit 2018 |
| `write_html_report`, `take_screenshot`, `reset_database` | allen Tests | seit 2019 |
| `compute_expected_working_width`, `set_overlap` | allen Section-Control-Tests | seit 2020 |
| die konkreten Teilbreiten und Erwartungswerte | einem Test | so lange wie der Test |

**Was daraus folgt:** Die Infrastruktur in Material A ist langlebiger Code mit hunderten Aufrufern. Eine Änderung dort wirkt wie eine Änderung an einer Bibliothek. Sie verdient denselben Schnitt nach Verantwortung wie Produktivcode.

Ein einzelner Test darf direkt und linear sein. Er ändert sich selten und betrifft nur sich selbst.

---

## Diskussionsanschluss

Nach dem Umbau gibt es sechs Module statt einer Klasse. Welche der angekündigten Änderungen D1 bis D6 wäre damit in einer Datei erledigt, und bei welcher müssten weiterhin zwei Teams zusammenarbeiten?
