# 1-4 · Trainer-Ergänzungsmaterial: Glossare je Kontext

## Kernidee für den Trainer

Diese Einheit ist die praktischste des Vormittags — und die, bei der Teilnehmer am ehesten sagen „das machen wir schon". Meistens machen sie es, aber falsch.

Der Kernsatz:

> **Ein Glossar ist nur innerhalb eines Bounded Context möglich.**

Über Kontextgrenzen hinweg gibt es keine eindeutige Definition. Wer trotzdem eines schreibt, landet zwangsläufig bei „je nach Kontext" — und damit bei einem Papier, das die Mehrdeutigkeit dokumentiert, statt sie auszuschließen.

## Einstieg über das Scheitern

Nicht mit „so schreibt man ein Glossar" beginnen, sondern mit dem Fallbeispiel: 84 Einträge, 31 Seiten, elf Zugriffe in acht Monaten.

**Die Frage vor dem Lesen:**

> „Wer von Ihnen hat ein Glossar im Unternehmen? Wer schlägt darin nach?"

Die Diskrepanz zwischen den beiden Handzeichen ist der Einstieg.

## Die Diagnose am Beispiel

Der zentrale Eintrag aus dem Fallbeispiel:

> **Kunde:** Natürliche oder juristische Person, die in einer Geschäftsbeziehung zum Unternehmen steht. Je nach Kontext kann dies der Vertragspartner, der Fahrzeugnutzer oder der Rechnungsempfänger sein.

**Die Frage dazu:**

> „Wem hilft dieser Eintrag?"

Antwort, die kommen muss: niemandem. Wer im Bereich arbeitet, weiß bereits, was er meint. Wer von außen liest, erfährt nur, dass es kompliziert ist.

**Der Anschluss:** Das ist kein Formulierungsproblem. Der Eintrag konnte nicht besser werden, weil er vier Kontexte abdecken sollte.

## Die sieben Merkmale eines unbrauchbaren Glossars

Diese Liste als Prüfraster austeilen — Teilnehmer erkennen ihr eigenes darin wieder:

| Merkmal | Warum es scheitert |
|---|---|
| Ein Verzeichnis für alle Bereiche | erzwingt Oberdefinitionen |
| „Je nach Kontext …" | dokumentiert das Problem |
| Alphabetisch sortiert | trennt Zusammengehöriges |
| Als eigenes Dokument abgelegt | niemand geht dorthin, um zu arbeiten |
| Ohne Zuständigkeit | veraltet ab Tag eins |
| Vollständigkeit als Ziel | 84 Einträge, 60 davon schlägt niemand nach |
| Lehrbuchdefinitionen | sagen nichts über dieses Unternehmen |

## Das Auswahlkriterium

Der praktisch wichtigste Punkt und der subjektivste:

> **Würde jemand diesen Eintrag nachschlagen?**

„Kennzeichen: amtliches Kennzeichen eines Fahrzeugs" schlägt niemand nach. Es steht trotzdem in fast jedem Glossar, weil Vollständigkeit als Tugend gilt.

**Einwand, der kommt:** „Das ist subjektiv." Stimmt. Die Alternative ist Vollständigkeit — und die führt zu 84 Einträgen mit elf Zugriffen. Ein subjektives Kriterium, das zu einem benutzten Verzeichnis führt, schlägt ein objektives, das zu einem unbenutzten führt.

## Abgrenzungen sind wertvoller als Definitionen

Der Satz, der im Fallbeispiel drei Wochen Nacharbeit verhindert hätte:

> **Mieter** — nicht zu verwechseln mit dem Rahmenvertragspartner.

**Trainerfrage:**

> „Welcher Eintrag in Ihrem Glossar hätte den letzten Fehler verhindert?"

## Die Übung

Drei Teile: Alteinträge prüfen, zwei Glossare bauen, Grenzen benennen.

**Was erfahrungsgemäß passiert:**

- Die Diagnose der neun Alteinträge geht schnell und macht Freude.
- Beim Bauen entsteht die Versuchung, Begriffe zu ergänzen, die in den Mitschriften nicht vorkommen. Hier eingreifen: nur was tatsächlich gesagt wurde.
- Aufgabe 5 (Kaution in beiden Kontexten) ist der Prüfstein. Viele deuten es als Kollision. Es ist keine — dieselbe Sache, zwei Sichten. Der Prüfstein aus 1-3 greift hier wieder.

**Wenn die Gruppe schnell fertig ist:** Aufgabe 7 vertiefen — die Gliederung. Nach Ablauf, nach Zusammenhang, nach Aggregat? Das ist eine echte Entwurfsfrage.

## Der Ort des Glossars

Elf Zugriffe in acht Monaten sind kein Inhaltsproblem, sondern ein Ortsproblem.

**Empfehlung, die man aussprechen sollte:** ins Repository, neben den Code, als Markdown. Dann liest es, wer ohnehin dort arbeitet — und es wird bei einer Änderung mitgeändert.

**Die stärkste Fassung:** Wenn Klassen und Methoden die Begriffe tragen, ist das Glossar eine Lesehilfe zum Modell statt ein Parallelwerk. Das ist der Zustand, den DDD anstrebt.

## Typische Fragen

**„Wer pflegt das?"**
Je Kontext eine Person. Bei zehn Einträgen ist das nebenbei möglich. Genau deshalb muss es kurz sein.

**„Was ist mit den Begriffen, die keinem Kontext zugeordnet sind?"**
Meistens sind sie historisch oder gehören zu einem Kontext, den niemand benannt hat. Beides ist ein Befund.

**„Brauchen wir dann vier Glossare?"**
Ja. Vier mit je zehn Einträgen sind zusammen kürzer als eines mit 84 — und werden gelesen.

## Zeitgerüst

| Teil | Minuten |
|---|---|
| Einstiegsfrage, Fallbeispiel | 12 |
| Diagnose des Beispieleintrags | 8 |
| Merkmale brauchbar/unbrauchbar | 8 |
| Übung | 15 |
| Auswertung | 10 |

## Übergang

> „Wir haben von vier Kontexten gesprochen, ohne den Begriff sauber eingeführt zu haben. Das holen wir jetzt nach — und stellen fest, dass die Frage ,was gehört hinein' schwerer ist als die Frage ,wo verläuft die Grenze'."
