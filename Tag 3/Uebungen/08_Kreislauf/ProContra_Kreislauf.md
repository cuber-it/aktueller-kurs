# Pro und Contra · Autonomie nach „wird ein Fehler bemerkt?“

Bewertet wird der Vorschlag aus dem Lösungspapier: fünf Regeln mit Durchsetzung, Stopp bei allem, was ändert, was geprüft wird.

---

## Pro

**Klare Grenze**
Der Agent korrigiert Technisches, meldet Fachliches.

**Die Lücke in der stärksten Leitplanke wird geschlossen**
`assertion_guard.py` vergleicht künftig auch `test_config.py`; eine geänderte Erwartung wird gemeldet.

**Prompt Injection hat eine Regel**
Und die häufigste Folge ist nach der Erweiterung technisch abgesichert.

**Anschluss an Tag 1 und 2**
Die Regeln haben dieselbe Form (MUST, SHOULD, DON'T) wie die Standards der Vortage.

---

## Contra

**Mehr Berichte, weniger grüne Tests**
Wert weicht ab → Meldung, auch wenn der Test falsch ist.

**Einordnung bleibt Urteil**
Test- oder AUT-Fehler entscheidet das Modell; der Mensch muss es lesen.

**DON'T-Regel ist Anweisung**
Gegen geschickt formulierten Text hilft sie nur teilweise.

---

## Bewertung

Der Vorschlag trägt, weil **Fehler an den Stellen aufgehalten werden, an denen sie sonst unbemerkt blieben**.

Gegenprobe – *dem Agenten auch Wertanpassungen erlauben, wenn der Testfall es sagt, bleiben Nachteile?* Ja: Ein Hinweis an Menschen im Testfall würde zur Anweisung. Der Testfall ist kein Auftraggeber des Agenten.

**Die Grenzen:**

1. **Berichte lesen.** Mehr Meldungen brauchen eine feste Stelle im Ablauf.
2. **Regeln als Kontext.** Nach den Kontextregeln des Teams in den Skill.
3. **Jährlich prüfen.** Welche Anweisung ist inzwischen technisch?

---

## Diskussionsfragen

1. Welche Regel fehlt?
2. Wer liest die Berichte?
3. Wie viel Autonomie in einem Jahr?
4. Wie verbinden Sie diese Regeln mit den Standards aus Tag 1 und 2?
