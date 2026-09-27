# Denkmodell · Aktion, Beobachtung und Bewertung trennen

Vier Stufen: **Signale → Erkenntnisse → Optionen → Entscheidung.**

---

## Stufe 1 · Signale

### Im Code

| Signal | Beispiel |
|---|---|
| Setzen und Prüfen in einem Aufruf | `test(value, set_setting=True)` |
| Umwandlung nach Typ der Erwartung | `type(value)(control.get())` |
| Meldungen nur mit Erwartung und Ergebnis | „Expected: 6.5. Found: 5.0“ |
| Prüfungen, die weiterlaufen lassen | `fail_test` ohne `raise_exception` |
| Ergebnis in Attribut, das erst in der Methode entsteht | `self.cur_value` |

### Im Nachtlauf

| Signal | Konkret |
|---|---|
| mehrere FAILs mit einer Ursache | vier Werte, eine Tastatur |
| Analyse beginnt bei der AUT | Speicherlogik geprüft |
| Video als einziger Beleg | Aufzeichnung zeigt die Ursache |

---

## Stufe 2 · Erkenntnisse

**1. Eine Prüfung sagt nur etwas über den Vergleich.**
War die Aktion davor erfolglos, ist die Abweichung eine Folge.

**2. Wer handelt, meldet, ob die Handlung gelang.**
Das gehört zur Aktion, nicht zur Prüfung danach.

**3. Umwandlungen sind Teil des Orakels.**
Wie Text zu Zahl oder Wahrheitswert wird, entscheidet über das Ergebnis.

**4. Weiterlaufen erzeugt Befunde und Folgefehler.**
Ob ein Test abbricht, hängt davon ab, ob die nächsten Schritte noch aussagekräftig sind.

**Was gesucht wird:** für jede Meldung die Stelle, die sie verursacht hat.

---

## Stufe 3 · Optionen

| Option | Käme in Frage, wenn |
|---|---|
| **Setzen und Prüfen getrennt** | die Aktion scheitern kann |
| **Aktion meldet ihr Scheitern** | eine Eingabe nicht ankommen kann |
| **ausdrückliche Umwandlung** | gelesener Typ und erwarteter Typ sich unterscheiden |
| **Abbruch nach Fehler** | nachfolgende Schritte vom Ergebnis abhängen |
| **Weiterlaufen** | nachfolgende Prüfungen unabhängig sind |

---

## Stufe 4 · Entscheidung

### Frage 1 — Kann die Aktion scheitern, ohne dass es gemeldet wird?

- **Ja** → die Aktion meldet ihr Scheitern selbst.

### Frage 2 — Unterscheiden sich gelesener und erwarteter Typ?

- **Ja** → Umwandlung ausdrücklich angeben.

### Frage 3 — Hängen folgende Schritte vom Ergebnis ab?

- **Ja** → abbrechen.
- **Nein** → FAIL eintragen, weiterlaufen.

---

## Der Denkweg auf einen Blick

```
Aktion                 →  meldet selbst, ob sie gelang
Beobachtung            →  Rohwert lesen
Umwandlung             →  ausdrücklich
Bewertung              →  Meldung mit Control, Real Name, Erwartung, Rohwert
Abhängige Folgeschritte?  ja → abbrechen   nein → weiter
```

---

## Die eine Prüffrage

> **Was sagt dieser rote Test, und was nicht?**

---

## Gegenproben

| Prüfung | Wenn ja, dann |
|---|---|
| Nennen mehrere FAILs dieselbe Ursache nicht? | Folgefehler |
| Steht in einer Meldung nur „Expected/Found“? | Diagnose fehlt |
| Wird ein `bool` aus Text mit `bool(...)` gebildet? | jeder nicht leere Text ist `True` |
| Setzt eine Prüfung selbst Werte? | Aktion und Bewertung vermischt |

---

## Wenn die Entscheidung steht

**Neue Tests trennen.** Bestehende Aufrufe mit `set_setting=True` bleiben, bis sie angefasst werden.

**Aktionen härten.** `set()` meldet, wenn die Tastatur nicht öffnet.

**Abbruchregel aufschreiben.** Pro Testschritt oder pro Test.

---

## Verwechslungen, die im Alltag vorkommen

| Verwechselt mit | Erkennungszeichen |
|---|---|
| Assertion mit Orakel | das Orakel ist die Quelle der Erwartung, die Assertion der Vergleich |
| FAIL mit Fehlerursache | ein FAIL zeigt, wo verglichen wurde |
| Weiterlaufen mit Robustheit | weitere FAILs können Folgen sein |
