# AV-2291 · Begriffskollisionen erheben und Kontextgrenzen vorschlagen

**Typ:** Story
**Komponente:** Datenmodell / Fachliche Architektur
**Priorität:** Hoch
**Verweist auf:** AV-2180 (Auswertung „Umsatz je Kunde", nicht auslieferbar)

---

## Story

**Als** Fachbereichsleitung
**möchte ich** wissen, welche Begriffe in den Bereichen unterschiedlich verwendet werden und wo die Grenzen zwischen den Bedeutungen verlaufen,
**damit** eine bereichsübergreifende Auswertung nicht an der Frage scheitert, was ein Kunde ist.

---

## Description

Die Auswertung „Umsatz je Kunde" (AV-2180) konnte nicht ausgeliefert werden. Vier Bereiche lieferten vier Zahlen mit vier verschiedenen Zählweisen.

Bei der Aufarbeitung zeigte sich, dass die Abweichung kein Datenfehler ist. **Die Bereiche meinen mit „Kunde" tatsächlich Verschiedenes**, und jede Bedeutung ist in ihrem Bereich richtig.

| Bereich | Zählte | Ergebnis für einen Konzernkunden |
|---|---|---|
| Vertrieb | Rahmenvertragspartner | 1 |
| Stationen | Fahrer | 340 |
| Abrechnung | Rechnungsempfänger | 4 |
| Werkstatt | Kostenträger | 1 (intern) |

**Vorgeschichte:** Ein zweitägiger Workshop sollte eine verbindliche Definition festlegen. Das Ergebnis war ein Kompromiss, den anschließend kein Bereich verwendete. Ein verteiltes Glossar hat den Sprachgebrauch nicht verändert.

**Nicht Gegenstand dieses Tickets:** Die technische Umsetzung. Es geht um die Erhebung und einen Vorschlag, nicht um Migration.

## Randbedingungen

- Fünf Bereiche: Vertrieb, Stationen, Flotte, Werkstatt, Abrechnung
- Die Tabelle `Kunde` hat 47 Spalten, die meisten für die meisten Sätze leer
- Zwei neue Spalten im letzten Jahr, beide bereichsspezifisch
- Die Bereiche haben eigene Zuständigkeiten und eigene Releasezyklen
- Ein früherer Vereinheitlichungsversuch ist gescheitert

## Akzeptanzkriterien

- **AK1** – Für jeden mehrdeutig verwendeten Begriff ist erhoben, was er in welchem Bereich bedeutet.
- **AK2** – Für jeden Begriff ist festgehalten, welche Angaben der jeweilige Bereich tatsächlich benötigt.
- **AK3** – Es ist benannt, wo verschiedene Wörter dieselbe Sache meinen und wo dasselbe Wort verschiedene Sachen meint.
- **AK4** – Es liegt ein Vorschlag vor, entlang welcher Grenzen die Bedeutungen getrennt werden können.
- **AK5** – Der Vorschlag sieht **keine** bereichsübergreifend einheitliche Definition vor, sofern sich zeigt, dass die Bedeutungen fachlich berechtigt verschieden sind.
- **AK6** – Für die gescheiterte Auswertung AV-2180 ist beschrieben, wie sie unter dem Vorschlag zustande käme.
- **AK7** – Der Vorschlag benennt, welche Begriffe an den Grenzen übersetzt werden müssen und wer für die Übersetzung zuständig ist.

## Hinweise

Ein erneuter Einigungsversuch auf eine gemeinsame Definition erfüllt AK5 nicht. Der erste Versuch ist gescheitert, weil der Kompromiss für keinen Bereich passte.

Ein Glossar allein erfüllt AK4 nicht. Es hält fest, was gilt, benennt aber keine Grenzen.

AK6 ist der Prüfstein: Ein Vorschlag, der die ursprüngliche Anforderung nicht mehr erfüllbar macht, löst das Problem nicht.

---

## Für den Kurs

Dieses Ticket nennt kein Konzept. Bearbeiten Sie es entlang des Leitwegs:

**Begriffe erheben → Kollisionen benennen → Grenzen vorschlagen → Übersetzung klären**

---
---

# Addendum · Woran erkennt man einen Sprachkonflikt?

## Im Gespräch mit dem Fachbereich

| Signal | Beispiel |
|---|---|
| „Bei uns heißt das anders" | zwei Wörter, eine Sache |
| „Das ist bei uns was anderes" | ein Wort, zwei Sachen — der gefährlichere Fall |
| Zwei Bereiche liefern unterschiedliche Zahlen für dieselbe Frage | und beide haben recht |
| Eine Definition wird in einem Workshop „festgelegt" | und danach von niemandem verwendet |
| Jemand erklärt einen Begriff mit „das kommt darauf an, wen Sie fragen" | die direkteste Ansage |
| Ein Glossar existiert, aber niemand nutzt es | es beschreibt einen Kompromiss, keine Praxis |

## Im System

| Signal | Konkret |
|---|---|
| Eine Tabelle mit vielen Spalten, die meist leer sind | jede Spalte gehört einem Bereich |
| Spalten wie `art`, `typ`, `status`, `kategorie` nebeneinander | Bedeutungsunterschiede, die als Merkmal getarnt sind |
| Ein Feld wird je nach Bereich anders befüllt | ohne dass das dokumentiert wäre |
| Auswertungen, die von Hand nachbearbeitet werden | die Software kann die Frage nicht beantworten |
| Kommentare in der Datenbank statt Dokumentation | „für Werkstatt immer 0 setzen" |

## Warum ein Wort mit zwei Bedeutungen schlimmer ist als zwei Wörter

**Zwei Wörter für eine Sache** fallen auf. Jemand fragt nach, es wird geklärt.

**Ein Wort für zwei Sachen** fällt nicht auf. Beide Seiten glauben, sich verstanden zu haben. Der Fehler zeigt sich erst, wenn Daten zusammengeführt werden — oft Jahre später und mit unklarer Ursache.

Deshalb ist die zweite Kollisionsart die, nach der man zuerst sucht.

## Was **kein** Sprachkonflikt ist

**Unterschiedliche Detailtiefe.** Wenn der Vertrieb den Kunden mit fünf Angaben führt und die Abrechnung mit zwanzig, ist das kein Konflikt, sondern unterschiedlicher Bedarf an derselben Sache.

**Verschiedene Sichten auf dasselbe.** Eine Rechnungsansicht und eine Vertragsansicht desselben Kunden sind zwei Sichten, kein Konflikt.

**Der Prüfstein:** Führt die Zusammenführung zu einem Widerspruch, oder nur zu einer Vereinigungsmenge? Widerspruch bedeutet Konflikt.
