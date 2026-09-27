# Denkmodell · Ein Architektur-Review im Bestand

Vier Stufen: **Signale → Erkenntnisse → Optionen → Entscheidung.**

---

## Stufe 1 · Signale

### Im Code

| Signal | Beispiel |
|---|---|
| Änderungen landen in vielen Tests | 58 Zurück-Navigationen mit Zielobjekt |
| Wartezeiten als Zahl im Aufruf | `snooze_time=8` |
| geteilter Zustand in Controls | `deviating_text` |
| zwei Änderungsrichtungen in einer Klasse | Aktionen × Control-Typen |
| konsequent eingehaltene Grenzen | kein direkter Squish-Aufruf in 983 Tests |

### Im Team

| Signal | Konkret |
|---|---|
| Regeln aus Einzelfällen | 20-Zeilen-Regel |
| Diskussion über Geschmack | „Screenplay ist moderner“ |
| funktionierende Entscheidungen nicht aufgeschrieben | Trennung Test/Squish |

---

## Stufe 2 · Erkenntnisse

**1. Beobachten und Bewerten sind zwei Schritte.**
Wer zuerst bewertet, sieht nur, was er erwartet.

**2. Change Cases machen Befunde sichtbar.**
Eine Struktur ist gut, wenn typische Änderungen an einer erwarteten Stelle landen.

**3. Beibehalten ist eine Entscheidung.**
Sie gehört mit Begründung in den Standard.

**4. Eine Regel braucht ein Problem.**
Eine Regel ohne Problem trifft Symptome und verhindert auch Sinnvolles.

**Was gesucht wird:** für jeden Ausschnitt die Entscheidung mit Begründung und für jede Regel das Problem, das sie verhindert.

---

## Stufe 3 · Optionen

| Option | Käme in Frage, wenn |
|---|---|
| **beibehalten** | Change Cases landen an der erwarteten Stelle |
| **vereinfachen** | eine Abstraktion leitet nur weiter |
| **ergänzen** | eine Fähigkeit fehlt, der Rest trägt |
| **gezielt umbauen** | ein Befund wiederholt sich |
| **nicht übernehmen** | eine Alternative bringt zu wenig |
| **offen** | Evidenz fehlt |

---

## Stufe 4 · Entscheidung

### Frage 1 — Landet der Change Case dort, wo die Verantwortung liegt?

- **Ja** → beibehalten.
- **Nein** → weiter.

### Frage 2 — Wiederholt sich der Befund?

- **Ja** → gezielt umbauen oder ergänzen.
- **Nein** → offen oder beibehalten mit Notiz.

### Frage 3 — Lässt sich eine Regel formulieren, die das Problem trifft?

- **Ja** → Regelkandidat mit Bereich, Ausnahme, Prüfbarkeit.
- **Nein** → Einzelfallentscheidung, keine Regel.

---

## Der Denkweg auf einen Blick

```
Ausschnitt
        ↓
Phase 1: beobachten, ohne Bewertung
        ↓
Phase 2: Change Cases           landet dort, wo erwartet → beibehalten
        ↓ Befund
Phase 3: Alternativen und Kosten
        ↓
Phase 4: Entscheidung mit Begründung
        ↓
Regel?  Problem, Bereich, Ausnahme, Prüfbarkeit
```

---

## Die eine Prüffrage

> **Welche beobachtbare Konsequenz unterscheidet die Varianten?**

---

## Gegenproben

| Prüfung | Wenn ja, dann |
|---|---|
| Enthält Phase 1 Wertungen? | Beobachtung und Bewertung vermischt |
| Gibt es keine Entscheidung „beibehalten“? | Stärken übersehen |
| Nennt eine Regel eine Zahl ohne Problem? | Symptom-Regel |
| Wird ein Pattern ohne Befund vorgeschlagen? | Checkliste statt Review |

---

## Wenn die Entscheidung steht

**Entscheidungen aufschreiben, auch „beibehalten“.**

**Regeln einordnen.** MUST nur, wo eine Verletzung einen belegten Schaden verursacht.

**Offenes offen lassen.** Mit dem, was fehlt, um zu entscheiden.

---

## Verwechslungen, die im Alltag vorkommen

| Verwechselt mit | Erkennungszeichen |
|---|---|
| Review mit Neuentwurf | ein Review bewertet, was da ist |
| Befund mit Geschmack | ein Befund hat eine beobachtbare Konsequenz |
| Regel mit Empfehlung | MUST gegen SHOULD |
| Einzelfall mit Muster | ein Befund an einer Stelle ist noch keine Regel |
