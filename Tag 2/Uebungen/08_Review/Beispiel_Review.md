# Beispiel · Beibehalten, vereinfachen, ergänzen oder umbauen? – in klein

Dieselbe Aufgabe an einem kleineren Gegenstand, vollständig durchgeführt.

---

## Der Gegenstand

GUI-Tests für ein Kassensystem im Kino. Ausschnitt: eine Hilfsfunktion zum Anmelden.

```python
def login(user):
    screens.login.user_field.set(user.name)
    screens.login.pin_field.set(user.pin)
    screens.login.ok_btn.click()
    squish.snooze(2)
    if screens.error.dialog.exists():
        screens.error.ok_btn.click()
        login(user)
```

Verwendet in 140 Tests.

---

## Phase 1 · Beobachten

| Frage | Antwort |
|---|---|
| Verantwortung | Benutzer anmelden |
| verwendet | Login-Screen, Fehlerdialog |
| verwendet von | 140 Tests |
| technisches Wissen | Reihenfolge der Felder, Fehlerdialog |
| Zustand, Nebenwirkungen | ruft sich bei Fehler selbst erneut auf, ohne Begrenzung |

---

## Phase 2 · Change Cases

| Change Case | Stellen | wo erwartet? |
|---|---|---|
| PIN wird durch Karte ersetzt | `login` | ja |
| Anmeldung dauert länger als 2 s | `login`, sonst sporadische Fehler | ja, aber `snooze` statt Zustand |
| falsche PIN soll getestet werden | nicht möglich, `login` wiederholt endlos | nein |

---

## Phase 3 · Alternativen

| Befund | Alternative | Kosten |
|---|---|---|
| `snooze(2)` | auf Hauptbildschirm warten | eine Zeile |
| endlose Wiederholung | Fehler melden statt wiederholen | Tests mit Glück werden rot |

---

## Phase 4 · Entscheidung

| Punkt | Entscheidung | Begründung |
|---|---|---|
| zentrale Funktion `login` | beibehalten | 140 Tests, ein Ort für den Anmeldeweg |
| `snooze(2)` | gezielt umbauen | Zustand „Hauptbildschirm“ ist abfragbar |
| Wiederholung bei Fehler | gezielt umbauen | verhindert Tests für falsche PIN und verdeckt Fehler |

---

## Regelkandidat

| Frage | Antwort |
|---|---|
| Regel | Hilfsfunktionen wiederholen eine Aktion nicht ohne Begrenzung und Protokolleintrag |
| Problem | verdeckte Fehler, Endlosschleifen |
| Bereich | alle Hilfsfunktionen |
| Ausnahme | keine |
| prüfbar | Review |
| Stufe | MUST |

---

## Was dieses Beispiel zeigt

**Beobachten zuerst.** Die Wiederholung fiel erst als Nebenwirkung auf, nicht als Bewertung.

**Change Cases finden Befunde.** „Falsche PIN testen“ zeigte das Problem.

**Beibehalten ist eine Entscheidung.** Die zentrale Funktion bleibt, begründet.
