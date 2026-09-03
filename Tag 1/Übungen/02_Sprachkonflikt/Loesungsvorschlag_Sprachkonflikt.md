# Lösungsvorschlag · Wo sprechen die Bereiche aneinander vorbei?

**Vorbemerkung:** Dies ist ein Vorschlag, keine Musterlösung. Kontextgrenzen sind Entwurfsentscheidungen — es gibt mehrere vertretbare Aufteilungen. Bewertet wird die Begründung, nicht die Übereinstimmung mit diesem Papier.

---

## 1 · Die Begriffstabelle

### Kunde

| Bereich | Bedeutung | Zählweise beim Konzernkunden |
|---|---|---|
| Vertrieb | Unternehmen mit Rahmenvertrag | 1 |
| Station | Person, die das Fahrzeug bewegt | 340 |
| Flotte | **existiert nicht** — stattdessen Station als Bedarfsmelder | — |
| Werkstatt | **existiert nicht** — stattdessen Kostenträger | — |
| Abrechnung | Rechnungsempfänger | 4 |

### Vertrag

| Bereich | Bedeutung | Laufzeit |
|---|---|---|
| Vertrieb | Rahmenvertrag mit Konditionen | 2–3 Jahre |
| Station | Mietvertrag für eine Anmietung | Tage |
| Flotte | **existiert nicht** | — |
| Werkstatt | Wartungsvertrag mit einer Werkstatt | laufend |
| Abrechnung | Abrechnungsvereinbarung | laufend |

### Fahrzeug

| Bereich | Bedeutung | Umfang |
|---|---|---|
| Vertrieb | **Kategorie** (Kompakt, Kombi, Transporter) | ~8 Kategorien |
| Station | konkretes Auto mit Kennzeichen | die auf dem Hof |
| Flotte | alles mit Fahrgestellnummer im Bestand | 8.400 |
| Werkstatt | Objekt mit Historie über Jahre | dieselben 8.400 |
| Abrechnung | Position auf einer Rechnung | — |

---

## 2 · Die Kollisionen

### Ein Wort, mehrere Bedeutungen

| Begriff | Bedeutungen |
|---|---|
| **Kunde** | Rahmenvertragspartner · Fahrer · Rechnungsempfänger |
| **Vertrag** | Rahmenvertrag · Mietvertrag · Wartungsvertrag · Abrechnungsvereinbarung |
| **Fahrzeug** | Kategorie · konkretes Auto · Bestandsobjekt |

**Vier Bedeutungen für „Vertrag"** ist der auffälligste Befund — und der am wenigsten beachtete, weil niemand ihn je zusammengetragen hat.

### Mehrere Wörter, eine Bedeutung

| Wörter | Gemeinsame Sache |
|---|---|
| Kunde (Werkstatt: *Kostenträger*) · Kunde (Abrechnung: *Rechnungsempfänger*) | teilweise dieselbe Versicherung |
| Fahrzeug (Flotte) · Fahrzeug (Werkstatt) | **dieselben 8.400 Objekte, verschiedene Sicht** |

Der zweite Fall ist bemerkenswert: Flotte und Werkstatt meinen dasselbe. Sie unterscheiden sich nur darin, welche Angaben sie brauchen — Lebenszyklus gegen Historie.

---

## 3 · Welche Kollisionsart ist gefährlicher

**Ein Wort mit mehreren Bedeutungen.**

| | fällt auf | Schadensmoment |
|---|---|---|
| Zwei Wörter, eine Sache | **ja** — jemand fragt nach | bei der Klärung, folgenlos |
| Ein Wort, zwei Sachen | **nein** — beide Seiten glauben sich verstanden zu haben | wenn Daten zusammengeführt werden, oft Jahre später |

Bei zwei Wörtern für dieselbe Sache stolpert man beim Lesen. Bei einem Wort für zwei Sachen stolpert niemand — bis eine Auswertung vier verschiedene Zahlen liefert.

Der Vorfall im Fallbeispiel ist genau dieser Fall. Die Software war nie fehlerhaft; sie hat vier Fragen korrekt beantwortet, die alle „Umsatz je Kunde" hießen.

---

## 4 · Der Preis einer Einigung

**Angenommen, „Kunde" wird verbindlich als *Rahmenvertragspartner* definiert:**

| Bereich | Preis |
|---|---|
| Station | Braucht ein zweites Wort für die Person am Tresen. Der gesamte Ausgabeprozess arbeitet mit dieser Person; sie ist die fachlich zentrale Größe. |
| Abrechnung | Kann Versicherungen nicht mehr als Kunden führen. Braucht einen zweiten Rechnungsempfängerbegriff — oder Rechnungen ohne Kunden. |
| Vertrieb | Kein Preis. Die Definition ist seine. |

**Umgekehrt, „Kunde" als *Fahrer*:**

| Bereich | Preis |
|---|---|
| Vertrieb | Verliert die Ebene, auf der er verhandelt. Ein Rahmenvertrag hat dann keinen Kunden. |
| Abrechnung | Rechnungen gehen an Fahrer statt an Firmen — fachlich falsch. |

**Der Befund:** Jede Einigung erzeugt bei mindestens zwei Bereichen einen Hilfsbegriff für das, was sie eigentlich meinen. Genau deshalb ist der Workshop im Fallbeispiel gescheitert: Der Kompromiss war für alle gleich unbrauchbar.

