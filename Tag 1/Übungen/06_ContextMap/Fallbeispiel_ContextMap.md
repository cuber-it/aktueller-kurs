# Fallbeispiel · Die Schnittstelle, die alle mitzog

**Situationstyp:** Ein Fremdsystem-Modell ist ins eigene durchgesickert — eine Änderung dort trifft Bereiche, die damit nichts zu tun haben.

---

## Ausgangslage

Derselbe Autovermieter, zwei Jahre nach der Kontextaufteilung. Die vier Kontexte stehen, die Glossare werden gepflegt.

Neu hinzugekommen ist die Anbindung an ein **Partnernetzwerk**: Ein internationaler Vermittler bucht über eine Schnittstelle Fahrzeuge bei uns. Rund 18 Prozent der Anmietungen kommen inzwischen darüber.

Dazu kommen drei weitere Fremdsysteme:

| System | Anbieter | Zweck |
|---|---|---|
| Partnernetzwerk | Vermittler | eingehende Buchungen |
| Leasingportal | Leasinggeber | Fahrzeugbestellung, Rückgabe |
| Schadensplattform | Versicherungsverbund | Schadensmeldung, Regulierung |
| Zahlungsdienstleister | Bank | Kartenzahlung, Kautionen |

## Wie es gewachsen ist

Die Anbindung des Partnernetzwerks stand unter Zeitdruck — der Vertrag war unterschrieben, der Starttermin fest.

Der Vermittler liefert Buchungen in seinem eigenen Format. Er hat eigene Begriffe dafür — englische Bezeichnungen für Buchung, Reisender und Fahrzeugklasse — und einen Statuscode mit vierzehn Ausprägungen.

Um Zeit zu sparen, wurden seine Begriffe **unverändert in die Anmietung übernommen**. Der Partnerstatus wurde zu einem Merkmal jeder Buchung, der Verweis auf den Reisenden zu einem Merkmal jeder Reservierung, und die eigenen Fahrzeugkategorien wurden um die Codes des Vermittlers erweitert.

Es funktionierte. In sechs Wochen war die Anbindung fertig.

Das Leasingportal kam ein Jahr später und wurde nach demselben Muster angebunden. Dann die Schadensplattform.

## Der Vorfall

Der Vermittler kündigte eine **Formatumstellung** an: Der Statuscode wird von vierzehn auf sechs Ausprägungen reduziert, drei alte Codes entfallen ersatzlos, zwei werden zusammengelegt. Vorlauf: acht Wochen.

Die Analyse ergab, dass der Partnerstatus an **31 Stellen** ausgewertet wird — davon:

| Bereich | Stellen | Zusammenhang |
|---|---|---|
| Anmietung | 12 | nachvollziehbar |
| Fakturierung | 9 | Rechnungsstellung hängt am Partnerstatus |
| Flotte | 6 | Verfügbarkeitsplanung |
| **Werkstatt** | **4** | **niemand konnte erklären, warum** |

Die vier Stellen in der Werkstatt stammten aus einer Auswertung, die einmal jemand gebaut hatte, weil der Statuscode zufällig eine Information enthielt, die sonst nirgends stand.

**Die Umstellung dauerte elf Wochen statt der geplanten drei.** Der Starttermin des Vermittlers musste verhandelt werden; es entstanden Vertragsstrafen.

**Vier Wochen nach der Umstellung** fiel auf, dass die Verfügbarkeitsplanung falsche Zahlen lieferte. Einer der zusammengelegten Codes war in der Flotte anders interpretiert worden als in der Anmietung.

## Was bei der Aufarbeitung auffiel

**Das Modell des Vermittlers war zum eigenen Modell geworden.** Seine Begriffe tauchten an Stellen auf, die mit dem Partnernetzwerk nichts zu tun hatten. Wer in der Werkstatt arbeitete, musste wissen, was ein Fahrzeugklassen-Code des Vermittlers bedeutet.

**Es gab keine Stelle, an der übersetzt wurde.** Zwischen Fremdformat und eigenem Modell lag nichts.

**Die Abhängigkeit war unsichtbar.** Niemand hatte eine Übersicht, welche Bereiche von welchem Fremdsystem abhängen. Die 31 Stellen mussten einzeln zusammengesucht werden.

**Bei den anderen drei Anbindungen ist es dasselbe.** Das Leasingportal und die Schadensplattform sind nach demselben Muster gebaut. Beide haben Formatumstellungen angekündigt.

## Was dauerhaft stört

- Jede Änderung bei einem Fremdanbieter löst eine Suche aus, wer betroffen ist.
- Verhandlungen mit Anbietern werden schwächer geführt, weil der eigene Aufwand einer Umstellung unbekannt ist.
- Neue Anbindungen werden nach demselben Muster gebaut, weil es schnell geht.

## Diskussionsfragen

1. Warum war die schnelle Anbindung damals eine vernünftige Entscheidung?
2. Ab wann hätte man es anders machen müssen — und woran hätte man das gemerkt?
3. Was hätte die vier Stellen in der Werkstatt verhindert?
4. Wo haben Sie so etwas?
