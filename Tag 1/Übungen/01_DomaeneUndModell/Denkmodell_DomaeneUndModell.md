# Denkmodell · Ein Modell an der Fachlichkeit ausrichten

Vier Stufen: **Signale → Erkenntnisse → Optionen → Entscheidung.**

---

## Stufe 1 · Signale

### Im Code

| Signal | Konkret |
|---|---|
| Klassen entsprechen 1:1 den Tabellen | die Speicherung bestimmt die Struktur |
| Technische Begriffe in Klassennamen | `Kopf`, `Position`, `Historie`, `Zuordnung`, `Mapping` |
| Nur Getter und Setter | das Modell trägt Daten, kein Verhalten |
| Statuscodes als Zahlen | `statusCode = 2` statt `Laufend` |
| Wahrheitswerte für fachliche Sachverhalte | `fahrerlaubnisGeprueft` — geprüft, aber mit welchem Ergebnis? |
| Klassen namens `…Service`, `…Manager`, `…Helper` | die Regeln liegen außerhalb des Modells |
| Ungültige Zustände sind konstruierbar | nichts hindert daran |
| Eine Regel steht an mehreren Stellen | es gibt keinen Ort dafür |

### Im Gespräch

| Signal | Beispiel |
|---|---|
| Der Fachbereich erkennt die Begriffe nicht | „Was ist eine Mietvertragsposition?" |
| Entwickler übersetzen bei jedem Gespräch | „Sie meinen die Verlängerung — bei uns ein Positionssatz" |
| „Wo findet X statt?" hat keine kurze Antwort | |
| Einarbeitung beginnt beim Datenmodell | die Fachlichkeit kommt danach |
| Ein Fehler braucht Tage zur Lokalisierung | obwohl die Berechnung stimmt |

---

## Stufe 2 · Erkenntnisse

**1. Ein Modell ist eine Auswahl, kein Abbild.**
Es entscheidet, was für einen Zweck wichtig ist. Was weggelassen wird, gehört zum Modell.

**2. Ein normalisiertes Schema ist kein fachliches Modell.**
Normalisierung vermeidet Redundanz — eine Eigenschaft der Speicherung. Beides kann gleichzeitig gelten: sauberes Schema, unbrauchbares Modell.

**3. Wo die Regel nicht im Modell steht, steht sie überall.**
Jeder Weg zum Modell muss sie kennen. Im Ticketfall waren es drei, und einer kannte sie anders.

**Was gesucht wird:** ein Modell, das die Fragen des Betriebs beantwortet und die Sprache des Fachbereichs trägt.

---

## Stufe 3 · Optionen

| Option | Käme in Frage, wenn |
|---|---|
| **Fachliches Modell mit Verhalten** | Regeln gelten und geschützt werden sollen |
| **Datenmodell mit Diensten** | vor allem gelesen und ausgewertet wird |
| **Umbenennung** | die Struktur stimmt, nur die Namen nicht |
| **Getrenntes Lese- und Schreibmodell** | beides gebraucht wird und sich widerspricht |
| **Nichts ändern** | das System stabil ist und selten geändert wird |

---

## Stufe 4 · Entscheidung

### Frage 1 — Erkennt der Fachbereich seine Begriffe wieder?

- **Ja** → das Modell trägt die Sprache. Weiter mit Frage 2.
- **Nein** → die Begriffe fehlen. Eine Umbenennung allein genügt nicht, wenn auch die Struktur nicht passt.

Der Prüfstein: Kann ein Fachvertreter das Modell lesen und sagen, ob es stimmt? Wenn ein Entwickler übersetzen muss, prüft der Fachvertreter die Übersetzung, nicht das Modell.

### Frage 2 — Gibt es einen Ort für jeden fachlichen Vorgang?

- **Ja** → eine Änderung ist lokalisierbar.
- **Nein**, ein Vorgang ist über mehrere Strukturen verteilt → der Begriff fehlt im Modell.

Die praktische Form: *Wo findet eine Verlängerung statt?* Wenn die Antwort fünf Klassen nennt, gibt es keinen Ort.

### Frage 3 — Sind ungültige Zustände konstruierbar?

- **Nein**, das Modell verweigert sie → gut.
- **Ja**, es verlässt sich auf den aufrufenden Code → jede Zugriffsstelle ist mitverantwortlich.

