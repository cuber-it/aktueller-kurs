# AV-2530 · Entwicklungsaufwand nach Unterscheidungsrelevanz ausrichten

**Typ:** Story
**Komponente:** Fachliche Architektur / IT-Strategie
**Priorität:** Hoch
**Verweist auf:** AV-2515 (Budgetplanung, Nachfrage der Geschäftsführung)

---

## Story

**Als** IT-Leitung
**möchte ich** für jeden Bereich begründen können, ob wir ihn selbst bauen, zukaufen oder als Standard nehmen,
**damit** Kapazität dort eingesetzt wird, wo sie einen Unterschied macht.

---

## Description

Bei der Budgetplanung (AV-2515) wurde festgestellt, dass rund **vier Fünftel** des Entwicklungsaufwands seit 2019 in Bereiche flossen, in denen sich das Unternehmen nicht vom Wettbewerb unterscheidet.

| Bereich | Aufwand seit 2019 | Unterscheidungsrelevant |
|---|---|---|
| Buchhaltung | 3 Jahre, 4–6 Entwickler | nein |
| Personalzeiterfassung | 8 Monate, 2 Entwickler | nein |
| Dokumentenarchiv | 6 Monate, 2 Entwickler | nein |
| **Verfügbarkeitsdisposition** | zugekauft, keine Weiterentwicklung | **ja** |
| Anmietungsabwicklung | laufend, 3 Entwickler | teilweise |

**Die Verfügbarkeitsdisposition ist das Verkaufsargument des Unternehmens.** Die Quote nicht erfüllter Reservierungen liegt bei 0,8 Prozent gegenüber 4 Prozent im Branchendurchschnitt.

**Das zugekaufte Modul von 2017** kann keine stationsübergreifende Umverteilung, keine Prognose, und rechnet einmal nachts. Um es herum sind gewachsen: eine Tabellenkalkulation zur Korrektur, ein selbstgeschriebener Vorschlagsdienst, eine Sonderregelliste für 23 Standorte.

**Die 0,8 Prozent werden zu einem erheblichen Teil durch manuelle Nachsteuerung von vier Disponenten erreicht.** Zwei davon gehen binnen fünf Jahren in Rente; ihr Wissen ist nicht dokumentiert.

**Befund zur Entscheidungsgrundlage:** Es existiert kein Kriterium. Entschieden wurde nach Dringlichkeit, verfügbarer Kapazität und danach, wer gerade fragte.

**Nicht Gegenstand:** Die Ablösung des Dispositionsmoduls. Zunächst geht es um Einordnung und Kriterium.

## Randbedingungen

- 22 Entwickler insgesamt
- Die Buchhaltung funktioniert und wird von 2 Entwicklern gepflegt, überwiegend wegen gesetzlicher Änderungen
- Die Kautionsabwicklung ist tatsächlich branchenuntypisch
- Sieben Länder mit unterschiedlicher Umsatzsteuer
- Ein Wechsel auf ein Standardprodukt für die Buchhaltung wurde nie geprüft

## Akzeptanzkriterien

- **AK1** – Jeder fachliche Bereich ist einer Kategorie zugeordnet: unterscheidungsrelevant, unterstützend oder Standard.
- **AK2** – Die Zuordnung ist begründet. Die Begründung nennt, **womit sich das Unternehmen unterscheidet** — nicht Umsatzanteil, Aufwand oder Datenmenge.
- **AK3** – Für jede Kategorie ist festgelegt, wie damit umgegangen wird: selbst bauen, zukaufen und anpassen, oder Standard unverändert nutzen.
- **AK4** – Für jeden Bereich ist der Ist-Zustand der Vorgehensweise dem Soll gegenübergestellt.
- **AK5** – Abweichungen zwischen Ist und Soll sind benannt, mit Aufwand und Risiko einer Korrektur.
- **AK6** – Für die Buchhaltung ist bewertet, ob eine Ablösung durch ein Standardprodukt sinnvoll ist — einschließlich der Frage, was mit der Kautionsabwicklung geschieht.
- **AK7** – Es ist beschrieben, wie die Zuordnung eines Bereichs künftig bei neuen Vorhaben erfolgt.
- **AK8** – Das Wissen der vier Disponenten ist als Risiko ausgewiesen, mit Vorschlag zum Umgang.

