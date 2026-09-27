# Pro und Contra · Drei Tools mit Vertrag, Bash für den Rest

Bewertet wird der Vorschlag aus dem Lösungspapier: `run_testcase`, `get_run_result`, `spy_screen` als Tools mit Vertrag; `ask` für verändernde Tools, `deny` für die Skripte über Bash.

---

## Pro

**Der teuerste Fehler ist technisch ausgeschlossen**
Kein Lauf ohne Rückfrage, auch in langen Sitzungen.

**Laufgrenze ohne Modell**
Der Server zählt.

**Strukturierte Ergebnisse**
Der Agent entscheidet nach `status`, nicht nach Meldungstext.

**Sitzungen bleiben flüssig**
Lesende Werkzeuge und Bash für Suche bleiben frei.

---

## Contra

**Ein Server mehr**
Er muss gebaut, gepflegt und verteilt werden.

**Skript-Entwicklung wird umständlicher**
`deny` für die Skripte stört, wer sie ändert; eine lokale Einstellung (`.claude/settings.local.json`) hebt das nicht auf, weil `deny` Vorrang hat.

**Rückfrage bei jedem Lauf**
Bei vielen Testfällen in einer Sitzung viele Rückfragen.

---

## Bewertung

Der Vorschlag trägt, weil **eine pauschale Freigabe jede Regel zur Bitte macht** und ein Lauf ohne Rückfrage Schaden außerhalb des Workflows anrichtet.

Gegenprobe – *nur `ask` für `Bash(*run_testcase.sh*)`, kein Server, bleiben Nachteile?* Weniger: Die Rückfrage ist gesichert. Es fehlen Laufgrenze und strukturierte Rückgabe. Als erster Schritt tragfähig.

**Die Grenzen:**

1. **Erst Freigaben, dann Server.** Die `ask`-Regel wirkt sofort.
2. **Skript-Entwicklung außerhalb des Agenten-Repos** oder mit eigener Konfiguration.
3. **Rückfragen bündeln** ist eine offene Frage (Target je Sitzung freigeben).

---

## Diskussionsfragen

1. Reicht Ihnen der erste Schritt mit Freigaben?
2. Welche weiteren Skripte würden Tools?
3. Wie viele Rückfragen je Sitzung sind zumutbar?
4. Wie entwickeln Sie die Skripte weiter, wenn Bash dafür gesperrt ist?
