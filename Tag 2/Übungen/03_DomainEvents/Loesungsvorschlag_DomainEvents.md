# Lösungsvorschlag · Meldung oder Auftrag?

---

## 1 · Die zwanzig Sätze

| # | Satz | Einordnung |
|---|---|---|
| 1 | Fahrzeug zurücknehmen | **Auftrag** |
| 2 | Vorgang wurde abgeschlossen | **Meldung** |
| 3 | Rechnung erstellen | **Auftrag** |
| 4 | Schaden wurde festgestellt | **Meldung** |
| 5 | Kaution freigeben | **Auftrag** |
| 6 | Reservierung ist eingegangen | **Meldung** |
| 7 | Datensatz gespeichert | **weder noch** |
| 8 | Fahrzeug wurde ausgegeben | **Meldung** |
| 9 | Prüftermin fortschreiben | **Auftrag** |
| 10 | Mietvertrag wurde verlängert | **Meldung** |
| 11 | Status auf 4 gesetzt | **weder noch** |
| 12 | Kunde hat storniert | **Meldung** |
| 13 | Punkte gutschreiben | **Auftrag** |
| 14 | Fahrerlaubnis wurde geprüft | **Meldung** |
| 15 | Fahrzeug ist ausgemustert worden | **Meldung** |
| 16 | Nachricht empfangen | **weder noch** |
| 17 | Zahlung ist eingegangen | **Meldung** |
| 18 | Mahnung versenden | **Auftrag** |
| 19 | Vorgang wurde storniert | **Meldung** |
| 20 | Feld geändert | **weder noch** |

**Neun Meldungen, sieben Aufträge, vier technische Sätze.**

Die vier technischen Sätze sind der interessanteste Teil: Sie klingen wie Meldungen (Vergangenheitsform), sagen aber nichts über die Fachwelt. „Status auf 4 gesetzt" beschreibt eine Speicheroperation, kein Geschehen.

---

## 2 · Die uneindeutigen Fälle

### Satz 14 · „Fahrerlaubnis wurde geprüft"

Klingt nach Meldung — ist aber unvollständig.

**Was fehlt:** das Ergebnis. „Geprüft" sagt nicht, ob sie gültig war.

**Die bessere Formulierung:** „Fahrerlaubnis wurde als gültig bestätigt" oder „Fahrerlaubnis wurde abgelehnt". Zwei Meldungen statt einer.

**Der Merkpunkt:** Eine Meldung, die nur sagt, dass etwas geprüft wurde, zwingt jeden Empfänger, das Ergebnis nachzuschlagen. Dasselbe Problem wie bei einem Merkmal, das nur „geprüft ja/nein“ festhält.

### Satz 6 · „Reservierung ist eingegangen"

Meldung — aber aus wessen Sicht?

Wenn die Reservierung selbst der Vorgang ist, ist es keine Meldung an andere, sondern der Vorgang selbst. Wenn sie von außen kommt (Partnernetzwerk), ist es eine Meldung.

**Der Merkpunkt:** Ob etwas eine Meldung ist, hängt davon ab, wer meldet.

### Satz 15 · „Fahrzeug ist ausgemustert worden"

Meldung, aber in der Passivform mit Hilfsverb. Sprachlich schwerfällig.

**Besser:** „Fahrzeug wurde ausgemustert". Die Form ist wichtiger, als sie scheint — sie hält die Meldungen einheitlich und lesbar.

---

## 3 · Aufträge zu Meldungen umformulieren

| Auftrag | Als Meldung |
|---|---|
| Fahrzeug zurücknehmen | Fahrzeug wurde zurückgenommen |
| Rechnung erstellen | **Rechnung wurde erstellt** |
| Kaution freigeben | Kaution wurde freigegeben |
| Prüftermin fortschreiben | **Prüftermin wurde fortgeschrieben** |
| Punkte gutschreiben | **Punkte wurden gutgeschrieben** |
| Mahnung versenden | Mahnung wurde versendet |

