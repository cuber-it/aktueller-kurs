# Beispiel · Was erzählt dieser Test? – in klein

Dieselbe Aufgabe an einem kleineren Gegenstand, vollständig durchgeführt.

---

## Der Gegenstand

GUI-Tests für das Wartungsmenü einer Aufzugssteuerung. Ein Test prüft die Fahrt in den Wartungsmodus:

```python
def test_maintenance_mode():
    screens.home.service_btn.click_and_wait(screens.pin.title)
    screens.pin.enter("4711")
    screens.service.modes_list.click_by_text("Wartung")
    screens.service.confirm_btn.click_and_wait(screens.status.mode_label)
    assert screens.status.mode_label.get() == "Wartung aktiv"
    assert screens.status.floor_label.get() == "EG"
```

---

## Schritt 1 · Ebenen

| Zeile | Ebene |
|---|---|
| `service_btn.click_and_wait(pin.title)` | Navigation |
| `pin.enter("4711")` | Bedienung (Anmeldung) |
| `modes_list.click_by_text("Wartung")` | Bedienung, fachlich: Modus wählen |
| `confirm_btn.click_and_wait(…)` | Bedienung |
| `mode_label.get() == …` | Prüfung |
| `floor_label.get() == "EG"` | Prüfung: Aufzug fährt ins Erdgeschoss |

---

## Schritt 2 · Fachliche Operationen

```python
def enter_service_menu(pin):
    screens.home.service_btn.click_and_wait(screens.pin.title)
    screens.pin.enter(pin)


def switch_to_mode(mode: Mode):
    screens.service.modes_list.click_by_text(mode.value)
    screens.service.confirm_btn.click_and_wait(screens.status.mode_label)


def test_maintenance_mode():
    enter_service_menu(TECHNICIAN_PIN)
    switch_to_mode(Mode.maintenance)
    assert screens.status.mode_label.get() == "Wartung aktiv"
    assert screens.status.floor_label.get() == "EG"
```

---

## Schritt 3 · Was bleibt sichtbar?

Die Prüfungen bleiben im Test. Ein Leser sieht: Wartungsmodus einschalten, danach steht der Aufzug im Erdgeschoss. Wie das Menü bedient wird, steht in zwei Funktionen.

---

## Was dieses Beispiel zeigt

**Die fachliche Operation nennt die Absicht, der Parameter die Variante.** `switch_to_mode(Mode.maintenance)` statt eines Attributnamens.

**Prüfungen bleiben im Test.** Sie sind die Aussage des Tests.

**Konstanten statt Werte.** `TECHNICIAN_PIN` statt `"4711"` sagt, wessen PIN.
