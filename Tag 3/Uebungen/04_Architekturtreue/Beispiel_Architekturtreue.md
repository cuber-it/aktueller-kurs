# Beispiel · Wo landet jeder Schritt? – in klein

Dieselbe Aufgabe an einem kleineren Gegenstand, vollständig durchgeführt.

---

## Der Gegenstand

Tests für ein Bibliotheksterminal. Szenario:

```gherkin
Scenario: Buch verlängern
  Given ein Leser hat das Buch "Moby Dick" ausgeliehen, Rückgabe morgen
  When er die Ausleihe um 14 Tage verlängert
  Then ist die Rückgabe in 15 Tagen fällig
```

Vorhanden im Framework: `screens.account.open()`, `screens.account.loan(title)`, `loan.due_date()`, `fixtures.create_loan(reader, title, due)`. Nicht vorhanden: ein Button „Verlängern“ im Screen Object der Ausleihe.

---

## Schritt 1 · Abbilden

| Zeile | Aufruf |
|---|---|
| Given | `fixtures.create_loan(reader, "Moby Dick", due=tomorrow)` |
| When | fehlt: `loan.extend_btn` |
| Then | `loan.due_date()` gegen `today + 15` |

---

## Schritt 2 · Die Lücke

Nicht raten. Den Button in der laufenden Anwendung ansehen (Spy), Real Name übernehmen, im Screen Object ergänzen, im Review bestätigen lassen. Bis dahin:

```python
@When("he extends the loan by |integer| days")
def step(context, days):
    # TODO: [helper-missing] extend button on the loan screen - spy run pending
    context.userData["loan"].extend(days)
```

---

## Schritt 3 · Dünne Schritte

```python
@Given("a reader has borrowed |any|, due tomorrow")
def step(context, title):
    context.userData["loan"] = fixtures.create_loan(READER, title, due=tomorrow())


@Then("the loan is due in |integer| days")
def step(context, days):
    test.compare(context.userData["loan"].due_date(), today() + timedelta(days=days))
```

---

## Was dieses Beispiel zeigt

**Die Lücke wird sichtbar, nicht überbrückt.** Ein TODO ist ein Befund für das Framework.

**Step-Funktionen rufen nur auf.** Wie verlängert wird, steht im Screen Object.

**Das Given nutzt einen kürzeren Weg.** Ob das zulässig ist, entscheidet, ob der Weg Teil der Aussage ist.
