# Denkmodell · Helper, Task oder Workflow?

Vier Stufen: **Signale → Erkenntnisse → Optionen → Entscheidung.**

---

## Stufe 1 · Signale

### Im Code

| Signal | Beispiel |
|---|---|
| Verzweigung nach einer Aktion in vielen Methoden | `if self.action == …` |
| Methoden je Typ mit gleichen Zweigen | `process_<typ>` |
| ein Weg durch Menüs, der die Aktion kennt | Fokus nur bei `set_to_ref` |
| Ergebnisse als verketteter Text | `self.names += ";" + …` |
| Helper, die mehrere Menüs und Prüfungen verbinden | `iterate_through_implement_settings` |

### Im Team

| Signal | Konkret |
|---|---|
| Schätzungen wachsen mit jeder Variante | 3 Tage für eine Aktion |
| Fehler in einem Zweig fallen spät auf | zwei Wochen |
| „Wo baue ich das ein?“ | Aktion oder Typ? |

---

## Stufe 2 · Erkenntnisse

**1. Zwei unabhängige Änderungsrichtungen brauchen zwei Orte.**
Aktionen und Control-Typen ändern sich aus verschiedenen Gründen.

**2. Ein Workflow beschreibt einen Weg, nicht was unterwegs passiert.**
Nimmt er eine Funktion entgegen, bleibt er von Aktionen unabhängig.

**3. Ein Task ist eine Testhandlung mit Bedeutung.**
„Parameter mit Referenz vergleichen“ ist ein Task, „Wert eines Schalters lesen“ ein technischer Helper.

**4. Wiederverwendung allein ist kein Grund für eine Schicht.**
Eine neue Schicht braucht eine eigene, erkennbare Verantwortung.

**Was gesucht wird:** die Änderungsrichtungen und für jede genau einen Ort.

---

## Stufe 3 · Optionen

| Option | Käme in Frage, wenn |
|---|---|
| **Zugriff je Typ (Tabelle oder Methode am Control)** | mehrere Aktionen denselben Zugriff brauchen |
| **Task als Funktion** | eine Aktion auf einzelne Parameter angewendet wird |
| **Workflow mit Funktionsparameter** | derselbe Weg für verschiedene Aktionen gegangen wird |
| **Aktion als Klasse mit Zustand** | eine Aktion Ergebnisse über alle Parameter sammelt |
| **alles lassen** | keine neue Aktion und kein neuer Typ absehbar |

---

## Stufe 4 · Entscheidung

### Frage 1 — Wie viele Stellen trifft eine neue Variante in jeder Richtung?

- **Eine** → gut geschnitten.
- **Mehrere** → die Richtungen sind vermischt.

### Frage 2 — Kennt der Weg die Aktion?

- **Ja** → Weg und Aktion trennen, Sonderfälle wie Fokus in den Task oder den Weg ohne Bedingung.

### Frage 3 — Hat jede neue Einheit eine eigene Verantwortung?

- **Nein** → keine neue Schicht.

---

## Der Denkweg auf einen Blick

```
Neue Variante (Aktion oder Typ)
        ↓
Wie viele Stellen?                 eine → fertig
        ↓ mehrere
Richtungen trennen: Zugriff je Typ | Task je Aktion | Weg ohne Aktion
        ↓
Jede Einheit mit eigener Verantwortung?    nein → zusammenlassen
```

---

## Die eine Prüffrage

> **Welche Änderung trifft diese Stelle, und trifft sie auch die anderen?**

---

## Gegenproben

| Prüfung | Wenn ja, dann |
|---|---|
| Braucht eine neue Aktion Änderungen in mehreren Methoden? | vermischte Richtungen |
| Enthält ein Workflow `if action == …`? | der Weg kennt die Aktion |
| Wird ein Ergebnis-Text später wieder zerlegt? | strukturierte Daten fehlen |
| Leitet eine neue Klasse nur weiter? | keine eigene Verantwortung |

---

## Wenn die Entscheidung steht

**Mit dem Zugriff beginnen.** Lesen und Setzen je Typ an einem Ort. Die vorhandenen Methoden können ihn sofort nutzen.

**Aktionen herauslösen.** Eine nach der anderen, die alte Klasse ruft sie auf.

**Den Weg zuletzt.** Er ist am längsten und am stabilsten.

---

## Verwechslungen, die im Alltag vorkommen

| Verwechselt mit | Erkennungszeichen |
|---|---|
| Task mit Helper | ein Task hat fachliche Bedeutung |
| Workflow mit Task | ein Workflow verbindet mehrere Tasks oder Bereiche |
| Strategy-Pattern mit Funktionsparameter | in Python genügt oft eine Funktion |
| Service Layer mit Sammelklasse | ein Service Layer hat eine eigene Verantwortung |
