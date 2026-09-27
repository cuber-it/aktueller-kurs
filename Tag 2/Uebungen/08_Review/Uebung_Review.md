# Übung · Beibehalten, vereinfachen, ergänzen oder umbauen?

Sie führen ein Architektur-Review an einem Ausschnitt Ihres Frameworks durch, in vier Phasen: beobachten, Change Cases durchspielen, Alternativen nur bei Befund, entscheiden. Ergebnis sind Entscheidungen und Regelkandidaten für die Standards Session.

Eine begründete Entscheidung „so lassen“ zählt genauso wie ein Umbauvorschlag.

---

## Material A · Kandidaten für den Ausschnitt

| Ausschnitt | Stelle | Umfang im Bestand |
|---|---|---|
| K1 Warten und Lesen in `Control` | `UI/controls.py`: `wait`, `wait_for_exists`, `exists`, `get_property_value`, `click_and_wait` | alle Tests |
| K2 Navigation im Test | Testfälle und Helper mit `back_btn.click_and_wait(<Objekt des Zielmenüs>)` | 58 Aufrufe |
| K3 verbliebene Wartezeiten | `snooze` und Parameter wie `snooze_time` | 51 `snooze`, davon 6 direkt nach Klicks |
| K4 Locator-Varianten | `deviating_text`, `deviating_container` | 23 Aufrufe |
| K5 Parameter-Aktionen | `MachineSettingsParameterTests` | 5 Methoden × 3 Aktionen |
| K6 Verifikation | `UIElementTest.test(..., set_setting=True)` | 16 Aufrufe |
| K7 Real Names | UI-Module, keine Object Map | 1 Testfall mit eigenen Real Names |
| K8 Lifecycle | `test_wrapper` | 978 von 983 Testfällen |

Die Gruppe wählt **einen** Ausschnitt. Die Übungen 01 bis 07 enthalten Material zu allen.

---

## Material B · Vorlage

| Phase | Fragen |
|---|---|
| 1 Beobachten | Welche Verantwortung? Wen verwendet er, wer ihn? Welches technische Wissen kapselt er? Welcher Zustand, welche Nebenwirkungen? |
| 2 Change Cases | Welche Stellen ändern sich bei Objektname, anderer AUT, zusätzlichem Schritt, zweitem Target, zusätzlicher Diagnose, AUT-Neustart? |
| 3 Alternativen | nur bei Befund: Verantwortung verschieben, anders schneiden, expliziter machen, direkte Nutzung, zusätzliche Abstraktion, vereinfachen |
| 4 Entscheidung | beibehalten, vereinfachen, ergänzen, gezielt umbauen, nicht übernehmen, offen |

---

## Aufgabe

### Teil 1 · Beobachten

**1.** Wählen Sie einen Ausschnitt aus Material A und beantworten Sie die Fragen aus Phase 1. Keine Bewertung.

### Teil 2 · Change Cases

**2.** Wählen Sie drei Change Cases, die Ihren Ausschnitt betreffen. Tragen Sie ein, welche Stellen sich ändern und ob das dort ist, wo Sie die Verantwortung erwarten.

**3.** Welcher Change Case belastet den Ausschnitt am stärksten?

### Teil 3 · Alternativen und Entscheidung

**4.** Nur wenn Teil 2 einen Befund ergibt: Nennen Sie zwei Alternativen und ihre Kosten.

**5.** Entscheiden Sie für jeden Befund: beibehalten, vereinfachen, ergänzen, gezielt umbauen, nicht übernehmen oder offen. Begründen Sie in einem Satz.

**6.** Was an Ihrem Ausschnitt würden Sie ausdrücklich beibehalten und warum?

### Teil 4 · Regelkandidaten

**7.** Formulieren Sie bis zu drei Regelkandidaten. Für jeden: Welches Problem verhindert er? Für welchen Bereich gilt er? Welche Ausnahme ist legitim? Automatisch prüfbar oder Review? MUST, SHOULD, MAY oder DON'T?

---

## Hinweise zur Bearbeitung

- Nicht die ganze Suite öffnen. Ein Ausschnitt genügt.
- Phase 1 ohne Wörter wie „schlecht“ oder „sollte“.
- Wenn Sie unsicher sind, fragen Sie: **Welche beobachtbare Konsequenz unterscheidet die Varianten?**
