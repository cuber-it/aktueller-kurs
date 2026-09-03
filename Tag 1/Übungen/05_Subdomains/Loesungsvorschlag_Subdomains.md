# Lösungsvorschlag · Wo lohnt der Aufwand?

---

## 1 und 2 · Die Einordnung

| # | Bereich | Kategorie | Begründung |
|---|---|---|---|
| 1 | Verfügbarkeitsdisposition | **Core** | Die Erfüllungsquote ist das Verkaufsargument; die Wettbewerber können es nachweislich nicht |
| 2 | Buchhaltung | **Generic** | Jedes Unternehmen führt Bücher; niemand wählt einen Vermieter wegen seines Kontenrahmens |
| 3 | Anmietungsabwicklung | **Supporting** | Ohne geht es nicht, aber jeder Vermieter gibt Fahrzeuge aus. Kein Unterschied |
| 4 | Personalzeiterfassung | **Generic** | Branchenunabhängig, Standardprodukte in großer Zahl |
| 5 | Dokumentenarchiv | **Generic** | Ablegen und Wiederfinden ist überall dasselbe |
| 6 | Kautionsabwicklung | **Supporting** | Branchenuntypisch, aber kein Verkaufsargument — niemand mietet wegen der Kautionsregeln |
| 7 | Flottenbeschaffung | **Supporting** | „Bei allen Vermietern gleich", laut Leiterin Flotte. Branchenlösungen vorhanden |
| 8 | Schadensabwicklung | **Supporting** | Notwendig, branchenüblich, Verbandsformat vorhanden |
| 9 | Firmenkundenkonditionen | **Supporting** | Alle Vermieter haben Rahmenverträge |
| 10 | Fahrerlaubnisprüfung | **Generic** | Externer Dienst, überall gleich |

**Nur ein Bereich ist Core.** Das ist normal — Core Domains sind selten, sonst wären sie keine.

**Prüfung der Begründungen (Aufgabe 2):** Keine nennt Umsatzanteil, Aufwand, Nutzerzahl oder Kompliziertheit. Die häufigste Falle bei Bereich 6: „Die Kautionsabwicklung ist kompliziert" ist keine Begründung für Core. Kompliziertheit ist kein Wert.

---

## 3 · Umgang je Kategorie

| Kategorie | Vorgehen | Wer arbeitet daran |
|---|---|---|
| **Core** | Selbst bauen, kontinuierlich weiterentwickeln | die besten Entwickler, dauerhaft |
| **Supporting** | Selbst bauen, wenn nichts passt — aber sparsam. Zukaufen, wo möglich | angemessene Besetzung, kein Perfektionismus |
| **Generic** | Standard nehmen. **Nicht anpassen** — lieber den eigenen Prozess anpassen | möglichst niemand |

**Die Regel für Generic ist die unbequemste:** Wer ein Standardprodukt anpasst, hat die Nachteile beider Wege — Lizenzkosten und Eigenentwicklung.

---

## 4 · Soll gegen Ist

| # | Bereich | Kategorie | Soll | Ist | Abweichung |
|---|---|---|---|---|---|
| 1 | Verfügbarkeitsdisposition | Core | selbst, laufend | zugekauft, kein Ausbau | **schwerwiegend** |
| 2 | Buchhaltung | Generic | Standard | Eigenentwicklung, 3 Jahre | **schwerwiegend** |
| 3 | Anmietungsabwicklung | Supporting | selbst, sparsam | selbst, 3 Entwickler | passt |
| 4 | Personalzeiterfassung | Generic | Standard | Eigenentwicklung, 8 Monate | erheblich |
| 5 | Dokumentenarchiv | Generic | Standard | Eigenentwicklung, 6 Monate | erheblich |
| 6 | Kautionsabwicklung | Supporting | selbst, sparsam | in der Buchhaltung eingebettet | **strukturell** |
| 7 | Flottenbeschaffung | Supporting | zukaufen | Eigenentwicklung „historisch" | erheblich |
| 8 | Schadensabwicklung | Supporting | selbst mit Verbandsformat | genau so | passt |
| 9 | Firmenkundenkonditionen | Supporting | selbst, sparsam | selbst | passt |
| 10 | Fahrerlaubnisprüfung | Generic | Standard nutzen | genau so | passt |

**Vier von zehn passen.** Zwei Abweichungen sind schwerwiegend und stehen in direktem Zusammenhang: Man hat die Core Domain zugekauft und eine Generic Subdomain selbst gebaut. Genau verkehrt herum.

---

## 5 · Der Widerspruch bei der Kautionsabwicklung

**Beide haben recht:**

- Der Leiter Abrechnung: Die Kautionsabwicklung ist branchenuntypisch. Kein Standardprodukt bildet sie ab.
- Die IT-Leitung: Man hat eine ganze Buchhaltung gebaut, um einen Sonderfall abzubilden.

**Die Auflösung liegt in der Trennung:**

| Teil | Kategorie | Vorgehen |
|---|---|---|
| **Kautionsabwicklung** — wann gesperrt, wann freigegeben, wann verrechnet | Supporting | selbst bauen, klein und eigenständig |
| **Buchhaltung** — Konten, Buchungen, Umsatzsteuer, Mahnwesen | Generic | Standardprodukt |

