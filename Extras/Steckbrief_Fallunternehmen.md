# Steckbrief · Das Fallunternehmen

Alle Übungen des Kurses spielen bei demselben Unternehmen. Diese Seite fasst zusammen, was über zwei Tage verstreut aufgebaut wird.

---

## Das Unternehmen

Eine **Autovermietung** im deutschsprachigen Raum, gewachsen aus einem Familienbetrieb.

| | |
|---|---|
| Stationen | 140 |
| Fahrzeuge | 8.400 |
| davon geleast | 2.400 |
| Firmenkunden | 1.240 |
| Abschlüsse täglich | 1.400, freitags bis 2.600 |
| Entwickler | 22 |
| Eigene Software seit | 2009 |

**Das Verkaufsargument:** Die Quote nicht erfüllter Reservierungen liegt bei 0,8 Prozent, im Branchendurchschnitt bei 4 Prozent. „Bei uns kriegen Sie das Auto — auch morgen früh in Landshut."

---

## Die vier Kontexte

Ergebnis der Übungen von Tag 1.

| Kontext | Verantwortet | Zentrale Begriffe |
|---|---|---|
| **Vertragsverwaltung** | Rahmenverträge, Konditionen, Firmenkunden | Kunde (= Unternehmen), Rahmenvertrag, Konditionsstaffel |
| **Anmietung** | Reservierung, Ausgabe, Rückgabe, Verlängerung | Vorgang, Mieter, Mietvertrag, Rückläufer, Kaution |
| **Flotte und Instandhaltung** | Bestand, Standorte, Wartung, Reparatur | Fahrzeug, Werkstattaufenthalt, Prüfbericht, Verwertung |
| **Fakturierung** | Rechnungen, Kautionen, Mahnwesen | Empfänger, Position, Sammelrechnung, Rahmen |

**Der Bereich Werkstatt** liegt innerhalb von „Flotte und Instandhaltung" — kein eigener Kontext.

---

## Die vier Fremdsysteme

| System | Anbieter | Beziehung |
|---|---|---|
| **Partnernetzwerk** | internationaler Vermittler, 18 % der Anmietungen | Conformist — kein Einfluss auf das Format |
| **Leasingportal** | Leasinggeber, 2.400 Fahrzeuge | Customer/Supplier — Absprache möglich |
| **Schadensplattform** | Versicherungsverbund | Conformist auf Open Host Service |
| **Zahlungsdienstleister** | Bank | Conformist auf Published Language |

---

## Die Personen

| Person | Rolle |
|---|---|
| **Frau Berger** | Vertrieb, Leiterin Firmenkundengeschäft |
| **Herr Yilmaz** | Stationsleiter München-Ost |
| **Herr Doblinger** | Flottenmanagement |
| **Frau Petrova** | Leiterin der zentralen Werkstattdisposition |
| **Herr Krause** | Leiter Abrechnung |
| **Frau Lindqvist** | IT-Leitung |

Dazu eine Disponentin mit 19 Jahren Erfahrung, deren Wissen über regionale Bedarfsspitzen nirgends aufgeschrieben ist.

---

## Die Vorfälle

Jede Übung geht von einem Vorfall aus. In zeitlicher Folge:

| Ticket | Was geschah | Übung |
|---|---|---|
| AV-2091 | Auswertung „Ausmusterungskandidaten" nach 11 Wochen geliefert, wird nicht genutzt | Domäne und Modell |
| AV-2180 | Auswertung „Umsatz je Kunde" nicht auslieferbar — vier Bereiche, vier Zahlen | Sprachkonflikt |
| AV-2298 | Prüfung auf falschen Kundenbegriff gebaut, 3 Wochen Nacharbeit | Glossar |
| AV-2398 | Workshop zur Zuständigkeit endet ohne Ergebnis | Canvas |
| AV-2515 | Budgetplanung: 4/5 des Aufwands ohne Unterscheidungsrelevanz | Subdomains |
| AV-2588 | Formatumstellung Partnernetzwerk: 11 statt 3 Wochen, Vertragsstrafen | Context Map |
| AV-3098 | Rechnung an abgemeldete Anschrift | Entity und Value Object |
| AV-3231 | Frankfurt-Flughafen blockiert, 11 Kunden abgewandert | Aggregate |
| AV-3358 | Störung beim Befragungsanbieter, 122 fehlende Rückmeldungen | Domain Events |
| AV-3471 | Selbstöffnung: vier Bereiche, vier Antworten zur Schadensfeststellung | Event Storming |
| AV-3594 | Regelprüfung dauert 3 Tage, Korrektur 2 Stunden | Architektur |
| AV-3715 | Ablösung seit 7 Jahren, kein Abschaltdatum | Legacy |

---

## Der Zustand des Altsystems

Ausgangspunkt mehrerer Übungen:

| Befund | Umfang |
|---|---|
| Kundenbegriff | 47 Merkmale, die meisten leer |
| Fahrzeugbegriff | 61 Merkmale, im Mittel 19 gefüllt |
| Statuscode des Vermittlers | ausgewertet an 31 Stellen in drei Kontexten |
| Glossar | 84 Einträge, 31 Seiten, 11 Zugriffe in 8 Monaten |
| Ablösung läuft seit | 2018, Parallelbetrieb 2,1 Vollzeitstellen |

---

## Die Fachbereiche und ihre Sicht auf „Kunde"

Der Ausgangsbefund des Kurses — derselbe Konzernkunde:

| Bereich | Meint | Zählt ihn als |
|---|---|---|
| Vertrieb | Rahmenvertragspartner | 1 |
| Station | Person am Tresen | 340 |
| Abrechnung | Rechnungsempfänger | 4 |
| Werkstatt | Kostenträger | 1 |

Vier Bedeutungen, vier Zahlen, kein Fehler.
