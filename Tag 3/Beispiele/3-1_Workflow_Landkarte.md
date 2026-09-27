# 3-1 · Landkarte: der KI-gestützte Testworkflow des Teams

Grundlage ist der Claude-Code-Skill des Teams zur Umsetzung freigegebener Testfälle (hier `testcase-implementer`). Die Landkarte zeigt, welche Schritte der Agent ausführt, welche Werkzeuge er dabei nutzt und wodurch jede Regel heute durchgesetzt wird.

## Ablauf

```text
Anforderung
   ↓
Test Story ──(Skill testcase-writer)──→ Test Case in Polarion
   ↓                                          │ Mensch prüft und gibt frei      ◆
   ↓                                          ▼
testcase-implementer
   1  Testfall holen                 fetch_testcase.py → JSON mit Schritten und gate
      gate = refuse → Stopp, warn → Rückfrage                                     ◆
   2  Referenztest suchen            freigegebene Liste, schwarze Liste
   3  Helper nachschlagen            generierte UI-Übersicht → Quelltext → Spy-Dump   ◆ vor Spy
   4  Schritte abbilden              Routing-Tabellen „Absicht → Aufruf“
   4b neue Helper platzieren         Tabelle nach Art der Fähigkeit, im Zweifel fragen ◆
   5  test.py zusammenbauen
   6  Suite erfragen                                                                ◆
   7  vier Dinge schreiben, check_test.py ausführen, Fehler beheben
   7b Lauf auf dem Target            run_testcase.sh, parse_run.py, höchstens 2 Läufe  ◆ vor Lauf
      assertion_guard.py snapshot / check
   8  Bericht nach festem Format
   ↓
Merge Request, Review                                                               ◆
```

◆ = menschlicher Kontrollpunkt

## Wodurch jede Regel heute durchgesetzt wird

| Regel | technisch erzwungen | Regel im Skill | Mensch |
|---|:-:|:-:|:-:|
| nur freigegebene Testfälle | `gate` im Skript | ✓ | Freigabe in Polarion |
| keine erfundenen Helper-Attribute | `check_test.py` A001 | ✓ | |
| keine Parallel-Helper | | ✓ | Review |
| vor dem Lauf fragen | | ✓ (Kommentar im Skript) | bestätigt |
| höchstens 2 Läufe | | ✓ | |
| Selector nicht ohne Spy ändern | | ✓ | |
| Assertion nie abschwächen | `assertion_guard.py` meldet Änderungen in `test.py`, nicht in `test_config.py` | ✓ | entscheidet |
| nur vier Dinge schreiben | `check_test.py` F003 für den Testordner | ✓ | Review |
| Test- oder AUT-Fehler begründen | | ✓ | liest Bericht |

## Fragen für die Bestandsaufnahme

1. Welche Zeilen der Tabelle würden Sie lieber technisch erzwingen?
2. Welcher Kontrollpunkt kostet im Alltag am meisten Zeit, welcher hat schon einmal einen Fehler verhindert?
3. Was passiert zwischen Schritt 8 und dem Merge Request?
