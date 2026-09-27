# Übung · Wo landet jeder Schritt?

Sie bilden ein Gherkin-Szenario auf Ihr Testframework ab. Dabei zeigt sich, welche Schritte vorhandene Controls, Screen Objects und Helper tragen, und wo etwas fehlt. Die Frage ist, was ein Agent an einer solchen Lücke tun soll.

---

## Material A · Das Szenario

Aus Übung 03:

```gherkin
Scenario: Neuen Traktor mit neuem Namen anlegen
  Given das Terminal hat nur den Standardtraktor "Tractor"
  When ich einen neuen Traktor mit dem Namen "Traktor 2" anlege
  Then enthält die Liste der Zugfahrzeuge "Tractor" und "Traktor 2"
  And "Traktor 2" ist ausgewählt
```

---

## Material B · Was es im Framework gibt

Für Anbaugeräte gibt es einen Button zum Anlegen. Aus `UI/machinesettings_ui.py` (gekürzt):

```python
class SubMenuAnyImplement(ListCtrlMixin):
    # This Sub Menu is for the Creation of new implements and the assignment of existing implements
    def __init__(self):
        ...
        self.add_new_implement_btn = Button(
            {"container": self.container, "objectName": "implementAddNew", "type": "ItemDelegate", "visible": True},
            "Add New Implement Button", MACHINESETTINGS_APP_NAME)
```

Verwendung in einem Testfall des Teams (gekürzt):

```python
masetth.submenu_machinesettings.click_unselected_front_implement()
masetth.submenu_any_implement.add_new_implement_btn.click_with_entry(option_text_front)
if masetth.submenu_any_implement.menu_list.get_by_text(option_text_front):
    test.passes(f"The CheckDelegate {option_text_front} is checked.")
else:
    test.fail(f"The CheckDelegate {option_text_front} is either not checked or not found!")
```

Für Traktoren gibt es im Framework **keinen** Button zum Anlegen. Es gibt `SubMenuTractionUnit` und `open_settings_default_tractor()`.

---

## Material C · Regeln aus dem Skill des Teams

- **No-Hallucination-Regel:** Kein Helper-Attribut erfinden. Suchreihenfolge: generierte UI-Übersicht → Anzeigetexte aus dem Quellcode → `UI/*.py` → Spy-Dump (nach Rückfrage) → `# TODO:` und fragen.
- **Platzierung neuer Helper (Schritt 4b):** Ein neues Element oder ein neuer Bildschirm gehört in das `UI/*.py` der App. Ein Weg über mehrere Menüs gehört als Funktion, die den erreichten Page Helper zurückgibt, in `helper/ui_test_modules/*_tests.py`.
- **Routing:** Umschalter und Listeneinträge prüfen mit `UIElementTest(...).test(...)`; einen bestimmten Eintrag einer Liste über `menu_list.get_delegate_by_text(text)`.

---

## Aufgabe

### Teil 1 · Abbilden

**1.** Legen Sie eine Tabelle an: Gherkin-Zeile → vorhandener Aufruf im Framework, oder „fehlt“.

**2.** Wie stellen Sie das `Given` her, ohne die UI-Schritte ins Szenario zu holen?

### Teil 2 · Die Lücke

**3.** Für „einen neuen Traktor anlegen“ gibt es keinen Button. Was darf ein Agent an dieser Stelle tun, was nicht?

**4.** Wohin gehört der fehlende Button, wenn er ergänzt wird? Wie würde er aussehen, und woher kommen `objectName` und `type`?

**5.** Die Prüfung im Beispiel aus Material B verwendet `test.passes` und `test.fail`. Wie sähe sie mit den Routing-Regeln aus Material C aus?

### Teil 3 · Step Definitions

**6.** Schreiben Sie die Step-Funktionen für das Szenario so dünn wie möglich. Wo steht der Code, der heute in `test.py` stünde?

**7.** Würde eine Schicht aus Step Definitions die Routing-Tabelle des Skills ersetzen, ergänzen oder verdoppeln?

---

## Hinweise zur Bearbeitung

- Nur Namen verwenden, die in Material B stehen. Für Fehlendes einen Platzhalter mit `# TODO:` schreiben.
- Squish-BDD-Syntax: `@Given("...")`, `@When`, `@Then`, `@Step` über `def step(context, …)`; Platzhalter `|word|`, `|integer|`, `|any|`.
- Wenn Sie unsicher sind, fragen Sie: **Gibt es das schon, und wenn nicht, wer entscheidet, wo es entsteht?**
