# Pro und Contra · Die vorgeschlagene Kontextaufteilung

Bewertet wird der Vorschlag aus dem Lösungspapier: vier Kontexte — Vertragsverwaltung, Anmietung, Flotte und Instandhaltung, Fakturierung.

---

## Pro

**Jeder Bereich behält seine Sprache**
Der Vertrieb sagt weiter „Kunde" und meint das Unternehmen, die Station sagt „Mieter" und meint die Person. Niemand muss einen Hilfsbegriff für das verwenden, was er eigentlich meint. Genau daran ist der Einigungsworkshop gescheitert.

**Die Modelle werden klein**
Statt einer Tabelle mit 47 überwiegend leeren Spalten hat jeder Kontext ein Modell mit den Angaben, die er tatsächlich braucht. Ein neues Feld betrifft einen Kontext, nicht alle.

**Missverständnisse werden unmöglich statt unwahrscheinlich**
Wenn „Kunde" nur noch in der Vertragsverwaltung existiert, kann niemand ihn mehr mit dem Fahrer verwechseln. Das ist konstruktiv gesichert, nicht durch Dokumentation.

**Die Bereiche können unabhängig arbeiten**
Eigene Modelle bedeuten eigene Änderungsrhythmen. Die Abrechnung kann ihren Rechnungsempfängerbegriff erweitern, ohne mit vier Bereichen abzustimmen.

**Anforderungen werden präziser**
„Umsatz je Kunde" ist unter dem Vorschlag nicht beantwortbar — und die Rückfrage führt zu „Umsatz je Rahmenvertragspartner". Das ist eindeutig und unstrittig. Die Unschärfe wird sichtbar, statt sich in vier Zahlen zu verstecken.

**Umbenennungen decken Unschärfen auf**
„Kunde" an der Station zu „Mieter" zu machen, kostet nichts und zwingt zur Genauigkeit. Beim Durchsprechen fiel auf, dass die Station ohnehin von der Person spricht.

**Flotte und Werkstatt zusammenzulegen spart eine Grenze**
Beide meinen dieselben 8.400 Objekte. Eine Grenze zwischen ihnen wäre Aufwand ohne fachlichen Anlass.

---

## Contra

**Vier Modelle statt einem**
Was vorher in einer Tabelle stand, liegt jetzt in vier Kontexten. Wer eine Übersicht über alles braucht, muss vier Stellen befragen. Für Auswertungen ist das aufwendiger als vorher.

**Die Übersetzung ist neue Arbeit**
Vier Grenzen bedeuten vier Übersetzungen, die gebaut, gepflegt und getestet werden müssen. Vorher gab es sie nicht — die Bereiche griffen direkt auf dieselbe Tabelle zu.

**Redundanz entsteht bewusst**
Der Rahmenvertragspartner in der Vertragsverwaltung und der Rechnungsempfänger in der Fakturierung sind oft dasselbe Unternehmen, aber zwei Datensätze. Eine Adressänderung muss an beiden Stellen ankommen. Das ist gewollt und trotzdem unangenehm.

**Die Zusammenlegung von Flotte und Werkstatt ist angreifbar**
Zwei Abteilungen, zwei Zuständige, zwei Änderungsrhythmen. Wer sie trennt, hat ebenfalls gute Gründe. Der Vorschlag entscheidet sich für die Zusammenlegung, weil die Objekte dieselben sind — das kann sich als falsch erweisen, wenn die Zusammenarbeit lockerer ist als angenommen.

**Migration bestehender Daten**
47 Spalten müssen auf vier Modelle verteilt werden. Bei fünfzehn Jahren Datenbestand ist unklar, welche Spalte in welchem Fall wie befüllt wurde. Die Dokumentation besteht aus Kommentaren in der Datenbank.

**Der Aufwand fällt sofort an, der Nutzen später**
Die Aufteilung kostet Monate. Der Gewinn zeigt sich erst, wenn die nächste Anforderung nicht wieder eine Grundsatzdiskussion auslöst.

**Die Grenzen sind eine Wette**
Sie beruhen auf dem heutigen Verständnis der Fachlichkeit. Ändert sich die Arbeitsteilung — etwa wenn Stationen künftig auch abrechnen —, sind sie falsch geschnitten.

---

## Bewertung

Der Fall trägt die Aufteilung, weil die Bedeutungen **fachlich berechtigt verschieden** sind und die Zusammenführung zu einem **Widerspruch** führt, nicht zu einer Vereinigungsmenge. Der gescheiterte Workshop ist der Beleg: Ein Kompromiss war nicht formulierbar, weil es keinen gibt.

Gegenprobe — *Aufteilung gedanklich zurücknehmen, bleiben Nachteile?* Ja: Die Tabelle wächst weiter, jede Anforderung löst dieselbe Diskussion aus, und Auswertungen bleiben handgemacht.

**Die Grenzen:**

1. **Die Zusammenlegung von Flotte und Werkstatt gehört überprüft.** Sie ist die einzige Entscheidung im Vorschlag, die nicht aus einem Widerspruch folgt, sondern aus einer Ähnlichkeit. Kriterium wäre: Ändern beide dasselbe Modell, oder arbeiten sie nur auf denselben Objekten?

2. **Die Migration ist nicht Teil des Vorschlags** und vermutlich der größere Aufwand. Ein Vorschlag ohne Migrationsweg ist eine halbe Antwort.

3. **Vier Kontexte könnten zu wenige sein.** Der Vorschlag folgt den fünf Bereichen. Ob innerhalb der Anmietung nicht weitere Grenzen liegen — etwa zwischen Ausgabe und Rückgabe —, ist nicht geprüft.

---

## Diskussionsfragen

1. Flotte und Werkstatt in einem Kontext oder in zweien? Woran machen Sie es fest?
2. Der Rahmenvertragspartner und der Rechnungsempfänger sind oft dasselbe Unternehmen. Wie gehen Sie mit der Redundanz um?
3. Wer sollte die Übersetzung an einer Grenze verantworten — Sender oder Empfänger?
4. Die Aufteilung kostet Monate. Wie begründen Sie das gegenüber der Geschäftsführung, die eine Auswertung wollte?
5. Wann wäre es richtig, bei einem gemeinsamen Modell zu bleiben?
