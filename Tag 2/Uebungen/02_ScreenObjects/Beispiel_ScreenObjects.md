# Beispiel · Was bietet ein Menü dem Test an? – in klein

Dieselbe Aufgabe an einem kleineren Gegenstand, vollständig durchgeführt.

---

## Der Gegenstand

GUI-Tests für das Bedienfeld eines Kaffeevollautomaten. Ein Test bereitet einen Cappuccino zu:

```python
def test_cappuccino():
    screens.home.drinks_btn.click()
    screens.drinks.cappuccino_btn.click()
    screens.strength.strong_btn.click()
    screens.strength.start_btn.click_and_wait(screens.progress.title)
    screens.progress.title.wait_for_not_exists(timeout_msec=60000)
    assert screens.home.message.get() == "Enjoy!"
```

Das Screen Object der Stärkeauswahl:

```python
class StrengthScreen:
    def __init__(self):
        self.strong_btn = Button({"objectName": "strengthStrong"})
        self.start_btn = Button({"objectName": "start"})
```

Neue Anforderung: **Nach der Stärke wird künftig die Tassengröße gewählt.**

---

## Schritt 1 · Was steht im Test, das zum Menü gehört?

| Stelle | gehört zu |
|---|---|
| `drinks_btn.click()` → Getränkeauswahl | `HomeScreen` |
| `start_btn.click_and_wait(screens.progress.title)` | `StrengthScreen`: wohin Start führt |
| `progress.title.wait_for_not_exists(60000)` | `ProgressScreen`: wann die Zubereitung fertig ist |

---

## Schritt 2 · Operationen entwerfen

```python
class HomeScreen:
    def open_drinks(self) -> "DrinksScreen":
        self.drinks_btn.click_and_wait(screens.drinks.title)
        return screens.drinks


class DrinksScreen:
    def choose(self, drink) -> "StrengthScreen":
        self.button_for(drink).click_and_wait(screens.strength.title)
        return screens.strength


class StrengthScreen:
    def start(self, strength) -> "ProgressScreen":
        self.button_for(strength).click()
        self.start_btn.click_and_wait(screens.progress.title)
        return screens.progress


class ProgressScreen:
    def wait_until_done(self) -> "HomeScreen":
        self.title.wait_for_not_exists(timeout_msec=60000)
        return screens.home
```

Der Test:

```python
def test_cappuccino():
    home = screens.home.open_drinks().choose("Cappuccino").start("strong").wait_until_done()
    assert home.message.get() == "Enjoy!"
```

---

## Schritt 3 · Die neue Anforderung

Die Tassengröße kommt zwischen Stärke und Start. Geändert wird `StrengthScreen.start`: Es gibt künftig `CupSizeScreen` zurück, und dort liegt `start`. Tests, die eine Standardgröße verwenden, bekommen eine zweite Methode `start_with_default_cup(strength)`. Kein Test kennt den Weg selbst.

---

## Was dieses Beispiel zeigt

**Navigation gehört zu dem Menü, von dem sie ausgeht.** Es weiß, wohin seine Buttons führen.

**Rückgabe des Ziels macht den Weg lesbar.** Die Kette im Test beschreibt den Ablauf in Begriffen der Maschine.

**Die Prüfung bleibt im Test.** `assert home.message.get() == "Enjoy!"` steht dort, wo die Testaussage steht.