**Was dabei auffällt:**

Die hervorgehobenen drei sind Meldungen **des Empfängers**, nicht des Auslösers.

„Rechnung erstellen" ist ein Auftrag an die Fakturierung. „Rechnung wurde erstellt" ist etwas, das die Fakturierung **selbst** meldet — nachdem sie auf „Vorgang wurde abgeschlossen" reagiert hat.

**Das ist der Kern der Entkopplung:**

| Falsch | Richtig |
|---|---|
| Anmietung sagt: „Fakturierung, erstelle eine Rechnung" | Anmietung sagt: „Vorgang abgeschlossen". Fakturierung hört zu und erstellt |

Wer einen Auftrag in eine Meldung umformuliert und dabei merkt, dass der Sender ein anderer wäre, hat die Kopplung gefunden.

---

## 4 · Die Meldung

> **Mietvorgang wurde abgeschlossen**

Vergangenheitsform, fachlich, ohne Empfänger im Kopf.

**Verworfene Formulierungen:**

| Vorschlag | Warum nicht |
|---|---|
| „Vorgang beendet" | „beendet" ist mehrdeutig — abgebrochen oder abgeschlossen? |
| „Abschluss durchgeführt" | technisch, keine Fachsprache |
| „Rechnung kann erstellt werden" | Empfänger im Kopf |
| „Vorgang abgeschlossen und Fahrzeug zurück" | zwei Meldungen in einer |

---

## 5 · Die Angaben je Empfänger

| Empfänger | Braucht |
|---|---|
| Fakturierung | Vorgangsnummer, Mieter, Rahmenvertrag, Zeitraum, Zusatzleistungen, Kaution, gefahrene Kilometer |
| Flotte | Fahrzeug, Rückgabestation, Kilometerstand |
| Partnernetzwerk | Vorgangsnummer, Partnerbuchungsnummer, Abschlusszeitpunkt |
| Kundenbindungsprogramm | Mieter, Umsatz |
| Werkstatt | Fahrzeug, Kilometerstand |
| Auswertung | Station, Kategorie, Zeitraum, Umsatz |
| Umweltbilanz | Fahrzeug, gefahrene Kilometer |
| Kundenbefragung | Mieter, Station, Abschlusszeitpunkt |

**Die Vereinigungsmenge:** Vorgangsnummer, Mieter, Fahrzeug, Station, Zeitraum, Kilometerstand, gefahrene Kilometer, Umsatz, Zusatzleistungen, Kaution, Rahmenvertrag, Partnerbuchungsnummer, Abschlusszeitpunkt.

**Dreizehn Angaben.** Das ist viel für eine Meldung.

**Zwei Wege:**

| Weg | Vorteil | Nachteil |
|---|---|---|
| **Alles mitschicken** | Empfänger brauchen nichts nachzuschlagen | Meldung wird groß; Änderungen an den Angaben betreffen alle |
| **Nur Kennungen mitschicken** | schlanke Meldung | Empfänger müssen nachfragen; bei nachträglicher Änderung sehen sie den neuen Stand |

**Der Vorschlag:** Ein Mittelweg. Die Meldung enthält die Kennungen (Vorgang, Fahrzeug, Mieter, Station) und die Angaben, die zum Zeitpunkt des Abschlusses gelten und sich danach nicht mehr ändern dürfen — Zeitraum, Kilometerstand, gefahrene Kilometer, Abschlusszeitpunkt.

**Begründung:** Was ein Beleg ist, gehört in die Meldung; was nachschlagbar bleibt, nicht. Dieselbe Überlegung wie bei der Anschrift auf der Rechnung in Übung 01.

---

## 6 · Eine Meldung oder mehrere?

**Eine reicht nicht.**

Drei der neun Empfänger reagieren nicht auf den Abschluss, sondern auf etwas anderes:

