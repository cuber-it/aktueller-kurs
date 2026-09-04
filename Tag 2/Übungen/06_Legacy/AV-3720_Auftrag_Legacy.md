# AV-3720 · Ablösung mit Umschaltkriterium neu aufsetzen

**Typ:** Story
**Komponente:** Ablösung Kernsystem
**Priorität:** Hoch
**Verweist auf:** AV-3715 (Budgetplanung 2026, Frage nach Abschaltdatum unbeantwortet)

---

## Story

**Als** IT-Leitung
**möchte ich** für jede Ablösungsstufe benennen können, woran erkennbar ist, dass sie abgeschlossen ist,
**damit** nicht nach sieben Jahren beide Systeme laufen und niemand sagen kann, wann eines abgeschaltet wird.

---

## Description

Die 2018 begonnene Ablösung des Kernsystems ist in Stufe 3 von 3 seit vier Jahren nicht abgeschlossen. Beide Systeme laufen.

| Stufe | Umfang | Geplant | Stand |
|---|---|---|---|
| 1 | Reservierung, Verfügbarkeit | 2019 | fertig, Altsystem läuft weiter |
| 2 | Anmietung, Rückgabe | 2020 | 2022 fertig, drei Stationen weiterhin alt |
| 3 | Abrechnung, Auswertung | 2021 | offen |

**Befunde der Aufarbeitung:**

| Befund | Umfang |
|---|---|
| Parallelbetrieb | seit 7 Jahren |
| Abgleichdienst | 40 Regeln, eigener Betrieb |
| Offene Abweichungen im Abgleich | 12 zum Prüfzeitpunkt |
| Stationen im Altsystem | 3, seit 2022 unverändert |
| Aufwand für den Parallelbetrieb | rund 2,1 Vollzeitstellen |
| Umschaltkriterium | **existiert nicht** |

**Kernbefund:** Der Plan nannte Termine, aber keine Bedingung, bei deren Eintritt das Alte abgeschaltet wird.

**Weiterer Befund:** Weil der Abgleich in beide Richtungen funktionieren musste, wurden Datenstrukturen des Altsystems im neuen nachgebildet — darunter der Kundenbegriff mit 47 Merkmalen und der Statuscode mit vierzehn Ausprägungen.

**Nicht Gegenstand:** Die Frage, ob die Ablösung richtig war. Sie läuft und soll abgeschlossen werden.

## Randbedingungen

- Drei Stationen nutzen das Altsystem; eine Umstellung ist technisch möglich, wurde nie beauftragt
- Die Abrechnung greift auf beide Systeme zu
- Der Abgleichdienst war für sechs Monate gedacht
- Drei Termine wurden gesetzt und verschoben
- Eine Arbeitsgruppe tagte 2024 ohne Wirkung

## Akzeptanzkriterien

- **AK1** – Für jede verbleibende Stufe ist ein Umschaltkriterium benannt: eine überprüfbare Bedingung, bei deren Eintritt das Altsystem für diesen Bereich abgeschaltet wird.
- **AK2** – Das Kriterium ist nicht „Stufe fertig", sondern nennt einen messbaren Zustand.
- **AK3** – Für die drei verbliebenen Stationen ist entschieden: umstellen oder als dauerhafte Ausnahme führen — mit Begründung und Kosten.
- **AK4** – Es ist beschrieben, in welcher Reihenfolge abgeschaltet wird und was jeweils vorher erfüllt sein muss.
- **AK5** – Für die aus dem Altsystem übernommenen Begriffe ist benannt, welche im neuen Modell bleiben sollen und welche mit der Abschaltung entfallen.
- **AK6** – Für den Abgleichdienst ist festgelegt, wann er entfällt.
- **AK7** – Der Aufwand des Parallelbetriebs wird laufend ausgewiesen, nicht nur einmalig ermittelt.
- **AK8** – Es ist benannt, wer die Abschaltung entscheidet und woran diese Person es festmacht.

