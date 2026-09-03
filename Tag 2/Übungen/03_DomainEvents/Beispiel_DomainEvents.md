# Beispiel · Meldungen in klein

Ein Geschehen, vier Empfänger, vollständig durchgeführt.

---

## Die Ausgangslage

Eine Arztpraxis. Wenn ein Patient behandelt wurde, müssen mehrere Stellen davon erfahren.

**Bisher:** Die Behandlungserfassung ruft nacheinander auf:

1. Abrechnung — erstellt die Kassenabrechnung
2. Terminverwaltung — schlägt einen Folgetermin vor
3. Labor — beauftragt angeordnete Untersuchungen
4. Rückrufliste — vermerkt Patienten für die Nachkontrolle

---

## Schritt 1 · Ist es geschehen oder soll es geschehen?

Die vier Aufrufe als Sätze:

| Aufruf | Als Satz | Vergangenheit möglich? |
|---|---|---|
| Abrechnung erstellen | „Abrechnung erstellen" | nein — Aufforderung |
| Folgetermin vorschlagen | „Folgetermin vorschlagen" | nein |
| Laboruntersuchung beauftragen | „Laboruntersuchung beauftragen" | nein |
| In Rückrufliste aufnehmen | „In Rückrufliste aufnehmen" | nein |

**Alle vier sind Aufträge.** Jeder hat einen Adressaten im Namen.

**Das Geschehen dahinter:**

> **Behandlung wurde abgeschlossen**

## Schritt 2 · Reagieren alle auf dasselbe?

| Empfänger | Reagiert eigentlich auf |
|---|---|
| Abrechnung | Behandlung wurde abgeschlossen |
| Terminverwaltung | Behandlung wurde abgeschlossen |
| Rückrufliste | Behandlung wurde abgeschlossen |
| **Labor** | **Untersuchung wurde angeordnet** |

**Das Labor fällt heraus.** Eine Untersuchung wird während der Behandlung angeordnet — nicht am Ende. Wer sie erst beim Abschluss beauftragt, verliert Zeit.

**Zwei Meldungen:**

| Meldung | Empfänger |
|---|---|
| Untersuchung wurde angeordnet | Labor |
| Behandlung wurde abgeschlossen | Abrechnung, Terminverwaltung, Rückrufliste |

**Der Nebenertrag:** Die Aufteilung deckt auf, dass Laboraufträge bisher zu spät herausgingen — ein Fehler, den niemand als solchen gesehen hat.

## Schritt 3 · Die Dringlichkeit

| Empfänger | Einordnung | Was passiert, wenn die Meldung nie ankommt? |
|---|---|---|
| Abrechnung | **zwingend** | Die Leistung wird nicht abgerechnet — direkter Verlust |
| Labor | **zwingend** | Die Untersuchung findet nicht statt — Behandlungsfehler möglich |
| Terminverwaltung | zeitnah | Kein Folgetermin vorgeschlagen — ärgerlich, aufholbar |
| Rückrufliste | nachrangig | Patient wird nicht erinnert |

**Zwei zwingend, einer zeitnah, einer nachrangig.**

**Für die zwingenden:** Meldung aufbewahren, Verarbeitungsstand festhalten, Frist überwachen. Beim Labor eine kurze Frist (Minuten), bei der Abrechnung eine lange (Tage).

## Schritt 4 · Was in die Meldung gehört

**Behandlung wurde abgeschlossen:**

| Angabe | Warum |
|---|---|
| Patientennummer | Kennung, nachschlagbar |
| Behandlungsnummer | Kennung |
| Abschlusszeitpunkt | gilt zu diesem Zeitpunkt, ändert sich nicht |
| erbrachte Leistungen | Beleg — muss unverändert bleiben |

**Nicht in der Meldung:** Diagnose, Anamnese, Medikation. Die Abrechnung schlägt nach, was sie braucht.

**Warum die Leistungen doch:** Sie sind der Beleg für die Abrechnung. Wenn jemand sie nachträglich ändert, muss die Abrechnung den Stand von damals sehen — dieselbe Überlegung wie bei einer Rechnungsanschrift.

---

## Was dieses Beispiel zeigt

**Vier Aufträge, zwei Meldungen.** Die Zahl sinkt, weil Aufträge Empfänger benennen und Meldungen Geschehen.

**Ein Empfänger reagiert auf etwas anderes.** Das Labor gehört nicht zum Abschluss. Solche Funde sind der eigentliche Ertrag.

**Der Fund deckt einen alten Fehler auf.** Laboraufträge gingen zu spät heraus — nicht wegen eines Programmfehlers, sondern weil sie am falschen Geschehen hingen.

**Zwingend ist nicht sofort.** Die Abrechnung darf Tage warten, das Labor nur Minuten. Beide sind zwingend.

---

## Zum Vergleich: was ein neuer Empfänger kostet

**Die Praxis will künftig ein Qualitätsregister beliefern.**

| | Bisher | Mit Meldungen |
|---|---|---|
| Zu ändern | Behandlungserfassung: fünfter Aufruf | nichts |
| Risiko | ein weiterer Kandidat für Zeitüberschreitungen | keines |
| Wer wird angefasst | eine Stelle, die mit Qualitätsregistern nichts zu tun hat | das Register meldet sich an |

**Der Unterschied ist nicht die Arbeit beim ersten Mal, sondern beim fünften, sechsten und neunten.**
