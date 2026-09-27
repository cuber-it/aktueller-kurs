# KI-301 · Regeln des Testfall-Skills nach Durchsetzung einordnen

**Typ:** Task
**Komponente:** KI-Workflow Testumsetzung
**Priorität:** Hoch

---

## Story

**Als** Teamleitung Testautomatisierung
**möchte ich** für jede Regel des Testfall-Skills wissen, wodurch sie durchgesetzt wird,
**damit** wir entscheiden können, welche Regeln technisch abgesichert werden müssen.

---

## Description

Der Skill `testcase-implementer` setzt freigegebene Testfälle in Squish-Tests um und führt sie auf einem Target aus. Seine Regeln stehen in `SKILL.md` und zwölf Referenzdokumenten.

**Bestand:**

| Was | Anzahl |
|---|---|
| Regeln mit „never“, „always“ oder „ask first“ in `SKILL.md` | über 20 |
| davon technisch geprüft (`gate`, `check_test.py`, `assertion_guard.py`) | eine Minderheit |
| Skripte | 8 |
| Kontrollpunkte mit Rückfrage an den Menschen | 5 |

**Befund:** Die Regel „Never run this without asking the engineer first“ steht im Kopf von `run_testcase.sh` und in `SKILL.md`. Ist `Bash` für die Sitzung pauschal freigegeben, hängt sie allein am Modell. Ein Lauf ohne Rückfrage auf einem geteilten Target ersetzt dessen Datensatz, auch wenn dort jemand anderes arbeitet.

**Befund zur Entstehung:** Der Skill ist sorgfältig geschrieben. Welche seiner Regeln nur vom Modell abhängen, hat niemand zusammengestellt.

**Nicht Gegenstand:** Die Umsetzung technischer Absicherungen (KI-356).

## Randbedingungen

- Der Workflow bleibt, wie er ist.
- Die Einordnung betrifft den Skill, nicht einzelne Tests.

## Akzeptanzkriterien

- **AK1** – Der Ablauf ist von der Anforderung bis zum Merge Request mit allen menschlichen Kontrollpunkten beschrieben.
- **AK2** – Jede Regel ist zugeordnet: technisch, Modell oder Mensch.
- **AK3** – Für jede Regel ist die Folge eines einmaligen Verstoßes benannt.
- **AK4** – Mindestens drei Regeln sind als Kandidaten für technische Durchsetzung markiert, mit Vorschlag.

## Hinweise

„Steht im Skill“ ist keine Durchsetzung. Die Frage ist, was passiert, wenn das Modell die Regel übersieht.

AK3 wird unbequem: Für manche Regeln ist die Folge klein, für andere, etwa einen Lauf ohne Rückfrage auf einem geteilten Target, nicht.

---

## Für den Kurs

Dieses Ticket nennt keine Lösung. Arbeiten Sie entlang der Frage:

**Was passiert, wenn das Modell diese Regel einmal nicht befolgt?**

---
---

# Addendum · Arten der Durchsetzung

| Art | Beispiel beim Team | Stärke | Schwäche |
|---|---|---|---|
| technisch, blockierend | `gate = refuse` stoppt | unabhängig vom Modell | nur für prüfbare Regeln |
| technisch, meldend | `check_test.py`, `assertion_guard.py check` | macht Verstöße sichtbar | Modell oder Mensch muss reagieren |
| Modell | „ask first“, „cap at 2 runs“ | flexibel, auch für Urteile | ein Übersehen genügt |
| Mensch | Freigabe, Suite-Wahl, Merge Request | fachliches Urteil | kostet Zeit, wird Routine |

Claude Code selbst bietet eine weitere technische Ebene: Freigaben je Werkzeug (`allow`, `ask`, `deny` in `.claude/settings.json`).
