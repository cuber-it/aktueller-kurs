# Beispiel · Welche Variante für welches Problem? – in klein

Dieselbe Aufgabe an einem kleineren Gegenstand, vollständig durchgeführt.

---

## Der Gegenstand

GUI-Tests für einen Ausleihautomaten in einer Bibliothek. Szenario: „Ein Buch ausleihen und prüfen, dass es auf dem Konto steht.“

Change Case: **Ausleihe ist künftig auch über eine App möglich, dieselben Tests sollen dort laufen.**

---

## Schritt 1 · Varianten

```python
# direkt
squish.mouseClick(squish.waitForObject({"objectName": "lendBtn"}))
squish.type(squish.waitForObject({"objectName": "barcodeField"}), "978-3-16")
test.compare(squish.waitForObject({"objectName": "accountList"}).count, 1)

# Screen Objects
kiosk.home.lend_btn.click()
kiosk.lend.enter_barcode("978-3-16")
test.compare(kiosk.account.book_count(), 1)

# Screen Objects + Task
lend_book(kiosk, "978-3-16")
test.compare(kiosk.account.book_count(), 1)

# Screenplay
reader = Actor("Leserin", UseKiosk(kiosk))
reader.attempts_to(LendBook("978-3-16"))
reader.should_see(BooksOnAccount(), 1)
```

---

## Schritt 2 · Der Change Case

| Variante | Änderung für die App |
|---|---|
| direkt | jeder Test neu |
| Screen Objects | Screen Objects für die App, jeder Test anders verdrahtet |
| Screen Objects + Task | `lend_book` bekommt eine zweite Implementierung, Tests wählen sie |
| Screenplay | neue Ability `UseApp`, `LendBook` fragt nach der Ability, Tests bekommen einen anderen Actor |

---

## Schritt 3 · Entscheidung

Für einen zweiten Bedienweg mit denselben Tests trägt Screenplay: Die Tasks bleiben, nur die Fähigkeit wechselt. Für einen einzigen Bedienweg genügt Screen Objects + Task.

---

## Was dieses Beispiel zeigt

**Der Change Case entscheidet.** Ohne zweiten Bedienweg bringt Screenplay vier neue Begriffe ohne Nutzen.

**Varianten lassen sich mischen.** Screenplay kann für die Ausleihe eingeführt werden, der Rest bleibt.

**Tasks sind der gemeinsame Kern.** Ob als Funktion oder als Screenplay-Task: Die Handlung ist benannt.
