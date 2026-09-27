# Denkmodell · Kontext für einen Coding-Agenten auswählen

Vier Stufen: **Signale → Erkenntnisse → Optionen → Entscheidung.**

---

## Stufe 1 · Signale

### Im Skill

| Signal | Beispiel |
|---|---|
| Methodenbeschreibungen mit Parametern | „Default timeout is 30 s“ |
| Zeilennummern | `controls.py:600` |
| dieselbe Regel in zwei Dateien | Routing in `code_patterns.md` und `controls_and_tests.md` |
| Gefahren mit Beispiel „wrong / right“ | `click_and_wait` bei umschaltender Quelle |
| Einträge zu Code, der sich geändert hat | Name angepasst, Semantik nicht |

### Im Team

| Signal | Konkret |
|---|---|
| generierte Tests wiederholen einen bekannten Fehler | Timeout, `None` |
| Befunde aus Reviews landen „irgendwo“ im Skill | Abschnitt „Lessons learned“ |
| Unklar, ob ein Befund ins Framework oder in den Skill gehört | |

---

## Stufe 2 · Erkenntnisse

**1. Kontext ist teuer und veraltet.**
Jede Zeile wird bei jedem Aufruf mitgeladen und kann still falsch werden.

**2. Was im Code steht, kann das Modell lesen.**
Der Kontext braucht, was der Code nicht sagt: Gefahren, Entscheidungen, Absichten.

**3. Namen lassen sich prüfen, Bedeutungen nicht.**
Darum Namen nennen, Bedeutung dem Code überlassen.

**4. Eine Framework-Änderung ist besser als ein Kontexteintrag.**
Sie gilt für Menschen und Modelle, ohne dass jemand sie lesen muss.

**Was gesucht wird:** für jeden Befund der Ort, an dem er am wenigsten veraltet.

---

## Stufe 3 · Optionen

| Option | Käme in Frage, wenn |
|---|---|
| **Framework ändern** | die Gefahr sich beseitigen lässt |
| **Gefahreneintrag** | die Gefahr bleibt und aus dem Code nicht erkennbar ist |
| **Routing-Zeile** | eine Absicht einen bestimmten Aufruf verlangt |
| **Prozessregel** | ein Vorgehen festgelegt ist, das der Code nicht kennt |
| **nicht aufnehmen** | der Code es sagt |

---

## Stufe 4 · Entscheidung

### Frage 1 — Lässt sich die Ursache im Framework beseitigen?

- **Ja, bald** → Framework ändern, Kontexteintrag höchstens übergangsweise.
- **Nein** → weiter.

### Frage 2 — Kann das Modell es aus dem Code herausfinden?

- **Ja** → nicht aufnehmen.
- **Nein** → Gefahr, Routing oder Prozessregel.

### Frage 3 — Gibt es den genannten Namen schon?

- **Nein** → nicht aufnehmen, bis es ihn gibt.

---

## Der Denkweg auf einen Blick

```
Befund
   ↓
im Framework beseitigbar?        ja → Framework
   ↓ nein
aus dem Code erkennbar?          ja → nicht aufnehmen
   ↓ nein
Gefahr / Routing / Prozessregel, an genau einer Stelle, nur existierende Namen
```

---

## Die eine Prüffrage

> **Kann das Modell das aus dem Quelltext selbst herausfinden?**

---

## Gegenproben

| Prüfung | Wenn ja, dann |
|---|---|
| Enthält der Eintrag einen Zahlenwert aus dem Code? | wird veralten |
| Nennt er eine Methode, die es nicht gibt? | lehrt einen Fehler |
| Steht dieselbe Aussage anderswo? | doppelt, eine wird veralten |
| Fehlt die Aussage, was zu tun ist? | Gefahr ohne Routing |

---

## Wenn die Entscheidung steht

**Jeden Eintrag mit Ablaufbedingung versehen.** „Entfällt, wenn …“

**Nach Framework-Änderungen suchen.** Einträge zu geänderten Methoden prüfen, nicht nur Namen.

---

## Verwechslungen, die im Alltag vorkommen

| Verwechselt mit | Erkennungszeichen |
|---|---|
| mehr Kontext mit besserem Kontext | Methodeninventare veralten |
| Gefahr mit Dokumentation | eine Gefahr sagt, was schiefgeht, nicht wie etwas funktioniert |
| Namensprüfung mit Aktualität | Bedeutung wird nicht geprüft |
