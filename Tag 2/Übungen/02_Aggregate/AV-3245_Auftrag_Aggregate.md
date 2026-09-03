# AV-3245 · Konsistenzgrenzen an der tatsächlichen Regel ausrichten

**Typ:** Story
**Komponente:** Anmietung
**Priorität:** Kritisch
**Verweist auf:** AV-3231 (Frankfurt-Flughafen, Ausgaben blockiert, 11 Kunden abgewandert)

---

## Story

**Als** Stationsmitarbeiter
**möchte ich** ein Fahrzeug ausgeben können, während meine Kollegin ein anderes zurücknimmt,
**damit** an starken Tagen nicht vier Leute aufeinander warten, obwohl sie an verschiedenen Vorgängen arbeiten.

---

## Description

Die Station wird als eine Einheit geführt. Bei jeder Änderung wird sie als Ganzes behandelt — Fahrzeuge, laufende Vorgänge, Reservierungen, Rückläufer, Öffnungszeiten.

**Umfang bei einer mittleren Station:**

| Bestandteil | Anzahl |
|---|---|
| Fahrzeuge | 40–90 |
| Laufende Mietvorgänge | 30–70 |
| Reservierungen (30 Tage) | 100–300 |
| Rückläufer in Aufbereitung | 5–15 |
| Öffnungszeiten und Sonderregelungen | 10–20 |

**Vorfall AV-3231:** An einem Freitagnachmittag griffen vier Tresenmitarbeiter, ein Nachtlauf, die Verfügbarkeitsanzeige und die Rückgabeerfassung gleichzeitig zu. Jeder Zugriff behandelte die ganze Station als Einheit.

| Kennzahl | Wert |
|---|---|
| Dauer einer Ausgabe (normal) | 2 Sekunden |
| Dauer an diesem Nachmittag | 90 Sekunden |
| Abgewanderte Kunden | 11 |

**Kernbefund:** Die Regel, die die Klammer rechtfertigt, lautet „ein Fahrzeug kann nicht gleichzeitig ausgegeben und reserviert sein". Sie betrifft **ein** Fahrzeug — nicht neunzig.

**Nicht Gegenstand:** Rechenleistung, Zeitüberschreitungen, Warteschlangen. Diese Wege wurden versucht und lösen die Ursache nicht.

## Randbedingungen

- 140 Stationen, größte mit 90 Fahrzeugen, kleinste mit 12
- An starken Tagen bis zu sechs gleichzeitige Zugriffe je Station
- Die Verfügbarkeitsanzeige der Webseite fragt im Minutentakt ab
- Ein Nachtlauf bestätigt Reservierungen
- Öffnungszeiten werden zentral gepflegt, unabhängig vom Tagesgeschäft

## Akzeptanzkriterien

- **AK1** – Für jede vorgeschlagene Klammer ist die Regel benannt, die sie rechtfertigt. Ohne Regel keine Klammer.
- **AK2** – Für jede Regel ist festgestellt, ob sie **sofort** gelten muss oder ob eine kurze Abweichung fachlich vertretbar ist.
- **AK3** – Zwei Vorgänge, die verschiedene Fahrzeuge betreffen, behindern sich nicht.
- **AK4** – Eine Änderung an den Öffnungszeiten behindert das Tagesgeschäft nicht.
- **AK5** – Die Verfügbarkeitsanzeige behindert Ausgaben nicht.
- **AK6** – Für jeden Bestandteil der heutigen Station ist angegeben, in welche Klammer er gehört und warum.
- **AK7** – Wo Regeln über Klammergrenzen hinweg gelten, ist beschrieben, wie sie nachgezogen werden und welche Abweichung dabei entstehen kann.
- **AK8** – Für die Regel „nicht gleichzeitig ausgegeben und reserviert" ist beschrieben, wie sie eingehalten wird, wenn Fahrzeug und Reservierung in getrennten Klammern liegen.

## Hinweise