**Die Einsicht dahinter:** Die Bedeutungen sind nicht verhandelbar, weil sie aus der Arbeit folgen. Ein Stationsleiter *kann* nicht anders als die Person vor sich als Kunden zu sehen — sie steht ja da.

---

## 5 · Vorschlag für die Aufteilung

Vier Grenzen, entlang der Aufgaben:

### Kontext 1 · Vertragsverwaltung (Vertrieb)

| | |
|---|---|
| Kunde | Unternehmen mit Rahmenvertrag |
| Vertrag | Rahmenvertrag mit Konditionsstaffel |
| Fahrzeug | Kategorie |

**Begründung:** Der Vertrieb arbeitet auf der Ebene von Vereinbarungen, nicht von Vorgängen. Konkrete Autos und konkrete Personen kommen in seiner Arbeit nicht vor.

### Kontext 2 · Anmietung (Station)

| | |
|---|---|
| Mieter | Person, die fährt |
| Mietvertrag | eine Anmietung |
| Fahrzeug | konkretes Auto mit Kennzeichen |

**Begründung:** Hier findet der Vorgang statt. Der zentrale Begriff ist der Mietvorgang, nicht die Geschäftsbeziehung.

**Beachten:** „Kunde" wird durch **Mieter** ersetzt. Das ist kein Verlust — es ist präziser, und die Station spricht ohnehin so, wenn man genauer hinhört („der Kunde am Tresen" meint die Person).

### Kontext 3 · Flotte und Instandhaltung (Flotte + Werkstatt)

| | |
|---|---|
| Fahrzeug | Objekt mit Fahrgestellnummer, Lebenszyklus und Historie |
| Kostenträger | wer eine Maßnahme bezahlt |

**Begründung für die Zusammenlegung:** Beide meinen dieselben 8.400 Objekte. Der Unterschied liegt in den Angaben, nicht in der Sache. Das ist kein Konflikt, sondern unterschiedlicher Bedarf — ein Fall für **ein** Modell mit verschiedenen Sichten.

**Gegenargument, das im Kurs kommen wird:** Beschaffung und Reparatur sind verschiedene Aufgaben mit verschiedenen Zuständigen. Wer die Kontexte trennt, hat ebenfalls recht — dann braucht es eine Übersetzung an der Grenze. Die Entscheidung hängt davon ab, wie eng die Zusammenarbeit tatsächlich ist.

### Kontext 4 · Fakturierung (Abrechnung)

| | |
|---|---|
| Rechnungsempfänger | wer die Rechnung erhält |
| Abrechnungsvereinbarung | Zahlungsziel, Skonto, Sammelrechnung |

**Begründung:** Ein Rechnungsempfänger ist nicht notwendig ein Kunde — eine Versicherung mietet nichts. Der Begriff ist eigenständig und darf es bleiben.

---

## 6 · Übersetzung an den Grenzen

| Grenze | Was übersetzt werden muss | Zuständig |
|---|---|---|
| Vertragsverwaltung → Anmietung | Konditionen des Rahmenvertrags müssen bei der Anmietung greifen. Übersetzt wird: Rahmenvertrag → gültige Konditionen für diesen Mietvorgang | Anmietung holt sich, was sie braucht |
| Anmietung → Flotte | Ausgabe und Rückgabe verändern Standort und Kilometerstand | Anmietung meldet, Flotte nimmt entgegen |
| Anmietung → Fakturierung | Ein abgeschlossener Mietvorgang wird zur Rechnungsposition. Übersetzt wird: Mieter + Rahmenvertrag → Rechnungsempfänger | Fakturierung bestimmt den Empfänger |
| Flotte → Fakturierung | Schadensfälle werden Versicherungen berechnet | Fakturierung |

**Wichtig:** Die Übersetzung gehört **in den empfangenden Kontext**. Wer Information braucht, übersetzt sie — nicht der Sender. Sonst muss der Sender alle Empfänger kennen.

---

## 7 · Die ursprüngliche Auswertung

„Umsatz je Kunde über alle Bereiche" ist unter diesem Vorschlag **nicht direkt beantwortbar** — und das ist richtig so, denn die Frage ist unterspezifiziert.

Beantwortbar wären:

| Frage | Kontext | Ergebnis für den Konzern |
|---|---|---|
| Umsatz je **Rahmenvertragspartner** | Vertragsverwaltung | 1 Zeile |
| Umsatz je **Rechnungsempfänger** | Fakturierung | 4 Zeilen |
| Anmietungen je **Mieter** | Anmietung | 340 Zeilen |

**Der Weg zur Gesamtauswertung:** Die Fakturierung kennt zu jeder Rechnung den Rahmenvertrag. Damit lässt sich Umsatz je Rahmenvertragspartner aggregieren — die Frage, die die Geschäftsführung vermutlich meinte.

**Der eigentliche Gewinn:** Die Anforderung wird präzisiert, statt einen Kompromiss zu erzwingen. Aus „Umsatz je Kunde" wird „Umsatz je Rahmenvertragspartner" — und das ist beantwortbar, eindeutig und unstrittig.

---

## Diskussionsanschluss

Der Vorschlag legt Flotte und Werkstatt in einen Kontext. Zwei Argumente stehen dagegen: verschiedene Zuständige, verschiedene Änderungsrhythmen. Was spricht dafür, was dagegen — und woran würden Sie es festmachen?
