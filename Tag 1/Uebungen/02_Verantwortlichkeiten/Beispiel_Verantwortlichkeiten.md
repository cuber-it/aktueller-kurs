# Beispiel · Wer ist hier wofür zuständig – in klein

Dieselbe Aufgabe an einem kleineren Gegenstand, vollständig durchgeführt.

---

## Der Gegenstand

Eine Software für ein kleines Hotel. Es geht um **Buchungen**.

```python
class BookingManager:
    def load_rates(self):
        return {"single": 89, "double": 129}

    def is_room_free(self, room, check_in, check_out):
        print(f"query calendar for {room}")
        return True

    def price_for(self, booking):
        nights = (booking.check_out - booking.check_in).days
        return nights * self.load_rates()[booking.room_type]

    def send_confirmation(self, booking):
        print(f"mail to {booking.guest_email}")


class Booking:
    def __init__(self, room_type, check_in, check_out, guest_email):
        self.room_type = room_type
        self.check_in = check_in
        self.check_out = check_out
        self.guest_email = guest_email
        self.cancelled = False
        self.refund = 0
```

Angekündigte Änderungen:

| Nr. | Änderung |
|---|---|
| E1 | Preise kommen künftig aus dem Channel-Manager statt aus einer festen Tabelle |
| E2 | Bestätigungen werden zusätzlich per SMS verschickt |
| E3 | Der Belegungskalender wird auf ein neues System umgestellt |

---

## Schritt 1 · Änderungsgründe

| Methode | E1 | E2 | E3 |
|---|---|---|---|
| `load_rates` | ja | | |
| `is_room_free` | | | ja |
| `price_for` | ja | | |
| `send_confirmation` | | ja | |

**Drei unabhängige Änderungsgründe.** Jede Änderung betrifft einen anderen Teil der Klasse, und keine betrifft den Rest.

Der Versuch eines Satzes: „`BookingManager` lädt Preise und prüft die Belegung und verschickt Bestätigungen." Die Aufzählung ist das Signal.

---

## Schritt 2 · Gruppieren

| Gruppe | Methoden | ändert sich bei |
|---|---|---|
| Preise | `load_rates`, `price_for` | E1 |
| Belegung | `is_room_free` | E3 |
| Benachrichtigung | `send_confirmation` | E2 |

Daraus werden drei Verantwortungen mit je einem Satz:

- **Preisliste:** kennt den Preis je Zimmertyp und Nacht.
- **Belegungskalender:** weiß, welches Zimmer wann frei ist.
- **Benachrichtigung:** informiert den Gast über seine Buchung.

---

## Schritt 3 · Die Invariante der Buchung

In `Booking` sind diese Zustände möglich:

```python
booking.check_out = booking.check_in      # null Nächte
booking.refund = 50                       # Erstattung ohne Stornierung
booking.cancelled = True                  # Stornierung ohne Erstattungsregel
```

Die Regeln, die gelten sollten:

- Die Abreise liegt nach der Anreise.
- Eine Erstattung gibt es nur für eine stornierte Buchung.
- Eine stornierte Buchung kann nicht erneut storniert werden.

```python
from datetime import date


class Booking:
    """Eine Zimmerbuchung für mindestens eine Nacht."""

    def __init__(
        self, room_type: str, check_in: date, check_out: date, guest_email: str
    ) -> None:
        if check_out <= check_in:
            raise ValueError("check_out must be after check_in")
        self.room_type = room_type
        self.guest_email = guest_email
        self._check_in = check_in
        self._check_out = check_out
        self._refund: int | None = None

    @property
    def nights(self) -> int:
        return (self._check_out - self._check_in).days

    @property
    def is_cancelled(self) -> bool:
        return self._refund is not None

    def cancel(self, refund: int) -> None:
        if self.is_cancelled:
            raise ValueError("booking is already cancelled")
        self._refund = refund
```

**Was sich geändert hat:** Stornierung und Erstattung sind ein einziger Vorgang. `is_cancelled` wird aus der Erstattung abgeleitet und kann ihr deshalb nicht widersprechen. Die Datumsregel prüft der Konstruktor.

---

## Schritt 4 · Feature Envy

`price_for` rechnet mit `check_in` und `check_out` der Buchung. Die Zahl der Nächte ist Wissen der Buchung und steht jetzt als `nights` dort.

Der Preis selbst bleibt in der Preisliste, denn er hängt von den Raten ab, die die Buchung nicht kennt:

```python
class RateTable:
    """Preis je Zimmertyp und Nacht."""

    def __init__(self, rates: dict[str, int]) -> None:
        self._rates = rates

    def price_for(self, booking: Booking) -> int:
        return booking.nights * self._rates[booking.room_type]
```

---

## Schritt 5 · Tell, don't ask

Vorher an der Rezeption:

```python
if not booking.cancelled:
    booking.cancelled = True
    booking.refund = 50
```

Nachher:

```python
booking.cancel(refund=50)
```

Die Prüfung, ob schon storniert wurde, gehört der Buchung. Die Rezeption sagt, was geschehen soll.

---

## Was dieses Beispiel zeigt

**Die Änderungsfrage schneidet Klassen besser als die Substantivfrage.** „Buchung" ist ein Substantiv, „Manager" auch. Erst die Frage nach den Änderungen zeigt, dass im Manager drei Verantwortungen stecken.

**Eine Invariante braucht einen Vorgang, nicht einen Unterstrich.** Stornierung und Erstattung sind ein Vorgang, also gibt es eine Methode dafür.

**Abgeleitete Werte speichert man nicht doppelt.** `is_cancelled` wird aus der Erstattung abgeleitet und kann ihr nicht widersprechen.

**Nicht jede Berechnung wandert zu den Daten.** Die Nächte gehören zur Buchung, der Preis zur Preisliste, weil er Wissen braucht, das die Buchung nicht hat.
