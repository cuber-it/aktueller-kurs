# Denkmodell · Szenarien ohne zweite Architektur umsetzen

Vier Stufen: **Signale → Erkenntnisse → Optionen → Entscheidung.**

---

## Stufe 1 · Signale

### Im erzeugten Code

| Signal | Beispiel |
|---|---|
| Squish-Aufrufe in Step-Funktionen | `mouseClick(waitForObject(names.x))` |
| eigene Object Map neben den UI-Modulen | `names.py` mit sieben Einträgen |
| Namen nach Muster ähnlicher Elemente | `tractorAddNew` nach `implementAddNew` |
| Prüfungen mit `test.passes`/`test.fail` statt Routing | Beispiel aus Material B |
| feste Eingaben, die sich je Lauf ändern | aufgezeichnete Lösung einer Aufgabe |

### Im Ablauf

| Signal | Konkret |
|---|---|
| erster Lauf scheitert an Namen | drei von sieben falsch |
| Lücke im Framework taucht als Laufzeitfehler auf | statt als Befund |

---

## Stufe 2 · Erkenntnisse

**1. Das Szenario sagt was, die Architektur sagt wie.**
Die Abbildung ist Arbeit des Implementierens, nicht des Szenarios.

**2. Eine Lücke im Framework ist ein Befund.**
Sie gehört dem Team, nicht dem Agenten.

**3. Ein geratener Name ist schlimmer als ein fehlender.**
Der fehlende fällt auf, der geratene sieht richtig aus.

**4. Step-Funktionen sind eine Schicht.**
Dünn gehalten verbinden sie Sprache und Framework; dick verdoppeln sie es.

**Was gesucht wird:** für jede Zeile der vorhandene Aufruf, und für jede Lücke der Ort und die Quelle des Real Names.

---

## Stufe 3 · Optionen

| Option | Käme in Frage, wenn |
|---|---|
| **vorhandener Aufruf** | Control, Screen Object oder Helper existiert |
| **Element ergänzen, Name aus Spy** | das Element existiert in der AUT |
| **Element ergänzen, Name aus Quellcode** | `objectName` im QML gesetzt |
| **TODO und Rückfrage** | Spy abgelehnt, Quellcode unklar |
| **Step-Funktionen** | Szenarien dauerhaft ausführbar sein sollen |
| **Routing-Tabelle wie bisher** | Szenarien nur Arbeitsmittel sind |

---

## Stufe 4 · Entscheidung

### Frage 1 — Gibt es den Aufruf?

- **Ja** → verwenden.
- **Nein** → weiter.

### Frage 2 — Gibt es das Element in der AUT?

- **Ja, Real Name belegbar** → im `UI/*.py` ergänzen.
- **Unklar** → TODO, Rückfrage.

### Frage 3 — Sollen Szenarien ausführbar werden?

- **Ja** → dünne Step-Funktionen, die nur aufrufen.
- **Nein** → Routing-Tabelle und `test.py` wie bisher.

---

## Der Denkweg auf einen Blick

```
Szenariozeile
   ↓
Aufruf vorhanden?                ja → verwenden
   ↓ nein
Element in der AUT belegbar?     ja → im UI-Modul ergänzen (Spy/Quellcode)
   ↓ nein
TODO [helper-missing] + Rückfrage
```

---

## Die eine Prüffrage

> **Gibt es das schon, und wenn nicht, wer entscheidet, wo es entsteht?**

---

## Gegenproben

| Prüfung | Wenn ja, dann |
|---|---|
| Steht ein Real Name in einer Step-Funktion? | zweite Architektur |
| Folgt ein neuer Name nur einem Muster? | geraten |
| Enthält eine Step-Funktion mehr als drei Zeilen? | Logik gehört ins Framework |
| Wird eine Lücke im Test überbrückt statt gemeldet? | Befund verloren |

---

## Wenn die Entscheidung steht

**Lücken sammeln.** Jede `[helper-missing]`-Markierung ist ein Ticket fürs Framework.

**Step-Funktionen nur, wo gebraucht.** Die Routing-Tabelle des Skills leistet für die Umsetzung dasselbe ohne Laufzeitschicht.

---

## Verwechslungen, die im Alltag vorkommen

| Verwechselt mit | Erkennungszeichen |
|---|---|
| Step Definition mit Page Object | Step-Funktionen beschreiben Sprache, nicht Bildschirme |
| TODO mit Versäumnis | ein TODO an einer Lücke ist korrektes Verhalten |
| Muster mit Beleg | gleiche Form heißt nicht gleicher Name |
