# 2-4 · Trainer-Ergänzungsmaterial: Domain Events

## Kernidee für den Trainer

Diese Einheit löst auf, was 2-3 offen gelassen hat: Wenn Aggregate klein sind, muss zwischen ihnen etwas fließen.

Der Kern in einem Satz:

> **Ein Ereignis berichtet, ein Command fordert.**

Und der Punkt, der im Alltag am meisten trägt:

> **Der Sender kennt seine Empfänger nicht.**

## Einstieg

**Die Formulierungsprobe.** Vier Sätze vorlesen, die Gruppe soll sortieren:

| Satz | Was ist es |
|---|---|
| „Rechnung erstellen" | Command |
| „Vorgang wurde abgeschlossen" | Event |
| „Fahrzeug zurücknehmen" | Command |
| „Kaution wurde freigegeben" | Event |

Das Kriterium fällt sofort auf: **Vergangenheitsform gegen Aufforderung.**

**Der Anschluss, der wichtiger ist als die Grammatik:**

| | Command | Event |
|---|---|---|
| Kann abgelehnt werden | ja | **nein** |
| Adressiert | einen bestimmten Empfänger | niemanden |
| Ist verhandelbar | ja | nein — es ist geschehen |

## Fachlich, nicht technisch

Der häufigste Fehler bei der ersten Anwendung:

| Kein Domain Event | Ein Domain Event |
|---|---|
| „Datensatz gespeichert" | „Vorgang abgeschlossen" |
| „Feld geändert" | „Schaden festgestellt" |
| „Nachricht empfangen" | „Buchung eingegangen" |

**Der Prüfstein:**

> Würde ein Fachvertreter diesen Satz sagen?

## Der Sender kennt die Empfänger nicht

Der Punkt mit dem größten praktischen Wert — und er ist derselbe wie bei den Bounded Contexts von gestern.

> Ein Aggregate meldet, dass etwas geschehen ist. Wer es braucht, hört zu.

**Trainerfrage:**

> „Was passiert, wenn ein vierter Empfänger dazukommt?"

Bei einem Ereignis: nichts am Sender. Bei einem direkten Aufruf: eine Änderung.

**Das ist die Verbindung zu Tag 1.** Wer seine Empfänger kennt, hängt von ihnen ab — bei Kontexten wie bei Aggregaten.

## Konsistenz über Grenzen

Hier schließt sich der Bogen zu 2-3:

| | |
|---|---|
| Innerhalb eines Aggregates | Regel gilt **sofort** |
| Zwischen Aggregaten | Regel wird **nachgezogen** — über ein Ereignis |

**Das bedeutet:** Zwischen den Aggregaten ist die Welt kurzzeitig widersprüchlich.

**Die Frage an den Fachbereich, die das entscheidet:**

> „Was passiert, wenn das für fünf Minuten nicht zusammenpasst?"

Meist: nichts. Genau deshalb funktioniert der Ansatz.

## Die drei häufigen Fehler

**Ereignisse als Aufforderung.** „Rechnung erstellen" ist ein Command. Wer so formuliert, hat einen verkleideten Aufruf gebaut.

**Zu viele Ereignisse.** Jede Zustandsänderung zu melden erzeugt Lärm. Gemeldet wird, was fachlich bedeutsam ist — nicht, was sich technisch ändert.

**Der Sender wartet auf Antwort.** Dann ist es kein Ereignis. Ein Ereignis ist eine Mitteilung ohne Erwartung.

## Ereignisse als Gesprächsmittel

Ein Punkt, der die Brücke zu 2-5 schlägt:

Fachleute erzählen von selbst in Ereignissen. „Dann kommt das Fahrzeug zurück, dann wird es geprüft, dann geht die Rechnung raus."

Deshalb eignen sich Ereignisse zur Modellerhebung — und deshalb beginnt Event Storming damit.

## Was das kostet — nicht auslassen

**Der Ablauf ist nicht mehr an einer Stelle ablesbar.** Wer wann worauf reagiert, steht verteilt. Das gehört dokumentiert, sonst versteht in zwei Jahren niemand mehr, was ein Ereignis auslöst.

**Reihenfolge und Zeitpunkt sind nicht garantiert.** Ereignisse kommen an, aber nicht notwendig sofort und nicht notwendig in der Reihenfolge des Sendens.

**Fehlerbehandlung wird schwieriger.** Wenn ein Empfänger scheitert, weiß der Sender nichts davon.

**Trainerfrage:**

> „Wer merkt, wenn ein Ereignis nicht verarbeitet wurde?"

## Die Übung

Erfahrungsgemäß:

- Die Command/Event-Unterscheidung geht schnell, wenn die Formulierungsprobe saß.
- **Die technischen Ereignisse werden übersehen.** „Status geändert" wirkt zunächst wie ein Ereignis. Gezielt nachfragen: Würde das ein Fachvertreter sagen?
- **Die Reihenfolge wird vorausgesetzt.** Wenn jemand einen Ablauf baut, der auf Reihenfolge angewiesen ist, ist das ein guter Diskussionspunkt.

## Zum Umgang mit gemischten Gruppen

Diese Einheit funktioniert bei PO und Management sehr gut — Ereignisse sind die natürliche Erzählform von Fachprozessen.

**Zurückstellen:**

| Frage | Antwort |
|---|---|
| „Wie wird das übertragen?" | Umsetzungsdetail |
| „Was ist Event Sourcing?" | Etwas anderes — Ereignisse als Speicherform. Kurz abgrenzen, nicht vertiefen |
| „Brauchen wir dafür einen Message Broker?" | Nein, nicht zwingend |

**Event Sourcing kurz abgrenzen**, falls es kommt: Domain Events **melden**, Event Sourcing **speichert** den Zustand als Folge von Ereignissen. Zwei Dinge, die oft verwechselt werden.

## Typische Fragen

**„Was, wenn die Reihenfolge doch wichtig ist?"**
Dann gehört das ausdrücklich sichergestellt — und ist ein Hinweis darauf, dass die beiden vielleicht ins selbe Aggregate gehören.

**„Wie viele Ereignisse sind zu viele?"**
Wenn niemand mehr sagen kann, was ein Vorgang auslöst.

**„Kann ein Ereignis rückgängig gemacht werden?"**
Nein. Was geschehen ist, bleibt geschehen. Es kann durch ein neues Ereignis richtiggestellt werden — „Rücknahme storniert" statt Löschung.

## Zeitgerüst

| Teil | Minuten |
|---|---|
| Formulierungsprobe, Command gegen Event | 10 |
| Fallbeispiel lesen lassen | 10 |
| Sender kennt Empfänger nicht, Konsistenz | 10 |
| Übung | 12 |
| Auswertung, was es kostet | 8 |

## Übergang

> „Ereignisse sind das, was Fachleute von selbst erzählen. Genau darauf baut eine Methode auf, mit der man eine ganze Domäne in einem Vormittag erheben kann."