## Hinweise

Ein weiterer Termin erfüllt AK1 nicht. Drei Termine wurden gesetzt und verschoben; ein vierter ändert nichts, solange kein Kriterium existiert.

AK2 zielt auf die Ursache: „Sobald Stufe 3 fertig ist" ist kein Kriterium, weil „fertig" nicht definiert ist.

AK5 betrifft einen Folgeschaden: Die alten Begriffe sind im neuen System, weil der Abgleich sie brauchte. Mit dem Abgleich entfällt ihr Grund — nicht automatisch ihre Existenz.

AK7 ist wirksamer, als es klingt. 2,1 Vollzeitstellen fielen sieben Jahre lang an, ohne dass jemand sie sah.

---

## Für den Kurs

Dieses Ticket nennt kein Konzept. Arbeiten Sie entlang der Frage:

**Woran erkennen wir, dass das Neue trägt?**

---
---

# Addendum · Wie eine Ablösung gelingt

## Die Grundform

> **Grenze ziehen, dahinter neu bauen, schrittweise umleiten.**

Ein Neubau mit Umschaltung an einem Tag ist selten beherrschbar: Das Alte ändert sich während des Baus weiter, und der Umschaltzeitpunkt trägt das gesamte Risiko.

## Die Übersetzung an der Grenze

Zwischen Alt und Neu steht eine Übersetzung. Sie verhindert, dass alte Begriffe ins neue Modell wandern.

**Sie arbeitet in beide Richtungen:**

| Richtung | Übersetzt |
|---|---|
| Alt → Neu | alte Begriffe in das neue Modell |
| Neu → Alt | neue Begriffe zurück in die alte Form |

**Die Rückrichtung wird regelmäßig vergessen** — und ist der Grund, warum im Fallbeispiel alte Strukturen im neuen System nachgebildet wurden.

## Das Umschaltkriterium

Der Punkt, an dem die meisten Ablösungen scheitern.

**Kein Kriterium:**

| Formulierung | Warum sie nicht trägt |
|---|---|
| „Sobald Stufe 3 fertig ist" | „fertig" ist nicht definiert |
| „Bis Ende des Jahres" | ein Termin, keine Bedingung |
| „Wenn alle zufrieden sind" | nicht überprüfbar |

**Ein Kriterium:**

| Formulierung |
|---|
| „Wenn alle Stationen 30 Tage ohne Rückfall im neuen System gearbeitet haben" |
| „Wenn der Abgleich 14 Tage keine Abweichung meldet" |
| „Wenn die letzten drei Auswertungen aus beiden Systemen identisch sind" |

**Der Unterschied:** Ein Kriterium ist überprüfbar und hat einen Zeitpunkt, an dem es eintritt.

## Wo anfangen

**Nicht beim Einfachsten**, obwohl das verlockend ist.

| Kriterium | Warum |
|---|---|
| Wo der Schmerz ist | sonst fehlt der Rückhalt für ein mehrjähriges Vorhaben |
| Wo die Grenze klar verläuft | eine unklare Grenze macht die Übersetzung beliebig |
| **Bei der Core Domain** | dort lohnt der Aufwand; Generic Subdomains kauft man |

## Die zwei Fehler

**Anbau ohne Grenze.** Die alten Begriffe wandern mit, und das Neue ist nach zwei Jahren wie das Alte — nur neuer.

**Alles auf einmal.** Das Vorhaben wird zu groß, verliert Rückhalt und wird abgebrochen. Danach ist die Lage schlechter als vorher, weil zwei halbfertige Systeme laufen.

## Der dritte Fehler, der seltener genannt wird

**Kein Ende definieren.** Wenn niemand sagt, wann abgeschaltet wird, läuft der Parallelbetrieb dauerhaft. Er kostet — und niemand sieht es, weil die Kosten verteilt anfallen.
