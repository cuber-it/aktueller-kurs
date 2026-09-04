# Lösungsvorschlag · Die Ablösung zu Ende bringen

---

## 1 · Die Umschaltkriterien

### Stufe 1 · Reservierung und Verfügbarkeit

> **Das Altsystem wird für Reservierungen abgeschaltet, wenn 30 Tage lang keine Reservierung mehr dort angelegt wurde und der Abgleich in dieser Zeit keine Abweichung im Reservierungsbestand gemeldet hat.**

**Überprüfbar:** ja — beides ist zählbar.
**Zeitpunkt:** der 30. Tag ohne Ereignis.

### Stufe 2 · Anmietung und Rückgabe

> **Das Altsystem wird für Anmietungen abgeschaltet, wenn alle 140 Stationen mindestens 30 Tage ohne Rückfall im neuen System gearbeitet haben.**

**Überprüfbar:** ja — je Station zählbar.
**Zeitpunkt:** 30 Tage nach Umstellung der letzten Station.

**Der Zusatz „ohne Rückfall" ist wichtig:** Er schließt aus, dass eine Station formal umgestellt ist und im Störungsfall auf das Alte zurückgreift.

### Stufe 3 · Abrechnung und Auswertung

> **Das Altsystem wird abgeschaltet, wenn drei aufeinanderfolgende Monatsabrechnungen vollständig aus dem neuen System erstellt wurden und die Ergebnisse mit der Vergleichsrechnung aus dem Altsystem übereinstimmen.**

**Überprüfbar:** ja — drei Abrechnungsläufe, ein Vergleich.
**Zeitpunkt:** nach dem dritten Monat.

**Warum drei:** Ein Monat kann zufällig stimmen. Drei decken Monats-, Quartals- und Sonderfälle ab.

---

## 2 · Warum „sobald Stufe 3 fertig ist" kein Kriterium ist

**Es fehlt die Definition von „fertig".**

| Was „fertig" bedeuten könnte | |
|---|---|
| Alle geplanten Funktionen umgesetzt | wer entscheidet, was geplant war? |
| Keine offenen Fehler | es gibt immer offene Fehler |
| Der Fachbereich ist zufrieden | nicht überprüfbar |
| Die Abnahme ist erfolgt | wann findet sie statt? |

**Ein Kriterium braucht drei Eigenschaften:**

1. **Überprüfbar** — jemand kann eindeutig ja oder nein sagen
2. **Zeitpunkt** — es tritt an einem bestimmten Tag ein
3. **Unabhängig von Meinung** — niemand kann es durch Bewertung verschieben

„Fertig" hat keine davon.

---

## 3 · Stufe 1 heute

**Wäre das Kriterium erfüllt?**

Vermutlich ja, was die Reservierungen betrifft — seit 2019 werden neue Reservierungen im neuen System angelegt.

**Was an der Abschaltung hindert:**

| Hindernis | Art |
|---|---|
| Der Abgleich läuft in beide Richtungen | technisch, aber lösbar |
| Die drei Stationen brauchen das Altsystem für Anmietungen | dort liegen auch Reservierungsdaten |
| Das Controlling zieht Auswertungen aus dem Altsystem | siehe Aufgabe 10 |
| Die Abrechnung greift auf beide zu | siehe Aufgabe 4 |

**Der Befund:** Stufe 1 ist seit sieben Jahren abschaltbereit. Sie wird nicht abgeschaltet, weil **andere Stufen** das Altsystem noch brauchen.

**Das ist die eigentliche Erkenntnis:** Die Stufen sind nicht unabhängig. Solange irgendetwas das Altsystem braucht, läuft alles weiter.

---

## 4 · Der Zirkel

**Die Abrechnung** kann erst umgestellt werden, wenn nur noch ein System läuft.
**Das Altsystem** kann erst abgeschaltet werden, wenn die Abrechnung umgestellt ist.

**Ein Zirkel.** Beide warten aufeinander.

**Warum er entstanden ist:** Die Abrechnung wurde als **letzte** Stufe geplant, obwohl sie von **allen** Daten abhängt. Wer zuletzt umstellt, was alles braucht, wartet auf alles.

**Die Auflösung:** Die Abrechnung muss **während** des Parallelbetriebs umgestellt werden — nicht danach.

Konkret: Sie zieht künftig nur aus dem neuen System. Für die Vorgänge der drei alten Stationen wird ein Weg gebaut, der sie ins neue überträgt — nicht abgleicht, sondern überträgt.

**Damit ist der Zirkel gebrochen:** Die Abrechnung wartet nicht mehr auf die Abschaltung, sondern die Abschaltung auf die Abrechnung.

