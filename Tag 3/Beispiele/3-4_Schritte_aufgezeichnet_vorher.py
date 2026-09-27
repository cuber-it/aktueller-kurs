"""3-4 · vorher · Step-Funktionen, wie Squish sie beim Aufzeichnen erzeugt

Akademisches Beispiel. Szenario aus dem Bestand des Teams: Entwicklermodus in den
Diagnoseeinstellungen einschalten. Nicht eigenständig lauffähig.

Beim Aufzeichnen eines BDD-Tests erzeugt Squish Step-Funktionen mit direkten Squish-Aufrufen
und Namen aus einer Object Map (names.py). Im Framework des Teams entstünde damit eine zweite
Schicht neben Controls, Screen Objects und Helpern:

- eigene Namen statt der Real Names in den UI-Modulen,
- kein enforceFocus(), den das Framework vor dem Umschalten braucht,
- die Aufgabe auf dem Ziffernblock (Quersumme einer angezeigten Zahl) als feste Eingabe:
  aufgezeichnet wird die Lösung von genau diesem einen Mal.

Dasselbe droht bei Step-Funktionen, die ein Werkzeug erzeugt, das das Framework nicht kennt.

    Feature: Entwicklermodus
      Scenario: Entwicklermodus einschalten
        Given developer mode is off
        When I switch developer mode on
        Then developer mode is on
"""
import names


@Given("developer mode is off")
def step(context):
    mouseClick(waitForObject(names.statusbar_settings_button))
    mouseClick(waitForObject(names.settings_diagnostics_button))
    test.compare(waitForObjectExists(names.diagnostics_developer_mode_switch).checked, False)


@When("I switch developer mode on")
def step(context):
    mouseClick(waitForObject(names.diagnostics_developer_mode_switch))
    type(waitForObject(names.numpad_input), "23")          # Lösung der beim Aufzeichnen angezeigten Aufgabe
    mouseClick(waitForObject(names.numpad_enter_button))


@Then("developer mode is on")
def step(context):
    test.compare(waitForObjectExists(names.diagnostics_developer_mode_switch).checked, True)
