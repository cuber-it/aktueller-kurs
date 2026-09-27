# KI-312 · Befunde aus der Architekturschulung in den Testfall-Skill übernehmen

**Typ:** Story
**Komponente:** Skill `testcase-implementer`, Referenzen
**Priorität:** Mittel

---

## Story

**Als** Entwickler, der den Testfall-Skill pflegt,
**möchte ich** die Befunde aus der Architekturschulung so in den Skill übernehmen, wie unsere Kontextregeln es verlangen,
**damit** der Skill neue Tests ohne diese Fehler erzeugt und nichts lehrt, was es nicht gibt.

---

## Description

In der Architekturschulung wurden Befunde zu Controls, Verifikation und Navigation erarbeitet. Einige betreffen Tests, die der Skill schreibt.

**Bestand:**

| Was | Anzahl |
|---|---|
| Referenzdokumente des Skills | 12 |
| davon immer geladen | 2 (Helper-Imports, Controls und Prüf-APIs) |
| Befunde aus der Schulung, die Tests betreffen | 5 |
| Prüfcodes in `check_references.py` | D1 bis D9 |

**Befund:** `check_references.py` prüft, ob die in den Referenzen genannten Namen existieren, nicht, ob die beschriebene Bedeutung stimmt. Beschreibt ein Absatz Parameter oder Standardwerte einer Methode, veraltet er unbemerkt, sobald sich der Wert im Code ändert.

**Befund zur Entstehung:** Der Absatz war ein Methodeninventar mit Semantik, genau das, was die eigenen Kontextregeln ausschließen.

**Nicht Gegenstand:** Die Behebung der Befunde im Framework.

## Randbedingungen

- Die Kontextregeln des Teams gelten (README des Skills).
- Nur existierende Methoden dürfen genannt werden.
- `check_references.py` muss sauber bleiben.

## Akzeptanzkriterien

- **AK1** – Jeder Befund ist eingeordnet: Gefahr, Routing, Konvention, nicht aufnehmen, oder Änderung am Framework.
- **AK2** – Aufgenommene Befunde stehen an genau einer Stelle.
- **AK3** – Kein Eintrag enthält Signaturen, Zeilennummern oder Methodeninventare.
- **AK4** – Kein Eintrag nennt eine Methode, die es noch nicht gibt.
- **AK5** – Für jeden Eintrag ist festgehalten, wann er entfällt.

## Hinweise

Die Befunde als Abschnitt „Lessons learned“ anzuhängen erfüllt AK2 nicht.

AK5 wird unbequem: Ein Eintrag, der nach einer Framework-Änderung stehen bleibt, lehrt ein Verhalten, das es nicht mehr gibt.

---

## Für den Kurs

Dieses Ticket nennt keine Lösung. Arbeiten Sie entlang der Frage:

**Kann das Modell das aus dem Quelltext selbst herausfinden?**

---
---

# Addendum · Kontextarten

| Art | beim Team | wann geladen |
|---|---|---|
| Skill-Datei | `SKILL.md` | immer |
| Referenz „always“ | Helper-Imports, Controls und Prüf-APIs | immer |
| Referenz „on demand“ | Code-Muster, Testaufbau, Testlauf, Spy, … | bei Bedarf |
| generierte Übersicht | UI-Übersicht aus `UI/*.py`, Anzeigetexte aus C++/QML | bei Bedarf, abschnittsweise |
| Aufgabe | Polarion-Testfall, Referenztest | je Aufruf |

Jede Zeile im Skill kostet bei jedem Aufruf Kontext und kann veralten. Ein Name wird geprüft, eine Beschreibung nicht.
