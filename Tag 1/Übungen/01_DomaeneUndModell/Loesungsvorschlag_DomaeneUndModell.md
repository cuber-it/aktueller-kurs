# Lösungsvorschlag · Ein Sachverhalt, zwei Zwecke

**Vorbemerkung:** Ein Vorschlag. Modellentscheidungen sind Ermessenssache; bewertet wird, ob jeder Begriff **für den genannten Zweck** gebraucht wird.

---

## 1 · Modell „Werkstattarbeit disponieren"

### Fahrzeug

| | |
|---|---|
| Merkmale | Alter, Laufleistung, Reparaturhistorie, letzter Wartungstermin |
| Zustand | verfügbar · in der Werkstatt · zur Verwertung gemeldet |
| Regel | Solange es in der Werkstatt ist, kann die Station es nicht vermieten |

### Werkstattaufenthalt

| | |
|---|---|
| Merkmale | Anlass (Wartung oder Schaden), Beginn, durchgeführte Arbeiten |
| Regel | Endet erst, wenn die Arbeit fertig **und** der Prüfbericht unterschrieben ist |
| Regel | Erst danach wird das Fahrzeug wieder freigegeben |

### Wartungsfälligkeit

| | |
|---|---|
| Merkmale | berechneter Termin aus Kilometerstand und letztem Termin |
| Regel | Wird vom System berechnet und von der Disposition geprüft |
| Offen | Die Erfahrung „manche werden härter rangenommen" ist nicht abgebildet — siehe Aufgabe 9 |

### Schadensbefund

| | |
|---|---|
| Merkmale | Fotos von der Rückgabe, Rückgabeprotokoll, Bewertung |
| Bewertung | **Unfall** oder **Verschleiß** |
| Regel | Bei Verschleiß zahlt keine Versicherung |

### Prüfbericht

| | |
|---|---|
| Merkmale | unterschrieben ja/nein |
| Regel | Voraussetzung für die Freigabe |

### Verwertungsmeldung

| | |
|---|---|
| Anlass | Reparatur lohnt nicht mehr |
| Empfänger | Flotte |

**Sechs Begriffe.**

**Nicht im Modell**, weil für diesen Zweck nicht gebraucht: Mieter, Mietpreis, Kaution, Rahmenvertrag, Station als Vermieterin.

---

## 2 · Modell „Anmietung abrechnen"

### Rechnungsposition

| | |
|---|---|
| Merkmale | Fahrzeugkategorie, Zeitraum, Tagessatz |
| Regel | Ergibt sich aus einer abgeschlossenen Anmietung |

### Fahrzeugkategorie

| | |
|---|---|
| Merkmale | Bezeichnung (Kompakt, Kombi, Transporter) |
| Bemerkung | **kein konkretes Fahrzeug** |

### Kilometerabrechnung

| | |
|---|---|
| Merkmale | Freikilometer laut Vertrag, gefahrene Kilometer |
| Regel | Nur bei Überschreitung entsteht eine Position |

### Schadensbewertung

| | |
|---|---|
| Merkmale | Schaden aufgenommen ja/nein, Bewertung Unfall oder Verschleiß, bei Unfall die Versicherung |
| Regel | Die Bewertung entscheidet, wer die Rechnung erhält |

### Empfänger

| | |
|---|---|
| Merkmale | Firmenkunde oder Privat, Rahmenvertrag, Zahlungsvereinbarung |
| Regel | Bei Unfallschaden kann die Versicherung Empfänger sein |

**Fünf Begriffe.**

**Nicht im Modell:** konkretes Fahrzeug, Alter, Reparaturhistorie, Werkstattaufenthalt, Prüfbericht.

---

## 3 · Der Vergleich

| Begriff | Werkstatt | Abrechnung |
|---|---|---|
| Fahrzeug | ja, konkret | nur als Kategorie |
| Kilometerstand | ja, für Wartungsfälligkeit | ja, nur bei Freikilometer-Überschreitung |
| Schaden | ja, Befund und Bewertung | ja, nur die Bewertung |
| Werkstattaufenthalt | ja | nein |
| Prüfbericht | ja | nein |
| Reparaturhistorie | ja | nein |
| Empfänger, Rahmenvertrag | nein | ja |
| Tagessatz, Zeitraum | nein | ja |

