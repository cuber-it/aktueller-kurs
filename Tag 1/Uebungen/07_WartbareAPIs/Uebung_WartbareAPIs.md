# Übung · Was dürfen andere Teams benutzen?

Sie untersuchen einen Ausschnitt aus einem Testframework, das mehrere Suite-Teams gemeinsam verwenden. Der Code funktioniert. Die Frage ist, welche Teile davon eine Schnittstelle sind, auf die sich andere verlassen dürfen, und wie diese Schnittstelle aussehen sollte.

**Es werden keine Squish-Kenntnisse benötigt.** Technische Zugriffe sind durch `print` ersetzt. Die fachlichen Details sind vereinfacht und erheben keinen Anspruch auf Richtigkeit.

---

## Material A · Die Modulstruktur des Frameworks

```text
testframework/
    common.py         340 Zeilen   ResultCollector, Konfiguration laden, Retry-Dekorator
    utils.py          610 Zeilen   Zeitformatierung, Screenshot-Ablage, Warten auf Dialoge, JSON-Hilfen
    helpers.py        280 Zeilen   Freischaltung, Testdaten erzeugen, Anbaugeräte anlegen
    test_helpers.py   190 Zeilen   Asserts für Tabellen, Vergleich von Screenshots
    screens.py        680 Zeilen   Zugriff auf Bildschirmelemente aller Bereiche
```

---

## Material B · Ein Ausschnitt aus `common.py`

```python
import json
import time


class ResultCollector:
    def __init__(self, output_dir):
        self.output_dir = output_dir
        self.results = {}
        self.started = time.time()

    def add(self, n, s, d, msg=None):
        """Adds a result."""
        self.results[n] = {"status": s, "duration": d, "message": msg}

    def get_results(self):
        """Returns the results."""
        return self.results

    def export(self, fmt="html"):
        """Schreibt den Bericht ins Ausgabeverzeichnis.

        fmt: "html" oder "json". Vorhandene Dateien werden überschrieben.
        Unbekannte Formate führen zu ValueError.
        """
        if fmt == "html":
            self._write_html()
        elif fmt == "json":
            self._write_json(self.output_dir + "/results.json")
        else:
            raise ValueError(f"unknown format: {fmt}")

    def _write_html(self):
        print(f"write HTML report to {self.output_dir}")

    def _write_json(self, path):
        with open(path, "w", encoding="utf-8") as file:
            json.dump(self.results, file)

    def _format_duration(self, seconds):
        return f"{seconds:.1f} s"

    def _failed(self):
        return [n for n, r in self.results.items() if r["status"] == "failed"]
```

---

## Material C · So verwenden die Suite-Teams den Collector

```python
# Team UT: markiert instabile Tests nachträglich
collector.add("select_implement", "passed", 3.2)
collector.results["select_implement"]["status"] = "flaky"

# Team AEF: schreibt JSON an einen eigenen Ort
collector._write_json("/shared/nightly/aef.json")
print(collector._format_duration(12.5))

# Team Einstellungen: bricht die Pipeline bei Fehlern ab
failed = collector._failed()
if failed:
    print(f"{len(failed)} tests failed")

# Team Section Control: wertet alle Ergebnisse aus
for name, result in collector.get_results().items():
    print(name, result["status"])
```

---

## Material D · Review-Kommentare aus dem letzten Quartal

Eine Auswahl aus Code-Reviews im Framework-Repository:

1. „Zeile ist länger als 88 Zeichen."
2. „Imports bitte alphabetisch sortieren."
3. „Hier fehlt ein Type Hint für den Rückgabewert."
4. „Die Methode heißt `proc` – was verarbeitet sie?"
5. „Warum ist diese Methode öffentlich? Soll das jemand von außen aufrufen?"
6. „Zwei Leerzeilen vor der Klassendefinition."
7. „Gehört das wirklich nach `utils.py`? Das hat mit Reporting zu tun."
8. „`json` wird importiert, aber nicht verwendet."
9. „Der Docstring sagt nicht, was bei einem unbekannten Format passiert."
10. „Bitte `camelCase` durch `snake_case` ersetzen."

Das Plattformteam, das das Framework pflegt:

> „Wir haben `_write_json` umbenannt und ihm einen zweiten Parameter gegeben. Das war doch privat, der Unterstrich sagt das. Dass drei Teams die Methode aufrufen, wussten wir nicht."

---

## Aufgabe

### Teil 1 · Lesen und einordnen

**1.** Legen Sie eine Tabelle an: Welche Namen aus Material B verwenden die Suite-Teams in Material C? Welche davon sind nach der Python-Konvention öffentlich, welche nicht? Was wollte jedes Team damit erreichen?

**2.** Welche Namen in Material B drücken eine Absicht aus, welche beschreiben nur eine Technik oder sind abgekürzt? Schlagen Sie für die unklaren Namen bessere vor.

**3.** Vergleichen Sie die drei Docstrings in Material B. Welcher beschreibt einen Vertrag, welche wiederholen nur den Methodennamen?

### Teil 2 · Die Schnittstelle entwerfen

**4.** Entwerfen Sie die öffentliche API des `ResultCollector` so, dass alle vier Teams ihr Ziel erreichen, ohne auf Namen mit Unterstrich zuzugreifen. Verwenden Sie Type Hints und Docstrings dort, wo sie einen Vertrag ausdrücken. Legen Sie fest, was das Modul über `__all__` als öffentlich erklärt.

**5.** Ein einzelnes Ergebnis ist heute ein Dictionary `{"status": ..., "duration": ..., "message": ...}`. Ersetzen Sie es durch einen geeigneten Datentyp. Was verhindert Ihr Entwurf bei Team UT? Ist der `ResultCollector` selbst ein Kandidat für `@dataclass`?

**6.** Schlagen Sie für Material A eine Modulstruktur vor, deren Namen die Verantwortung erkennen lassen. Ordnen Sie jeden genannten Inhalt einem Modul oder Package zu.

### Teil 3 · Regeln ableiten

**7.** Ordnen Sie die folgenden Regelkandidaten in **MUST**, **SHOULD**, **MAY** oder **DON'T** ein und geben Sie an, ob ein Werkzeug die Regel prüfen kann:

- Öffentliche Funktionen und Methoden des Frameworks sind typannotiert.
- Code wird mit einem automatischen Formatter formatiert.
- Module heißen `utils`, `helpers` oder `common`.
- Testcode der Suite-Teams greift auf Namen mit führendem Unterstrich aus dem Framework zu.
- Jede Methode hat einen Docstring.
- Reine Datenträger werden als `dataclass` geschrieben.
- Jedes Modul des Frameworks deklariert seine öffentlichen Namen in `__all__`.

**8.** Mehrere Teams lesen heute `collector.results` direkt. Das Plattformteam will verhindern, dass Ergebnisse von außen verändert werden. Wie erreichen Sie das, ohne die **lesenden** Aufrufstellen zu ändern?

**9.** Welche der zehn Review-Kommentare aus Material D könnte ein Werkzeug entscheiden, welche brauchen ein menschliches Designurteil?

---

## Hinweise zur Bearbeitung

- Der Code muss nicht ausgeführt werden. Er sollte aber so geschrieben sein, dass er lauffähig wäre.
- Die Aufrufstellen der Suite-Teams dürfen sich ändern. Ihr Ziel muss erreichbar bleiben.
- Wenn Sie unsicher sind, ob ein Name öffentlich sein sollte, fragen Sie: **Soll sich fremder Code darauf verlassen dürfen, auch nach der nächsten Version?**
- Für die Aufgaben 1 bis 3 und 9 genügen Stichpunkte oder eine Tabelle.
