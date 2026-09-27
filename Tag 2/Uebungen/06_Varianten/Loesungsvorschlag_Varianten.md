# Lösungsvorschlag · Welche Variante für welches Problem?

**Vorbemerkung:** Ein Vorschlag, keine Musterlösung. Bewertet wird, ob die Entscheidung **an Change Cases begründet** ist.

---

## 1 · Varianten

```python
# direkt
squish.mouseClick(squish.waitForObject(STATUSBAR_SETTINGS_BUTTON))
# … Klicks bis ins Untermenü …
button = squish.waitForObject({"objectName": "itemGnssSourceJ1939", "type": "CheckDelegate", "visible": True})
squish.mouseClick(button)
test.compare(button.checked, True)

# Screen Objects ohne Helper
uih.statusbar.settings_action_btn.click_and_wait(setth.menu_settings.implement_btn)
setth.menu_settings.implement_btn.click_and_wait(masetth.submenu_machinesettings.title_bar_title)
masetth.submenu_machinesettings.open_settings_default_tractor()
masetth.submenu_traction_unit.gnss_gnss_source_btn.click_while_exists()
masetth.submenu_gnss_source.sae_j1939_btn.set(True)
UIElementTest(masetth.submenu_gnss_source.sae_j1939_btn).test(True)

# Screen Objects + Task
select_gnss_source(GnssSource.sae_j1939)
assert_selected_gnss_source(GnssSource.sae_j1939)

# Screenplay
driver = Actor("Fahrer", OperateTerminal(test_exec_helper.target))
driver.attempts_to(SelectGnssSource(GnssSource.sae_j1939))
driver.should_see(SelectedGnssSource(), GnssSource.sae_j1939)
```

---

## 2 · Heutiger Stand

Screen Objects + Task, gemischt mit direktem Control-Zugriff im Test (`sae_j1939_btn.set(True)`).

---

## 3 · Change Cases

| | direkt | Screen Objects | SO + Task | Screenplay |
|---|---|---|---|---|
| C1 Auswahlliste statt Untermenü | alle Tests | alle Tests (Weg) + SO | Task + SO | Task + SO |
| C2 objectName | alle Tests | SO | SO | SO |
| C3 Servicetechniker sieht mehr | alle betroffenen Tests | Tests mit Rollenlogik | Task mit Rollenparameter | Ability oder Actor |
| C4 zweite AUT | alle Tests doppelt | zweite Screen Objects, Tests doppelt | zweite Task-Implementierung | zweite Ability, Tasks bleiben |

---

## 4 · Der unterscheidende Change Case

C4. Nur Screenplay lässt Tests unverändert, wenn die Handlung über einen zweiten Weg geht. C2 ist ab Screen Objects überall gleich.

---

## 5 · Neue Konzepte von Screenplay

| Konzept | im Bestand |
|---|---|
| Interaction | Controls (`click`, `set`) |
| Task | Helper-Funktionen (`open_gnss_source_submenu`) |
| Question | teilweise: `UIElementTest`, `get()` |
| Ability | nicht vorhanden |
| Actor | nicht vorhanden |

Neu wären Actor und Ability.

---

## 6 · Stellungnahme

Eine Umstellung aller Tests lässt sich mit den Change Cases nicht begründen. Für die sechs Tests mit zwei AUTs (C4) wäre Screenplay eine lokale Ergänzung, sobald dort weitere Tests dazukommen. Rollen (C3) lassen sich auch mit einem Parameter am Task lösen.

---

## 7 · Teamregel

SHOULD: Neue Tests verwenden Tasks mit fachlichem Namen. Screenplay wird ergänzt, wo dieselbe Handlung über mehrere Bedienwege getestet wird.

---

## Diskussionsanschluss

Wie viele Tests über zwei AUTs müsste es geben, damit Sie Screenplay ergänzen?