**Zwei Begriffe überschneiden sich vollständig** (Schadensbewertung), **zwei teilweise** (Fahrzeug, Kilometerstand), **acht gar nicht**.

---

## 4 · Der Begriff „Fahrzeug"

| | Werkstatt | Abrechnung |
|---|---|---|
| Was gemeint ist | ein konkretes Auto mit Historie | eine Kategorie |
| Merkmale | Alter, Laufleistung, was schon dran war | Bezeichnung |
| Lebensdauer im Blick | Jahre | die Dauer einer Anmietung |
| Anzahl | 8.400 Einzelobjekte | acht Kategorien |

**Ist das dieselbe Sache?**

Nein. Die Werkstatt meint ein **Einzelobjekt**, die Abrechnung eine **Klasse von Objekten**. Herr Krause sagt ausdrücklich, welches konkrete Auto es war, interessiere ihn nicht.

Das ist kein Detailunterschied, sondern eine andere Sache mit demselben Namen. Die Zusammenführung ergäbe einen Widerspruch: 8.400 gegen 8.

**Dieser Befund führt direkt zu 1-3 und 1-5.** Er ist der erste Hinweis darauf, dass ein Modell für alles nicht trägt.

---

## 5 · „Wenn es hier ist, gehört es mir"

**Das ist eine Regel**, und zwar eine der wichtigsten im Werkstattmodell.

Sie sagt: Der Werkstattaufenthalt **entzieht** das Fahrzeug der Station. Solange er läuft, ist das Fahrzeug nicht vermietbar — unabhängig davon, wem es „auf dem Papier" gehört.

**Wo sie steht:** Als Regel am Begriff *Fahrzeug* oder am *Werkstattaufenthalt*. Beide Zuordnungen sind vertretbar; wichtig ist, dass sie **im Modell** steht und nicht als Randbemerkung.

**Warum das mehr ist als ein Merkmal:**

| | |
|---|---|
| Merkmal wäre | „Zustand: in der Werkstatt" |
| Regel ist | „In diesem Zustand ist Vermieten ausgeschlossen" |

Ein Merkmal beschreibt, eine Regel schließt aus. Wer nur das Merkmal führt, muss die Ausschlusslogik an jeder Stelle wiederholen, an der vermietet wird.

---

## 6 · Der Schaden in beiden Modellen

| | Werkstatt braucht | Abrechnung braucht |
|---|---|---|
| Fotos | ja | nein |
| Rückgabeprotokoll | ja | nein |
| Bewertung Unfall/Verschleiß | **erzeugt sie** | **nutzt sie** |
| Versicherung | nein | ja, bei Unfall |

**Wo die Information entsteht:** Die Bewertung entsteht in der **Werkstatt**. Frau Petrova sagt: „Manchmal sehe ich schon daran, dass es kein Unfall war, sondern Verschleiß."

**Wer sie braucht:** Die Abrechnung. Herr Krause sagt: „Danach entscheidet sich, wer die Rechnung bekommt."

**Was daraus folgt:** Zwischen den beiden Modellen fließt Information — die Bewertung. Alles andere am Schaden bleibt jeweils dort, wo es gebraucht wird.

Das ist der erste Fall einer **Übersetzung an einer Grenze**, ohne dass der Begriff schon eingeführt wäre.

---

## 7 · Ein gemeinsames Modell

Es müsste enthalten:

| Aus der Werkstatt | Aus der Abrechnung |
|---|---|
| Fahrzeug als Einzelobjekt | Fahrzeug als Kategorie |
| Alter, Laufleistung, Reparaturhistorie | Tagessatz, Zeitraum |
| Werkstattaufenthalt, Prüfbericht | Empfänger, Rahmenvertrag |
| Fotos, Rückgabeprotokoll | Zahlungsvereinbarung |
| Verwertungsmeldung | Freikilometer |

**Was auffällt — drei Dinge:**

**Erstens:** „Fahrzeug" müsste beides zugleich sein — Einzelobjekt und Kategorie. Das geht nur, wenn man zwei Begriffe daraus macht. Damit ist der Begriff, um den es geht, nicht mehr eindeutig.

