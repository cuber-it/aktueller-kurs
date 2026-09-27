# KI-323 · Testfälle vor der Umsetzung auf Beobachtbarkeit prüfen

**Typ:** Story
**Komponente:** Testentwurf, Skill `testcase-writer`
**Priorität:** Mittel

---

## Story

**Als** Verantwortliche für die Testspezifikation
**möchte ich**, dass Testfälle vor der Freigabe beobachtbare Erwartungen und ausdrückliche Vorbedingungen haben,
**damit** ein automatisierter Test prüft, was der Testfall meint, und nicht nur den Bedienweg.

---

## Description

Testfälle entstehen aus Test Stories mit dem Skill `testcase-writer` und werden in Polarion geprüft und freigegeben. Der Skill `testcase-implementer` setzt sie um.

**Bestand:**

| Was | Anzahl |
|---|---|
| Testfälle in der Spezifikation der Integrationstests | 155 auf 142 Seiten |
| Titel, die unter zwei Kennungen vorkommen | 2 |
| Testfälle mit einem Expected, das mehrere Aussagen enthält (Stichprobe von 20) | 9 |

**Befund:** Der Standardtraktor heißt bereits „Tractor“ und ist nach dem Zurücksetzen ausgewählt. Wird der Testfall „Neuen Traktor anlegen“ wörtlich umgesetzt (Name „Tractor“, Prüfung „Eintrag ausgewählt“), ist die Prüfung auch dann erfüllt, wenn das Anlegen scheitert.

**Befund zur Entstehung:** Die Erwartung „angelegt und ausgewählt“ war richtig gemeint, aber nicht so formuliert, dass sie den Ausgangszustand ausschließt.

**Nicht Gegenstand:** Die Umsetzung in Squish (KI-334).

## Randbedingungen

- Polarion bleibt das führende System für Testfälle.
- Der `testcase-writer` kann um einen Zwischenschritt ergänzt werden.

## Akzeptanzkriterien

- **AK1** – Der Testfall liegt als Gherkin-Szenario vor, jede `Then`-Zeile ist beobachtbar.
- **AK2** – Vorbedingungen, die das Ergebnis verfälschen können, stehen als `Given`.
- **AK3** – Fehlende Szenarien sind benannt.
- **AK4** – Offene Fragen an die Fachseite sind aufgeschrieben.
- **AK5** – Es ist entschieden, wo im Weg Story → Testfall → Test die Zwischenrepräsentation steht.

## Hinweise

Das Szenario um einen eindeutigen Namen wie „Tractor-4711“ zu ergänzen erfüllt AK2 nur zur Hälfte: Der Fall „Name existiert schon“ ist dann nicht geprüft.

AK5 wird unbequem: Eine zweite Darstellung neben Polarion kann auseinanderlaufen.

---

## Für den Kurs

Dieses Ticket nennt keine Lösung. Arbeiten Sie entlang der Frage:

**Woran würde ein Beobachter sehen, dass das Verhalten eingetreten ist?**

---
---

# Addendum · Given, When, Then

| Teil | beschreibt | nicht |
|---|---|---|
| `Given` | den Zustand vor der Aktion | wie er hergestellt wird |
| `When` | die fachliche Aktion | die Klickfolge |
| `Then` | eine beobachtbare Folge | „funktioniert“, „ist korrekt“ |

## Typische Lücken, die Gherkin sichtbar macht

| Lücke | Erkennungszeichen im Testfall |
|---|---|
| unbeobachtbare Erwartung | „ist angelegt“, „funktioniert“ |
| fehlender Ausgangszustand | erster Schritt ist schon Aktion |
| mehrere Aussagen in einem Expected | „angelegt und ausgewählt“ |
| fehlende Varianten | kein Abbruch, kein Fehlerfall |
