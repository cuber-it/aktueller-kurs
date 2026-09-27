# Denkmodell · Eine Zwischenrepräsentation vor dem Code

Vier Stufen: **Signale → Erkenntnisse → Optionen → Entscheidung.**

---

## Stufe 1 · Signale

### Im Testfall

| Signal | Beispiel |
|---|---|
| Expected mit mehreren Aussagen | „angelegt und ausgewählt“ |
| Expected ohne Beobachtungsweg | „ist angelegt“ |
| erster Schritt ist eine Aktion | kein Ausgangszustand |
| Testdaten gleich einem Vorgabewert | „Tractor“ |
| identische Testfälle unter zwei Kennungen | Duplikat |

### Im Ablauf

| Signal | Konkret |
|---|---|
| grüne Tests, die nichts beweisen | Prüfung auf einen Zustand, den es vorher schon gab |
| Fragen an die Fachseite erst nach der Automatisierung | „Darf der Name doppelt sein?“ |
| Review prüft Form, nicht Beobachtbarkeit | Freigabe trotz Lücke |

---

## Stufe 2 · Erkenntnisse

**1. Ein Testfall beschreibt oft den Bedienweg besser als die Wirkung.**
Wer das System kennt, lässt den Ausgangszustand weg.

**2. Eine Automatisierung übernimmt die Lücken des Testfalls.**
Der Skill setzt um, was da steht.

**3. Given, When, Then trennen Zustand, Aktion und Beobachtung.**
Die Trennung macht fehlende Teile sichtbar.

**4. Eine zweite Darstellung kann auseinanderlaufen.**
Gherkin neben Polarion braucht eine klare Rolle.

**Was gesucht wird:** für jede Erwartung, woran sie beobachtet wird und welcher Ausgangszustand sie verfälschen könnte.

---

## Stufe 3 · Optionen

| Option | Käme in Frage, wenn |
|---|---|
| **Gherkin als Zwischenschritt im testcase-writer** | Testfälle aus Stories entstehen und vor der Freigabe geprüft werden |
| **Gherkin statt Polarion-Schritten** | Polarion das Format unterstützt und das Team umstellen will |
| **Prüfliste für Reviews** | kein neues Format gewünscht ist |
| **ausführbares BDD** | Szenarien dauerhaft die Tests steuern sollen (3-4) |

---

## Stufe 4 · Entscheidung

### Frage 1 — Findet das heutige Review die Lücken?

- **Ja** → kein neues Format.
- **Nein** → weiter.

### Frage 2 — Wo entstehen die Lücken?

- Beim Schreiben aus der Story → Zwischenschritt im `testcase-writer`.
- Beim Übertragen in Code → Prüfung im `testcase-implementer`.

### Frage 3 — Soll Gherkin bestehen bleiben?

- **Ja** → einziges führendes Format festlegen.
- **Nein** → Gherkin als Arbeitsschritt, Ergebnis zurück nach Polarion.

---

## Der Denkweg auf einen Blick

```
Testfall
   ↓
Erwartung beobachtbar?            nein → Then umformulieren
   ↓
Ausgangszustand genannt?          nein → Given ergänzen
   ↓
Varianten fehlen?                 ja → Szenarien ergänzen
   ↓
Fragen an die Fachseite, dann Freigabe
```

---

## Die eine Prüffrage

> **Woran würde ein Beobachter sehen, dass das Verhalten eingetreten ist?**

---

## Gegenproben

| Prüfung | Wenn ja, dann |
|---|---|
| Wäre das Then auch vor dem When wahr? | Ausgangszustand fehlt |
| Enthält das Then „und“? | zwei Aussagen |
| Nennt das Szenario Widgets? | Bedienweg statt Verhalten |

---

## Wenn die Entscheidung steht

**Als Arbeitsschritt einführen.** Der `testcase-writer` erzeugt zuerst Szenarien, der Mensch prüft, dann entstehen die Polarion-Schritte.

**Duplikate beim selben Schritt suchen.** Szenarien lassen sich leichter vergleichen als Tabellen.

---

## Verwechslungen, die im Alltag vorkommen

| Verwechselt mit | Erkennungszeichen |
|---|---|
| Gherkin mit BDD-Framework | hier nur Darstellung |
| Szenario mit Testskript | keine Klicks, keine Widgets |
| Freigabe mit Beobachtbarkeit | ein freigegebener Testfall kann unbeobachtbar sein |
