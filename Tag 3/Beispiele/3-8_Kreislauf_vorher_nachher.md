# 3-8 · Der geschlossene Kreislauf: heute und mit MCP-Werkzeugen

Grundlage ist Schritt 7b des Skills des Teams. Links der heutige Stand, rechts derselbe Kreislauf mit dem Server aus 3-7 und den Freigaben aus 3-6.

## Ablauf

```text
                heute                                         mit MCP
test.py fertig, check_test.py sauber              test.py fertig, check_test.py sauber
        ↓                                                  ↓
assertion_guard.py snapshot                        assertion_guard.py snapshot
        ↓                                                  ↓
Modell fragt nach (Regel)            ◆             run_testcase  →  Claude Code fragt (ask)   ◆
        ↓                                                  ↓
Bash: run_testcase.sh                              Server: Laufgrenze, Namensprüfung
        ↓                                                  ↓
Bash: parse_run.py → Text                          RunResult { status, summary, runs_used }
        ↓                                                  ↓
Modell liest Text, begründet                       Modell liest status, begründet
Test- oder AUT-Fehler (Regel)                      Test- oder AUT-Fehler (Regel)
        ↓                                                  ↓
Korrektur (erlaubte Arten: Regel)                  Korrektur (erlaubte Arten: Regel)
        ↓                                                  ↓
2. Lauf? Modell zählt (Regel)                      2. Lauf? Server zählt, 3. wird verweigert
        ↓                                                  ↓
assertion_guard.py check                           assertion_guard.py check
        ↓                                                  ↓
Bericht                              ◆             Bericht                                    ◆
```

◆ = menschlicher Kontrollpunkt

## Was sich ändert und was nicht

| Teil des Kreislaufs | heute | mit MCP |
|---|---|---|
| Rückfrage vor dem Lauf | Regel | technisch (`ask`) |
| Laufgrenze | Regel | technisch (Server) |
| Ergebnis lesen | Text über Bash | strukturierte Rückgabe |
| „Lauf hat nicht begonnen“ erkennen | Text lesen | `not_started` |
| Test- oder AUT-Fehler begründen | Regel | Regel |
| erlaubte Korrekturen | Regel | Regel |
| Assertion nicht abschwächen | `assertion_guard.py`, prüft nur `test.py`; erwartete Werte in `test_config.py` bleiben ungeprüft | unverändert, Erweiterung um `test_config.py` nötig |
| Selector nicht ohne Spy ändern | Regel | Regel; mit einem Tool `spy_dump` prüfbar, ob vor einer Selector-Änderung gespäht wurde |

## Fragen für die Standards Session

1. Welche Regeln sollen technisch durchgesetzt werden, welche bleiben Regeln für das Modell?
2. Reicht die Kombination aus Claude-Code-Freigaben und Bash-Skripten, oder lohnt ein eigener Server?
3. Squish MCP der Qt Company oder eigener Server: Welche Leitplanken des Teams müssten beim fremden Server nachgebaut werden?
