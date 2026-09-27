# Pro und Contra · Regeln nach Durchsetzung einordnen und die teuren technisch absichern

Bewertet wird der Vorschlag aus dem Lösungspapier: Liste aller Regeln mit Durchsetzung und Folge; R4, R5, R8 technisch absichern.

---

## Pro

**Das Risiko wird sichtbar**
Welche Regeln nur vom Modell abhängen, steht jetzt an einer Stelle.

**Schaden außerhalb des Workflows wird verhindert**
R4 als `ask`-Freigabe verhindert einen Lauf ohne Rückfrage, unabhängig davon, wie lang die Sitzung ist.

**Wenig Aufwand für den Anfang**
Eine Freigaberegel in `.claude/settings.json` ist eine Zeile.

**Der Skill bleibt, wie er ist**
Die Regeln bleiben als Erklärung für das Modell stehen.

---

## Contra

**Mehr Rückfragen**
Jeder Lauf fragt nach. In Sitzungen mit vielen Testfällen stört das.

**Doppelte Pflege**
Regeln stehen im Skill und in Freigaben oder Skripten.

**Nicht jede Regel ist fassbar**
R3 und R9 bleiben beim Modell und im Review.

---

## Bewertung

Der Vorschlag trägt, weil **der teuerste Verstoß mit einer Zeile Konfiguration verhindert werden kann**.

Gegenprobe – *nur die Regel im Skill deutlicher formulieren, bleiben Nachteile?* Ja: Sie hängt weiterhin am Modell, und lange Sitzungen bleiben das Risiko.

**Die Grenzen:**

1. **Rückfragen bündeln.** Eine Sitzung könnte ein Target einmal freigeben, nicht jeden Lauf.
2. **Pflege.** Jede neue Regel im Skill bekommt eine Zeile in der Liste.
3. **Eigene Targets für Agenten** bleiben sinnvoll, wo möglich.

---

## Diskussionsfragen

1. Welche Regel sichern Sie zuerst ab?
2. Wie viele Rückfragen je Sitzung sind zumutbar?
3. Wer pflegt die Liste?
4. Welche Regel soll ausdrücklich beim Modell bleiben?
