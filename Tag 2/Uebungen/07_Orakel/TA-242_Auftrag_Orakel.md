# TA-242 · Prüfungen melden Folgefehler statt Ursache

**Typ:** Bug
**Komponente:** Verifikation (`ui_test_modules/base_ui_test.py`)
**Priorität:** Hoch

---

## Story

**Als** Verantwortlicher für die Auswertung des Nachtlaufs
**möchte ich** aus einer FAIL-Meldung erkennen, ob eine Aktion oder eine Prüfung gescheitert ist,
**damit** ich Fehler der AUT von Fehlern des Tests unterscheiden kann.

---

## Description

`UIElementTest.test(value, set_setting=True)` setzt einen Wert und prüft ihn in einem Aufruf. Scheitert das Setzen, meldet die Prüfung eine Abweichung.

**Bestand:**

| Was | Anzahl |
|---|---|
| `UIElementTest` | 148 |
| `test(..., set_setting=True)` | 16 |
| Prüfungen, die bei Abweichung abbrechen | 0 (FAIL, Test läuft weiter) |

**Befund:** Scheitert die Eingabe, trägt `click_with_entry` „Keyboard didn't open“ ein, und der Test läuft weiter. Die folgenden Vergleiche melden Abweichungen, die nur Folgen sind. Im Protokoll steht die Ursache zwischen mehreren scheinbar eigenständigen Fehlern.

**Befund zur Entstehung:** `set_setting=True` spart eine Zeile im Test. Scheitert das Setzen, trägt `click_with_entry` einen FAIL ein und der Test läuft weiter. Die folgenden Vergleiche melden Abweichungen, die nur Folgen sind.

**Nicht Gegenstand:** Die übrigen Prüfarten von `UIElementTest`.

## Randbedingungen

- Die 148 bestehenden Aufrufe laufen weiter.
- Ein FAIL bricht einen Test heute nicht ab. Das ist beabsichtigt: Ein Lauf soll möglichst viele Befunde liefern.
- Die Umwandlung `type(value)(…)` bleibt für die bestehenden Aufrufe erhalten.

## Akzeptanzkriterien

- **AK1** – In neuen Tests stehen Setzen und Prüfen in getrennten Aufrufen.
- **AK2** – Scheitert das Setzen, folgen im selben Testschritt keine Vergleiche, die nur Folgen melden.
- **AK3** – Die Umwandlung des gelesenen Werts ist ausdrücklich angegeben, wenn sie nicht trivial ist.
- **AK4** – Die Meldung nennt Control, Real Name, Erwartung und gelesenen Rohwert.
- **AK5** – Für Folgefehler ist entschieden, ob der Test abbricht.

## Hinweise

`set_setting=True` einfach zu entfernen erfüllt AK2 nicht: `click_with_entry` meldet das Scheitern, bricht aber nicht ab.

AK5 wird unbequem: Abbrechen verhindert Folgefehler, aber auch weitere Befunde.

---

## Für den Kurs

Dieses Ticket nennt keine Lösung. Arbeiten Sie entlang der Frage:

**Was sagt dieser rote Test, und was nicht?**

---
---

# Addendum · Aktion, Beobachtung, Bewertung

```text
Aktion  →  AUT  →  Beobachtung  →  Vergleich mit Erwartung  →  Ergebnis
```

| Teil | Beispiel |
|---|---|
| Aktion | `control.set("6.5")` |
| Beobachtung | `control.get()` |
| Orakel | Erwartung 6.5 aus der Referenz |
| Bewertung | Vergleich, PASS oder FAIL |

## Ursachen eines roten Tests

| Ursache | Hinweis in der Meldung |
|---|---|
| AUT-Fehler | Aktion gelungen, Wert falsch |
| Testfehler | falsche Erwartung, falsches Control |
| Umgebung | Target nicht erreichbar, Datensatz fehlt |
| Synchronisation | Objekt nicht da, Wert noch nicht aktualisiert |
