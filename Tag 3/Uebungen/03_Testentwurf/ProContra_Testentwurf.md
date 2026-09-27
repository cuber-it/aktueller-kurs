# Pro und Contra · Gherkin als Arbeitsschritt im testcase-writer

Bewertet wird der Vorschlag aus dem Lösungspapier: Der `testcase-writer` erzeugt zuerst Szenarien, ein Mensch prüft sie, dann entstehen die Polarion-Schritte.

---

## Pro

**Lücken werden vor dem Code sichtbar**
Ausgangszustand, Beobachtbarkeit, fehlende Varianten. Der vergebene Name „Tractor“ fällt vor der Umsetzung auf.

**Fragen an die Fachseite kommen früh**
Nicht erst, wenn ein Test unerwartet grün oder rot ist.

**Polarion bleibt führend**
Kein zweites System, keine doppelte Pflege.

**Szenarien lassen sich vergleichen**
Duplikate fallen leichter auf.

---

## Contra

**Ein Schritt mehr**
Jeder Testfall geht durch eine zusätzliche Prüfung.

**Übersetzung in Polarion-Schritte**
Aus einem Szenario mit Background werden Schritte mit Vorbedingung. Dabei kann wieder etwas verloren gehen.

**Das Review muss es können**
Szenarien prüfen verlangt die Frage nach Beobachtbarkeit, nicht nur nach Vollständigkeit.

---

## Bewertung

Der Vorschlag trägt, weil **die Lücke im Testfall liegt, nicht im Code**.

Gegenprobe – *nur eine Prüfliste für das Review, kein Gherkin, bleiben Nachteile?* Ja: Die Prüfliste wird abgehakt; das Szenario zwingt zu Given und Then.

**Die Grenzen:**

1. **Nur für neue Testfälle.** Bestehende werden bei Anlass überarbeitet.
2. **Given in Polarion abbilden.** Eine eigene Vorbedingungszeile je Testfall.
3. **Kein ausführbares BDD.** Die Szenarien steuern keine Tests (3-4).

---

## Diskussionsfragen

1. Wer prüft die Szenarien: Autor, Fachseite oder Automatisierung?
2. Wie bilden Sie `Given` in Polarion ab?
3. Welche bestehenden Testfälle würden Sie zuerst überarbeiten?
4. Soll der `testcase-writer` selbst Fragen an die Fachseite formulieren?
