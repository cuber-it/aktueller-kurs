# Fallbeispiel · Das Modell, das keiner Frage antwortete

**Situationstyp:** Ein System bildet alle Daten ab und beantwortet keine fachliche Frage — weil nie festgelegt wurde, wozu das Modell da ist.

---

## Ausgangslage

Ein Autovermieter mit 140 Stationen. Die Software wird seit 2009 im Haus entwickelt.

Am Anfang stand ein Auftrag: „Wir brauchen ein System, das unsere Fahrzeuge und Vermietungen verwaltet." Ein externer Berater erhob den Bestand — welche Daten es gibt, welche Formulare ausgefüllt werden, welche Listen geführt werden.

Daraus entstand ein Modell. Es umfasste alles, was irgendwo aufgeschrieben wurde.

## Wie es gewachsen ist

Das Vorgehen war naheliegend und effizient. Wo eine Abteilung eine Angabe führte, kam sie ins Modell. Nach fünfzehn Jahren umfasst der Fahrzeugbegriff 61 Merkmale.

Ein Auszug:

| Merkmal | Wer führt es | Wer braucht es |
|---|---|---|
| Kennzeichen | alle | alle |
| Leasingvertragsnummer | Flotte | Flotte |
| Innenraumfarbe | Beschaffung | niemand mehr |
| Standort | Station | Station, Flotte |
| Reifenprofiltiefe letzte Prüfung | Werkstatt | Werkstatt |
| Kategorie | Vertrieb | Vertrieb, Abrechnung |
| Letzte Innenreinigung | Station | Station |
| Verwertungserlös | Flotte | Buchhaltung |
| Erstzulassung | Beschaffung | Flotte, Werkstatt |

Von 61 Merkmalen sind bei einem beliebigen Fahrzeug im Mittel **19** gefüllt.

## Der Vorfall

Die Werkstattdisposition beantragte eine Auswertung: **„Welche Fahrzeuge sollten wir ausmustern statt weiter zu reparieren?"**

Die Frage ist fachlich klar. Frau Petrova, die Leiterin, beantwortet sie täglich aus dem Kopf: Bei manchen Fahrzeugen sieht sie nach dem dritten Getriebeschaden, dass es sich nicht mehr lohnt.

Die Entwicklung nahm den Auftrag an und kam nach zwei Wochen zurück mit der Frage, was genau ausgewertet werden solle.

**Das Modell konnte die Frage nicht beantworten**, obwohl alle nötigen Daten vorhanden waren:

- Reparaturen sind erfasst — aber als Einzelvorgänge mit Datum und Betrag, ohne Bezug zueinander. Dass drei davon dasselbe Bauteil betrafen, steht nirgends.
- Ein Fahrzeug hat einen Zustand, aber der heißt „verfügbar", „vermietet" oder „in Werkstatt" — es gibt keinen Zustand „grenzwertig".
- Was „lohnt sich nicht mehr" bedeutet, ist im Modell nicht vorhanden. Es ist eine Bewertung, und Bewertungen kommen nicht vor.

**Die Auswertung wurde nach elf Wochen geliefert** — als Liste aller Fahrzeuge mit ihren Reparaturkosten, sortiert absteigend. Frau Petrova benutzt sie nicht. Sie sagt, die teuersten seien nicht die problematischen; problematisch seien die, bei denen dasselbe dreimal kaputtgeht.

## Was bei der Aufarbeitung auffiel

**Das Modell wurde aus den Daten gebaut, nicht aus den Fragen.** Der Berater hatte erhoben, was aufgeschrieben wird — nicht, was entschieden werden muss.

**Es gab nie einen benannten Zweck.** „Fahrzeuge und Vermietungen verwalten" ist kein Zweck, sondern eine Zuständigkeit. Ohne Zweck lässt sich nicht entscheiden, was ins Modell gehört.

**Die Begriffe der Fachbereiche fehlen.** Frau Petrova spricht von „grenzwertig" und „lohnt nicht mehr". Beide kommen im Modell nicht vor — obwohl sie ihre täglichen Entscheidungen tragen.

**Was fehlt, fällt nicht auf.** Ein Modell mit 61 Merkmalen wirkt vollständig. Dass ein Begriff fehlt, merkt man erst, wenn jemand eine Frage stellt, die ihn braucht.

## Was bisher versucht wurde

**Weitere Merkmale ergänzen.** Nach der gescheiterten Auswertung wurde ein Feld „Ausmusterungsempfehlung" angelegt, das jemand von Hand setzen sollte. Es ist bei 40 von 8.400 Fahrzeugen gefüllt.

**Eine Auswertungsdatenbank.** Alle Daten wurden in ein zweites System gespiegelt, in dem freier abgefragt werden kann. Die Frage bleibt dieselbe unbeantwortbar — nur schneller.

## Diskussionsfragen

1. Alle nötigen Daten waren vorhanden. Warum war die Frage trotzdem nicht beantwortbar?
2. Was hätte der Berater 2009 anders fragen müssen?
3. Warum hilft das Feld „Ausmusterungsempfehlung" nicht?
4. Wo haben Sie so etwas?
