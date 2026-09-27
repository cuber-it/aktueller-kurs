# Pro und Contra · Regeln nach Prüfart einordnen, C004 mit Liste, API als Ziel

Bewertet wird der Vorschlag aus dem Lösungspapier.

---

## Pro

**Jede Regel greift**
Statt nur im Standard zu stehen, hat jede eine Prüfart.

**„never guess“ bleibt gewahrt**
Statische Prüfungen nur, wo eindeutig; KI-Review für Urteil.

**Die „wrong“-Variante wird gefunden**
C004 mit Liste erkennt `layout_manager_btn`.

**Ziel ist weniger Regelwerk**
Mit einer sicheren API entfallen Liste, Prüfung und Checklistenpunkt.

---

## Contra

**Liste muss gepflegt werden**
Ein neuer Umschalter ist ungeschützt, bis er eingetragen ist.

**Warnungen im Bestand**
13 Aufrufe folgen der „right“-Variante und würden gemeldet.

**KI-Review ist nicht reproduzierbar**
Zwei Läufe können Unterschiedliches finden.

---

## Bewertung

Der Vorschlag trägt, weil **er die bestehende Prüfphilosophie des Teams fortsetzt** und das dokumentierte Beispiel abdeckt.

Gegenprobe – *nur die Abschlussliste deutlicher formulieren, bleiben Nachteile?* Ja: Das Modell kann sie weiterhin übersehen.

**Die Grenzen:**

1. **Liste an einer Stelle**, von `check_references.py` gegen die Coding-Regeln geprüft.
2. **Warnung für die „right“-Variante** erst nach der Entscheidung über `click_and_wait`.
3. **KI-Review-Befunde** zählen; was wiederkehrt, wird statisch.

---

## Diskussionsfragen

1. Welche Regel würden Sie als erste statisch prüfen?
2. Soll die „right“-Variante gemeldet werden?
3. Wie testen Sie Ihre Prüfungen gegen die Beispiele der Coding-Regeln?
4. Wo sollen KI-Review-Ergebnisse stehen?
