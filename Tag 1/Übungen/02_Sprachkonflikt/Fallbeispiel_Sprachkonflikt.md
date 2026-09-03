# Fallbeispiel · Der Kunde, den es dreimal gab

**Situationstyp:** Ein Begriff bedeutet in jeder Abteilung etwas anderes — und das fällt erst auf, wenn eine gemeinsame Auswertung gefordert wird.

---

## Ausgangslage

Ein Autovermieter mit 140 Stationen im deutschsprachigen Raum. Gewachsen aus einem Familienbetrieb, seit 2009 mit eigener Software.

Fünf Bereiche arbeiten mit derselben Datenbasis:

| Bereich | Aufgabe |
|---|---|
| Vertrieb | Reservierungen, Rahmenverträge, Firmenkunden |
| Stationen | Ausgabe und Rücknahme vor Ort |
| Flotte | Beschaffung, Bestand, Standortverteilung |
| Werkstatt | Wartung, Reparatur, Prüftermine |
| Abrechnung | Rechnungen, Mahnwesen, Kautionen |

## Wie es gewachsen ist

Die erste Fassung kannte einen Kundenbegriff und einen Fahrzeugbegriff. Das genügte, solange dreißig Stationen an einer Kasse abrechneten.

Mit dem Firmenkundengeschäft kam die Unterscheidung zwischen dem Unternehmen, das den Rahmenvertrag hält, und der Person, die tatsächlich fährt. Der Vertrieb ergänzte ein Merkmal für die Kundenart.

Die Werkstatt brauchte Fahrzeuge, die es im Vertrieb nicht gibt — Werkstattersatzwagen, Überführungsfahrzeuge, ausgemusterte Einheiten mit Restwert. Sie ergänzte ein Merkmal für den Fahrzeugstatus.

Die Abrechnung brauchte Kunden, die keine sind: Versicherungen, die eine Schadensrechnung erhalten, Leasinggeber, die Rückläufer abwickeln. Sie ergänzte ein Merkmal für den Abrechnungstyp.

Nach fünfzehn Jahren trägt der Kundenbegriff 47 Merkmale. Bei einem beliebigen Kunden sind die meisten davon leer.

## Der Vorfall

Die Geschäftsführung verlangte eine Auswertung: **Umsatz je Kunde über alle Bereiche.**

Vier Bereiche lieferten vier Zahlen, die sich nicht zusammenführen ließen.

- Der **Vertrieb** zählte Rahmenvertragspartner. Ein Konzern mit zwölf Tochterfirmen war **ein** Kunde.
- Die **Stationen** zählten Fahrer. Derselbe Konzern erschien als 340 Kunden.
- Die **Abrechnung** zählte Rechnungsempfänger. Der Konzern erschien viermal — je Landesgesellschaft eine Rechnungsadresse.
- Die **Werkstatt** kannte keine Kunden, sondern Kostenträger. Für sie war der Konzern eine interne Kostenstelle.

Vier Wochen Abstimmung ergaben keine Einigung. Jeder Bereich beharrte darauf, dass seine Zählung richtig sei — **und jeder hatte recht.**

Die Auswertung wurde schließlich von Hand erstellt, in einer Tabellenkalkulation, mit einer Fußnote über die Zählweise. Sie wird bis heute so erstellt.

## Was dauerhaft stört

- **Jede neue Anforderung an die Kundendaten** löst dieselbe Diskussion aus. Beim letzten Mal ging es um die Frage, ob ein Fahrer ohne Rahmenvertrag ein Kunde ist.
- **Der Kundenbegriff wächst weiter.** Zwei neue Merkmale im letzten Jahr, beide für einen einzelnen Bereich, beide für die übrigen bedeutungslos.
- **Neue Mitarbeiter brauchen Monate**, bis sie wissen, welches Merkmal für welchen Bereich gilt. Aufgeschrieben ist es nirgends.
- **Ein Fehler in der Kautionsabrechnung** blieb vier Monate unbemerkt, weil die Abrechnung mit einem Kundenbegriff arbeitete, den die Station anders befüllt hatte.

## Was bisher versucht wurde

**Ein gemeinsames Datenmodell.** Ein Workshop mit allen Bereichen sollte die verbindliche Definition von „Kunde" festlegen. Nach zwei Tagen stand ein Kompromiss, den anschließend niemand verwendete — er passte für keinen Bereich richtig.

**Eine Vereinheitlichung der Begriffe.** Ein Glossar wurde erstellt und per Rundschreiben verteilt. Es hängt in zwei Büros aus. Im Sprachgebrauch hat sich nichts geändert.

## Diskussionsfragen

1. Warum hat der Workshop kein tragfähiges Ergebnis gebracht?
2. Was wäre der Preis, wenn sich alle Bereiche auf **eine** Definition von „Kunde" einigen würden?
3. Ist es ein Fehler, dass vier Bereiche vier verschiedene Bedeutungen verwenden?
4. Wo haben Sie so etwas?
