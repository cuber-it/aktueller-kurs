# Übung · Wer setzt welche Regel durch?

Sie zerlegen den KI-gestützten Workflow, mit dem Ihr Team freigegebene Testfälle in Squish-Tests umsetzt. Der Workflow funktioniert. Die Frage ist, an welcher Stelle der Agent entscheidet, wo ein Mensch, und wodurch jede Regel tatsächlich durchgesetzt wird.

---

## Material A · Die Schritte des Skills

Aus `SKILL.md` des Skills `testcase-implementer` (gekürzt):

| Schritt | Inhalt | Werkzeug |
|---|---|---|
| 1 | Testfall aus Polarion holen, Freigabestatus prüfen (`gate`: refuse, warn, ok) | `fetch_testcase.py` |
| 2 | Anwendungsbereich bestimmen, ähnlichsten freigegebenen Referenztest suchen | `find`, `grep` |
| 3 | Helper-Attribute nachschlagen; wenn nicht auffindbar: Spy-Dump nach Rückfrage | generierte UI-Übersicht, `spy_dump.sh`, `find_object.py` |
| 4 | Schritte auf Aufrufe abbilden (Routing-Tabellen) | Referenzen |
| 4b | Platz neuer Helper festlegen, im Zweifel fragen | Platzierungstabelle |
| 5 | `test.py` zusammenbauen | |
| 6 | Suite beim Menschen erfragen, vor jedem Schreiben | `AskUserQuestion` |
| 7 | vier Dinge schreiben, statisch prüfen, Fehler beheben | `check_test.py` |
| 7b | nach Rückfrage auf dem Target ausführen, höchstens 2 Läufe | `run_testcase.sh`, `parse_run.py`, `assertion_guard.py` |
| 8 | Bericht nach festem Format | `report_format.md` |

---

## Material B · Regeln aus dem Skill

| Nr. | Regel |
|---|---|
| R1 | Nur Testfälle mit Status „Active“ umsetzen; bei „Draft“ nachfragen. |
| R2 | Kein Helper-Attribut erfinden, das in den Quellen nicht steht. |
| R3 | Keine Parallel-Helper; erst nach der Absicht suchen, dann schreiben. |
| R4 | Vor jedem Lauf fragen und die Kosten nennen: exklusives Target, Lizenzplatz, Datensatz wird ersetzt. |
| R5 | Höchstens 2 Läufe, dann an den Menschen zurück. |
| R6 | Einen Selector nicht ändern, ohne ihn im Spy-Dump gesehen zu haben. |
| R7 | Eine Assertion nie abschwächen, keinen Timeout erhöhen, keine Erwartung an das Gerät anpassen. |
| R8 | Genau vier Dinge schreiben: `test.py`, `test_config.py`, `config.xml`, eine Zeile in `suite.conf`. |
| R9 | Bei jedem Fehlschlag begründen: Test- oder AUT-Fehler? |

---

## Aufgabe

### Teil 1 · Landkarte

**1.** Zeichnen Sie den Ablauf von der Anforderung bis zum Merge Request. Markieren Sie jeden Punkt, an dem ein Mensch entscheidet.

**2.** Wo gibt es heute Medienbrüche oder manuelle Rückkopplungen?

### Teil 2 · Durchsetzung

**3.** Ordnen Sie jeder Regel aus Material B zu, wodurch sie heute durchgesetzt wird: technisch (Skript, Prüfung), durch das Modell (Regel im Skill) oder durch einen Menschen.

**4.** Welche Regel verursacht den größten Schaden, wenn das Modell sie einmal nicht befolgt?

**5.** Die Folie zur Einheit sagt: „Kein Zugriff auf die laufende Anwendung.“ Stimmt das für Ihren Agenten? Was sieht und was verändert er heute?

### Teil 3 · Kandidaten

**6.** Wählen Sie drei Regeln, die Sie lieber technisch durchsetzen würden. Wie könnte das jeweils aussehen?

**7.** Welche Regel sollte bewusst beim Modell oder beim Menschen bleiben? Begründen Sie.

---

## Hinweise zur Bearbeitung

- Beschreiben Sie den Ist-Stand, nicht das Ziel.
- „Technisch“ heißt: Der Verstoß ist ohne Mitwirkung des Modells unmöglich oder wird automatisch gemeldet.
- Wenn Sie unsicher sind, fragen Sie: **Was passiert, wenn das Modell diese Regel einmal nicht befolgt?**
