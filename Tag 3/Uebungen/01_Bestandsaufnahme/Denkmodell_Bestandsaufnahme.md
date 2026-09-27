# Denkmodell · Einen KI-Workflow nach Durchsetzung einordnen

Vier Stufen: **Signale → Erkenntnisse → Optionen → Entscheidung.**

---

## Stufe 1 · Signale

### In Skill und Skripten

| Signal | Beispiel |
|---|---|
| Regeln in Großbuchstaben oder fett | „**Never run** …“ |
| Regeln als Kommentar im Skript | Kopf von `run_testcase.sh` |
| dieselbe Regel an zwei Stellen | Skript und `SKILL.md` |
| Prüfskripte für einen Teil der Regeln | `check_test.py`, `assertion_guard.py` |
| Werkzeugfreigaben pauschal | `Bash` für die Sitzung erlaubt |

### Im Team

| Signal | Konkret |
|---|---|
| Verstöße trotz vorhandener Regel möglich | Lauf ohne Rückfrage |
| Regeln werden verstärkt statt durchgesetzt | fett, zweimal |
| Unklarheit, was der Agent darf | „Darf er Helper ändern?“ |

---

## Stufe 2 · Erkenntnisse

**1. Eine Regel im Kontext ist eine Bitte an das Modell.**
Sie wird meist befolgt, aber nicht immer. Wie oft nicht, lässt sich schwer messen.

**2. Technische Durchsetzung ist unabhängig vom Modell.**
Sie wirkt auch in langen Sitzungen, nach Kontextverdichtung und bei anderen Modellen.

**3. Nicht jede Regel lässt sich technisch fassen.**
„Test- oder AUT-Fehler begründen“ verlangt Urteil.

**4. Die Folge eines Verstoßes bestimmt den Bedarf.**
Eine Regel mit Folgen außerhalb des Workflows (Datensatz eines Kollegen) braucht mehr als eine Bitte.

**Was gesucht wird:** für jede Regel die Art der Durchsetzung und die Folge eines Verstoßes.

---

## Stufe 3 · Optionen

| Option | Käme in Frage, wenn |
|---|---|
| **technisch blockieren** | der Verstoß eindeutig erkennbar ist und Schaden anrichtet |
| **technisch melden** | der Verstoß erkennbar ist, ein Mensch aber entscheiden soll |
| **Werkzeugfreigabe einschränken** | eine Aktion nur mit Rückfrage erfolgen soll |
| **beim Modell lassen** | die Regel Urteil verlangt und die Folge klein ist |
| **beim Menschen lassen** | die Entscheidung fachlich ist |

---

## Stufe 4 · Entscheidung

### Frage 1 — Was passiert bei einem einzelnen Verstoß?

- **Schaden außerhalb des Workflows** → technisch durchsetzen.
- **Fehler im Ergebnis, im Review erkennbar** → melden genügt.
- **gering** → beim Modell lassen.

### Frage 2 — Ist der Verstoß maschinell erkennbar?

- **Ja** → Prüfung oder Freigabe.
- **Nein** → Mensch oder Modell, mit klarer Formulierung.

---

## Der Denkweg auf einen Blick

```
Regel
   ↓
Folge eines einzelnen Verstoßes?      außerhalb des Workflows → technisch
   ↓
maschinell erkennbar?                 ja → blockieren oder melden
   ↓ nein
Urteil nötig?                         fachlich → Mensch, sonst Modell
```

---

## Die eine Prüffrage

> **Was passiert, wenn das Modell diese Regel einmal nicht befolgt?**

---

## Gegenproben

| Prüfung | Wenn ja, dann |
|---|---|
| Steht eine Regel an zwei Stellen, aber in keinem Skript? | Verstärkung statt Durchsetzung |
| Ist ein Werkzeug pauschal freigegeben, dessen Aufruf Schaden anrichtet? | Freigabe einschränken |
| Wird eine Prüfung ausgegeben, aber nicht ausgewertet? | melden ohne Reaktion |

---

## Wenn die Entscheidung steht

**Mit den teuren Regeln beginnen.** Datenverlust, fremde Targets, Assertions.

**Freigaben vor Code.** Eine `ask`-Regel in Claude Code ist schneller umgesetzt als ein Server.

**Die Liste pflegen.** Jede neue Regel im Skill bekommt eine Zeile: Durchsetzung, Folge.

---

## Verwechslungen, die im Alltag vorkommen

| Verwechselt mit | Erkennungszeichen |
|---|---|
| dokumentiert mit durchgesetzt | ein Verstoß ist ohne Mitwirkung des Modells möglich |
| Rückfrage mit Freigabe | eine Rückfrage des Modells ist eine Regel, eine `ask`-Freigabe ist technisch |
| Prüfung mit Blockade | `check_test.py` meldet, verhindert aber nichts |
