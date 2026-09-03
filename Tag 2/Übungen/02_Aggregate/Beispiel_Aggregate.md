# Beispiel · Konsistenzgrenzen in klein

Ein Sachverhalt, vier Regeln, vollständig durchgeführt.

---

## Die Ausgangslage

Eine Bibliothek. Der Kontext **Ausleihe**.

Bestandteile:

| # | Bestandteil |
|---|---|
| 1 | Benutzerkonto |
| 2 | Ausleihen des Benutzers |
| 3 | Exemplare im Bestand |
| 4 | Vormerkungen auf Titel |
| 5 | Öffnungszeiten der Zweigstelle |

## Die Regeln

| # | Regel | Aussage der Bibliothekarin |
|---|---|---|
| R1 | Ein Exemplar ist entweder verfügbar oder ausgeliehen | „Das muss stimmen, sonst gebe ich zweimal dasselbe raus" |
| R2 | Ein Benutzer darf höchstens 20 Medien gleichzeitig haben | „Wenn er kurz 21 hat, ist das nicht schlimm — beim nächsten Mal fällt es auf" |
| R3 | Wer überzogene Medien hat, darf nichts ausleihen | „Das prüfe ich beim Rausgeben, das muss sitzen" |
| R4 | Ein vorgemerkter Titel wird dem Wartenden zugeteilt | „Wenn das eine Stunde dauert, merkt es keiner" |

---

## Schritt 1 · Die Dringlichkeit

| Regel | Einordnung | Beleg |
|---|---|---|
| R1 | **sofort** | „sonst gebe ich zweimal dasselbe raus" |
| R2 | **zeitnah** | „wenn er kurz 21 hat, ist das nicht schlimm" |
| R3 | **sofort** | „das muss sitzen" |
| R4 | **zeitnah** | „wenn das eine Stunde dauert, merkt es keiner" |

**Zwei von vier sofort.** Wie in der großen Übung: Der überwiegende Teil der Regeln verträgt Verzögerung.

## Schritt 2 · Die Klammern

### Klammer A · Exemplar

| | |
|---|---|
| Enthält | ein Exemplar, sein Zustand (verfügbar, ausgeliehen, in Bearbeitung) |
| Regel | R1 |
| Exemplare | eines je physischem Buch |

### Klammer B · Benutzerkonto

| | |
|---|---|
| Enthält | Benutzer, seine laufenden Ausleihen, Anzahl überzogener Medien |
| Regel | R3 — die Ausleihsperre muss beim Ausleihen sofort gelten |
| Exemplare | eines je Benutzer |

### Vormerkungen

Keine Klammer. R4 gilt zeitnah; jede Vormerkung steht für sich.

### Öffnungszeiten

Keine Konsistenzklammer — eine Ordnungseinheit für selten Geändertes.

## Schritt 3 · Die Regel über die Grenze

**R1 betrifft Klammer A**, R3 betrifft Klammer B. Eine Ausleihe berührt beide.

| Was geschieht | Wo |
|---|---|
| Prüfen, ob der Benutzer ausleihen darf | Klammer B |
| Exemplar auf „ausgeliehen" setzen | Klammer A |
| Ausleihe im Konto vermerken | Klammer B |

**Zwei Klammern in einem Vorgang.** Nach der Faustregel ein Warnsignal.

**Warum es hier vertretbar ist:** Die beiden Regeln greifen nacheinander, nicht ineinander. Erst wird geprüft (B), dann gesetzt (A), dann vermerkt (B). Zwischen den Schritten kann nichts Widersprüchliches entstehen, weil ein Exemplar nur einmal ausgegeben wird — der Zustand in A ist die Sicherung.

**Die Alternative** wäre, das Exemplar in die Benutzerklammer zu ziehen. Dann wäre die Klammer so groß wie der ganze Bestand — genau der Fehler aus der großen Übung.

## Schritt 4 · R2 — die Regel, die keine ist

„Höchstens 20 Medien" betrifft **alle** Ausleihen eines Benutzers. Die liegen in Klammer B, also ist die Regel dort durchsetzbar.

**Aber:** Die Bibliothekarin sagt, kurzzeitige Überschreitung sei egal.

**Was das bedeutet:** R2 könnte auch außerhalb geprüft werden — als Warnung statt als Sperre. Da sie ohnehin in einer Klammer liegt, ist die Frage hier gegenstandslos.

**Der Merkpunkt:** Nicht jede Regel, die durchsetzbar ist, muss durchgesetzt werden. Wenn der Fachbereich Abweichung erlaubt, ist eine harte Sperre Überbau — und führt zu Ausnahmen, die jemand von Hand freischalten muss.

---

## Was dieses Beispiel zeigt

**Zwei Klammern für fünf Bestandteile.** Die Öffnungszeiten und die Vormerkungen brauchen keine.

**Die Klammer ist so groß wie die Regel.** Ein Exemplar, nicht der Bestand. Ein Benutzer, nicht alle.

**Ein Vorgang darf zwei Klammern berühren**, wenn die Regeln nacheinander greifen und der Zustand in einer der beiden die Sicherung trägt.

**„Durchsetzbar" ist nicht dasselbe wie „muss durchgesetzt werden".** Wo der Fachbereich Abweichung erlaubt, ist eine Sperre unnötig.

---

## Zum Vergleich: die große Klammer

Angenommen, man führt die **Zweigstelle** als Einheit — mit allen Exemplaren, allen Benutzern, allen Ausleihen.

| Vorgang | Betroffen |
|---|---|
| Frau Meier leiht ein Buch | ganze Zweigstelle |
| Herr Kaya gibt ein Buch zurück | ganze Zweigstelle |
| Jemand ändert die Öffnungszeiten | ganze Zweigstelle |

Drei Vorgänge, die nichts miteinander zu tun haben, warten aufeinander.

**Das ist derselbe Fehler wie bei der Station** — nur mit weniger Verkehr, weshalb er länger unbemerkt bleibt.
