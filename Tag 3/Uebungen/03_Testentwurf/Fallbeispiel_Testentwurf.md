# Fallbeispiel · Ein Testfall, der den Ausgangszustand prüft

**Situationstyp:** Ein Testfall beschreibt Bedienweg und sichtbare Folge, aber nicht den Ausgangszustand. Die Erwartung kann schon vor der Aktion erfüllt sein.

---

## Ausgangslage

Testfälle für die Maschineneinstellungen entstehen aus Test Stories, werden in Polarion geprüft und von einem Claude-Code-Skill in Squish-Tests umgesetzt.

## Wie es gewachsen ist

Die Testfälle schreiben Personen, die das Terminal genau kennen. Dass jedes Terminal mit einem Standardtraktor ausgeliefert wird, ist für sie selbstverständlich und steht deshalb nicht im Testfall.

## Was auffällt

**Die Erwartung ist ohne Aktion erfüllbar.** „Neuer Traktor ‚Tractor‘ angelegt und ausgewählt“: Der Standardtraktor heißt bereits „Tractor“ und ist nach dem Zurücksetzen ausgewählt.

**Der Testfall steht zweimal in der Spezifikation.** Mit identischen Schritten unter zwei Kennungen.

**Ein Skill setzt um, was dasteht.** Er übernimmt die Lücke des Testfalls in den Test.

## Naheliegende Ansätze

**Namen mit Zeitstempel.** Der Test wird aussagekräftig, der Fall „Name existiert schon“ bleibt ungeprüft.

## Diskussionsfragen

1. An welcher Stelle sollte eine solche Lücke auffallen?
2. Was macht ein `Given` sichtbar?
3. Kann ein Skill, der Testfälle schreibt, solche Lücken finden?
4. Wo haben Sie so etwas?