| Empfänger | Reagiert eigentlich auf |
|---|---|
| Flotte (Standort) | **„Fahrzeug wurde zurückgenommen"** — das geschieht vor dem Abschluss |
| Werkstatt (Prüftermin) | **„Fahrzeug wurde zurückgenommen"** — der Kilometerstand steht dann fest |
| Umweltbilanz | **„Fahrzeug wurde zurückgenommen"** — dito |

**Der Unterschied ist fachlich bedeutsam:** Ein Vorgang bleibt offen, wenn ein Schaden ungeklärt ist — das Fahrzeug steht aber schon auf dem Hof. Wer den Standort erst beim Abschluss fortschreibt, hat ihn tagelang falsch.

**Zwei Meldungen:**

| Meldung | Empfänger |
|---|---|
| **Fahrzeug wurde zurückgenommen** | Flotte, Werkstatt, Umweltbilanz |
| **Mietvorgang wurde abgeschlossen** | Fakturierung, Partnernetzwerk, Kundenbindung, Auswertung, Kundenbefragung |

**Das ist ein Nebenertrag der Übung:** Die Aufteilung deckt einen Fehler auf, den es schon vorher gab — der Standort wurde zu spät fortgeschrieben.

---

## 7 · Die Dringlichkeit

| Empfänger | Einordnung | Beleg |
|---|---|---|
| Fakturierung | **zwingend**, nicht sofort | „einen Tag später ist kein Problem, gar nicht schon" |
| Flotte | **zwingend**, zeitnah | „bevor jemand das Fahrzeug wieder vermietet — Minuten, nicht Stunden" |
| Partnernetzwerk | **zwingend**, binnen 48 Stunden | „nach 48 Stunden fragt er nach" |
| Kundenbindung | zeitnah | Punkte sollten beim nächsten Besuch da sein |
| Werkstatt | zeitnah | Prüftermin ist eine Planungsgröße |
| Auswertung | nachrangig | Kennzahlen werden ohnehin täglich betrachtet |
| Umweltbilanz | nachrangig | Jahresauswertung |
| Kundenbefragung | nachrangig | „nach drei Tagen, sofort oder abends egal" |

**Drei zwingend, zwei zeitnah, drei nachrangig.**

---

## 8 · Sicherstellung für die zwingenden Empfänger

**Der Kern:** „Zwingend" heißt nicht „sofort", sondern „muss ankommen".

| Maßnahme | Wirkung |
|---|---|
| Meldungen werden aufbewahrt, bis sie verarbeitet sind | ein Empfänger, der ausfällt, holt nach |
| Je Empfänger wird festgehalten, bis wohin er verarbeitet hat | der Stand ist ablesbar |
| Für zwingende Empfänger gibt es eine Frist | Fakturierung 24 Stunden, Flotte 15 Minuten, Partnernetzwerk 24 Stunden |
| Bei Fristüberschreitung wird gemeldet | an die Betriebsüberwachung |

**Wichtig:** Der Sender wartet auf niemanden. Er meldet und ist fertig. Die Sicherstellung liegt beim Aufbewahren und Überwachen, nicht beim Abschluss.

---

## 9 · Wie ein ausgebliebener Aufruf auffällt

**Der Vorfall entstand, weil ein Aufruf nie stattfand.** Der Wiederholungslauf griff nicht, weil es keinen Fehler gab, den er hätte wiederholen können.

**Im Vorschlag ist das anders:**

Die Meldung wird beim Abschluss erzeugt und aufbewahrt — unabhängig davon, ob ein Empfänger sie abholt. Für jeden Empfänger ist festgehalten, bis wohin er verarbeitet hat.

**Damit ist die Frage beantwortbar:** „Welche Meldungen hat das Partnernetzwerk noch nicht verarbeitet?"

**Bei den 340 Abschlüssen** hätte die Überwachung nach 24 Stunden gemeldet, dass 340 Meldungen unverarbeitet sind. Statt drei Wochen Klärung wäre es ein Tag gewesen.

