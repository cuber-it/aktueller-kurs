# 3-6 · vorher · Werkzeug als Skript, Regeln als Kommentar und Skill-Text

Ausschnitte aus dem Skill des Teams, gekürzt und anonymisiert.

## Kopf von `scripts/run_testcase.sh`

```bash
#!/bin/bash
# Runs one test case against a target with squishrunner - the verification step that used to be
# done by hand in the Squish IDE.
#
# Never run this without asking the engineer first: it takes an exclusive target and a Squish
# license seat, and most tests call replace_data_set(), which wipes the target's settings and
# data directories before the test starts. See references/test_run.md.
#
# Usage:
#   run_testcase.sh <target-ip> <suite-name> <testcase-dir-name>
#
# Environment:
#   RUN_CACHE    where run logs are written (outside the repo on purpose)
#
# Example:
#   run_testcase.sh 198.51.100.17 suite_Settings tst_1_6_TC_1011_Settings_Language_list_completeness
```

## Die zugehörigen Regeln in `SKILL.md`, Schritt 7b (sinngemäß)

- **Vorher fragen** und die Kosten nennen: exklusives Target, Lizenzplatz, Datensatz wird ersetzt. „Überspringen“ ist eine gültige Antwort, der Test gilt dann als nicht verifiziert.
- **Nie ausführen:** Tests mit physischen Schritten, Updater-Tests, Tests mit fehlender Simulation.
- **Höchstens 2 Läufe**, dann an den Menschen zurück.
- **Nur erlaubte Korrekturen:** falsches Attribut, falscher Selector, fehlendes Warten. Nie eine Assertion abschwächen, einen Timeout erhöhen oder eine Erwartung an das Gerät anpassen.

## Was davon technisch durchgesetzt ist

| Regel | durchgesetzt durch |
|---|---|
| Parameter und Reihenfolge | Positionsargumente, Prüfung im Skript |
| Rückfrage vor dem Lauf | Modell befolgt Regel |
| keine physischen oder Updater-Tests | Modell befolgt Regel |
| höchstens 2 Läufe | Modell befolgt Regel |
| Ergebnis | Text auf stdout, Protokoll in `RUN_CACHE` |
| Fehlerarten | Text der Meldung („does not answer a ping“, „No Squish license“) |

In Claude Code läuft das Skript über das Werkzeug `Bash`. Ist `Bash` freigegeben, sind auch andere Aufrufe möglich.