---

## 5 · Die Reihenfolge

| # | Schritt | Vorher erfüllt sein muss |
|---|---|---|
| 1 | Die drei Stationen umstellen | nichts — sofort machbar, sechs Wochen |
| 2 | Historische Auswertungsdaten übertragen | siehe Aufgabe 10 |
| 3 | Abrechnung auf das neue System umstellen | Schritt 1 (alle Vorgänge im Neuen) |
| 4 | Abgleich auf eine Richtung reduzieren (Neu → Alt) | Schritte 1 und 3 |
| 5 | Stufe-3-Kriterium prüfen: drei Monate Abrechnung | Schritt 3 |
| 6 | Abgleich abschalten | Schritt 5 |
| 7 | Altsystem abschalten | Schritte 2, 5, 6 |

**Der erste Schritt ist der wichtigste** — und der, der seit 2022 nicht getan wurde.

**Schritt 4 ist ein Zwischenziel:** Ein einseitiger Abgleich ist erheblich einfacher als ein beidseitiger. Er sichert nur noch den Rückweg, falls etwas schiefgeht.

---

## 6 · Die Rechnung zu den drei Stationen

| Größe | Wert |
|---|---|
| Umstellung | 3 Stationen × 2 Wochen = 6 Wochen ≈ 30 Arbeitstage |
| Parallelbetrieb | 2,1 Vollzeitstellen ≈ 420 Arbeitstage im Jahr |

**Aber:** Die Umstellung der drei Stationen beendet den Parallelbetrieb nicht allein — sie ist nur eine Voraussetzung.

**Die ehrliche Rechnung:**

| | |
|---|---|
| Umstellung der Stationen | 30 Arbeitstage |
| Anteil am Parallelbetrieb, der dadurch entfällt | schwer zu beziffern; die Stationen sind ein Hindernis von mehreren |

**Was sich beziffern lässt:** Der Parallelbetrieb kostet seit 2022 rund 420 Arbeitstage im Jahr, also etwa 1.680 Arbeitstage in vier Jahren. Die Stationsumstellung kostet 30.

**Selbst wenn sie nur ein Fünftel des Hindernisses beseitigt**, hätte sich der Aufwand nach wenigen Wochen amortisiert.

**Der eigentliche Befund:** Niemand hat je gerechnet. Die Kosten des Parallelbetriebs wurden erst 2026 beziffert — nach sieben Jahren.

---

## 7 · Die übernommenen Begriffe

| Begriff | Bleiben oder entfallen | Begründung |
|---|---|---|
| **Kundenbegriff mit 47 Merkmalen** | **entfallen** | Er war die Ursache des Sprachkonflikts. Im neuen Modell gibt es vier Kontexte mit eigenen Kundenbegriffen |
| **Statuscode mit 14 Ausprägungen** | **entfallen** | Ersetzt durch benannte Zustände je Aggregate |
| **Stationsnummernkreis** | **bleiben** | Er ist fachlich etabliert; Stationen werden im Betrieb über diese Nummer angesprochen |
| **Vorgangsnummer im alten Format** | siehe Aufgabe 9 | |

**Der Unterschied:** Kundenbegriff und Statuscode sind **technische Altlasten**, die nur wegen des Abgleichs existieren. Der Stationsnummernkreis ist ein **fachlicher Begriff**, den der Betrieb verwendet.

**Der Prüfstein:** Verwendet der Fachbereich ihn? Dann bleibt er. Wurde er nur nachgebildet, damit der Abgleich funktioniert? Dann entfällt er.

---

## 8 · Was den Kundenbegriff verhindert hätte

**Eine Übersetzung an der Grenze, in beide Richtungen.**

Der Abgleich brauchte den alten Kundenbegriff — aber nur **an der Grenze**, nicht im neuen Modell.

| Was geschah | Was hätte geschehen sollen |
|---|---|
| Der alte Begriff wurde im neuen Modell nachgebildet | Der alte Begriff bleibt an der Grenze; die Übersetzung erzeugt daraus neue Begriffe |
| Der Abgleich liest und schreibt direkt im neuen Modell | Der Abgleich spricht mit der Übersetzung, nicht mit dem Modell |

**Der Aufwand:** Eine Übersetzung mit 47 Merkmalen auf vier Kontexte ist aufwendig — und genau deshalb wurde sie nicht gebaut.

**Der Preis dieser Ersparnis:** Der Kundenbegriff ist im neuen System und muss dort wieder herausoperiert werden.

**Die Lehre:** Die Übersetzung an der Grenze ist die teuerste Einzelmaßnahme einer Ablösung — und die, deren Fehlen am teuersten wird.