**Der entscheidende Unterschied:** Die Meldung existiert, auch wenn niemand sie abholt. Ein Aufruf, der nicht stattfindet, hinterlässt nichts.

---

## 10 · Der neue Interessent

**Die Buchhaltung will bei Abschluss eine Rückstellung bilden.**

**Was geändert werden muss:** nichts an der Anmietung.

Die Buchhaltung hört auf „Mietvorgang wurde abgeschlossen" und bildet ihre Rückstellung. Sie meldet sich als Empfänger an; der Sender erfährt davon nichts.

**Falls sie eine Angabe braucht, die nicht in der Meldung steht** — etwa den Rahmenvertrag —, gibt es zwei Wege: Sie schlägt ihn nach, oder die Meldung wird erweitert. Das Zweite betrifft alle Empfänger und sollte die Ausnahme sein.

**Zum Vergleich, bisher:** ein zehnter Aufruf in der Abschlussstelle, eine Änderung an einer Klasse, die mit Rückstellungen nichts zu tun hat, und ein zehnter Kandidat für Zeitüberschreitungen.

---

## 11 · Der Preis

**Erstens: Der Ablauf ist nicht mehr ablesbar.**
Bisher stand in der Abschlussstelle, was geschieht — neun Aufrufe untereinander. Jetzt steht dort eine Meldung, und wer darauf reagiert, ist verteilt. Das gehört dokumentiert, sonst versteht es in zwei Jahren niemand.

**Zweitens: Reihenfolge und Zeitpunkt sind nicht garantiert.**
Die Rechnung kann vor der Standortfortschreibung erstellt werden oder danach. Wo eine Reihenfolge nötig ist, muss sie ausdrücklich hergestellt werden.

**Drittens: Die Meldung muss aufbewahrt werden.**
Bei 1.400 Abschlüssen täglich und acht Empfängern entsteht ein Bestand, der verwaltet und irgendwann gelöscht werden muss.

**Viertens: Die Überwachung ist neue Arbeit.**
„Welche Meldungen sind unverarbeitet" muss gebaut, betrieben und beobachtet werden. Ohne sie ist der Vorschlag nicht besser als vorher — nur anders.

**Fünftens: Fehler beim Empfänger sind unsichtbarer.**
Wenn die Kundenbefragung eine Meldung falsch verarbeitet, merkt es niemand. Bei einem direkten Aufruf hätte man wenigstens eine Fehlermeldung gesehen.

---

## 12 · Warum die Fakturierung zwingend ist

**Weil „zwingend" und „sofort" zwei verschiedene Dinge sind.**

| | Bedeutung |
|---|---|
| **zwingend** | Muss ankommen. Wenn nicht, entsteht Schaden. |
| **sofort** | Muss unverzüglich geschehen. |

Die Fakturierung ist **zwingend, aber nicht sofort**: Eine Rechnung einen Tag später ist unproblematisch, eine ausbleibende Rechnung bedeutet, dass Geld nicht eingefordert wird.

Die Flotte ist **zwingend und zeitnah**: Der Standort muss stimmen, bevor jemand das Fahrzeug wieder vermietet.

**Die Kundenbefragung ist weder noch:** Wenn sie ausfällt, geht keine Einladung raus. Ärgerlich, aber kein Schaden.

**Warum die Unterscheidung wichtig ist:** Sie bestimmt, was überwacht werden muss. Zwingende Empfänger brauchen eine Frist und eine Meldung bei Überschreitung. Nachrangige nicht.

---

## Diskussionsanschluss

Der Vorschlag teilt eine Meldung in zwei — „Fahrzeug zurückgenommen" und „Vorgang abgeschlossen". Dabei fiel auf, dass der Standort bisher zu spät fortgeschrieben wurde. Wie viele solcher Fehler stecken vermutlich noch in den anderen sieben Aufrufen?
