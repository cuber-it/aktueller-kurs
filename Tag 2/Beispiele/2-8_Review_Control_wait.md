# 2-8 · Ausgefüllte Review-Vorlage: Warten in `Control`

Beispiel für einen Review-Ausschnitt, bearbeitet nach den vier Phasen aus 2-8. Grundlage ist
`UI/controls.py` im Testframework des Teams. Die Entscheidungen in Phase 4 sind Vorschläge,
entscheiden muss das Team.

## Phase 1 · Beobachten

| Frage | Antwort |
|---|---|
| Verantwortung | `Control.wait`, `wait_for_exists`, `exists`, `get_property_value`, `click_and_wait`: auf UI-Objekte warten, sie finden und lesen |
| verwendet | `squish.waitForObject`, `squish.waitForObjectExists`, `object.exists`, `squish.waitFor`, Target-Helper (Kontextwechsel, Neuverbindung) |
| verwendet von | allen Screen Objects, allen Helpern, `UIElementTest`, indirekt allen 983 Testfällen |
| gekapseltes Wissen | Kontextwechsel vor jedem Zugriff, Neuverbindung bei Null-Objekt, Timeouts |
| Zustand, Nebenwirkungen | wechselt den aktiven Application Context; kann die Anwendung trennen und neu verbinden |

## Phase 2 · Change Cases

| Change Case | betroffene Stellen |
|---|---|
| Ein Feld erscheint erst 0,3 s nach dem Menü | `get_property_value` liest ohne Warten: "Found: None". Möglicherweise heute durch `snooze` im Test ausgeglichen |
| Ein Panel öffnet langsamer als 0,5 s | `click_and_wait` klickt erneut. Bei umschaltenden Quellen (`layout_manager_btn`) schließt der zweite Klick das Panel; die Coding-Regeln sichern das nur für den Aufrufer ab |
| Ein Objekt wurde in der AUT umbenannt | `wait` meldet es und liefert `None`; `get` meldet stattdessen "Found: None" ohne Hinweis auf das fehlende Objekt |
| Die AUT startet während des Tests neu | Null-Objekt-Schleife in `wait` und `wait_for_exists` verbindet neu, ohne Eintrag im Log |

## Phase 3 · Alternativen, nur bei Befund

| Befund | Alternative |
|---|---|
| Lesen ohne Warten | `get_property_value` wartet mit kurzem Lese-Timeout, sonst Abbruch mit Real Name (Beispiel 2-3) |
| Wiederholungsklick | einmal klicken, dann warten; Wiederholen als eigene Methode für Controls, die verschwinden (Beispiel 2-3) |
| stille Neuverbindung | Neuverbindung beibehalten, aber mit `test.log` sichtbar machen |

## Phase 4 · Entscheidung

| Punkt | Vorschlag |
|---|---|
| Kontextwechsel im Control | **beibehalten**: nimmt jedem Test Arbeit ab |
| Lesen ohne Warten | **gezielt umbauen** |
| Wiederholungsklick in `click_and_wait` | **gezielt umbauen**, Fälle mit verlorenen Klicks vorher benennen |
| Neuverbindung bei Null-Objekt | **ergänzen**: Log-Eintrag |

## Regelkandidaten

- SHOULD: Lesende Methoden warten auf das Objekt und melden ein fehlendes Objekt mit Real Name.
- SHOULD: Wiederholte Klicks nur, wo die Schleife den geklickten Control selbst beobachtet.
- MUST (bereits Teamregel): kein `snooze` nach einem Navigationsklick.
