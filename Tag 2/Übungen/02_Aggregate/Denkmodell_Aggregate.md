# Denkmodell · Konsistenzgrenzen ziehen

Vier Stufen: **Signale → Erkenntnisse → Optionen → Entscheidung.**

---

## Stufe 1 · Signale

### Für eine zu große Klammer

| Signal | Konkret |
|---|---|
| Vorgänge warten aufeinander, die nichts miteinander zu tun haben | vier Tresen, ein Wartezustand |
| Für eine kleine Änderung wird viel geladen | 90 Fahrzeuge für einen Vorgang |
| Große Exemplare sind schlechter dran als kleine | der Engpass wächst mit der Menge |
| Selten Geändertes blockiert häufig Geändertes | Öffnungszeiten gegen Tagesgeschäft |
| Die Klammer heißt wie eine Organisationseinheit | Station, Filiale, Abteilung |
| Mehr Rechenleistung hilft nur vorübergehend | der Engpass ist strukturell |

### Für eine zu kleine Klammer

| Signal | Konkret |
|---|---|
| Eine Regel wird regelmäßig verletzt | sie ist nicht durchsetzbar |
| Ein Vorgang ändert mehrere Klammern gleichzeitig | falsch geschnitten oder ein Ereignis fehlt |
| Widersprüchliche Zustände fallen im Betrieb auf | die Abweichung ist nicht vertretbar |

### Im Gespräch mit dem Fachbereich

| Signal | Deutet auf |
|---|---|
| „Das darf nie passieren" | sofort — Klammer gerechtfertigt |
| „Fünf Minuten sind egal" | zeitnah — getrennte Klammern |
| „Das fällt erst am Vortag auf" | irgendwann — keine Klammer |
| „Das korrigiere ich hinterher" | zeitnah |

---

## Stufe 2 · Erkenntnisse

**1. Eine Klammer braucht eine Regel.**
Ohne benennbare Regel, die sofort gelten muss, gehören zwei Dinge nicht zusammen.

**2. Die Dringlichkeit ist eine fachliche Frage.**
Ob eine Regel sofort gelten muss, entscheidet der Fachbereich — nicht die Entwicklung und nicht die Datenbank.

**3. Die meisten Regeln sind nicht sofort.**
Erfahrungsgemäß muss nur ein Bruchteil der genannten Regeln jederzeit gelten. Genau das erlaubt kleine Klammern.

**Was gesucht wird:** die kleinstmögliche Gruppe, in der eine Sofort-Regel gilt.

---

## Stufe 3 · Optionen

| Option | Käme in Frage, wenn |
|---|---|
| **Eine Klammer** | eine Regel zwischen allen Teilen sofort gelten muss |
| **Getrennte Klammern, Nachziehen** | die Regel zeitnah genügt |
| **Getrennte Klammern, Prüfung beim Zugriff** | die Regel sofort gilt, aber selten verletzt wird und der Zeitraum klein ist |
| **Zustand verlagern** | die Regel innerhalb einer Klammer gilt, wenn ein Merkmal umzieht |
| **Regel zur Warnung herabstufen** | sie ist eine Planungsgröße, keine Zusicherung |

Die letzten beiden werden oft übersehen und lösen die meisten schwierigen Fälle.

---

## Stufe 4 · Entscheidung

### Frage 1 — Gibt es eine Regel?

> **Welche Regel verbindet diese Dinge?**

- **Eine benennbare Regel** → weiter mit Frage 2
- **„Das gehört doch zusammen"** → keine Klammer

**Was keine Begründung ist:** Zugehörigkeit · gemeinsames Lesen · gleiche Tabelle · Bequemlichkeit.

### Frage 2 — Muss sie sofort gelten?

> **Was passiert, wenn das für fünf Minuten nicht zusammenpasst?**

| Antwort | Konsequenz |
|---|---|
| „Das darf nie passieren" | dieselbe Klammer |
| „Fünf Minuten sind egal" | getrennte Klammern, Nachziehen |
| „Fällt erst später auf" | keine Klammer, Warnung genügt |

**Diese Frage gehört dem Fachbereich gestellt.** Sie klingt technisch und ist fachlich.