## Hinweise

AK2 ist der Kern. „Wir machen viel Umsatz damit" begründet keine Unterscheidungsrelevanz — die Buchhaltung verarbeitet den gesamten Umsatz und unterscheidet niemanden.

AK6 hat eine Falle: Die Kautionsabwicklung ist tatsächlich besonders. Die Frage ist, ob diese Besonderheit eine eigene Buchhaltung rechtfertigt oder ob sie sich abtrennen lässt.

AK7 zielt darauf, dass sich der Befund nicht wiederholt. Ohne Kriterium wird beim nächsten Vorhaben wieder nach Dringlichkeit entschieden.

---

## Für den Kurs

Dieses Ticket nennt kein Konzept. Arbeiten Sie entlang der Frage:

**Womit unterscheidet sich dieses Unternehmen — und wo fließt der Aufwand hin?**

---
---

# Addendum · Die drei Arten von Fachbereichen

Der Katalog unterscheidet drei Arten. Die Einteilung betrifft den **Problemraum** — sie beschreibt, was das Unternehmen tut, nicht wie die Software geschnitten ist.

## Core Domain

**Das, womit sich das Unternehmen unterscheidet.**

| | |
|---|---|
| Erkennungszeichen | Ein Wettbewerber könnte es nicht einfach nachmachen. Es steht im Verkaufsgespräch. |
| Vorgehen | Selbst bauen, mit den besten Leuten |
| Aufwand | gerechtfertigt, auch hoher |
| Beispiel hier | Verfügbarkeitsdisposition |

## Supporting Subdomain

**Notwendig für das Geschäft, aber nicht unterscheidend.**

| | |
|---|---|
| Erkennungszeichen | Ohne geht es nicht, aber es ist branchenüblich. Kein Wettbewerbsvorteil. |
| Vorgehen | Selbst bauen, wenn nichts passt — aber sparsam. Zukaufen, wenn möglich. |
| Aufwand | so gering wie vertretbar |
| Beispiel hier | Anmietungsabwicklung (teilweise) |

## Generic Subdomain

**Überall gleich, überall verfügbar.**

| | |
|---|---|
| Erkennungszeichen | Es gibt Standardprodukte. Andere Branchen haben dasselbe Problem. |
| Vorgehen | Standard nehmen, nicht anpassen |
| Aufwand | minimal |
| Beispiel hier | Buchhaltung, Zeiterfassung, Dokumentenarchiv |

## Die Prüffrage

> **Würde ein Wettbewerber, der dies genauso gut kann wie wir, uns gefährlich?**

- **Ja, und er kann es nicht** → Core
- **Ja, aber alle können es** → Supporting
- **Nein, es ist gleichgültig** → Generic

## Was **kein** Kriterium ist

| Scheinkriterium | Warum es nicht trägt |
|---|---|
| Umsatzanteil | Die Buchhaltung verarbeitet 100 Prozent des Umsatzes |
| Datenmenge | sagt nichts über Bedeutung |
| Aufwand bisher | zirkulär — man begründet die Vergangenheit mit sich selbst |
| Zahl der Nutzer | die Zeiterfassung nutzen alle |
| Wie wichtig es sich anfühlt | jede Abteilung hält ihres für zentral |
| Wie kompliziert es ist | Kompliziertheit ist kein Wert |

## Subdomain und Bounded Context

Die häufigste Verwechslung im ganzen Kurs:

| | Subdomain | Bounded Context |
|---|---|---|
| Raum | **Problemraum** — was das Unternehmen tut | **Lösungsraum** — wie die Software geschnitten ist |
| Bestimmt durch | das Geschäft | den Entwurf |
| Verändert sich | selten, mit dem Geschäftsmodell | mit dem Entwurf |

**Sie fallen nicht notwendig zusammen.** Eine Core Domain kann über mehrere Kontexte verteilt sein; ein Kontext kann Teile mehrerer Subdomains bedienen.

**Wünschenswert ist Deckungsgleichheit** — sie ist ein Zeichen dafür, dass der Entwurf der Fachlichkeit folgt. Erzwingen lässt sie sich nicht.
