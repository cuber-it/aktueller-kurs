# KI-345 · Regeln aus der Architekturschulung in Prüfungen überführen

**Typ:** Story
**Komponente:** `check_test.py`, KI-Review
**Priorität:** Mittel

---

## Story

**Als** Verantwortliche für die Qualität generierter Tests
**möchte ich** für jede neue Teamregel wissen, wie sie geprüft wird,
**damit** Regeln nicht nur im Standard stehen, sondern bei jedem Test greifen.

---

## Description

Aus der Architekturschulung stammen neue Regeln für Tests. Das Prüfskript `check_test.py` deckt einen Teil ab, andere verlangen Urteil.

**Bestand:**

| Was | Anzahl |
|---|---|
| Prüfcodes in `check_test.py` | 23 (Gruppen A bis G) |
| davon Warnungen zu Synchronisation (C003, C004) | 2 |
| Regelkandidaten aus der Schulung | 7 |
| `click_and_wait` auf `layout_manager_btn` im aktiven Bestand | 13 |

**Befund:** Ein Test, der nach `layout_manager_btn.click_and_wait(...)` auf einen Eintrag im Panel wartet, entspricht der „wrong“-Variante der Coding-Regeln. `check_test.py` meldet ihn nicht, weil C004 nur Namen mit `_toggle` oder `_switch` prüft.

**Befund zur Entstehung:** Die Regel stand in der Dokumentation und in der Abschlussliste, die Prüfung erkannte das dokumentierte Beispiel nicht.

**Nicht Gegenstand:** Die Änderung von `click_and_wait` selbst (Tag 2).

## Randbedingungen

- „never guess“ gilt für jede neue Prüfung.
- KI-Reviews ergänzen, sie ersetzen keine deterministische Prüfung.

## Akzeptanzkriterien

- **AK1** – Jede Regel ist einer Prüfart zugeordnet, mit Begründung.
- **AK2** – C004 erkennt den dokumentierten Fall.
- **AK3** – Für regelbasierte KI-Reviews gibt es einen Prüfauftrag mit dem Teamstandard als Maßstab.
- **AK4** – Es ist festgelegt, wohin KI-Review-Ergebnisse gehen.

## Hinweise

Alle sieben Regeln als KI-Review zu behandeln erfüllt AK1 nicht. Was eine Maschine sicher prüfen kann, prüft sie.

AK2 wird unbequem: Die „right“-Variante der Coding-Regeln ist zeitabhängig. Soll C004 sie melden?

---

## Für den Kurs

Dieses Ticket nennt keine Lösung. Arbeiten Sie entlang der Frage:

**Kann eine Maschine das sicher entscheiden, oder braucht es Urteil?**

---
---

# Addendum · Prüfarten

| Prüfart | Stärke | Schwäche |
|---|---|---|
| statisch (AST, Suche) | schnell, reproduzierbar, CI-tauglich | nur Form, keine Absicht |
| Laufzeit (Testlauf) | echtes Verhalten | Target, Zeit, Lizenz |
| KI-Review gegen Standard | Absicht, Zusammenhänge | nicht reproduzierbar, kann irren |
| API-Änderung | Fehler unmöglich | Aufwand, betrifft Bestand |
