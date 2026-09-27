# Pro und Contra · Lokale Ergänzung statt Umstellung

Bewertet wird der Vorschlag aus dem Lösungspapier: keine Umstellung auf Screenplay, Tasks für neue Tests, Screenplay nur für Handlungen über mehrere Bedienwege.

---

## Pro

**Entscheidung an Änderungen belegt**
C4 unterscheidet die Varianten, die anderen nicht. Das ist eine Begründung, kein Geschmack.

**Bestand bleibt**
983 Tests laufen weiter.

**Kleine Schritte**
Tasks mit fachlichem Namen verbessern die Lesbarkeit sofort, ohne neue Begriffe.

**Screenplay bleibt möglich**
Wo es trägt, kann es ergänzt werden.

---

## Contra

**Zwei Stile, später drei**
Direkte Control-Zugriffe, Tasks und an einer Stelle Screenplay.

**Aus einer Umstellung wird eine Ergänzung**
Wer sich Screenplay für alle Tests wünscht, bekommt es an einer Stelle.

**C3 wird nicht gelöst**
Rollen über Parameter funktionieren, bleiben aber verstreut.

---

## Bewertung

Der Vorschlag trägt, weil **nur einer von vier Change Cases Screenplay verlangt** und dieser sechs Tests betrifft.

Gegenprobe – *alles auf Screenplay umstellen, bleiben Nachteile?* Ja: vier neue Begriffe für 983 Tests, während drei der vier Change Cases schon heute auf eine oder zwei Stellen beschränkt sind.

**Die Grenzen:**

1. **Schwelle festlegen.** Ab wie vielen Tests über mehrere Bedienwege wird Screenplay eingeführt?
2. **Stilregeln.** Wann direkt, wann Task, wann Screenplay muss aufgeschrieben werden.
3. **Prototyp mit Change Case.** Ein kleiner Prototyp zeigt Nutzen erst, wenn er an einer konkreten Änderung gemessen wird, nicht nur an Machbarkeit.

---

## Diskussionsfragen

1. Welche Schwelle würden Sie festlegen?
2. Wie würden Sie einen Prototyp anlegen, der Nutzen zeigt und nicht nur Machbarkeit?
3. Wo in Ihrem Framework gibt es Handlungen über mehrere Bedienwege?
4. Welche Regel schreiben Sie in den Standard?
