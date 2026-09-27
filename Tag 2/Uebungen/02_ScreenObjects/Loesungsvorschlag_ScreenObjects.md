# Lösungsvorschlag · Was bietet ein Menü dem Test an?

**Vorbemerkung:** Ein Vorschlag, keine Musterlösung. Welche Operationen ein Screen Object anbietet, hängt davon ab, welche Wege die Tests gehen. Bewertet wird, ob **Wissen über Wege beim Menü** liegt und ob **der Test nur noch sagt, was er will**.

---

## 1 · Page-Object-Ideen in `SubMenuMachineSettings`

| Idee | umgesetzt? |
|---|---|
| ein Objekt je Menü | ja |
| Real Names an einer Stelle | ja |
| Operationen statt Controls | teilweise: zwei Navigationsmethoden |
| Navigation liefert das Ziel | nein |
| Warten auf den Zielzustand in der Operation | teilweise: `wait_for_exists` vor dem Klick, danach nichts |

---

## 2 · Wissen über Menüwege

| Stelle | gehört in |
|---|---|
| Statusleiste → Einstellungen → Maschine | `StatusBar.open_settings()`, `MenuSettings.open_machine_settings()` |
| Maschine → Traktor → GNSS-Quelle | `SubMenuMachineSettings.open_tractor_settings()`, `SubMenuTractionUnit.open_gnss_source()` |
| wohin Zurück aus der GNSS-Quelle führt | `SubMenuGNSSSource.go_back()` |
| Reihenfolge beim Schließen der Menüs | je Menü ein `go_back()`, die Kette ergibt die Reihenfolge |

`open_gnss_source_submenu` bleibt als fachlicher Helper bestehen und verwendet die Navigationsmethoden.

---

## 3 · Die zwei Öffnen-Methoden

Sie unterscheiden sich in Button (`implement_settings_btn` gegen `tractor_settings_btn`) und Text (Parameter gegen `"Tractor"`). Zusammengeführt:

```python
def _open_settings_of(self, name, button):
    entry = self.menu_list.delegate.with_text(name)
    target = button.inside(entry)
    target.wait_for_exists()
    squish.snooze(MENU_ROLL_OUT_TIME)  # Give the menu Time to roll out all options
    target.click(quiet=True)

def open_implement_settings_by_text(self, text):
    self._open_settings_of(text, self.implement_settings_btn)
    return helper.submenu_implement

def open_settings_default_tractor(self):
    self._open_settings_of("Tractor", self.tractor_settings_btn)
    return helper.submenu_traction_unit
```

`with_text` und `inside` sind aus Aufgabe 6. Das kurze `snooze(MENU_ROLL_OUT_TIME)` ist kommentiert und überbrückt eine Animation; es bleibt.

---

## 4 · `go_back()`

```python
class SubMenuGNSSSource(ListCtrlMixin):
    def go_back(self) -> "SubMenuTractionUnit":
        self.back_btn.click_and_wait(helper.submenu_traction_unit.traction_unit_title_txt)
        return helper.submenu_traction_unit
```

Die Zeile im Test:

```python
traction_unit = masetth.submenu_gnss_source.go_back()
```

Führt der Zurück-Button nach einem Umbau in ein anderes Menü, ändert sich nur `go_back()`: Sie wartet auf den Titel des neuen Ziels und gibt dessen Screen Object zurück. Tests, die danach Methoden des Menüs Zugfahrzeug aufrufen, fallen dabei sofort auf, weil der Rückgabetyp nicht mehr passt.

---

## 5 · `close_machine_settings_menus` mit `go_back()`

```python
class SubMenuTractionUnit(AnyDeviceSubMenuMixin):
    def go_back(self) -> "SubMenuMachineSettings":
        self.back_btn.click_and_wait(helper.submenu_machinesettings.title_bar_title)
        return helper.submenu_machinesettings


class SubMenuMachineSettings(ListCtrlMixin):
    def go_back(self) -> "MenuSettings":
        self.back_btn.click_while_exists()
        return setth.menu_settings


def close_machine_settings_menus():
    masetth.submenu_traction_unit.go_back().go_back().go_back()
```

Kommt ein Menü dazwischen, ändert sich das `go_back()` des Menüs, aus dem man zurückkehrt. Die Funktion bleibt gleich, solange die Zahl der Schritte gleich bleibt. Ändert sie sich, zeigt der Rückgabetyp der Kette die Stelle.

Die Coding-Regeln des Teams verlangen für Wege über mehrere Menüs bereits „a function that returns the page helper it landed on“. `go_back()` wendet das auf jeden einzelnen Schritt an.

---

## 6 · Varianten ohne geteilten Zustand

`deviating_name_value` stellt den Real Name nach dem `yield` wieder her, ohne `try/finally`. Wirft der Block, bleibt der veränderte Real Name im geteilten Control. Der nächste Aufruf speichert den falschen Wert als „vorher“ und stellt ihn wieder her.

```python
class Control:
    def with_text(self, text):
        variant = copy(self)
        variant.name = {**self.name, "text": text}
        variant.display_name = f"{self.display_name} '{text}'"
        return variant

    def inside(self, container):
        variant = copy(self)
        variant.name = {**self.name, "container": dict(container.name)}
        variant.display_name = f"{self.display_name} in {container.display_name}"
        return variant
```

Das geteilte Control bleibt unverändert. Kleinste Korrektur des Bestands wäre ein `try/finally` in `deviating_name_value`.

---

## 7 · Soll `go_back()` prüfen?

| dafür | dagegen |
|---|---|
| Eine gescheiterte Navigation meldet sich sofort mit dem Menü, das fehlt | Warten auf das Ziel ist bereits eine Prüfung; eine zweite ist doppelt |
| Der Test bleibt frei von Navigationsprüfungen | Tests, die gerade eine gescheiterte Navigation prüfen wollen, brauchen einen anderen Weg |

Vorschlag: `go_back()` wartet auf das Ziel und meldet mit `fail_test(..., raise_exception=True)`, wenn es nicht kommt. Eine eigene Prüfung darüber hinaus ist nicht nötig.

---

## 8 · Keine Object Map

Kein Problem, solange jeder Real Name einmal steht (heute der Fall: 1 Testfall mit eigenen Real Names). Eine Änderung wie „`objectName` des Eintrags SAE J1939 ändert sich“ ist eine Zeile im UI-Modul. Eine Object Map würde diese Zeile an einen anderen Ort verschieben, aber nicht einsparen.

---

## Diskussionsanschluss

Welche fünf Wege gehen Ihre Tests am häufigsten? Mit diesen würden Sie anfangen.