Die Kautionsabwicklung entscheidet **fachlich**, was mit einer Kaution geschieht. Sie erzeugt daraus Buchungssätze und übergibt sie. Die Buchhaltung bucht, was sie bekommt — das kann jedes Standardprodukt.

**Der Fehler war die Kopplung.** Weil die Kautionslogik in der Buchhaltung stecken sollte, musste die Buchhaltung selbst gebaut werden. Getrennt hätte ein Standardprodukt genügt.

**Das ist der praktische Kern der Subdomain-Einteilung:** Wenn ein Sonderfall eine ganze Generic Subdomain in die Eigenentwicklung zieht, ist die Grenze falsch gezogen.

**Der Aufwand einer Korrektur ist erheblich** — drei Jahre Entwicklung stehen im Raum. Das spricht nicht dagegen, es einzuordnen; es spricht dafür, den Befund bei der nächsten großen Änderung zu berücksichtigen.

---

## 6 · Was die Disponentin sagt

> „Ich weiß, dass in Landshut dienstags Bedarf ist, weil da ein Werk Schulungen macht. Das steht nirgends."

**Für die Einordnung:** Das bestätigt Core. Die 0,8 Prozent entstehen nicht durch das zugekaufte Modul, sondern durch Wissen, das im Unternehmen steckt. Genau das ist der Unterschied zum Wettbewerb — und genau das gehört in Software, nicht in Köpfe.

**Das Modul kann diese Regel nicht abbilden.** Deshalb kompensieren vier Menschen täglich.

**Für das Risiko:** Das Verkaufsargument des Unternehmens hängt an vier Personen. Zwei gehen binnen fünf Jahren.

| | |
|---|---|
| Eintrittswahrscheinlichkeit | hoch — Rente ist planbar |
| Auswirkung | die Erfüllungsquote sinkt, das Verkaufsargument entfällt |
| Vorlauf | fünf Jahre, wenn man jetzt beginnt |

**Vorschlag:** Bevor das Modul ersetzt wird, das Wissen erheben. Was die Disponenten tun und warum, ist die Anforderung an das neue System. Wer erst baut und dann fragt, baut das alte Modul nach.

---

## 7 · Die drei ersten Änderungen

### Erstens: Wissen der Disponenten erheben

| | |
|---|---|
| Risiko | hoch, mit Frist — zwei Personen gehen |
| Nutzen | ohne dieses Wissen ist jede Weiterentwicklung blind |
| Warum zuerst | die Frist läuft, unabhängig von allem anderen |

### Zweitens: Verfügbarkeitsdisposition selbst bauen

| | |
|---|---|
| Risiko | hoch — die Core Domain läuft auf einem Modul von 2017 mit Behelfslösungen |
| Nutzen | das Verkaufsargument wird ausbaufähig statt kompensiert |
| Warum zweitens | setzt Erstens voraus |

### Drittens: Flottenbeschaffung durch Branchenlösung ersetzen

| | |
|---|---|
| Risiko | gering |
| Nutzen | setzt Entwickler frei, die für Zweitens gebraucht werden |
| Warum drittens | die Leiterin Flotte sagt selbst, dass Branchenlösungen alles können. Geringster Widerstand |

**Nicht zuerst: die Buchhaltung.** Die Abweichung ist schwerwiegend, aber sie funktioniert und bindet nur zwei Entwickler. Der Umbau wäre groß und der Nutzen gering — man tauscht laufende Kosten gegen einmalige. Richtig wäre, sie bei der nächsten großen gesetzlichen Änderung neu zu bewerten.

**Nicht: Zeiterfassung und Dokumentenarchiv.** Beide sind gebaut und bezahlt. Ein Wechsel kostet mehr, als er spart. Der Befund ist eine Lehre für künftige Entscheidungen, kein Auftrag zur Korrektur.

---

## 8 · Die neue App

**Selbstöffnung ohne Tresenbesuch.**

**Die Prüffrage:** Würde ein Wettbewerber, der das genauso gut kann, uns gefährlich?

| Überlegung | |
|---|---|
| Können die Wettbewerber das? | Die großen Anbieter haben es. Es ist kein Alleinstellungsmerkmal |
| Ist es notwendig? | zunehmend — Erwartungshaltung der Kunden |
| Unterscheidet es uns? | nein, aber sein Fehlen fällt auf |

**Einordnung: Supporting.** Notwendig, um nicht zurückzufallen, aber kein Vorteil.

**Konsequenz:** Sparsam bauen oder zukaufen. Keine Eigenentwicklung mit den besten Leuten.

**Aber:** Es gibt eine Verbindung zur Core Domain. Wenn Selbstöffnung bedeutet, dass Fahrzeuge auch ohne besetzte Station ausgegeben werden können, erweitert das die Verfügbarkeit — und das ist Core.

**Die Unterscheidung:** Die App selbst ist Supporting. Die Frage, welche Fahrzeuge an unbesetzten Standorten verfügbar gemacht werden können, gehört zur Disposition und ist Core.

**Wie entschieden wird, bevor gebaut wird:** Die Einordnung gehört in den Vorschlag, mit Begründung. Ohne sie landet das Vorhaben bei dem, der Kapazität hat — so wie bisher.

---

## Diskussionsanschluss

Die Buchhaltung ist Generic, aber gebaut und bezahlt. Ein Wechsel kostet mehr als er spart. Wann ist eine falsche Einordnung ein Grund zum Handeln, und wann nur eine Lehre für das nächste Mal?
