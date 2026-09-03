# Lösungsvorschlag · Zwei Modelle für denselben Sachverhalt

---

## 1 · Begriffe aus Material A, die in Modell 1 fehlen

| Begriff des Fachbereichs | In Modell 1 |
|---|---|
| **Vorgang** | nicht vorhanden — es gibt `MietvertragKopf` |
| **Verlängerung** | als `positionsTyp = 2` codiert |
| **offen** (Vorgang bleibt offen) | teilweise über `statusCode`, aber nicht als Begriff |
| **ausgeben** | nicht vorhanden — nur `statusCode = 2` |
| **abschließen** | nicht vorhanden — nur `statusCode = 4` |
| **gültige Fahrerlaubnis** | als Wahrheitswert `fahrerlaubnisGeprueft` |
| **Schaden, Tankfüllung, Kaution als offene Punkte** | drei getrennte Mechanismen |

Sieben Begriffe, die im Gespräch selbstverständlich sind und im Modell nicht vorkommen.

**Bemerkenswert:** Die Stationsleiterin sagt kein einziges Mal „Kopf", „Position" oder „Statuscode". Diese Wörter stammen aus der Datenhaltung.

---

## 2 · Wo sie in Modell 2 auftauchen

| Begriff | In Modell 2 |
|---|---|
| Vorgang | die Klasse `Mietvorgang` |
| Verlängerung | `verlaengernBis(datum)` und `Zeitraum.verlaengertUm` |
| offen | `offenePunkte`, Liste von `OffenerPunkt` |
| ausgeben | `ausgeben(fahrerlaubnis)` |
| abschließen | `abschliessen()` |
| gültige Fahrerlaubnis | Parameter von `ausgeben` |
| offene Punkte | eigene Klasse mit drei Arten |

**Alle sieben sind wiederzufinden** — als Klasse, Methode oder Feld. Das ist der Unterschied zwischen einem Modell, das die Fachlichkeit trägt, und einem, das Daten trägt.

---

## 3 · „Verlängern geht nur einmal"

### In Modell 1

**Nirgends im Modell.** Die Regel müsste in `MietvertragService` stehen, etwa:

> Zähle Positionen mit `positionsTyp = 2` für diesen Kopf. Wenn ≥ 1, ablehnen.

**Die Folgen:**

- Wer eine Position direkt anlegt, umgeht die Regel.
- Die Regel steht an so vielen Stellen, wie es Wege zur Verlängerung gibt — im Vorfall AV-2088 waren es drei.
- Nichts im Modell verrät, dass es die Regel gibt.

### In Modell 2

In `verlaengernBis(datum)`. Der `Zeitraum` weiß, ob er bereits verlängert wurde.

**Die Folgen:**

- Es gibt genau einen Weg zu verlängern.
- Die Regel ist dort, wo sie gilt.
- Wer die Klasse liest, sieht die Regel.

---

## 4 · „Ausgeben nur bei Fahrerlaubnis und Kaution"

### In Modell 1

In einem Dienst, der `fahrerlaubnisGeprueft` und `kautionStatusCode` prüft, bevor er `statusCode` auf 2 setzt.

**Das Problem:** `statusCode` ist ein setzbares Feld. Jeder Code, der `setStatusCode(2)` aufruft, umgeht die Prüfung. Das Modell schützt sich nicht.

### In Modell 2

Zweistufig:

- `kannAusgegebenWerden()` beantwortet die Frage mit Begründung — für die Oberfläche, die eine Schaltfläche ausgraut.
- `ausgeben(fahrerlaubnis)` führt die Prüfung erneut durch und verweigert, wenn sie nicht erfüllt ist.

**Es gibt keinen Setter für den Zustand.** Der Übergang von `Reserviert` zu `Laufend` ist nur über `ausgeben()` erreichbar.

---

## 5 · Der widersprüchliche Zustand

**Fachlich möglich?** Nein. Material A sagt: „Wenn was offen ist — Schaden, Tankfüllung, Kaution — bleibt der Vorgang offen."

Ein abgeschlossener Vorgang mit unerledigtem Schaden ist ein Widerspruch.

**Was das über Modell 1 sagt:**

Das Modell **erlaubt ungültige Zustände**. Es verhindert sie nicht, sondern verlässt sich darauf, dass der aufrufende Code sie vermeidet.

Damit ist jede Stelle, die auf das Modell zugreift, mitverantwortlich für die fachliche Richtigkeit. Bei drei Verlängerungswegen bedeutet das drei Stellen, die es richtig machen müssen — und eine, die es nicht tat.

**In Modell 2:** `abschliessen()` prüft die offenen Punkte und verweigert. Der Zustand ist nicht konstruierbar.

**Die allgemeine Regel:** Ein Modell sollte ungültige Zustände **unmöglich** machen, nicht nur unerwünscht. Der Unterschied ist der zwischen einer Zusicherung und einer Absprache.