**Zweitens:** Von rund vierzehn Merkmalen wären für jeden Zweck etwa fünf leer oder bedeutungslos. Herr Krause sähe Reparaturhistorien, Frau Petrova Zahlungsvereinbarungen.

**Drittens:** Die Regeln widersprechen sich nicht, aber sie gelten jeweils nur für einen Teil. „Bei Verschleiß zahlt keine Versicherung" ist für die Werkstatt eine Beobachtung, für die Abrechnung eine Entscheidungsregel.

---

## 8 · Der Preis eines gemeinsamen Modells

**Für die Werkstatt:**

- Sie sieht Merkmale, die sie nicht braucht und nicht beurteilen kann.
- Ihre Frage „was war schon dran" wird schwerer zu beantworten, weil sie zwischen Abrechnungsdaten liegt.
- Bei jeder Änderung an der Abrechnung muss geprüft werden, ob die Werkstatt betroffen ist.

**Für die Abrechnung:**

- Sie muss mit Einzelfahrzeugen umgehen, obwohl sie Kategorien abrechnet.
- Eine Auswertung „Umsatz je Kategorie" wird zur Aggregation über Einzelobjekte.
- Änderungen am Werkstattmodell betreffen sie ohne fachlichen Grund.

**Für beide:**

- Keiner kann sein Modell allein ändern.
- Die Frage „was bedeutet Fahrzeug" hat keine eindeutige Antwort mehr.

**Der Nutzen wäre:** eine Stelle statt zwei, keine Übersetzung nötig. Bei zwei Merkmalen, die tatsächlich gemeinsam gebraucht werden (Bewertung, Kilometerstand), ist das ein schlechtes Geschäft.

---

## 9 · Die Erfahrung „manche werden härter rangenommen"

**Gehört sie ins Modell?**

Zwei vertretbare Antworten:

| Antwort | Begründung |
|---|---|
| **Ja** | Sie beeinflusst eine fachliche Entscheidung — wann ein Fahrzeug zur Wartung muss. Was eine Entscheidung bestimmt, gehört ins Modell. |
| **Noch nicht** | Sie ist nicht ausformuliert. Solange niemand sagen kann, **woran** man es erkennt, lässt sie sich nicht abbilden. |

**Der gemeinsame Kern beider Antworten:** Die Erfahrung steckt in einem Kopf. Solange sie dort bleibt, ist die Wartungsplanung von einer Person abhängig.

**Der Modellierungsschritt** wäre, aus der Erfahrung ein Merkmal zu machen — etwa eine Einsatzart oder ein Belastungsprofil je Fahrzeug. Das ist keine technische Frage, sondern eine an Frau Petrova.

**Was nicht ins Modell gehört:** die Erfahrung als solche. Ein Modell kann kein „Bauchgefühl" abbilden. Es kann abbilden, **woran** sich das Bauchgefühl festmacht — sobald das benannt ist.

---

## 10 · Die Frage an Frau Petrova

Mehrere funktionieren. Die beste zielt auf das **Merkmal**, nicht auf die Erfahrung:

> **„Woran sehen Sie, dass ein Fahrzeug härter rangenommen wurde?"**

Mögliche Antworten und was daraus folgt:

| Antwort | Modellierung |
|---|---|
| „An der Station — die Bergstandorte sind härter" | Merkmal *Standortprofil* |
| „An der Kundenart — Handwerker fahren anders" | Merkmal *Einsatzart* am Mietvorgang |
| „Am Fahrzeugtyp — die Transporter" | schon vorhanden, nur nicht genutzt |
| „Das kann ich nicht sagen, das sehe ich einfach" | nicht modellierbar; dann bleibt die Prüfung menschlich, und das ist ein Befund |

**Was nicht funktioniert:** „Können Sie Ihre Erfahrung formalisieren?" — die Antwort ist nein, weil die Frage zu abstrakt ist.

**Die zweite gute Frage:** „Bei welchen Fahrzeugen lagen Sie zuletzt daneben?" — Fehler sind oft aufschlussreicher als Regeln.

---

## Diskussionsanschluss

Beide Modelle sind klein — sechs und fünf Begriffe. Ein System, das beide Zwecke bedient, hat vermutlich eine Tabelle mit vierzig Spalten. Wo ist der Unterschied entstanden?
