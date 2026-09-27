# Übung · Wie viel darf der Agent allein?

Sie legen für den geschlossenen Kreislauf aus Umsetzung, Lauf, Auswertung und Korrektur fest, wo der Agent allein weitermacht, wo er stoppt und wo ein Mensch entscheidet. Ergebnis ist ein erster Entwurf der Regeln für KI-gestütztes Test Engineering.

---

## Material A · Der Kreislauf heute (Schritt 7b)

```text
test.py fertig, check_test.py sauber
   → assertion_guard.py snapshot
   → Rückfrage an den Menschen                                   ◆
   → run_testcase.sh, parse_run.py
   → Urteil: Test- oder AUT-Fehler, mit Begründung
   → erlaubte Korrektur
   → 2. Lauf (höchstens)
   → assertion_guard.py check
   → Bericht                                                     ◆
```

Erlaubte Korrekturen laut Skill: falsches Attribut, falscher Selector oder `type:`, falscher Anzeigetext, fehlendes Warten oder Neuverbinden, falscher Import. Nie erlaubt: Assertion löschen oder abschwächen, Timeout erhöhen, erwarteten Wert an das Gerät anpassen.

---

## Material B · Zwei Hinweise aus dem Skill

- „`Passes: 0` is normal“: `UIElementTest` meldet nur Fehler. Ein gesunder Lauf zeigt null bestandene Prüfungen.
- „Two runs is enough to apply a diagnosis, not enough to guess your way to green.“

---

## Material C · Fragen aus der Standards Session

- Welche Schritte dürfen autonom laufen?
- Wo sind menschliche Kontrollpunkte nötig?
- Welche Regeln muss KI-generierter Code erfüllen?
- Wie sichern wir Reproduzierbarkeit?
- Wie gehen wir mit Vertrauen, Guardrails und Prompt Injection um?

---

## Aufgabe

### Teil 1 · Stoppen

**1.** Nennen Sie alle Bedingungen, unter denen der Agent heute stoppt. Welche fehlen?

**2.** Warum ist die Grenze 2 Läufe und nicht 5? Was spricht für 1?

**3.** Ein Lauf zeigt `Passes: 0` und `verdict : PASS`. Was muss der Agent prüfen, bevor er „bestanden“ meldet? `assertion_guard.py` vergleicht die Assertion-Zeilen in `test.py`. Wo stehen bei Ihnen die erwarteten Werte, und was folgt daraus?

### Teil 2 · Entscheiden

**4.** Welche Fehlerbilder darf der Agent selbst korrigieren, welche muss er melden? Ordnen Sie zu: Selector passt nicht, Wert weicht ab, Lauf nicht gestartet, Test läuft ins Timeout, Referenzbild fehlt.

**5.** Wo in Material A würden Sie einen weiteren Kontrollpunkt setzen, wo einen entfernen?

### Teil 3 · Regeln

**6.** Formulieren Sie fünf Regeln für KI-gestütztes Test Engineering als MUST, SHOULD oder DON'T. Mindestens eine zu Prompt Injection.

**7.** Welche Ihrer Regeln lassen sich technisch durchsetzen, welche bleiben Anweisung? Beziehen Sie Übung 01 und 06 ein.

---

## Hinweise zur Bearbeitung

- Es gibt keine richtige Zahl an Kontrollpunkten, nur begründete.
- Prompt Injection heißt hier: Anweisungen in Daten, die der Agent liest (Testfalltext, Protokolle, Kommentare).
- Wenn Sie unsicher sind, fragen Sie: **Was verliert das Team, wenn der Agent hier falsch entscheidet, und merkt es jemand?**
