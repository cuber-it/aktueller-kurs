# Lösungsvorschlag · Was prüft dieser Testfall wirklich?

**Vorbemerkung:** Ein Vorschlag, keine Musterlösung. Bewertet wird, ob **jedes Then beobachtbar** ist und ob **der Ausgangszustand das Ergebnis nicht vorwegnimmt**.

---

## 1 · Gherkin

```gherkin
Feature: Traktor anlegen

  Background:
    Given das Terminal hat nur den Standardtraktor "Tractor"

  Scenario: Neuen Traktor mit neuem Namen anlegen
    When ich einen neuen Traktor mit dem Namen "Traktor 2" anlege
    Then enthält die Liste der Zugfahrzeuge "Tractor" und "Traktor 2"
    And "Traktor 2" ist ausgewählt

  Scenario: Neuen Traktor mit vorhandenem Namen anlegen
    When ich einen neuen Traktor mit dem Namen "Tractor" anlege
    Then erscheint ein Hinweis, dass der Name schon vergeben ist
    And die Liste der Zugfahrzeuge enthält "Tractor" genau einmal

  Scenario: Anlegen abbrechen
    When ich einen neuen Traktor beginne und die Eingabe abbreche
    Then enthält die Liste der Zugfahrzeuge nur "Tractor"
```

---

## 2 · Zuordnung

| Schritt | Rolle |
|---|---|
| Geräteeinstellungen öffnen | Weg, gehört in keines der drei |
| Traktor hinzufügen | When |
| Menüs schließen | Aufräumen, kein Then |
| „angelegt und ausgewählt“ | zwei Then |

---

## 3 · „Angelegt und ausgewählt“

Angelegt: Die Liste enthält einen Eintrag mehr als vorher. Ausgewählt: Genau dieser Eintrag ist markiert. Beides lässt sich nur mit einem Namen beobachten, den es vorher nicht gab.

---

## 4 · Name existiert schon

Der Testfall prüft dann den Ausgangszustand. Es fehlen: vorhandener Name, Abbruch, leerer Name, sehr langer Name.

---

## 5 · Fragen an die Fachseite

1. Darf ein Name doppelt vorkommen?
2. Wird der neue Traktor immer ausgewählt, auch wenn schon einer ausgewählt ist?
3. Welche Zeichen und Längen sind erlaubt?

---

## 6 · Einordnung

Als Zwischenschritt im `testcase-writer`: Er erzeugt aus der Story Szenarien, ein Mensch prüft sie mit den Fragen aus Aufgabe 5, dann entstehen die Polarion-Schritte. Polarion bleibt führend, Gherkin ist Arbeitsmittel.

---

## 7 · Duplikat

Zwei Szenarien mit identischem Text fallen beim Lesen leichter auf als zwei Tabellen in einer Spezifikation mit 142 Seiten und 155 Testfällen. Sicher gefunden werden sie nur durch einen Vergleich, etwa durch einen Agenten, der Testfälle gegeneinander prüft (3-5).

---

## Diskussionsanschluss

Welche weiteren Testfälle in Ihrer Spezifikation prüfen einen Zustand, den es vor der Aktion schon gab?