### Frage 3 — Wie klein geht es?

Für jeden Teil der Klammer:

> **Braucht die Regel ihn?**

Was die Regel nicht braucht, gehört nicht hinein — auch wenn es sachlich dazugehört.

### Frage 4 — Wenn die Regel über die Grenze geht

| Weg | Wann |
|---|---|
| **Nachziehen über ein Ereignis** | zeitnah genügt |
| **Prüfen beim Zugriff** | sofort nötig, Zeitraum klein, Verletzung selten |
| **Zustand verlagern** | die Regel gilt innerhalb einer Klammer, wenn ein Merkmal dorthin zieht |
| **Herabstufen zur Warnung** | es ist eine Planungsgröße |

---

## Der Denkweg auf einen Blick

```
Was soll in dieselbe Klammer?
        ↓
Welche Regel verbindet sie?          keine → keine Klammer
        ↓ eine Regel
Muss sie sofort gelten?              nein → getrennte Klammern
        ↓ ja
Braucht die Regel jeden Teil?        nein → Teil herausnehmen
        ↓ ja
Geht die Regel ueber die Grenze?     ja → nachziehen, pruefen,
        ↓ nein                             verlagern oder herabstufen
                    KLAMMER STEHT
```

---

## Die eine Prüffrage

> **Muss es im selben Moment stimmen?**

Und die Gegenfrage an den Fachbereich:

> **Was passiert, wenn das für fünf Minuten nicht zusammenpasst?**

---

## Gegenproben

| Prüfung | Wenn ja, dann |
|---|---|
| Lautet die Begründung „gehört zusammen"? | keine Regel, keine Klammer |
| Wächst der Engpass mit der Menge? | zu große Klammer |
| Blockiert Selten-Geändertes das Tagesgeschäft? | zwei Klammern |
| Ändert ein Vorgang mehrere Klammern? | falsch geschnitten oder Ereignis fehlt |
| Heißt die Klammer wie eine Abteilung? | Verdacht auf Zuständigkeit statt Regel |

---

## Wenn die Entscheidung steht

**Im Zweifel kleiner.**
Eine zu kleine Klammer merkt man, wenn eine Regel verletzt wird — das fällt auf und ist reparierbar. Eine zu große merkt man erst unter Last, und dann ist der Umbau teuer.

**Eine Änderung, eine Klammer.**
Wer in einem Vorgang mehrere ändert, hat falsch geschnitten oder braucht ein Ereignis. Die Faustregel deckt die meisten Fehlschnitte auf.

**Verweise statt Verschachtelung.**
Eine Klammer verweist auf eine andere über deren Kennung, statt sie zu enthalten. Der Mietvorgang merkt sich, **welches** Fahrzeug — nicht alles über das Fahrzeug.

**Zwischen den Klammern ist die Welt zeitweise widersprüchlich.**
Das muss fachlich vertretbar sein und gehört ausgesprochen. Wer es verschweigt, bekommt es bei der ersten Auswertung vorgehalten.

**Manche Regel ist gar keine.**
„Reservierungen überschreiten die Fahrzeugzahl nicht" klingt wie eine Regel und ist eine Planungsgröße. Solche Fälle erkennt man an der Antwort „das fällt am Vortag auf".

**Ein Zustand am richtigen Ort ersetzt eine große Klammer.**
Wenn „reserviert" ein Zustand des Fahrzeugs ist statt eine Beziehung zwischen Fahrzeug und Reservierung, gilt die Regel innerhalb einer kleinen Klammer. Solche Verlagerungen lohnen die Suche.

---

## Verwechslungen, die im Alltag vorkommen

| Verwechselt mit | Erkennungszeichen |
|---|---|
| Zusammengehörigkeit | sachlich verwandt ist nicht dasselbe wie gemeinsam gültig |
| Datenmodell | die Tabellenstruktur entscheidet nichts über Konsistenzgrenzen |
| Zuständigkeit | eine Abteilung ist keine Klammer |
| Lesezugriff | gemeinsam angezeigt heißt nicht gemeinsam geändert |
| Bounded Context | eine Modellgrenze, keine Konsistenzgrenze — ein Kontext enthält mehrere Klammern |