---

## 9 · Die Vorgangsnummer

**Dafür:**

- Kunden und Partner kennen sie; sie steht auf Rechnungen und in Verträgen
- Der Vermittler verwendet sie in seinen Systemen
- Ein Formatwechsel bedeutet Abstimmung mit allen Beteiligten

**Dagegen:**

- Das Format stammt aus 2009 und hat einen begrenzten Nummernkreis
- Es enthält eine Stationskennung, die bei stationsübergreifenden Vorgängen nicht mehr passt

**Vorschlag: bleiben, aber begrenzt.**

Die vorhandenen Nummern bleiben gültig. Für neue Vorgänge wird das Format beibehalten, solange der Nummernkreis reicht. Die Ablösung des Formats wird als eigenes Vorhaben geführt — nicht als Teil der Systemablösung.

**Begründung:** Ein Formatwechsel während einer Ablösung erhöht das Risiko ohne Not. Zwei Änderungen gleichzeitig sind schwerer zu beurteilen als zwei nacheinander.

---

## 10 · Die historischen Auswertungen

**Das Problem:** Das Controlling zieht aus dem Altsystem, weil die Zahlen bis 2009 zurückreichen. Im neuen beginnen sie 2019.

**Drei Wege:**

| Weg | Bewertung |
|---|---|
| **Altdaten ins neue System übertragen** | aufwendig — die alten Begriffe passen nicht auf das neue Modell |
| **Auswertungsdaten getrennt aufbewahren** | ein eigener Bestand nur für Auswertungen, gespeist aus beiden Systemen |
| **Altsystem als Nur-Lese-Archiv behalten** | scheinbar einfach, hält aber das Altsystem am Leben |

**Der Vorschlag: der zweite Weg.**

Ein Auswertungsbestand, der die Kennzahlen enthält — nicht die Vorgänge. Aus dem Altsystem einmalig gefüllt für 2009 bis 2019, aus dem neuen laufend fortgeschrieben.

**Warum nicht der dritte:** Ein Nur-Lese-Altsystem ist immer noch ein System. Es braucht Betrieb, Sicherung, gelegentlich Wartung — und irgendwann läuft die Plattform darunter aus.

**Warum nicht der erste:** Vorgänge aus 2009 auf ein Modell von 2019 zu übertragen bedeutet, die alten Begriffe zu übersetzen — für Daten, die niemand mehr im Einzelnen ansieht.

**Der Kern:** Für Auswertungen braucht man Kennzahlen, nicht Vorgänge. Das ist ein kleinerer Gegenstand.

---

## 11 · Zwei Risiken

**Erstens: Die Abrechnungsumstellung während des Parallelbetriebs.**

Sie bricht den Zirkel, verlagert aber Risiko: Wenn die Abrechnung aus dem neuen System falsch rechnet, fällt es erst bei der Monatsabrechnung auf.

**Gegenmaßnahme:** Die drei Vergleichsmonate aus dem Kriterium für Stufe 3 sind genau dafür da — beide Systeme rechnen parallel, die Ergebnisse werden verglichen.

**Zweitens: Die Übertragung der Vorgänge aus den drei Stationen.**

Sie ist ein einmaliger Weg, der gebaut, geprüft und danach weggeworfen wird. Solche Wege sind fehleranfällig, weil sie nur einmal laufen.

**Gegenmaßnahme:** Erst mit einer Station, dann prüfen, dann die übrigen zwei.

---

## 12 · Wer entscheidet

**Die Abschaltung entscheidet, wer den Parallelbetrieb bezahlt** — also die Leitung, die das Budget verantwortet.

**Nicht die IT-Leitung allein:** Sie hat sieben Jahre lang die Entscheidung nicht getroffen, weil sie sie technisch begründen musste und immer ein Hindernis fand.

**Woran sie es festmacht:** an den Kriterien aus Aufgabe 1. Sie sind so formuliert, dass jemand ohne technische Kenntnis prüfen kann, ob sie erfüllt sind.

**Der Zusatz, der fehlt:** Ein Termin, an dem die Kriterien **überprüft** werden — nicht erfüllt sein müssen, sondern angesehen werden. Monatlich, mit Bericht.

**Warum das wirkt:** Die Kosten des Parallelbetriebs waren sieben Jahre lang unsichtbar. Ein monatlicher Bericht macht sie sichtbar — und das ist wirksamer als ein vierter Termin.

---

## Diskussionsanschluss

Die drei Stationen hätten seit 2023 umgestellt werden können. Niemand hat es beauftragt, weil das Altsystem ohnehin lief. Was hätte diese Entscheidung erzwungen?
