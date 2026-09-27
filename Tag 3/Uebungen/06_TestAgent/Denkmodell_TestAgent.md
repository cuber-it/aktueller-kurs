# Denkmodell · Werkzeuge eines Test-Agenten schneiden

Vier Stufen: **Signale → Erkenntnisse → Optionen → Entscheidung.**

---

## Stufe 1 · Signale

### In Skripten und Freigaben

| Signal | Beispiel |
|---|---|
| Regeln als Kommentar im Skript | „Never run this without asking“ |
| Positionsargumente | `<target-ip> <suite> <tst_dir>` |
| Text als Ergebnis | Meldungen statt Status |
| pauschale Freigabe eines allgemeinen Werkzeugs | `Bash` |
| Zählen im Modell | „höchstens 2 Läufe“ |

### Im Team

| Signal | Konkret |
|---|---|
| Läufe ohne Rückfrage | trotz Regel im Skill möglich |
| zähe Sitzungen bei einzelnen Freigaben | Rückkehr zur pauschalen Freigabe |

---

## Stufe 2 · Erkenntnisse

**1. Ein allgemeines Werkzeug erbt die gefährlichste Fähigkeit.**
Wer `Bash` erlaubt, erlaubt auch den Testlauf.

**2. Ein spezielles Werkzeug kann seine eigenen Grenzen tragen.**
Laufbegrenzung, erlaubte Werte, Rückfrage.

**3. Die Wirkung bestimmt die Freigabe.**
Lesen frei, Zerstören mit Rückfrage.

**4. Strukturierte Rückgaben ersetzen Textauswertung.**
Der Agent entscheidet nach einem Status, nicht nach einer Meldung.

**Was gesucht wird:** die kleinste Menge an Tools mit klarer Wirkung und je Tool die Grenzen, die es selbst durchsetzt.

---

## Stufe 3 · Optionen

| Option | Käme in Frage, wenn |
|---|---|
| **Bash mit Musterfreigaben** | wenige Skripte, schneller Einstieg |
| **eigener MCP-Server** | Grenzen und Rückgaben im Tool gebraucht werden |
| **fremder MCP-Server** | er die nötigen Fähigkeiten und Grenzen hat (Übung 07) |
| **Tool weglassen** | der Workflow es nicht braucht |

---

## Stufe 4 · Entscheidung

### Frage 1 — Braucht der Workflow die Fähigkeit?

- **Nein** → kein Tool.

### Frage 2 — Welche Wirkung hat sie?

- lesend → `allow`
- verändernd, lokal → `allow` oder `ask`
- zerstörend oder fremde Ressourcen → `ask`, Grenzen im Tool

### Frage 3 — Welche Regel lässt sich im Tool durchsetzen?

- Zählen, erlaubte Werte, Vorbedingungen → ins Tool.
- Urteil → beim Modell.

---

## Der Denkweg auf einen Blick

```
Fähigkeit
   ↓
gebraucht?            nein → weglassen
   ↓
Wirkung?              lesend → allow; zerstörend → ask
   ↓
Regeln ins Tool: Parameter, Zähler, Vorbedingungen
   ↓
Umweg sperren (deny)
```

---

## Die eine Prüffrage

> **Was darf der Agent ohne Rückfrage, und was passiert, wenn er es falsch macht?**

---

## Gegenproben

| Prüfung | Wenn ja, dann |
|---|---|
| Kann der Agent dasselbe über Bash tun? | `deny` fehlt |
| Liefert ein Tool ungefilterte Protokolle? | Rückgabe zu groß |
| Gibt es Tools, die kein Schritt braucht? | zu viel Fähigkeit |

---

## Wenn die Entscheidung steht

**Mit Freigaben beginnen.** `ask` für `Bash(*run_testcase.sh*)` wirkt sofort.

**Dann das Tool.** Zähler und Status im Server.

---

## Verwechslungen, die im Alltag vorkommen

| Verwechselt mit | Erkennungszeichen |
|---|---|
| Rückfrage mit Freigabe | das Modell fragt / Claude Code fragt |
| Tool mit Skript | ein Tool hat einen Vertrag |
| mehr Tools mit mehr Können | jedes Tool vergrößert den Aktionsraum |
