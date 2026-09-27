# Übung · Was prüft dieser Testfall wirklich?

Sie übertragen einen freigegebenen Testfall aus der Testspezifikation in Gherkin. Der Testfall ist geprüft und freigegeben. Die Frage ist, ob die strukturierte Zwischendarstellung Lücken oder Mehrdeutigkeiten sichtbar macht, bevor Code entsteht.

---

## Material A · Der Testfall

Nachgebildet nach der Testspezifikation des Teams, Inhalt in eigenen Worten, Kennung geändert.

**TC-2014 · Neuen Traktor anlegen**  
Art: manuell · Status: Active

| Schritt | Beschreibung | Erwartetes Ergebnis |
|---|---|---|
| Geräteeinstellungen öffnen | Einstellungsmenü öffnen, Geräte wählen. | Die Geräteeinstellungen werden angezeigt. |
| Traktor hinzufügen | Zugfahrzeug wählen, „Neuen Traktor hinzufügen“ wählen, „Tractor“ eingeben und bestätigen. | Der neue Traktor ist angelegt und ausgewählt. |
| Menüs schließen | Mit dem Zahnrad der Statusleiste alle Menüs schließen. | Der Hauptbildschirm wird angezeigt. |

---

## Material B · Zwei Beobachtungen aus der Spezifikation und dem Framework

- Die Spezifikation enthält diesen Testfall zweimal, mit identischen Schritten unter zwei Kennungen.
- Im Framework heißt der Standardtraktor bereits „Tractor“: `open_settings_default_tractor()` sucht den Eintrag mit genau diesem Text.

---

## Material C · Der Weg des Teams

```text
Test Story ──(Skill testcase-writer)──→ Testfälle in Polarion ──(Review, Freigabe)──→ testcase-implementer
```

Der Implementierungs-Skill verlangt für jede prüfbare Erwartung eine Assertion und meldet `# Expected:`-Kommentare ohne Assertion (`check_test.py` F004).

---

## Aufgabe

### Teil 1 · Übertragen

**1.** Schreiben Sie den Testfall als Gherkin-Szenario mit `Given`, `When`, `Then`. Jede `Then`-Zeile muss beobachtbar sein.

**2.** Welche Schritte des Testfalls sind Vorbedingung, welche Aktion, welche Erwartung?

### Teil 2 · Lücken

**3.** Was bedeutet „angelegt und ausgewählt“? Wie beobachtet man es?

**4.** Was passiert, wenn es schon einen Traktor namens „Tractor“ gibt? Welche Szenarien fehlen?

**5.** Welche Fragen an die Fachseite ergeben sich?

### Teil 3 · Einordnen

**6.** An welcher Stelle im Weg aus Material C würde Gherkin stehen: als Ersatz für den Polarion-Testfall, als Zwischenschritt im `testcase-writer`, oder gar nicht?

**7.** Wie hätte ein Review mit Gherkin das Duplikat aus Material B gefunden, oder nicht?

---

## Hinweise zur Bearbeitung

- Gherkin hier als Zwischenrepräsentation, nicht als ausführbare BDD-Schicht.
- Keine Widget-Namen oder Klickfolgen in die Szenarien.
- Wenn Sie unsicher sind, fragen Sie: **Woran würde ein Beobachter sehen, dass das Verhalten eingetreten ist?**
