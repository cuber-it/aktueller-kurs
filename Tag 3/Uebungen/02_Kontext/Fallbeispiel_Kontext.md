# Fallbeispiel · Beschreibungen, die still veralten

**Situationstyp:** Kontext beschreibt Code, statt auf ihn zu verweisen. Eine Namensprüfung findet Umbenennungen, eine geänderte Bedeutung bleibt stehen.

---

## Ausgangslage

Ein Claude-Code-Skill hat Referenzdokumente, die bei Bedarf geladen werden, und ein Prüfskript, das jeden dort genannten Import, jede Klasse und jede Methode gegen den Code abgleicht. Die Kontextregeln des Teams sind streng: keine Methodeninventare, keine Signaturen, keine Zeilennummern.

## Wie es gewachsen ist

Ältere Absätze in den Referenzen beschreiben Helper-Methoden mit Parametern und Standardwerten. Neue Befunde, etwa aus einer Schulung, warten auf Aufnahme.

## Was auffällt

**Die Prüfung prüft Namen, nicht Bedeutung.** Ändert sich der Standardwert einer Methode, bleibt ein Satz wie „Default timeout is 30 s“ unbemerkt falsch.

**Beschreibende Absätze widersprechen den eigenen Regeln.** Ein Methodeninventar mit Semantik ist genau das, was die Kontextregeln ausschließen.

**Neue Befunde brauchen einen Ort.** Ob Gefahr, Routing-Zeile, Framework-Änderung oder gar nichts, entscheidet, wie schnell der Eintrag veraltet.

## Naheliegende Ansätze

**Nach jedem Refactoring die Referenzen durchsehen.** Wird leicht vergessen, wenn das Prüfskript sauber ist.

**Befunde als Abschnitt „Lessons learned“ anhängen.** Sammelt Beschreibungen, die veralten.

## Diskussionsfragen

1. Wie muss ein Eintrag lauten, damit ein Refactoring ihn nicht falsch macht?
2. Welche Befunde gehören in den Skill, welche ins Framework?
3. Wann sollte ein Eintrag wieder verschwinden?
4. Wo haben Sie so etwas?
