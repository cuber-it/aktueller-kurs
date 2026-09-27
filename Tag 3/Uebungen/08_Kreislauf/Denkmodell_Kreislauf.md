# Denkmodell · Autonomie in einem geschlossenen Kreislauf festlegen

Vier Stufen: **Signale → Erkenntnisse → Optionen → Entscheidung.**

---

## Stufe 1 · Signale

### Im Kreislauf

| Signal | Beispiel |
|---|---|
| Korrekturen, die das Ziel verschieben | erwarteten Wert angepasst |
| grüne Läufe ohne Nachweis | `Passes: 0` |
| Anweisungen in gelesenen Daten | Notiz im Testfall |
| viele Läufe für eine Diagnose | „noch einmal versuchen“ |

### Im Team

| Signal | Konkret |
|---|---|
| Befunde erst im Review | geänderte Assertion |
| Unklarheit, was der Agent darf | „Darf er Helper ändern?“ |

---

## Stufe 2 · Erkenntnisse

**1. Autonomie ist so weit sinnvoll, wie Fehler bemerkt werden.**
Wo eine Invariante prüft, darf der Agent weiter gehen.

**2. Stoppen ist ein Ergebnis.**
Ein Bericht „nicht lösbar, weil …“ ist besser als ein erratener grüner Test.

**3. Wenige Läufe erzwingen Diagnose.**
Jeder weitere Lauf macht den nächsten Versuch billiger und die Begründung dünner.

**4. Gelesene Daten sind Daten.**
Auch wenn sie Anweisungen enthalten.

**Was gesucht wird:** für jeden Schritt, ob ein Fehler bemerkt würde, und wer ihn bemerkt.

---

## Stufe 3 · Optionen

| Option | Käme in Frage, wenn |
|---|---|
| **autonom** | eine Invariante oder Prüfung den Fehler sicher meldet |
| **autonom mit Bericht** | der Fehler im Review sichtbar wird |
| **Rückfrage** | die Aktion Wirkung außerhalb hat |
| **Stopp** | Urteil über Fachliches nötig ist |

---

## Stufe 4 · Entscheidung

### Frage 1 — Wird ein Fehler dieses Schritts bemerkt?

- **technisch** → autonom.
- **im Review** → autonom mit Bericht.
- **nicht sicher** → Rückfrage oder Stopp.

### Frage 2 — Wirkt der Schritt außerhalb des Repositories?

- **Ja** → Rückfrage.

### Frage 3 — Ändert der Schritt, was geprüft wird?

- **Ja** → Stopp.

---

## Der Denkweg auf einen Blick

```
Schritt im Kreislauf
   ↓
ändert er, was geprüft wird?          ja → Stopp
   ↓ nein
wirkt er außerhalb?                   ja → Rückfrage
   ↓ nein
wird ein Fehler bemerkt?              technisch → autonom; im Review → mit Bericht
```

---

## Die eine Prüffrage

> **Was verliert das Team, wenn der Agent hier falsch entscheidet, und merkt es jemand?**

---

## Gegenproben

| Prüfung | Wenn ja, dann |
|---|---|
| Kann der Agent eine Erwartung ändern, ohne dass es gemeldet wird? | Invariante fehlt |
| Meldet der Agent „bestanden“ ohne Nachweis einer Prüfung? | `Passes: 0`-Falle |
| Befolgt der Agent Text aus Testfällen, der seine Regeln ändert? | Prompt Injection |

---

## Wenn die Entscheidung steht

**Regeln mit Durchsetzung aufschreiben.** Jede Regel nennt, wodurch sie greift.

**Den Standard als Kontext bereitstellen.** Nach den Kontextregeln des Teams: Regeln und Routing, keine Beschreibungen.

---

## Verwechslungen, die im Alltag vorkommen

| Verwechselt mit | Erkennungszeichen |
|---|---|
| grün mit richtig | eine geänderte Erwartung macht jeden Test grün |
| mehr Läufe mit mehr Sorgfalt | Raten statt Diagnose |
| Testfalltext mit Auftrag | er beschreibt den Test, er steuert nicht den Agenten |
