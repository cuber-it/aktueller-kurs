# Übung · Welche Werkzeuge, mit welchen Grenzen?

Sie entwerfen die Werkzeugschnittstelle eines Test-Agenten auf Basis der Skripte, die Ihr Skill heute über Bash aufruft. Die Frage ist, welche Fähigkeiten der Agent braucht, welche Wirkung jede hat und welche Regeln technisch an der Schnittstelle durchgesetzt werden können.

---

## Material A · Die Skripte des Skills

| Skript | Aufgabe | Ausgabe | Wirkung |
|---|---|---|---|
| `fetch_testcase.py <ID>` | Testfall aus Polarion holen | JSON mit Schritten und `gate` | liest |
| `run_testcase.sh <target-ip> <suite> <tst_dir>` | Test auf einem Target ausführen | Protokoll `<suite>__<tst>__<stempel>.log`, Verweis `…__latest.log` | exklusives Target, Lizenzplatz, Datensatz ersetzt |
| `parse_run.py <log>` | Protokoll verdichten | `verdict : PASS`/`FAIL`/`INCOMPLETE …`, Assertions, erster Fehler; Exit 0/1/2 | liest |
| `spy_dump.sh`, `find_object.py` | Objektbaum der laufenden AUT erfassen und abfragen | Dump-Datei, Abfrageergebnis | exklusives Target und Lizenzplatz, nur nach Rückfrage |
| `assertion_guard.py snapshot/check/show <test.py>` | Assertions vor und nach Korrekturen vergleichen | Exit 1 bei Änderung | liest, schreibt Snapshot |
| `check_test.py <tst_dir>` | statische Prüfung | Befunde mit Codes, Exit 1 bei Fehler | liest |

---

## Material B · Regeln für Läufe (SKILL.md, Schritt 7b, sinngemäß)

- Vorher fragen und die Kosten nennen: exklusives Target, Lizenzplatz, Datensatz wird ersetzt.
- Nicht ausführen: Tests mit physischen Schritten, Updater-Tests, Tests mit fehlender Simulation.
- Höchstens 2 Läufe, dann an den Menschen.
- Nur erlaubte Korrekturen; nie Assertion abschwächen, Timeout erhöhen, Erwartung an das Gerät anpassen.
- Selector nicht ändern, ohne ihn im Spy-Dump gesehen zu haben.

---

## Material C · Freigaben in Claude Code

In `.claude/settings.json`: `permissions` mit den Listen `allow`, `ask`, `deny`. Regeln haben die Form `Werkzeug` oder `Werkzeug(Muster)`, MCP-Tools heißen `mcp__<server>__<tool>`. `deny` hat Vorrang, `ask` erzwingt eine Rückfrage.

---

## Aufgabe

### Teil 1 · Werkzeuge

**1.** Welche Skripte aus Material A werden Tools eines Test-Agenten? Welche bleiben Bash, welche braucht der Agent gar nicht?

**2.** Ordnen Sie jedes Tool ein: nur lesend, verändernd, zerstörend.

### Teil 2 · Verträge

**3.** Entwerfen Sie den Vertrag für `run_testcase`: Parameter mit Typ und Einschränkung, Rückgabe, unterscheidbare Fehler.

**4.** Welche Regeln aus Material B können im Tool durchgesetzt werden, welche bleiben beim Modell?

**5.** Entwerfen Sie den Vertrag für einen Spy-Dump. Was gibt das Tool zurück, damit der Agent den Dump nie selbst lesen muss?

### Teil 3 · Freigaben

**6.** Schreiben Sie die `permissions` für `.claude/settings.json`: Was ist frei, was fragt nach, was ist gesperrt?

**7.** Warum ist eine `deny`-Regel für den direkten Bash-Aufruf von `run_testcase.sh` nötig, wenn es ein Tool gibt?

---

## Hinweise zur Bearbeitung

- Weniger Tools sind besser, solange der Workflow sie nicht braucht.
- Rückgaben kompakt und strukturiert, keine ungefilterten Protokolle.
- Wenn Sie unsicher sind, fragen Sie: **Was darf der Agent ohne Rückfrage, und was passiert, wenn er es falsch macht?**
