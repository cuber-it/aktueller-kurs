# Lösungsvorschlag · Wer setzt welche Regel durch?

**Vorbemerkung:** Ein Vorschlag, keine Musterlösung. Bewertet wird, ob **jede Regel einer Durchsetzung zugeordnet** ist und ob die **Folgen eines Verstoßes** die Kandidaten bestimmen.

---

## 1 · Landkarte

```text
Anforderung → Test Story → (testcase-writer) → Test Case → Freigabe in Polarion ◆
   → testcase-implementer: holen, gate → Referenz → Helper (Spy nach Rückfrage ◆)
   → Abbilden, Platzierung (im Zweifel fragen ◆) → Suite erfragen ◆
   → schreiben, check_test.py → Lauf nach Rückfrage ◆ (höchstens 2)
   → Bericht → Merge Request, Review ◆
```

---

## 2 · Medienbrüche

- Test Story und Test Case in Polarion, Code im Repository: Rückfluss von Befunden (etwa „Expected nicht prüfbar“) nach Polarion ist manuell.
- Laufergebnisse liegen im Cache außerhalb des Repositories; im Merge Request steht nur der Bericht.

---

## 3 · Durchsetzung

| Regel | heute | Folge eines Verstoßes |
|---|---|---|
| R1 Status | technisch (`gate`) | — |
| R2 keine erfundenen Attribute | technisch meldend (`check_test.py` A001) | Laufzeitfehler, im Lauf sichtbar |
| R3 keine Parallel-Helper | Modell, Review | Duplikat im Framework |
| R4 vor Lauf fragen | Modell | Datensatz fremder Arbeit gelöscht |
| R5 höchstens 2 Läufe | Modell | Target lange belegt, Raten statt Diagnose |
| R6 Selector nur nach Spy | Modell | geratener Selector, falsche Diagnose |
| R7 Assertion nie abschwächen | technisch meldend für `test.py` (`assertion_guard.py`); erwartete Werte in `test_config.py` ungeprüft (Übung 08) | grüner Test, der nichts prüft |
| R8 vier Dinge schreiben | teils technisch (`check_test.py` F003 im Testordner) | Änderungen am Framework ohne Review |
| R9 Test- oder AUT-Fehler begründen | Modell | falsche Zuordnung, Aufwand im Review |

---

## 4 · Größter Schaden

R4. Der Schaden trifft Menschen außerhalb des Workflows und ist nicht rückgängig zu machen.

---

## 5 · Zugriff auf die laufende Anwendung

Der Agent führt Tests aus (`run_testcase.sh`), liest Ergebnisse (`parse_run.py`) und den Objektbaum (`spy_dump.sh`). Er verändert das Target (Datensatz). Die Folie beschreibt einen Agenten ohne Werkzeuge.

---

## 6 · Kandidaten

| Regel | Vorschlag |
|---|---|
| R4 | `Bash(*run_testcase.sh*)` in `ask` statt pauschaler Bash-Freigabe; besser ein MCP-Tool mit `ask` (Übung 06, 07) |
| R5 | Zähler im Ausführungsskript oder im MCP-Server |
| R8 | Prüfung im Commit-Hook: geänderte Dateien außerhalb des Testordners melden |

---

## 7 · Bewusst beim Modell oder Menschen

R9 bleibt beim Modell, mit Pflicht zur Begründung im Bericht; das Urteil prüft der Mensch im Review. R3 bleibt im Review: Ob ein Helper ein Duplikat ist, verlangt Kenntnis der Absicht.

---

## Diskussionsanschluss

Welche Regel würden Sie morgen technisch absichern, mit welchem Aufwand?
