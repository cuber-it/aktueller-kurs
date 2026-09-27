# 3-3 · nachher · Derselbe Testfall als Gherkin

Eine mögliche Richtung. Gherkin als Zwischenrepräsentation vor dem Review, nicht als ausführbare BDD-Schicht.

---

```gherkin
Feature: Werkseinstellungen wiederherstellen

  Background:
    Given das Terminal ist betriebsbereit
    And die Sprache ist auf "Deutsch" statt auf den Werkswert "English" gestellt

  Scenario: Zurücksetzen bestätigen
    When ich in den Systemeinstellungen "Werkseinstellungen wiederherstellen" wähle
    And ich die Warnung bestätige
    Then startet das Terminal neu
    And nach dem Neustart wird der Hauptbildschirm angezeigt
    And die Sprache ist "English"

  Scenario: Zurücksetzen abbrechen
    When ich in den Systemeinstellungen "Werkseinstellungen wiederherstellen" wähle
    And ich die Warnung abbreche
    Then startet das Terminal nicht neu
    And die Sprache ist weiterhin "Deutsch"
```

---

## Was die Zwischenrepräsentation sichtbar gemacht hat

| Befund | im Polarion-Testfall |
|---|---|
| Die fachliche Erwartung (Einstellungen auf Werkswert) fehlte | nur der Bedienweg geprüft |
| Ohne geänderte Einstellung vorher ist Zurücksetzen nicht beobachtbar | keine Vorbedingung |
| Der Abbruch ist ein eigener Fall | nur im Expected erwähnt (rotes X) |
| Welche Einstellungen zurückgesetzt werden, ist offen | Frage an die Fachseite |
| Wie lange der Neustart dauern darf, ist offen | „warten, bis abgeschlossen“ |

## Was Gherkin hier nicht leistet

- Es ersetzt nicht die Freigabe in Polarion. Szenarien können dort als Testfälle landen.
- Es sagt nichts darüber, wie ein Neustart im Test abgewartet wird. Das ist Architektur (3-4) und beim Team eine Frage des Target-Helpers.
- Die zwei offenen Fragen beantwortet nur die Fachseite.