---

## 6 · Der Wahrheitswert `fahrerlaubnisGeprueft`

**Was fehlt, gemessen an Material A:**

Die Stationsleiterin sagt „**gültige** Fahrerlaubnis". Ein Wahrheitswert `geprueft` beantwortet eine andere Frage:

| Frage | `fahrerlaubnisGeprueft` |
|---|---|
| Wurde geprüft? | ja |
| War das Ergebnis positiv? | **nicht ablesbar** |
| Wann wurde geprüft? | nicht ablesbar |
| Ist die Prüfung noch gültig? | nicht ablesbar |
| Welche Fahrerlaubnisklasse? | nicht ablesbar |

Ein `true` kann bedeuten: geprüft und gültig — oder geprüft und ungültig, mit einer Ablehnung an anderer Stelle.

**In Modell 2** ist die Fahrerlaubnis ein Parameter von `ausgeben()`. Damit ist sie zum Zeitpunkt der Ausgabe vorzulegen, und ihre Beschaffenheit kann geprüft werden.

**Das Muster dahinter:** Ein Wahrheitswert komprimiert eine fachliche Aussage auf ein Bit und verliert dabei, worum es ging. Solche Felder sind ein verlässliches Zeichen dafür, dass ein Begriff fehlt.

---

## 7 · Welches Modell dem Fachvertreter vorlegen?

**Modell 2.**

Er liest `Mietvorgang`, `ausgeben`, `verlaengernBis`, `abschliessen`, `offenePunkte` — alles Begriffe, die er selbst verwendet. Er kann sagen: „Verlängern geht nur einmal, das stimmt" oder „Nein, bei Firmenkunden auch zweimal."

**Bei Modell 1** müsste ein Entwickler übersetzen: „`positionsTyp = 2` bedeutet Verlängerung." Nach der Übersetzung prüft der Fachvertreter die Übersetzung, nicht das Modell.

**Das ist der praktische Kern:** Ein Modell, das der Fachbereich nicht lesen kann, kann er auch nicht prüfen. Fehler bleiben, bis sie im Betrieb auffallen — im Ticketfall vier Monate lang.

---

## 8 · Welches ist einfacher?

**Kommt darauf an, was gemessen wird.**

| Maß | Modell 1 | Modell 2 |
|---|---|---|
| Zahl der Felder | mehr | weniger |
| Zahl der Methoden | fast keine | mehrere je Klasse |
| Aufwand, ein Feld zu lesen | gering | gering |
| Aufwand, eine fachliche Frage zu beantworten | **hoch** — mehrere Klassen, Regel woanders | gering — eine Methode |
| Aufwand, etwas Falsches zu tun | **gering** | hoch — das Modell wehrt sich |
| Zahl der Stellen, die eine Regel kennen müssen | viele | eine |

**Modell 1 ist einfacher zu bauen. Modell 2 ist einfacher zu benutzen.**

Der Unterschied zeigt sich nicht bei der Erstellung, sondern bei der zwanzigsten Änderung. Im Ticketfall nach fünfzehn Jahren: elf Tage Analyse für eine Korrektur.

**Einfachheit ist keine Eigenschaft des Codes, sondern der Fragen, die man damit beantworten muss.**

---

## 9 · Was Modell 1 kann und Modell 2 nicht

Mindestens vier Punkte:

**Beliebige Auswertungen.** Modell 1 legt alle Daten offen. Eine Auswertung „alle Verlängerungen im März nach Station" ist eine Abfrage. In Modell 2 müsste dafür eine Methode existieren oder ein Lesemodell danebengestellt werden.

**Nachträgliche Korrekturen.** Wenn ein Datensatz falsch ist, lässt er sich in Modell 1 direkt richtigstellen. Modell 2 verweigert Zustände, die es für ungültig hält — auch bei einer berechtigten Korrektur. Dafür braucht es einen eigenen Weg.

**Historie.** `FahrzeugStatusHistorie` und `PreisHistorie` halten den Verlauf fest. Modell 2 kennt nur den aktuellen Zustand; die Historie müsste ergänzt werden.

**Datenmigration und Import.** Beim Einspielen von Altdaten passen nicht alle Sätze zu den heutigen Regeln. Modell 1 nimmt sie, Modell 2 lehnt sie ab.

**Die Abwägung:** Modell 2 kauft Schutz mit Flexibilität. Wo Auswertung, Korrektur und Migration wichtiger sind als Regelsicherheit, ist Modell 1 nicht falsch — es ist dann aber eine bewusste Entscheidung und keine Folge der Datenbankstruktur.

---

## Diskussionsanschluss

Modell 2 erschwert Auswertungen, weil es Daten hinter Methoden verbirgt. Wie beantworten Sie „alle Verlängerungen im März nach Station", ohne das Modell aufzuweichen?
