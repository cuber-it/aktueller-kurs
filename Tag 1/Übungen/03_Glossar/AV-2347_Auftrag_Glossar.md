# AV-2347 · Glossare je Kontext einführen

**Typ:** Story
**Komponente:** Fachliche Architektur / Dokumentation
**Priorität:** Mittel
**Verweist auf:** AV-2291 (Kontextaufteilung), AV-2298 (Fehlentwicklung Kundenprüfung, 3 Wochen Nacharbeit)

---

## Story

**Als** Entwicklerin, die neu in einen Bereich kommt,
**möchte ich** an einer Stelle nachlesen können, was ein Begriff **hier** bedeutet,
**damit** ich nicht auf eine Bedeutung baue, die in meinem Bereich nicht gilt.

---

## Description

Das 2024 erstellte Glossar (84 Einträge, 31 Seiten, alphabetisch) wird nicht verwendet.

**Befunde nach acht Monaten:**

| Kennzahl | Wert |
|---|---|
| Abrufe aus dem Intranet | 11, davon 7 in der ersten Woche |
| Anforderungsdokumente mit Verweis | 0 |
| Tickets mit unpräzisiertem mehrdeutigem Begriff | 9 von 12 (Stichprobe) |
| Entwickler, die das Dokument kannten | nicht alle |

**Ursachen laut Aufarbeitung:**

Für die neun meistverwendeten Begriffe enthält das Glossar Oberdefinitionen mit Aufzählung der Sonderfälle. Beispiel:

> **Kunde:** Natürliche oder juristische Person, die in einer Geschäftsbeziehung zum Unternehmen steht. Je nach Kontext kann dies der Vertragspartner, der Fahrzeugnutzer oder der Rechnungsempfänger sein.

Diese Formulierung hilft niemandem: Wer im Bereich arbeitet, weiß bereits, was er meint. Wer von außen liest, erfährt nur, dass es mehrdeutig ist.

**Weitere Mängel:** alphabetische Sortierung trennt Zusammengehöriges · keine Zuständigkeit für die Pflege · historische Bezeichnungen stehen gleichberechtigt neben aktuellen.

**Folgeschaden:** In AV-2298 wurde eine Prüfung auf den falschen Kundenbegriff gebaut. Nacharbeit drei Wochen.

**Nicht Gegenstand:** Die Kontextaufteilung selbst — die ist in AV-2291 beschlossen.

## Randbedingungen

- Die vier Kontexte aus AV-2291 stehen fest: Vertragsverwaltung, Anmietung, Flotte und Instandhaltung, Fakturierung
- Rund 20 Begriffe werden bereichsübergreifend verwendet, etwa 60 sind bereichsspezifisch
- Neue Begriffe entstehen laufend, etwa fünf bis zehn im Jahr
- Es gibt keine Rolle, die für fachliche Begriffe zuständig ist

## Akzeptanzkriterien

- **AK1** – Je Kontext existiert ein eigenes Begriffsverzeichnis. Es enthält nur, was in diesem Kontext gilt.
- **AK2** – Innerhalb eines Kontextes ist jeder Begriff **eindeutig**. Formulierungen mit „je nach Kontext" oder „kann auch bedeuten" sind unzulässig.
- **AK3** – Für Begriffe, die in mehreren Kontexten vorkommen, ist festgehalten, dass und wie sie sich unterscheiden.
- **AK4** – Für jeden Begriff ist erkennbar, ob er an einer Kontextgrenze übersetzt wird und wohin.
- **AK5** – Die Verzeichnisse sind nicht alphabetisch, sondern nach fachlichem Zusammenhang gegliedert.
- **AK6** – Historische und nicht mehr verwendete Begriffe sind als solche gekennzeichnet oder entfernt.
- **AK7** – Je Kontext ist eine Person benannt, die das Verzeichnis pflegt.
- **AK8** – Es ist festgelegt, bei welchem Anlass ein Eintrag entsteht oder geändert wird.
- **AK9** – Das Verzeichnis liegt dort, wo damit gearbeitet wird, nicht in einem separaten Dokumentenablagesystem.

## Hinweise

Ein überarbeitetes Gesamtglossar erfüllt AK1 und AK2 nicht. Solange ein Verzeichnis alle Bereiche abdecken soll, entstehen wieder Oberdefinitionen.

AK2 ist der Kern. Ein Begriffsverzeichnis, das Mehrdeutigkeit dokumentiert statt sie auszuschließen, beschreibt das Problem, statt es zu lösen.

AK9 zielt auf die Nutzung: Elf Abrufe in acht Monaten sind kein Dokumentationsproblem, sondern ein Ortsproblem.

---

## Für den Kurs

Dieses Ticket nennt kein Konzept. Arbeiten Sie entlang der Frage:

**Was gilt hier — und was gilt hier nicht?**

---
---

# Addendum · Was ein brauchbares Glossar von einem unbrauchbaren unterscheidet

## Merkmale eines unbrauchbaren Glossars

| Merkmal | Warum es scheitert |
|---|---|
| **Ein Verzeichnis für alle Bereiche** | erzwingt Oberdefinitionen, die niemandem helfen |
| **„Je nach Kontext…"** | dokumentiert das Problem, statt es zu lösen |
| **Alphabetisch sortiert** | trennt, was fachlich zusammengehört |
| **Als eigenes Dokument abgelegt** | niemand geht dorthin, um zu arbeiten |
| **Ohne Zuständigkeit** | veraltet ab dem Tag der Fertigstellung |
| **Vollständigkeit als Ziel** | 84 Einträge, von denen 60 niemand nachschlägt |
| **Definitionen aus dem Lehrbuch** | „Kunde: wer Leistungen bezieht" — sagt nichts über dieses Unternehmen |

## Merkmale eines brauchbaren Glossars

| Merkmal | Wirkung |
|---|---|
| **Ein Verzeichnis je Kontext** | Eindeutigkeit ist möglich |
| **Eindeutige Definition, keine Aufzählung** | beantwortet die Frage, die jemand hat |
| **Nach fachlichem Zusammenhang gegliedert** | man findet Verwandtes beim Lesen |
| **Beispiel statt Definition, wo möglich** | „Ein Mieter ist die Person, die den Führerschein vorlegt" |
| **Abgrenzung mitgeschrieben** | „Nicht zu verwechseln mit dem Rahmenvertragspartner" |
| **Übersetzungshinweis an Grenzen** | „Wird in der Fakturierung zum Rechnungsempfänger" |
| **Am Ort der Arbeit** | im Repository neben dem Code, nicht im Ablagesystem |
| **Benannte Zuständigkeit** | jemand ist ansprechbar |

## Die zentrale Regel

> **Ein Glossar ist nur innerhalb eines Kontextes möglich.**

Über Kontextgrenzen hinweg gibt es keine gemeinsame Definition — sonst wäre es keine Grenze. Wer ein bereichsübergreifendes Glossar baut, arbeitet gegen die Aufteilung, die er gerade beschlossen hat.

## Wann ein Glossar überhaupt nützt

**Nicht** als Nachschlagewerk für alle Fälle. Es wird gelesen:

- beim **Einstieg** in einen Kontext — was gilt hier?
- bei einem **Missverständnis** — was war noch mal gemeint?
- beim **Formulieren** einer Anforderung — welches Wort ist richtig?

Alle drei Anlässe sind selten und punktuell. Deshalb muss ein Glossar **kurz** sein und **am richtigen Ort** liegen — nicht vollständig.
