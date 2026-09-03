# AV-3372 · Empfänger vom Auslöser entkoppeln

**Typ:** Story
**Komponente:** Anmietung
**Priorität:** Hoch
**Verweist auf:** AV-3358 (Störung Befragungsanbieter, 122 fehlende Rückmeldungen, 3 Wochen Klärung)

---

## Story

**Als** Entwicklerin im Anmietungsteam
**möchte ich** einen neuen Interessenten anschließen können, ohne den Abschluss eines Mietvorgangs zu ändern,
**damit** eine Störung bei einem Randbeteiligten nicht dazu führt, dass fachlich zwingende Meldungen ausbleiben.

---

## Description

Der Abschluss eines Mietvorgangs ruft **neun Stellen nacheinander** auf. Jeder neue Interessent wurde als weiterer Aufruf ergänzt.

| Empfänger | Seit | Fachlich zwingend |
|---|---|---|
| Fakturierung | 2019 | **ja** |
| Flotte (Standort) | 2019 | **ja** |
| Kundenbindungsprogramm | 2020 | nein |
| Werkstatt (Prüftermin) | 2021 | nein |
| Auswertung | 2022 | nein |
| Partnernetzwerk | 2023 | **ja**, bei Partnerbuchungen |
| Umweltbilanz | 2024 | nein |
| Kundenbefragung | 2025 | nein |

**Vorfall AV-3358:** Der Anbieter der Kundenbefragung war vier Stunden nicht erreichbar. Die Aufrufe liefen in eine Zeitüberschreitung von 30 Sekunden. Da die Kundenbefragung vor dem Partnernetzwerk stand, wurde dieses nicht mehr erreicht.

| Kennzahl | Wert |
|---|---|
| Betroffene Abschlüsse | 340 |
| Ohne Rückmeldung an das Partnernetzwerk | 340 |
| Nachträglich von Hand nachgemeldet | 218 |
| Nicht mehr auffindbar | 122 |
| Klärungsdauer mit dem Vermittler | 3 Wochen |

**Kernbefund:** Der Abschluss kennt seine Empfänger. Jeder neue Interessent bedeutet eine Änderung an einer Stelle, die mit ihm fachlich nichts zu tun hat.

**Nicht Gegenstand:** Die Auswahl einer Übertragungstechnik. Es geht um die fachliche Entkopplung.

## Randbedingungen

- Neun Empfänger, zwei bis drei davon fachlich zwingend
- Etwa 1.400 Abschlüsse täglich, an Freitagen bis 2.600
- Drei Empfänger sind Fremdsysteme außerhalb des eigenen Betriebs
- Ein Wiederholungslauf für gescheiterte Aufrufe existiert
- Die Reihenfolge wurde bereits einmal umgestellt

## Akzeptanzkriterien

- **AK1** – Der Abschluss eines Mietvorgangs kennt seine Empfänger nicht.
- **AK2** – Ein neuer Interessent kann angeschlossen werden, ohne dass die Anmietung geändert wird.
- **AK3** – Eine Störung bei einem Empfänger wirkt sich nicht auf andere Empfänger aus.
- **AK4** – Eine Störung bei einem Empfänger verzögert den Abschluss nicht.
- **AK5** – Für jeden Empfänger ist festgelegt, ob seine Verarbeitung zwingend, zeitnah oder nachrangig ist.
- **AK6** – Für zwingende Empfänger ist beschrieben, wie sichergestellt wird, dass sie erreicht werden.
- **AK7** – Es ist erkennbar, wenn eine Meldung nicht verarbeitet wurde. Der Fall „Aufruf fand nie statt" muss auffallen.
- **AK8** – Die Meldung ist fachlich formuliert und in der Vergangenheitsform. Sie beschreibt, was geschehen ist, nicht was zu tun ist.
- **AK9** – Für jeden der neun heutigen Empfänger ist angegeben, auf welche Meldung er reagiert. Wo mehrere Empfänger dieselbe Meldung brauchen, ist das benannt.

## Hinweise

Eine kürzere Zeitüberschreitung erfüllt AK4 nicht. Sie verkürzt das Warten, beseitigt es nicht.

Eine geänderte Reihenfolge erfüllt AK3 nicht. Wer hinten steht, fällt weiterhin aus.

AK7 ist der Punkt, an dem der Wiederholungslauf versagte: Er greift bei gescheiterten Aufrufen, nicht bei ausgebliebenen.

AK8 ist keine Formalie. Wer „Rechnung erstellen" meldet, hat den Empfänger im Kopf und damit die Entkopplung verfehlt.

---

## Für den Kurs

Dieses Ticket nennt kein Konzept. Arbeiten Sie entlang der Frage:

**Was ist geschehen — und wen geht es an?**

---
---

# Addendum · Meldung oder Auftrag

## Die eine Unterscheidung

| | Auftrag | Meldung |
|---|---|---|
| Form | „Rechnung erstellen" | „Vorgang wurde abgeschlossen" |
| Zeitform | Aufforderung | Vergangenheit |
| Adressiert | einen bestimmten Empfänger | niemanden |
| Kann abgelehnt werden | **ja** | nein — es ist geschehen |
| Der Sender erwartet | eine Ausführung | nichts |
| Bei neuem Interessenten | Sender ändern | Sender unverändert |

**Der Prüfstein:** Wenn Sie den Satz in die Vergangenheit setzen und er ergibt keinen Sinn, ist es ein Auftrag.

## Fachlich, nicht technisch

| Keine Meldung | Eine Meldung |
|---|---|
| „Datensatz gespeichert" | „Vorgang abgeschlossen" |
| „Feld geändert" | „Schaden festgestellt" |
| „Nachricht empfangen" | „Buchung eingegangen" |
| „Status auf 4 gesetzt" | „Fahrzeug zurückgenommen" |

**Der Prüfstein:** Würde ein Fachvertreter diesen Satz sagen?

## Signale für eine fehlende Entkopplung

| Signal | Konkret |
|---|---|
| Eine Stelle ruft mehrere Empfänger nacheinander auf | die Liste wächst mit jedem Interessenten |
| Die Reihenfolge wurde schon einmal umgestellt | ein Hinweis darauf, dass sie über Schaden entscheidet |
| Eine Störung bei einem Randbeteiligten trifft einen zwingenden | sie hängen an derselben Kette |
| Der Auslöser wird geändert, obwohl sich an ihm nichts ändert | er kennt zu viele |
| Zeitüberschreitungen werden verkürzt | ein Symptom, keine Ursache |

## Was Meldungen nicht lösen

**Reihenfolge und Zeitpunkt.** Meldungen kommen an, aber nicht notwendig sofort und nicht notwendig in der Reihenfolge des Sendens. Wo Reihenfolge nötig ist, muss sie ausdrücklich hergestellt werden.

**Fehlerbehandlung beim Empfänger.** Wenn ein Empfänger scheitert, weiß der Sender nichts davon. Das ist gewollt — aber jemand muss es merken.

**Zwingende Verarbeitung.** Eine Meldung, die niemand verarbeitet, fällt nicht auf. Wo Verarbeitung zwingend ist, braucht es eine Überwachung.

**Die Nachvollziehbarkeit.** Der Ablauf ist nicht mehr an einer Stelle ablesbar. Wer wann worauf reagiert, gehört dokumentiert.