Der Unterschied zwischen einer **Zusicherung** und einer **Absprache**. Absprachen halten, bis jemand sie nicht kennt.

### Frage 4 — Wird mehr gelesen oder mehr entschieden?

- **Entschieden** — Regeln, Zustandsübergänge, Zulässigkeit → fachliches Modell mit Verhalten.
- **Gelesen** — Auswertungen, Berichte, Suchen → ein Datenmodell ist angemessen.
- **Beides, im Widerspruch** → getrennte Modelle für Lesen und Schreiben.

Diese Frage entscheidet, ob der Aufwand gerechtfertigt ist. Ein Auswertungssystem braucht kein Verhalten.

---

## Der Denkweg auf einen Blick

```
Fachliche Fragen sind im Code nicht beantwortbar
        ↓
Das Modell folgt der Speicherung statt der Fachlichkeit
        ↓
Optionen: fachliches Modell · Datenmodell · Umbenennung · Trennung
        ↓
Erkennt der Fachbereich die Begriffe?      nein → Begriffe fehlen
        ↓ ja
Gibt es einen Ort je Vorgang?              nein → Begriff fehlt im Modell
        ↓ ja
Sind unguelt. Zustaende konstruierbar?     ja → Regeln gehoeren ins Modell
        ↓ nein
Mehr gelesen oder mehr entschieden?        gelesen → Datenmodell genuegt
        ↓ entschieden
                    FACHLICHES MODELL MIT VERHALTEN
```

---

## Die eine Prüffrage

> **Kann ein Fachvertreter dieses Modell lesen und sagen, ob es stimmt?**

---

## Gegenproben

| Prüfung | Wenn ja, dann |
|---|---|
| Wird das System vor allem ausgewertet? | ein Datenmodell ist angemessen |
| Ist das System stabil und wird selten geändert? | der Umbau lohnt nicht |
| Stimmt die Struktur, nur die Namen nicht? | eine Umbenennung genügt |
| Braucht man beides — Regeln und freie Auswertung? | getrennte Modelle prüfen |
| Sind die Regeln trivial? | Verhalten im Modell wäre Überbau |

---

## Wenn die Entscheidung steht

**Der Schutz kostet Flexibilität.**
Ein Modell, das ungültige Zustände verweigert, verweigert sie auch bei einer berechtigten Korrektur, bei einer Datenmigration und beim Import von Altdaten. Für diese Fälle braucht es eigene Wege — bewusst gebaut, nicht durch Umgehung.

**Auswertungen werden schwieriger.**
Wo Daten hinter Methoden liegen, ist „alle Verlängerungen im März nach Station" keine Abfrage mehr. Die übliche Antwort ist ein eigenes Lesemodell, das aus denselben Daten gespeist wird.

**Ein Wahrheitswert für einen fachlichen Sachverhalt ist ein Warnzeichen.**
`fahrerlaubnisGeprueft` komprimiert eine Aussage auf ein Bit und verliert, worum es ging. Solche Felder zeigen zuverlässig an, dass ein Begriff fehlt.

**Zustandscodes als Zahlen ebenfalls.**
`statusCode = 2` bedeutet etwas, das nirgends steht. Ein benannter Zustand trägt die Bedeutung mit sich.

**Das Modell muss nicht alles abbilden.**
Es ist eine Auswahl für einen Zweck. Was ein anderer Kontext braucht, gehört nicht hinein — auch wenn es dieselben Daten sind.

**Die Umbenennung ist der billigste erste Schritt und der schwächste.**
Sie verbessert die Lesbarkeit, ohne die Struktur zu ändern. Wer sie für erledigt hält, hat den Aufwand ohne den Nutzen.

---

## Verwechslungen, die im Alltag vorkommen

| Verwechselt mit | Erkennungszeichen |
|---|---|
| Datenmodell | beschreibt Speicherung, nicht Fachlichkeit — beide können gleichzeitig richtig sein |
| Klassendiagramm | eine Darstellung, kein Modell |
| Normalisierung | eine Eigenschaft der Speicherung |
| Objektorientierung | Klassen mit Gettern und Settern sind noch kein fachliches Modell |
| Anforderungsdokument | beschreibt, was gebaut wird, nicht wie die Fachlichkeit strukturiert ist |
