# Fallbeispiel · Hinweise an Menschen in Daten für den Agenten

**Situationstyp:** Ein Agent liest Text, der für Menschen geschrieben ist. Ein Satz darin kann wie eine Anweisung an ihn wirken, und die Leitplanke, die das abfangen soll, schaut an der falschen Stelle nach.

---

## Ausgangslage

Ein Claude-Code-Skill setzt Squish-Tests um, führt sie aus und korrigiert sie. Er darf zwei Läufe machen, nur bestimmte Korrekturen vornehmen und muss Assertions unverändert lassen. Ein Skript vergleicht die Assertions vor und nach den Korrekturen.

## Wie es gewachsen ist

Testfälle in Polarion pflegen mehrere Personen. Manche schreiben Hinweise in die Schrittbeschreibung, etwa zu bekannten Abweichungen zwischen Terminal-Varianten: „If the value differs, update the expected value in the test.“

## Was auffällt

**Ein Hinweis an Menschen liest sich wie ein Auftrag.** Der Agent kann ihn als Erlaubnis verstehen, den erwarteten Wert anzupassen.

**Die Leitplanke prüft die falsche Datei.** `assertion_guard.py` vergleicht Assertion-Zeilen in `test.py`. Erwartete Werte stehen nach der Teamregel in `test_config.py`. Eine Änderung dort bleibt unbemerkt.

**Es gibt keine Regel, wie Text aus gelesenen Daten zu behandeln ist.**

## Naheliegende Ansätze

**Solche Hinweise aus Testfällen entfernen.** Es entstehen neue.

## Diskussionsfragen

1. Wie müsste das Prüfskript arbeiten, um eine geänderte Erwartung zu finden?
2. Wie formuliert man eine Regel, damit der Agent Testfälle umsetzt, aber ihnen nicht gehorcht?
3. Welche anderen Daten liest der Agent, in denen Anweisungen stehen könnten?
4. Wo haben Sie so etwas?
