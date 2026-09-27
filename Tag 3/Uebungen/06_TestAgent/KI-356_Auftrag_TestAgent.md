# KI-356 · Testläufe des Agenten technisch absichern

**Typ:** Story
**Komponente:** KI-Workflow Testumsetzung, Werkzeuge
**Priorität:** Hoch
**Verweist auf:** KI-301 (Einordnung der Regeln)

---

## Story

**Als** Teamleitung Testautomatisierung
**möchte ich**, dass ein Agent Tests nur über eine Schnittstelle mit festen Grenzen ausführen kann,
**damit** Rückfrage und Laufbegrenzung nicht davon abhängen, ob das Modell sie befolgt.

---

## Description

Der Skill ruft seine Skripte über das Werkzeug `Bash` auf. KI-301 hat ergeben, dass die teuersten Regeln nur vom Modell abhängen.

**Bestand:**

| Was | Stand |
|---|---|
| Skripte des Skills | 8 |
| davon verändern ein Target | 2 (`run_testcase.sh`, `spy_dump.sh`) |
| Regeln für Läufe in Schritt 7b | 5 |
| davon technisch durchgesetzt | 1 (`assertion_guard.py` meldet) |
| Freigabe von `Bash` in typischen Sitzungen | pauschal |

**Befund:** siehe KI-301. Die Rückfrage vor dem Lauf hängt am Modell, solange `Bash` pauschal freigegeben ist.

**Befund zur Entstehung:** Pauschale Bash-Freigaben machen jede Regel im Skill zu einer Bitte.

**Nicht Gegenstand:** Die Wahl zwischen eigenem Server und Squish MCP der Qt Company (KI-367).

## Randbedingungen

- Die Skripte bleiben; die Schnittstelle kapselt sie.
- Rückgaben sind strukturiert und kompakt.
- Freigaben liegen im Repository (`.claude/settings.json`), damit sie für alle gelten.

## Akzeptanzkriterien

- **AK1** – Jedes Tool ist als lesend, verändernd oder zerstörend eingeordnet.
- **AK2** – Ein Lauf ist ohne Rückfrage nicht möglich.
- **AK3** – Der dritte Lauf desselben Testfalls wird verweigert.
- **AK4** – Die Rückgabe unterscheidet bestanden, fehlgeschlagen, unvollständig, nicht gestartet, verweigert, Zeitüberschreitung.
- **AK5** – Der direkte Aufruf der Skripte über Bash ist gesperrt.

## Hinweise

Nur `ask` für `Bash` insgesamt erfüllt AK2 formal, erzeugt aber eine Rückfrage für jedes `grep`.

AK5 wird unbequem: Beim Entwickeln der Skripte selbst braucht man sie direkt.

---

## Für den Kurs

Dieses Ticket nennt keine Lösung. Arbeiten Sie entlang der Frage:

**Was darf der Agent ohne Rückfrage, und was passiert, wenn er es falsch macht?**

---
---

# Addendum · Tool-Vertrag

| Teil | Inhalt |
|---|---|
| Name | eindeutig, Verb + Gegenstand |
| Beschreibung | Zweck und Wirkung, auch was es nicht tut |
| Annotationen (MCP) | `read_only_hint`, `destructive_hint`, `idempotent_hint` |
| Parameter | klein, typisiert, eingeschränkt |
| Rückgabe | Struktur mit festem Status |
| Fehler | unterscheidbar, mit Ursache |
