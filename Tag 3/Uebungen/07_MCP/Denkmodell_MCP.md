# Denkmodell · Eigenen oder fremden MCP-Server wählen

Vier Stufen: **Signale → Erkenntnisse → Optionen → Entscheidung.**

---

## Stufe 1 · Signale

### Bei den Werkzeugen

| Signal | Beispiel |
|---|---|
| fremder Server mit vielen Tools | Squish MCP: ausführen, anlegen, Feature-Dateien |
| fremder Server ohne Wissen über das Framework | eigene Real Names |
| eigener Server mit wenigen Tools | 2 Tools |
| Leitplanken nur als Anweisung | Regeldatei |

### Im Team

| Signal | Konkret |
|---|---|
| Diskussion über Fähigkeiten statt Grenzen | „Squish MCP kann mehr“ |
| unbekannte Versionen | Portal-Version nicht geprüft |
| knappe Wartungszeit | „Wer pflegt den eigenen?“ |

---

## Stufe 2 · Erkenntnisse

**1. Ein Tool setzt nur durch, was in Parametern und Implementierung steht.**
Alles andere ist Anweisung.

**2. Die Rückfrage stellt der Client.**
Sie ist bei jedem Server gleich stark, wenn die Freigaben stimmen.

**3. Ein fremder Server kennt das Werkzeug, nicht das Projekt.**
Wissen über das Framework muss aus dem Skill kommen.

**4. Server lassen sich schichten.**
Ein eigener Server kann einen fremden nutzen und davor prüfen.

**Was gesucht wird:** für jede Leitplanke der Ort, an dem sie mit dem jeweiligen Server steht.

---

## Stufe 3 · Optionen

| Option | Käme in Frage, wenn |
|---|---|
| **eigener Server um die Skripte** | Leitplanken im Tool gebraucht werden, wenige Fähigkeiten reichen |
| **fremder Server** | seine Fähigkeiten gebraucht werden und Leitplanken über Freigaben reichen |
| **eigener Server vor fremdem** | beides |
| **nur Freigaben für Bash** | als erster Schritt |

---

## Stufe 4 · Entscheidung

### Frage 1 — Welche Leitplanken müssen im Tool stehen?

- Zähler, erlaubte Werte, Vorbedingungen → eigener Server oder Schicht davor.

### Frage 2 — Welche Fähigkeiten des fremden Servers braucht der Workflow?

- **Keine** → eigener Server.
- **Einige** → prüfen, ob sie über den eigenen Server gekapselt werden können.

### Frage 3 — Wer pflegt?

- Kein Team frei → kleinster eigener Server oder nur Freigaben.

---

## Der Denkweg auf einen Blick

```
Leitplanken
   ↓
müssen im Tool stehen?       ja → eigener Server (evtl. vor fremdem)
   ↓ nein
reichen Freigaben?           ja → fremder Server oder Bash mit Freigaben
```

---

## Die eine Prüffrage

> **Welche Leitplanke steht im Werkzeug, welche nur in einer Anweisung?**

---

## Gegenproben

| Prüfung | Wenn ja, dann |
|---|---|
| Wird ein Server gewählt, weil er mehr Tools hat? | Fähigkeit statt Grenze |
| Erzeugt der Server Code mit eigenen Namen? | Parallelarchitektur (Übung 04) |
| Hängt eine Leitplanke an einer Regeldatei? | Anweisung |

---

## Wenn die Entscheidung steht

**Mit Freigaben beginnen.** Sie wirken bei jedem Server.

**Portal-Version prüfen, bevor entschieden wird.** Mit Blick auf die Leitplanken.

---

## Verwechslungen, die im Alltag vorkommen

| Verwechselt mit | Erkennungszeichen |
|---|---|
| offiziell mit passend | der Hersteller kennt das Projekt nicht |
| MCP-Server mit Agent | der Server stellt Werkzeuge bereit, entscheidet nichts |
| Regeldatei mit Durchsetzung | eine Regeldatei ist Kontext |
