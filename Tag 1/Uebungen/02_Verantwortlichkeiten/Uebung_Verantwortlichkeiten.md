# Übung · Wer ist hier wofür zuständig?

Sie untersuchen Testcode für die Einstellungen von Anbaugeräten in einem Landmaschinen-Terminal. Der Code funktioniert und wird von vielen Tests benutzt. Die Frage ist, welche Verantwortung die einzelnen Klassen tragen und wo Entscheidungen getroffen werden, die eigentlich einem anderen Objekt gehören.

**Es werden keine Squish-Kenntnisse benötigt.** Technische Zugriffe auf die Oberfläche sind durch `print` ersetzt. Die fachlichen Regeln sind vereinfacht und erheben keinen Anspruch auf Vollständigkeit.

---

## Material A · Die Hilfsklasse

```python
import configparser


class ImplementTestHelper:
    """Hilfsfunktionen für die Tests der Geräteeinstellungen."""

    def load_config(self):
        parser = configparser.ConfigParser()
        parser.read("implement_tests.ini")
        return parser

    def unlock_service_menu(self):
        config = self.load_config()
        print(f"type pin: {config['service']['pin']}")
        print("click: unlockButton")

    def enter_section(self, section_no, width_cm):
        print(f"click: section {section_no}")
        print(f"type: {width_cm}")

    def set_overlap(self, percent):
        print("click: overlapButton")
        print(f"type: {percent}")

    def wait_for_confirmation_dialog(self):
        print("wait for object: confirmationDialog")

    def compute_expected_working_width(self, widths_cm, overlap_percent):
        total = sum(widths_cm)
        return round(total - total * overlap_percent / 100)

    def take_screenshot(self, name):
        print(f"screenshot: {name}.png")

    def write_html_report(self, test_name, passed):
        config = self.load_config()
        folder = config["report"]["folder"]
        print(f"write {folder}/{test_name}.html passed={passed}")

    def reset_database(self):
        config = self.load_config()
        print(f"DELETE FROM implements on {config['database']['host']}")
```

---

## Material B · Ein Anbaugerät als Datenobjekt

```python
class Implement:
    def __init__(self):
        self.sections = []
        self.working_width_cm = 0
        self.status = "draft"
        self.saved_at = None


# aus einem Testdaten-Builder
implement = Implement()
implement.sections.append(("section 1", 300))
implement.status = "saved"

# aus einem anderen Test
implement = Implement()
implement.sections.append(("section 1", 300))
implement.working_width_cm = 300
implement.sections.append(("section 2", 300))
implement.saved_at = "2026-09-22 10:14"
```

---

## Material C · Zwei Stellen aus Tests und Reporting

```python
from datetime import datetime


# C1 · aus einem Test
if terminal.state == "ready" and terminal.implement is not None:
    terminal.last_action = datetime.now()
    terminal.switch_section(section_no)


# C2 · aus dem Reporting
class ReportWriter:
    def section_width(self, section):
        return section.nozzle_count * section.nozzle_spacing_cm - section.overlap_cm

    def write_line(self, section):
        print(f"{section.name}: {self.section_width(section)} cm")
```

---

## Material D · Was sich im nächsten Halbjahr ändern wird

| Nr. | Änderung | Quelle |
|---|---|---|
| D1 | Der Bericht soll zusätzlich als JSON erzeugt werden | Teamleitung Qualitätssicherung |
| D2 | Das Servicemenü wird künftig per USB-Lizenzstick statt PIN freigeschaltet | Produktmanagement |
| D3 | Konfiguration kommt aus Umgebungsvariablen statt aus einer INI-Datei | Betrieb der Testinfrastruktur |
| D4 | Der Bestätigungsdialog wird durch eine Meldung in der Statusleiste ersetzt | Produktmanagement |
| D5 | Die Datenbank wird über eine REST-Schnittstelle zurückgesetzt statt per SQL | Betrieb der Testinfrastruktur |
| D6 | Die Überlappung wird künftig je Teilbreite statt für das ganze Gerät eingestellt | Fachbereich Applikationstechnik |

---

## Aufgabe

### Teil 1 · Änderungsgründe

**1.** Ordnen Sie jeder Methode von `ImplementTestHelper` die Änderungen aus Material D zu, die sie betreffen würden. Wie viele voneinander unabhängige Änderungsgründe hat die Klasse?

**2.** Formulieren Sie die Verantwortung von `ImplementTestHelper` in einem Satz. Gelingt das, ohne mehrere Aufgaben mit „und" aneinanderzureihen?

**3.** Gruppieren Sie die Methoden nach Zusammengehörigkeit. Welche Gruppen ändern sich gemeinsam, welche unabhängig voneinander?

### Teil 2 · Invarianten schützen

**4.** Welche Zustände von `Implement` entstehen in Material B, die fachlich nicht gültig sind? Formulieren Sie die Regeln, die für ein gültiges Anbaugerät gelten sollten.

**5.** Bauen Sie `Implement` so um, dass diese Regeln nicht mehr verletzt werden können, ohne dass ein Aufrufer bewusst Implementierungsdetails anfasst.

**6.** Genügt es, die Attribute in `_sections`, `_working_width_cm`, `_status` umzubenennen? Begründen Sie.

### Teil 3 · Tell, don't ask und Feature Envy

**7.** Schreiben Sie C1 so um, dass der Test nicht mehr selbst entscheidet, ob das Terminal bereit ist. Wohin wandert die Prüfung, wohin die Aktualisierung von `last_action`?

**8.** `ReportWriter.section_width` greift ausschließlich auf Daten der Teilbreite zu. Wo gehört die Berechnung hin? Was ändert sich, wenn D6 umgesetzt wird?

**9.** Nicht jede Abfrage ist ein Verstoß gegen Tell, don't ask. Nennen Sie zwei Stellen in Testcode, an denen ein Objekt legitim nach seinem Zustand gefragt wird.

### Teil 4 · Testcode ist Code

**10.** Ein Kollege sagt: „Das ist nur Testcode, da lohnt sich kein Design." Welche Teile aus Material A werden von vielen Tests über Jahre benutzt, welche gehören zu einem einzelnen Test? Was folgt daraus für die Frage, wie sorgfältig sie geschnitten sein sollten?

---

## Hinweise zur Bearbeitung

- Der Code muss nicht ausgeführt werden. Er sollte aber so geschrieben sein, dass er lauffähig wäre.
- Für Teil 1 genügt eine Tabelle. Ein Umbau von `ImplementTestHelper` ist nicht verlangt, eine Skizze der neuen Aufteilung reicht.
- Wie die neuen Klassen zueinanderfinden, ist Thema von 1-3 und 1-5. Hier zählt nur, wer wofür zuständig ist.
- Wenn Sie unsicher sind, ob eine Methode in eine Klasse gehört, fragen Sie: **Welches Ereignis würde sie ändern – und ändert dasselbe Ereignis auch den Rest der Klasse?**
