# TA-248 · Review der Testarchitektur vor der Festlegung des Teamstandards

**Typ:** Task
**Komponente:** Testarchitektur
**Priorität:** Hoch
**Verweist auf:** TA-201, TA-212, TA-218, TA-224, TA-231, TA-236, TA-242

---

## Story

**Als** Testautomatisierungsteam
**möchten wir** vor der Festlegung des Standards jede betroffene Stelle einmal begründet bewerten,
**damit** der Standard auf Befunden beruht und funktionierende Entscheidungen ausdrücklich bestätigt.

---

## Description

Die Tickets der letzten Wochen haben Befunde an mehreren Stellen gesammelt. Vor der Standards Session soll jede Stelle nach demselben Schema bewertet werden.

**Bestand:** Kandidaten und Umfang siehe Material A der Übung.

**Befund:** Regeln, die aus Einzelfällen abgeleitet werden, treffen oft ein Symptom. Eine Regel wie „keine Helper mit mehr als 20 Zeilen“ verhindert unübersichtliche Helper, aber auch lange, geradlinige Abläufe wie das Durchgehen aller Geräteparameter.

**Nicht Gegenstand:** Umsetzung der Entscheidungen.

## Randbedingungen

- Jede Gruppe bewertet einen Ausschnitt.
- „Beibehalten“ ist eine gleichwertige Entscheidung.
- Regelkandidaten gehen in die Standards Session, dort wird entschieden.

## Akzeptanzkriterien

- **AK1** – Für den Ausschnitt ist Phase 1 ohne Bewertung dokumentiert.
- **AK2** – Mindestens drei Change Cases sind durchgespielt.
- **AK3** – Jede Entscheidung ist in einem Satz begründet.
- **AK4** – Mindestens eine Entscheidung „beibehalten“ ist begründet.
- **AK5** – Regelkandidaten nennen Problem, Geltungsbereich, Ausnahme und Prüfbarkeit.

## Hinweise

Eine Liste von Verbesserungen erfüllt AK4 nicht.

AK5 wird unbequem: Viele Regeln lassen sich nicht automatisch prüfen.

---

## Für den Kurs

Dieses Ticket nennt keine Lösung. Arbeiten Sie entlang der Frage:

**Welche beobachtbare Konsequenz unterscheidet die Varianten?**

---
---

# Addendum · Entscheidungen

| Entscheidung | Bedeutung |
|---|---|
| beibehalten | funktioniert mit angemessener Komplexität |
| vereinfachen | Abstraktion kostet mehr, als sie bringt |
| ergänzen | eine konkrete Fähigkeit oder Grenze fehlt |
| gezielt umbauen | wiederkehrendes Problem rechtfertigt die Änderung |
| nicht übernehmen | Alternative bringt keinen ausreichenden Nutzen |
| offen | Evidenz reicht noch nicht |

## Vom Befund zur Regel

| Frage | Beispiel |
|---|---|
| Welches Problem verhindert sie? | zweiter Klick schließt das Panel |
| Wo gilt sie? | Quellen, die umschalten |
| Welche Ausnahme ist legitim? | Controls, die nach Erfolg verschwinden |
| Automatisch prüfbar? | teilweise: Suche nach `click_and_wait` auf bekannten Umschaltern; vollständig nur über eine sichere API |
