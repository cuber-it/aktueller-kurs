# 2-5 · Trainer-Ergänzungsmaterial: Event Storming

## Kernidee für den Trainer

Die einzige Einheit des Kurses, die eine **Methode** vermittelt statt eines Begriffs. Sie wird gemacht, nicht erklärt.

Der Kern:

> **Man beginnt mit dem, was geschehen ist — weil Fachleute darüber von selbst erzählen.**

Modellbegriffe kommen zuletzt. Wer mit Aggregaten anfängt, verliert den Fachbereich in der ersten Viertelstunde.

## Ehrlichkeit vorweg

**Event Storming lebt von vielen Händen an einer Wand.** Bei drei bis fünf Teilnehmern und online ist es eine geschwächte Fassung.

Das ausdrücklich sagen — die Teilnehmer merken es ohnehin. Was trotzdem trägt:

- Die Reihenfolge der Schritte
- Warum mit Ereignissen begonnen wird
- Was Hotspots leisten
- Wann die Methode nichts bringt

**Was im Kursformat nicht erlebbar ist:** die Dynamik von zwölf Leuten, die gleichzeitig kleben und sich dabei widersprechen. Darauf hinweisen.

## Der Ablauf

Nicht vortragen, sondern durchführen. Ein reduzierter Durchlauf mit dem Autovermieter-Fall dauert etwa 25 Minuten.

| Schritt | Was | Farbe |
|---|---|---|
| 1 | Ereignisse sammeln, Vergangenheitsform | orange |
| 2 | Auf einer Zeitachse ordnen | |
| 3 | Hotspots markieren — Streit und offene Fragen | rot |
| 4 | Commands ergänzen: was löst das Ereignis aus | blau |
| 5 | Akteure ergänzen: wer löst den Command aus | klein gelb |
| 6 | Aggregate finden: wo werden Commands verarbeitet | hellgelb |

**Die Farben sind Konvention und variieren je nach Quelle.** Wichtig ist nur, dass sie im Raum einheitlich verwendet werden — das sollte man sagen, sonst entsteht der Eindruck einer Norm.

## Warum Ereignisse zuerst

Der didaktische Kern, der ausgesprochen gehört:

> Fragen Sie einen Sachbearbeiter nach seinem Datenmodell — Sie bekommen nichts. Fragen Sie ihn, was passiert — Sie bekommen alles.

Ereignisse sind die natürliche Erzählform. Alles andere wird daraus abgeleitet.

## Hotspots sind das wertvollste Ergebnis

Der Punkt, den Anfänger übersehen.

Ein roter Zettel bedeutet: Hier sind sich zwei nicht einig, oder niemand weiß es. Das ist kein Störfall, sondern der eigentliche Ertrag — solche Stellen sind sonst unsichtbar.

**Trainerhinweis:** Im Durchlauf ausdrücklich zum Markieren auffordern. „Wo sind Sie sich nicht sicher?"

**Beim Autovermieter-Fall entstehen erfahrungsgemäß Hotspots bei:** Wer entscheidet über Schadensbewertung? Wann gilt ein Vorgang als abgeschlossen? Was passiert bei Rückgabe an einer fremden Station?

## Die drei Detailstufen

Kurz nennen, nicht vertiefen:

| Stufe | Zweck |
|---|---|
| Big Picture | Überblick über eine ganze Domäne, Kandidaten für Kontextgrenzen |
| Process Level | ein Ablauf im Detail |
| Design Level | Aggregate und Modellbegriffe |

**Im Kurs wird Big Picture gemacht.** Das ist die Stufe mit dem besten Verhältnis von Aufwand zu Ertrag.

## Was die Methode nicht leistet

Ausdrücklich sagen, sonst entstehen falsche Erwartungen:

- **Sie ersetzt keinen Entwurf.** Das Ergebnis ist Rohmaterial.
- **Sie entscheidet nichts.** Hotspots werden markiert, nicht aufgelöst.
- **Sie ersetzt nicht den Fachbereich.** Ohne die Leute, die es wissen, ist es eine Entwicklerrunde mit Zetteln.

## Der Durchlauf im Kurs

**Vorbereitung:** Ein Board mit Zeitachse, Farben erklärt. Bei Online-Durchführung vorher einrichten, nicht im Termin.

**Ablauf:**

| Phase | Minuten |
|---|---|
| Methode erklären | 8 |
| Ereignisse sammeln (still, jeder für sich) | 5 |
| Ordnen und Doppelungen zusammenführen | 5 |
| Hotspots markieren | 3 |
| Commands und Akteure | 5 |
| Aggregate-Kandidaten | 5 |
| Auswertung | 8 |

**Wichtig beim Sammeln:** erst still und einzeln, dann gemeinsam ordnen. Wer sofort diskutiert, bekommt die Meinung des Lautesten.

## Online-Besonderheiten

| Was | Wie |
|---|---|
| Board | vorher einrichten, Farben vorbelegen |
| Sammeln | jeder in seinem eigenen Bereich, dann zusammenschieben |
| Ordnen | eine Person schiebt, die anderen sprechen |
| Hotspots | jeder darf jederzeit einen roten Zettel setzen |

**Ohne Whiteboard-Werkzeug:** Als geteilte Liste machbar. Die Zeitachse wird zur Reihenfolge, die Farben zu Präfixen. Deutlich schwächer, aber die Schritte bleiben nachvollziehbar.

## Zum Umgang mit gemischten Gruppen

**Die stärkste Einheit für PO und Management** — sie können hier führen statt zuzuhören.

Wenn die Gruppe gemischt ist, die Fachvertreter zuerst sammeln lassen. Devs neigen dazu, technische Ereignisse zu schreiben; das gibt die Richtung falsch vor.

## Typische Fragen

**„Wie lange dauert das in echt?"**
Big Picture für eine mittlere Domäne: ein halber bis ganzer Tag mit acht bis fünfzehn Leuten.

**„Wer moderiert?"**
Jemand, der die Domäne nicht kennt, ist im Vorteil — er fragt nach, wo andere annehmen.

**„Was macht man mit dem Ergebnis?"**
Fotografieren, Hotspots als Aufgaben aufnehmen, Kontextgrenzen-Kandidaten weiterverfolgen. Das Board selbst überlebt selten.

**„Geht das auch ohne Zettel?"**
Ja, aber schlechter. Das gleichzeitige Kleben vieler Hände ist der Kern.

## Zeitgerüst

| Teil | Minuten |
|---|---|
| Methode und Farben | 8 |
| Durchlauf | 25 |
| Auswertung, was es leistet und was nicht | 12 |

## Übergang

> „Wir haben jetzt Ereignisse, Commands und Aggregate-Kandidaten. Was fehlt, ist die Frage, wo das alles im System liegt — und wie man verhindert, dass Technik ins Modell sickert."
