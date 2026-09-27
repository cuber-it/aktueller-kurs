# Beispiel · Was gehört in den Skill? – in klein

Dieselbe Aufgabe an einem kleineren Gegenstand, vollständig durchgeführt.

---

## Der Gegenstand

Ein Team lässt einen Coding-Agenten Datenbank-Migrationen für eine Vereinsverwaltung schreiben. Der Agent hat eine Anleitung mit Regeln. Drei neue Erkenntnisse sollen hinein:

| Nr. | Erkenntnis |
|---|---|
| E1 | `add_column(..., default=...)` sperrt bei großen Tabellen die Tabelle minutenlang. |
| E2 | Die Hilfsfunktion `backfill(table, column, fn)` verarbeitet 1.000 Zeilen je Durchgang. |
| E3 | Migrationen an der Tabelle `members` brauchen eine Freigabe des Vorstands. |

---

## Schritt 1 · Einordnen

| Nr. | Kategorie | Begründung |
|---|---|---|
| E1 | Gefahr | aus dem Code nicht erkennbar, führt zu Ausfall |
| E2 | nicht aufnehmen | steht im Docstring von `backfill`, der Agent kann es lesen |
| E3 | Prozessregel | nirgends im Code, entscheidet über das Vorgehen |

---

## Schritt 2 · Schreiben

```markdown
### ⚠️ `add_column` with a default locks large tables
On tables above ~100k rows the lock lasts minutes. Add the column without default, then
`backfill`, then set the default.

| Add a column with a default to a large table | `add_column` without default → `backfill` → `alter_default` |
```

Prozessregel in der Anleitung:

```markdown
Migrations touching `members` need board approval. Stop after writing the migration and ask.
```

---

## Schritt 3 · Wann entfällt der Eintrag?

E1 entfällt, wenn eine eigene Hilfsfunktion `add_column_safely` die drei Schritte kapselt. Dann steht in der Routing-Zeile nur noch dieser Name, die Gefahr steht im Docstring.

---

## Was dieses Beispiel zeigt

**Was im Code steht, gehört nicht in den Kontext.** E2 wäre eine Beschreibung, die veralten kann.

**Gefahr und Routing gehören zusammen, aber an verschiedene Orte.** Die Gefahr erklärt, die Routing-Zeile sagt, was zu tun ist.

**Ein Framework-Umbau macht Kontext überflüssig.** Das ist das Ziel, nicht der Verlust.
