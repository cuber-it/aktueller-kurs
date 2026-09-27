# Fallbeispiel · Regeln, die am Modell hängen

**Situationstyp:** Ein KI-Workflow ist sorgfältig dokumentiert, aber viele seiner Regeln hängen daran, dass das Modell sie befolgt.

---

## Ausgangslage

Ein Claude-Code-Skill setzt freigegebene Testfälle in Squish-Tests um: Testfall holen, `test.py` schreiben, statisch prüfen, auf einem Target ausführen, berichten.

## Wie es gewachsen ist

Der Skill entstand aus Review-Rückmeldungen. Was ein Mensch im Review fand, wurde eine Regel. Heute enthält er zahlreiche Regeln mit „never“, „always“ oder „ask first“. Einige wurden in Skripte übernommen: Ein Testfall mit falschem Status wird abgewiesen, erfundene Helper-Attribute meldet eine statische Prüfung.

## Was auffällt

**Die Rückfrage vor dem Lauf ist nicht durchgesetzt.** Sie steht im Kopf von `run_testcase.sh` und im Skill. Ist `Bash` für die Sitzung freigegeben, kann der Lauf auch ohne Rückfrage starten.

**Die Folgen sind ungleich verteilt.** Eine übersehene Formatierungsregel fällt im Review auf. Ein Lauf ohne Rückfrage auf einem geteilten Target ersetzt dessen Datensatz.

**Es gibt keine Übersicht, welche Regeln nur am Modell hängen.**

## Naheliegende Ansätze

**Die Regel deutlicher formulieren.** Sie hängt weiter am Modell.

**Eigene Targets für Agenten-Läufe.** Hilft, wo genug Terminals da sind.

## Diskussionsfragen

1. Welche Regel des Skills sollte technisch durchgesetzt sein?
2. Warum hilft eine fett geschriebene Regel wenig?
3. Welche weiteren Regeln haben Folgen außerhalb des Workflows?
4. Wo haben Sie so etwas?
