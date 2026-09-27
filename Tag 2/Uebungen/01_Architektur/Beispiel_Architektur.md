# Beispiel · Wo landet diese Änderung? – in klein

Dieselbe Aufgabe an einem kleineren Gegenstand, vollständig durchgeführt.

---

## Der Gegenstand

GUI-Tests für einen Fahrkartenautomaten im Nahverkehr. Ein Ausschnitt:

```python
# tests/test_single_ticket.py
def test_buy_single_ticket():
    with machine_session():
        choose_ticket("Einzelfahrt", zone="AB")
        pay_with_card()
        assert_receipt_contains("Einzelfahrt AB")


# flows/tickets.py
def choose_ticket(name, zone):
    screens.start.tickets_btn.click()
    screens.tickets.entry(name).click()
    screens.zones.entry(zone).click()


# screens/tickets.py
class TicketScreen:
    def entry(self, name):
        return Button({"type": "TicketTile", "text": name, "visible": True})


# controls.py
class Button:
    def click(self):
        squish.mouseClick(squish.waitForObject(self.name))
```

Drei Änderungen:

| Nr. | Änderung |
|---|---|
| E1 | Die Kacheln heißen künftig `TicketCard` statt `TicketTile`. |
| E2 | Die Zonenwahl kommt vor die Fahrkartenwahl. |
| E3 | Bezahlung mit Karte braucht künftig eine PIN-Eingabe. |

---

## Schritt 1 · Schichten zuordnen

| Schicht | Datei | Verantwortung |
|---|---|---|
| Testfall | `tests/test_single_ticket.py` | was geprüft wird |
| Ablauf | `flows/tickets.py` | welcher Weg zu einer Fahrkarte führt |
| Screen | `screens/tickets.py` | wie Elemente eines Bildschirms gefunden werden |
| Control | `controls.py` | wie mit Squish gewartet und geklickt wird |

---

## Schritt 2 · Änderungen verfolgen

| Änderung | betroffen | Schichten |
|---|---|---|
| E1 | `TicketScreen.entry` | eine |
| E2 | `choose_ticket` | eine |
| E3 | `pay_with_card` (Ablauf), neuer Screen für die PIN | zwei, beide unterhalb des Testfalls |

Kein Testfall ändert sich. Das ist die Aussage der Landkarte: Jede der drei Änderungen hat einen erkennbaren Ort.

---

## Schritt 3 · Kopplung einordnen

| Kopplung | Einordnung |
|---|---|
| Testfall → `choose_ticket` | notwendig, fachlich |
| `choose_ticket` → Screens | notwendig, der Ablauf muss Bildschirme kennen |
| Screen → Real Name | notwendig, an einer Stelle |
| Control → Squish | notwendig, an einer Stelle |

---

## Was dieses Beispiel zeigt

**Eine Landkarte beschreibt Verantwortung, nicht Verzeichnisse.** Dieselbe Datei kann zwei Schichten enthalten, dieselbe Schicht mehrere Dateien.

**Änderungen sind der Prüfstein.** Eine Schicht ist gut beschrieben, wenn sich für jede typische Änderung sagen lässt, ob sie dort landet.

**Beschreiben geht vor Bewerten.** Ob E3 besser in einem eigenen Ablauf „mit PIN bezahlen“ stünde, ist eine zweite Frage.
