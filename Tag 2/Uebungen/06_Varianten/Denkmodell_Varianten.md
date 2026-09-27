# Denkmodell · Eine Architekturvariante wählen

Vier Stufen: **Signale → Erkenntnisse → Optionen → Entscheidung.**

---

## Stufe 1 · Signale

### Im Code

| Signal | Beispiel |
|---|---|
| dieselbe Handlung über mehrere Bedienwege | Einstellung am Terminal und über das Virtual Terminal |
| Rollen mit unterschiedlichem Verhalten | Fahrer, Service |
| Tests kennen Wege | `open_…` im Test, danach Controls |
| Handlungen ohne Namen | Folgen von Control-Aufrufen |

### Im Team

| Signal | Konkret |
|---|---|
| Vorschläge, ein Muster überall einzuführen | „alles umstellen“ |
| Diskussion ohne Change Case | zwei Lager, keine Entscheidung |
| Prototypen, die nur Machbarkeit zeigen | drei Tests mit Screenplay |

---

## Stufe 2 · Erkenntnisse

**1. Varianten sind Werkzeuge, keine Stufen.**
Direkter Code ist für lokale, einmalige Bedienung angemessen.

**2. Nutzen zeigt sich an Änderungen.**
Eine Variante lohnt sich, wenn sie eine absehbare Änderung auf eine Stelle beschränkt.

**3. Hybrid ist der Normalfall.**
Eine Variante kann an einer Stelle ergänzt werden, ohne den Rest umzustellen.

**4. Jede Variante bringt Begriffe mit.**
Wer sie einführt, muss sie erklären, dokumentieren und durchhalten.

**Was gesucht wird:** der Change Case, der die Varianten unterscheidet.

---

## Stufe 3 · Optionen

| Option | Käme in Frage, wenn |
|---|---|
| **direkt** | Bedienung lokal, einmalig, selbst Prüfgegenstand |
| **Screen Objects** | Wissen über Bildschirme gebündelt werden soll |
| **Screen Objects + Tasks** | Handlungen in vielen Tests vorkommen |
| **Screenplay** | dieselbe Handlung über mehrere Bedienwege oder Rollen |
| **hybrid** | nur einzelne Bereiche von einer Variante profitieren |

---

## Stufe 4 · Entscheidung

### Frage 1 — Gibt es einen Change Case, den die heutige Variante schlecht trägt?

- **Nein** → nichts ändern.
- **Ja** → weiter.

### Frage 2 — Welche Variante beschränkt ihn auf eine Stelle?

- Die Variante mit den wenigsten neuen Begriffen, die das leistet.

### Frage 3 — Betrifft der Change Case alle Tests oder einen Bereich?

- **Einen Bereich** → dort ergänzen.
- **Alle** → Umstellung schrittweise planen.

---

## Der Denkweg auf einen Blick

```
Vorschlag für eine Variante
        ↓
Change Case, den der Bestand schlecht trägt?     nein → nichts ändern
        ↓ ja
Kleinste Variante, die ihn auf eine Stelle bringt
        ↓
Bereich oder alles?      Bereich → dort ergänzen
```

---

## Die eine Prüffrage

> **Welche Änderung macht diese Variante leichter, und was kostet sie?**

---

## Gegenproben

| Prüfung | Wenn ja, dann |
|---|---|
| Wird eine Variante mit „modern“ begründet? | Change Case fehlt |
| Zeigt ein Prototyp nur, dass es funktioniert? | Nutzen nicht belegt |
| Ändern sich bei einem Change Case in allen Varianten gleich viele Stellen? | er unterscheidet die Varianten nicht |

---

## Wenn die Entscheidung steht

**Lokal beginnen.** Dort, wo der Change Case liegt.

**Begriffe erklären.** Neue Begriffe in die Architekturübersicht aufnehmen.

**Grenze festlegen.** Wann ein neuer Test die neue Variante verwendet und wann nicht.

---

## Verwechslungen, die im Alltag vorkommen

| Verwechselt mit | Erkennungszeichen |
|---|---|
| Screenplay mit „nach POM“ | kein Nachfolger, eine andere Aufteilung |
| Lesbarkeit mit Architektur | ein Test kann gut lesbar und trotzdem schlecht änderbar sein |
| hybrid mit unsauber | hybrid ist gewählt, unsauber ist zufällig |
