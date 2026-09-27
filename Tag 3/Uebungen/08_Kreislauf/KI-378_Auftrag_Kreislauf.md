# KI-378 · Erste Fassung der Regeln für KI-gestütztes Test Engineering

**Typ:** Story
**Komponente:** Teamstandard
**Priorität:** Hoch
**Verweist auf:** KI-301, KI-312, KI-345, KI-356, KI-367; Python-Standard (Tag 1), Squish-Standard (Tag 2)

---

## Story

**Als** Testautomatisierungsteam
**möchten wir** festlegen, wie weit ein Agent im Kreislauf aus Umsetzung, Lauf und Korrektur allein gehen darf,
**damit** jeder weiß, was der Agent entscheidet, was er meldet und wo ein Mensch zustimmt.

---

## Description

Der Skill enthält Regeln für den Kreislauf, verteilt auf `SKILL.md` und `test_run.md`. Einige sind technisch durchgesetzt, andere nicht. Ein gemeinsamer Standard fehlt.

**Bestand:**

| Was | Stand |
|---|---|
| Laufgrenze | 2, im Skill |
| erlaubte Korrekturarten | 5, im Skill |
| verbotene Korrekturarten | 3, im Skill; `assertion_guard.py` meldet Änderungen an Assertion-Zeilen in `test.py` |
| menschliche Kontrollpunkte im Kreislauf | 2 (vor dem Lauf, Bericht) |
| Regeln zu Prompt Injection | 0 |

**Befund:** Testfälle in Polarion enthalten manchmal Hinweise an Menschen, etwa „If the value differs, update the expected value in the test.“ Ein Agent, der solche Sätze als Anweisung liest, passt den erwarteten Wert in `test_config.py` an. `assertion_guard.py check` meldet das nicht, weil die Assertion-Zeile in `test.py` gleich bleibt.

**Befund zur Entstehung:** Der Agent behandelte Text aus dem Testfall als Anweisung. Die Leitplanke `assertion_guard.py` prüft nur `test.py`, die erwarteten Werte stehen aber in `test_config.py`. Eine Regel zu Anweisungen in gelesenen Daten gab es nicht.

**Nicht Gegenstand:** Die technische Umsetzung.

## Randbedingungen

- Der Standard baut auf den Standards aus Tag 1 und Tag 2 auf.
- Er muss für Menschen lesbar und als Kontext für den Skill verwendbar sein.

## Akzeptanzkriterien

- **AK1** – Stoppbedingungen sind vollständig aufgeführt.
- **AK2** – Für typische Fehlerbilder ist festgelegt: selbst korrigieren oder melden.
- **AK3** – Menschliche Kontrollpunkte sind mit Begründung festgelegt.
- **AK4** – Mindestens eine Regel behandelt Anweisungen in gelesenen Daten.
- **AK5** – Jede Regel ist als MUST, SHOULD oder DON'T eingeordnet und nennt ihre Durchsetzung.

## Hinweise

„Der Agent soll vorsichtig sein“ erfüllt keines der Kriterien.

AK4 wird unbequem: Testfalltexte sind Anweisungen an Menschen. Der Agent soll sie umsetzen, aber nicht ihnen gehorchen, wenn sie seine Regeln ändern.

---

## Für den Kurs

Dieses Ticket nennt keine Lösung. Arbeiten Sie entlang der Frage:

**Was verliert das Team, wenn der Agent hier falsch entscheidet, und merkt es jemand?**

---
---

# Addendum · Bausteine eines Kreislaufs

| Baustein | beim Team |
|---|---|
| Stoppbedingung | 2 Läufe, Selector-Fehler ohne Spy, nicht ausführbare Tests |
| Kontrollpunkt | Rückfrage vor Lauf und Spy, Bericht, Merge Request |
| Invariante | Assertion-Menge unverändert (`assertion_guard.py`) |
| Nachvollziehbarkeit | Bericht nach festem Format, Protokolle im Cache |