Mehr Rechenleistung erfüllt AK3 nicht. Der Engpass entsteht durch die Größe der Einheit, nicht durch die Geschwindigkeit.

AK2 ist die eigentliche Entwurfsfrage. Sie ist **fachlich** zu beantworten, nicht technisch: Was passiert, wenn eine Regel für fünf Minuten nicht gilt?

AK8 ist der schwierigste Punkt. Wer die Klammer verkleinert, muss sagen, wie die ursprüngliche Regel weiterhin eingehalten wird.

---

## Für den Kurs

Dieses Ticket nennt kein Konzept. Arbeiten Sie entlang der Frage:

**Was muss im selben Moment stimmen?**

---
---

# Addendum · Woran man eine Konsistenzgrenze erkennt

## Die eine Frage

> **Muss es im selben Moment stimmen?**

| Antwort | Konsequenz |
|---|---|
| Ja, sofort und immer | dieselbe Klammer |
| Nein, darf kurz auseinanderlaufen | getrennte Klammern, Nachziehen |

**Die Frage gehört dem Fachbereich gestellt**, nicht der Entwicklung:

> „Was passiert, wenn das für fünf Minuten nicht zusammenpasst?"

Erfahrungsgemäß lautet die Antwort öfter „nichts", als Entwickler erwarten.

## Ohne Regel keine Klammer

Der Satz, der die meisten Fehlschnitte verhindert:

> Wenn Sie keine Regel benennen können, die zwischen zwei Dingen sofort gelten muss, gehören sie nicht in dieselbe Klammer.

**Was keine Begründung ist:**

| Scheinbegründung | Warum sie nicht trägt |
|---|---|
| „Das gehört doch zusammen" | Zugehörigkeit ist keine Regel |
| „Das wird immer gemeinsam gebraucht" | gemeinsam **lesen** ist etwas anderes als gemeinsam **gültig sein** |
| „Das liegt in derselben Tabelle" | Ablage ist keine Modellfrage |
| „Sonst brauchen wir zwei Zugriffe" | Bequemlichkeit ist kein Kriterium |

## Signale für eine zu große Klammer

| Signal | Konkret |
|---|---|
| Vorgänge warten aufeinander, die nichts miteinander zu tun haben | vier Tresen, ein Wartezustand |
| Für eine kleine Änderung wird viel geladen | 90 Fahrzeuge für einen Vorgang |
| Große Exemplare sind schlechter dran als kleine | der Engpass wächst mit der Menge |
| Etwas Selten-Geändertes blockiert Häufig-Geändertes | Öffnungszeiten gegen Tagesgeschäft |
| Die Klammer heißt wie eine Organisationseinheit | Station, Abteilung, Filiale — Verdacht auf Zuständigkeit statt Regel |

## Signale für eine zu kleine Klammer

| Signal | Konkret |
|---|---|
| Eine Regel wird regelmäßig verletzt | sie kann nicht durchgesetzt werden |
| Ein Vorgang ändert mehrere Klammern gleichzeitig | falsch geschnitten oder ein Ereignis fehlt |
| Widersprüchliche Zustände fallen im Betrieb auf | die Abweichung ist nicht vertretbar |

## Wenn eine Regel über Klammergrenzen geht

Zwei Wege:

| Weg | Wann |
|---|---|
| **Nachziehen über ein Ereignis** | wenn eine kurze Abweichung vertretbar ist |
| **Prüfen beim Zugriff** | wenn die Regel sofort gelten muss, aber nicht dieselbe Klammer rechtfertigt |

Der zweite Weg wird oft übersehen. Eine Prüfung „ist dieses Fahrzeug reserviert" kann stattfinden, ohne dass Fahrzeug und Reservierung in derselben Klammer liegen — sie ist dann nicht absolut sicher, aber praktisch ausreichend, wenn der Zeitraum klein ist.

## Die Faustregel

> **Eine Änderung, eine Klammer.**

Wer in einem Vorgang mehrere Klammern ändert, hat entweder falsch geschnitten oder braucht ein Ereignis.
