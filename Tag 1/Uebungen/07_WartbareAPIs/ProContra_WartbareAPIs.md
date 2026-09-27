# Pro und Contra · Eine festgelegte öffentliche Schnittstelle für den ResultCollector

Bewertet wird der Vorschlag aus dem Lösungspapier: `record`, `results` als nur lesbare Sicht, `failed`, `export_json`, `export_html` und `format_duration` als öffentliche Schnittstelle, `TestResult` als eingefrorene Dataclass, `__all__` je Modul, Module nach Verantwortung, Formatierung und Lint-Regeln in der CI.

---

## Pro

**Die Schnittstelle steht im Code**
`__all__`, Namen ohne Unterstrich, Type Hints und Docstrings ändern sich mit dem Code. Die Frage „Was dürfen wir verwenden?" beantwortet das Modul selbst, nicht eine Wiki-Seite von 2022.

**Die Bedürfnisse der Teams haben einen offiziellen Weg**
Eigenes JSON-Ziel, formatierte Laufzeit, fehlgeschlagene Tests, Nachtragen eines instabilen Tests: Alle vier Teams erreichen ihr Ziel ohne `_`-Namen. Eine Umbenennung von `_write_json` trifft dann keine Methode, die jemand von außen aufruft.

**Erfasste Ergebnisse sind geschützt**
Die Sicht `results` und der unveränderliche `TestResult` verhindern, dass ein Team die Ergebnisse eines anderen verändert. Ersetzen geht nur über `record`, und das ist im Code sichtbar.

**Namen und Docstrings tragen Information**
`export_json(path)` und `record(result)` erklären sich. Docstrings stehen dort, wo sie etwas sagen, das nicht im Namen steht.

**Reviews werden frei für Designfragen**
Sechs von zehn Kommentaren aus Material D übernimmt ein Werkzeug. Im letzten Quartal betrafen 160 von 420 Kommentaren Formatierung, Importreihenfolge und Leerzeilen. Diese Fragen hätte ein Werkzeug entschieden.

**Die Umstellung kann schrittweise geschehen**
`get_results` bleibt mit einer `DeprecationWarning` erhalten. Die Teams stellen um, wenn sie die neue Version übernehmen.

---

## Contra

**Alle vier Teams müssen ihren Code anpassen**
`add` wird zu `record`, `result["status"]` zu `result.status`, `_write_json` zu `export_json`. Bei 87 Zugriffen in 41 Dateien ist das spürbarer Aufwand, der bei den Suite-Teams anfällt, nicht beim Plattformteam.

**Die öffentliche Schnittstelle wird größer**
`format_duration` und `failed` waren intern und sind jetzt Vertrag. Das Plattformteam kann sie nicht mehr ohne Ankündigung ändern.

**`record` mit Ersetzen ist eine Festlegung**
Ein zweites Ergebnis mit gleichem Namen ersetzt das erste. Wer versehentlich zwei Tests gleich benennt, verliert ein Ergebnis ohne Meldung.

**`__all__` schützt nicht**
Ein Team, das `from reporting import _something` schreibt, wird nicht gehindert. Die Wirkung hängt davon ab, dass der Linter-Check auf `_`-Zugriffe in allen Repositories aktiv ist.

**Die Modulstruktur ändert alle Importe**
`from testframework.common import ResultCollector` wird zu `from testframework.reporting import ResultCollector`. Ohne Übergangsmodul bricht jede bestehende Importzeile.

**Werkzeuge müssen erst eingeführt werden**
Formatter und Linter auf einen gewachsenen Bestand anzuwenden, erzeugt einmalig große Diffs. Laufende Branches bekommen Konflikte.

---

## Bewertung

Der Fall trägt die Festlegung, weil **die fehlende Schnittstelle bereits Schaden verursacht hat**: Zwei Tage Ausfall durch eine Umbenennung, 87 Zugriffe, von denen das Plattformteam nichts wusste, eine Wiki-Seite, die nicht mehr stimmt.

Gegenprobe – *nur die Konvention durchsetzen, also `_`-Zugriffe per Linter verbieten, ohne neue öffentliche Funktionen, bleiben Nachteile?* Ja: Die Teams verlieren ihre Wege, ohne Ersatz zu bekommen. Sie würden die Regel umgehen oder den Code kopieren.

**Die Grenzen:**

1. **Der Aufwand liegt bei den Suite-Teams.** Das Plattformteam sollte die Umstellung begleiten, etwa durch Übergangsmodule für die alten Importe und eine Liste der betroffenen Stellen.

2. **Nicht jedes Bedürfnis ist geprüft.** Der Vorschlag bedient die vier Fälle aus Material C. Die übrigen der 87 Zugriffe sind noch einzeln zu bewerten.

3. **Die Ersetzungsregel von `record` ist offen.** Ob ein doppelter Testname ersetzt, abgewiesen oder gewarnt werden soll, ist eine fachliche Frage an die Teams.

---

## Diskussionsfragen

1. Wer trägt den Aufwand einer API-Umstellung, und wer sollte ihn tragen?
2. Wie lange sollte eine veraltete Methode wie `get_results` erhalten bleiben?
3. Soll `record` einen doppelten Testnamen ersetzen, abweisen oder mit einer Warnung ersetzen?
4. Welche Regeln aus Aufgabe 7 würden Sie in Ihrem Team als MUST festlegen, und wer prüft sie?
5. Gibt es in Ihrem Code ein Modul, das `common` oder `utils` heißt? Welche Verantwortung hat es?
