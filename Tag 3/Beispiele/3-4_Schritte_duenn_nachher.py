"""3-4 · nachher · Dünne Step-Funktionen auf der vorhandenen Architektur

Eine mögliche Richtung. Ausschnitt, nicht eigenständig lauffähig.

Die Step-Funktionen enthalten keine Squish-Aufrufe und keine Real Names. Sie rufen die
vorhandenen Helper des Teams auf (helper/ui_test_modules/settings_tests.py):

- enable_developer_mode()   öffnet die Diagnose, löst die Aufgabe auf dem Ziffernblock,
                            prüft den Schalter, kehrt zum Hauptbildschirm zurück
- disable_developer_mode()  entsprechend zum Ausschalten

Die Then-Prüfung verwendet die Aufrufe aus der Routing-Tabelle des Teams (click_and_wait für
Navigation mit Zielprüfung, UIElementTest für den Zustand), wie im freigegebenen Referenztest.

Diskussionspunkt aus Tag 2 (2-7, Aktion und Orakel): Beide Helper prüfen am Ende selbst mit
UIElementTest(...).test(True/False). Die Then-Zeile prüft damit ein zweites Mal. Soll die
Prüfung im Helper bleiben, oder gehört sie ausschließlich ins Then?

    Feature: Entwicklermodus
      Scenario: Entwicklermodus einschalten
        Given developer mode is off
        When I switch developer mode on
        Then developer mode is on
"""
from UI.generic_ui import helper as uih
from UI.terminalui_settings import helper as setth
from ui_test_modules.base_ui_test import UIElementTest
from ui_test_modules.settings_tests import disable_developer_mode, enable_developer_mode


@Given("developer mode is off")
def step(context):
    disable_developer_mode()


@When("I switch developer mode on")
def step(context):
    enable_developer_mode()


@Then("developer mode is on")
def step(context):
    uih.statusbar.settings_action_btn.click_and_wait(setth.menu_settings.diagnostics_btn)
    setth.menu_settings.diagnostics_btn.click_and_wait(setth.submenu_diagnostics.developer_mode_toggle)
    UIElementTest(setth.submenu_diagnostics.developer_mode_toggle).test(True)
