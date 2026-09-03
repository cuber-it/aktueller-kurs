# 1-1 · Trainer-Ergänzungsmaterial: Einführung und Abgrenzung

## Kernidee für den Trainer

Diese Einheit hat zwei Aufgaben, und die zweite ist die wichtigere:

1. Klären, was DDD ist.
2. **Klären, was es nicht ist** — und wann es sich nicht lohnt.

Teilnehmer kommen mit sehr unterschiedlichen Vorstellungen. Manche halten DDD für eine Architektur, manche für Microservices, manche für eine Modellierungsnotation. Wer diese Erwartungen nicht früh geradezieht, diskutiert zwei Tage gegen ein Missverständnis.

## Einstieg

**Empfohlener Auftakt — die Sammelfrage.** Bevor irgendetwas erklärt wird:

> „Was verbinden Sie mit Domain-Driven Design? Ein Stichwort genügt."

Die Antworten anschreiben und stehen lassen. Am Ende der Einheit darauf zurückkommen: Was davon stimmt, was ist etwas anderes.

Erfahrungsgemäß kommen: Microservices, Aggregate, Event Sourcing, „viel Theorie", „das Buch von Evans", Hexagonale Architektur.

**Der zweite Teil der Sammelfrage** — und der eigentlich wertvolle:

> „Nennen Sie ein aktuelles Ärgernis in Ihrem eigenen Code."

Diese Antworten mitschreiben und über beide Tage aufheben. Sie sind der Praxisbezug, den man mit fremden Fallbeispielen nicht herstellen kann. Bei drei bis fünf Teilnehmern tragen drei bis fünf Fälle den ganzen Kurs.

## Problemraum und Lösungsraum

Die Unterscheidung wirkt zunächst akademisch und wird an Tag 1 dreimal gebraucht — bei Subdomains, bei Bounded Contexts und bei ihrer Abgrenzung voneinander. Deshalb hier sauber einführen.

| | Problemraum | Lösungsraum |
|---|---|---|
| Beschreibt | was das Unternehmen tut | wie die Software geschnitten ist |
| Bestimmt durch | das Geschäft | den Entwurf |
| Ändert sich | mit dem Geschäftsmodell | mit dem Entwurf |
| Einheit | Subdomain | Bounded Context |

**Bild, das trägt:** Der Problemraum ist die Landschaft, der Lösungsraum die Landkarte. Eine Landkarte kann gut oder schlecht sein; die Landschaft ist, wie sie ist.

## Was DDD nicht ist

Diese Liste ausdrücklich vorlesen. Sie erspart Diskussionen.

| Verwechslung | Klarstellung |
|---|---|
| Microservices | DDD sagt nichts über Verteilung. Bounded Contexts können in einem Monolithen liegen |
| Eine Architektur | Hexagonal, Onion, Schichten — alle vereinbar, keine vorgeschrieben |
| Ein Framework | Es gibt Bibliotheken, aber DDD ist keine |
| Event Sourcing | Eine mögliche Umsetzung, keine Voraussetzung |
| Eine Notation | Es gibt keine DDD-Diagrammsprache |
| Objektorientierung | Hilfreich, aber nicht zwingend |

**Trainerfrage dazu:**

> „Kann man DDD in einem Monolithen betreiben?"

Antwort: ja, und historisch war es der Normalfall. Das Buch von 2003 kennt keine Microservices.

## Wann es sich lohnt — und wann nicht

Der ehrliche Teil der Einführung. Wer ihn auslässt, verkauft ein Allheilmittel.

**Lohnt:**

- Fachliche Komplexität, die über Datenverwaltung hinausgeht
- Langlebige Systeme mit fortlaufender Änderung
- Verstreutes Fachwissen, teure Missverständnisse
- Mehrere Teams am selben Gegenstand

**Lohnt nicht:**

- Einfache Datenverwaltung ohne Regeln
- Kurzlebige Anwendungen
- Technisch dominierte Probleme
- Ein Team, ein überschaubarer Gegenstand

**Trainerfrage:**

> „Wo würden Sie in Ihrem Haus **kein** DDD machen?"

Wer diese Frage beantworten kann, hat die Einführung verstanden.

## Der Preis

Ausdrücklich nennen:

- Höherer Abstimmungsaufwand mit dem Fachbereich
- Längere Anlaufzeit, bis Struktur trägt
- Mehr Klassen, mehr Grenzen, mehr Übersetzung
- Der Nutzen zeigt sich erst bei fortlaufender Änderung

Teilnehmer, die den Preis kennen, argumentieren im eigenen Haus überzeugender als solche, die nur die Vorteile gehört haben.

## Typische Fragen und Antworten

**„Brauchen wir dafür den Fachbereich im Raum?"**
Ja. Ohne Zugang zu Fachwissen ist DDD nicht durchführbar. Wo der Fachbereich nicht verfügbar ist, ist das die erste zu lösende Aufgabe.

**„Wir haben schon ein Datenmodell — reicht das nicht?"**
Ein Datenmodell beschreibt Speicherung. Die Frage kommt in 1-2 wieder und wird dort beantwortet.

**„Ist das nicht nur objektorientierte Analyse mit neuen Wörtern?"**
Die Überschneidung ist real. Neu ist die Betonung der Sprache, der Grenzen und der strategischen Einordnung.

## Zeitgerüst

| Teil | Minuten |
|---|---|
| Sammelfrage und eigene Ärgernisse | 15 |
| Domäne, Problem-/Lösungsraum | 10 |
| Was DDD nicht ist | 10 |
| Wann es sich lohnt, der Preis | 10 |
| Rückblick auf die Sammelfrage | 5 |

## Übergang zur nächsten Einheit

> „Wir haben gesagt, die Fachlichkeit bestimmt die Struktur. Jetzt sehen wir uns an, was ein Modell eigentlich ist — und warum ein Datenbankschema keines ist."
