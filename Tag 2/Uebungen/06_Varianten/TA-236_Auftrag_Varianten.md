# TA-236 · Vorschlag „Umstellung auf Screenplay“ bewerten

**Typ:** Spike
**Komponente:** Testarchitektur
**Priorität:** Mittel

---

## Story

**Als** Teamleitung Testautomatisierung
**möchte ich** eine begründete Bewertung, ob und wo Screenplay unsere Architektur ergänzt,
**damit** wir nicht aus Begeisterung umbauen und nicht aus Gewohnheit ablehnen.

---

## Description

Es liegt der Vorschlag vor, alle Tests auf Screenplay umzustellen. Die Testsuite nutzt heute Screen Objects, Controls und Helper mit fachlichen Namen.

**Bestand:**

| Was | Anzahl |
|---|---|
| Testfälle | 983 |
| Testfälle mit direktem Squish-Aufruf | 0 |
| Rollen in den Tests (Fahrer, Service) | 2, heute über PIN-Eingabe im Test unterschieden |
| Tests, die dieselbe Handlung auf zwei AUTs ausführen | 6 |

**Befund:** Kosten und Nutzen einer Umstellung wurden bisher nicht an konkreten Änderungen gezeigt. Die Diskussion dreht sich um Lesbarkeit und Modernität.

**Nicht Gegenstand:** Eine Umstellung. Dieses Ticket bewertet.

## Randbedingungen

- Die bestehenden 983 Tests laufen weiter.
- Eine Ergänzung darf lokal sein.
- Das Ergebnis ist eine Empfehlung mit Begründung.

## Akzeptanzkriterien

- **AK1** – Ein Szenario ist in mindestens drei Varianten skizziert.
- **AK2** – Für vier Change Cases ist je Variante angegeben, was sich ändert.
- **AK3** – Neue Konzepte jeder Variante sind benannt.
- **AK4** – Die Empfehlung nennt die Umstände, unter denen Screenplay ergänzt würde.

## Hinweise

„Screenplay ist moderner“ erfüllt AK4 nicht.

AK2 wird unbequem: Für einige Change Cases sind die Varianten gleich teuer.

---

## Für den Kurs

Dieses Ticket nennt keine Lösung. Arbeiten Sie entlang der Frage:

**Welche Änderung macht diese Variante leichter, und was kostet sie?**

---
---

# Addendum · Varianten auf einen Blick

| Variante | Kern | Kosten |
|---|---|---|
| direkter Testcode | alles im Test | Änderungen treffen viele Tests |
| Screen Objects | Wissen über Bildschirme gebündelt | Tests kennen Wege |
| Screen Objects + Tasks | Wege und Handlungen gebündelt | eine Ebene mehr |
| Screenplay | Actor mit Abilities führt Tasks aus, Questions beobachten | vier neue Konzepte |
| hybrid | gezielt kombiniert | Regeln nötig, wann was |

## Screenplay kurz

| Begriff | Bedeutung |
|---|---|
| Actor | wer handelt (Fahrer, Service) |
| Ability | was der Actor kann (Terminal bedienen, Dateien lesen) |
| Task | was erreicht werden soll |
| Interaction | technische Aktion |
| Question | was beobachtet wird |
