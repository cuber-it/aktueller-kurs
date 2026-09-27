# Beispiel · Die Design Challenge – in klein

Dieselben vier Phasen an einem kleineren Gegenstand, vollständig durchgeführt.

---

## Der Gegenstand

Ein Paketdienst prüft automatisiert, ob Sendungen als zugestellt gemeldet werden.

```python
API_URL = "https://tracking.example/api"


class HttpToolbox:
    def get_json(self, path):
        print(f"GET {API_URL}{path}")
        # Platzhalter: Antwort des Sendungsdienstes
        return {"status": "zugestellt"}


class DeliveryCheck(HttpToolbox):
    def __init__(self):
        self.checked = []

    def check_delivered(self, parcel_id):
        data = self.get_json(f"/parcels/{parcel_id}")
        delivered = data["status"] == "zugestellt"
        self.checked.append(parcel_id)
        print(f"{parcel_id}: {'OK' if delivered else 'OFFEN'}")
        return delivered
```

Der Code funktioniert. `DeliveryCheck().check_delivered("P-1001")` gibt `P-1001: OK` aus und liefert `True`.

---

## Phase 1 · Markieren, ohne zu ändern

| Stelle | Kategorie | Beobachtung |
|---|---|---|
| `class DeliveryCheck(HttpToolbox)` | Vererbung | Eine Prüfung ist keine Art von HTTP-Werkzeugkiste. Sie benutzt sie. |
| `API_URL` auf Modulebene | Abhängigkeit | Die Adresse ist nicht am Konstruktor sichtbar und nicht austauschbar. |
| `get_json` über `self` | Abhängigkeit | Der Netzzugriff kommt über die Basisklasse. Ein Test ohne Netz ist nur durch Überschreiben möglich. |
| `data["status"] == "zugestellt"` | technische Kopplung | Das Antwortformat des Dienstes steht in der Prüflogik. |
| `self.checked.append(...)` | Zustand | Die Liste wird gefüllt, aber nirgends gelesen. |
| `print(...)` in `check_delivered` | Verantwortung | Prüfen und Ausgeben sind in einer Methode. |

---

## Phase 2 · Change Requests

| Change Request | Betroffene Stellen |
|---|---|
| **a** – Ein Partnerdienst meldet `delivered` statt `zugestellt` und hat eine andere Adresse. | `API_URL`, Vergleich in `check_delivered` |
| **b** – Die Prüfung soll ohne Netz testbar sein. | `HttpToolbox`, Vererbung, `check_delivered` |
| **c** – Die Ausgabe soll als CSV erfolgen. | `print` in `check_delivered` |

**Hotspot:** `check_delivered` ist bei allen drei Change Requests betroffen. Dort treffen Netzzugriff, Formatwissen und Ausgabe zusammen.

---

## Phase 3 · Zwei Zielentwürfe

### Entwurf A · Kollaborateur übergeben, Prüfung als Funktion

```python
class TrackingClient:
    """Liest den Rohstatus einer Sendung beim Sendungsdienst."""

    def __init__(self, base_url):
        self._base_url = base_url

    def status(self, parcel_id):
        print(f"GET {self._base_url}/parcels/{parcel_id}")
        return "zugestellt"  # Platzhalter: Antwort des Dienstes


DELIVERED_STATES = {"zugestellt", "delivered"}


def is_delivered(client, parcel_id):
    """Wahr, wenn der Sendungsdienst die Zustellung meldet."""
    return client.status(parcel_id) in DELIVERED_STATES


delivered = is_delivered(TrackingClient("https://tracking.example/api"), "P-1001")
print(f"P-1001: {'OK' if delivered else 'OFFEN'}")
```

Ein Test ohne Netz:

```python
class FixedStatus:
    def __init__(self, status):
        self._status = status

    def status(self, parcel_id):
        return self._status


assert is_delivered(FixedStatus("delivered"), "P-1001")
assert not is_delivered(FixedStatus("in Zustellung"), "P-1001")
```

| Neu | Löst | Was wäre ohne schlechter |
|---|---|---|
| `TrackingClient` mit `base_url` | a, b | Adresse bliebe global, Netzzugriff nur über Vererbung ersetzbar |
| `DELIVERED_STATES` | a | jeder neue Dienst bräuchte eine weitere Bedingung im Vergleich |
| `is_delivered` als Funktion | b, c | Prüfen und Ausgeben blieben gekoppelt |

**Entfernt:** die Liste `checked`. Sie wurde nie gelesen.

### Entwurf B · Ein Vertrag, eine Klasse je Dienst

```python
from typing import Protocol


class StatusSource(Protocol):
    def is_delivered(self, parcel_id: str) -> bool: ...


class HomeCarrier:
    """Eigener Sendungsdienst, meldet 'zugestellt'."""

    def __init__(self, base_url: str) -> None:
        self._base_url = base_url

    def is_delivered(self, parcel_id: str) -> bool:
        print(f"GET {self._base_url}/parcels/{parcel_id}")
        status = "zugestellt"  # Platzhalter: Antwort des Dienstes
        return status == "zugestellt"


class PartnerCarrier:
    """Partnerdienst mit eigenem Format, meldet 'delivered'."""

    def __init__(self, base_url: str) -> None:
        self._base_url = base_url

    def is_delivered(self, parcel_id: str) -> bool:
        print(f"GET {self._base_url}/shipments/{parcel_id}")
        status = "delivered"  # Platzhalter: Antwort des Dienstes
        return status == "delivered"


def print_status(source: StatusSource, parcel_id: str) -> None:
    delivered = source.is_delivered(parcel_id)
    print(f"{parcel_id}: {'OK' if delivered else 'OFFEN'}")
```

Hier kennt jeder Dienst sein eigenes Format. Die Übersetzung in „zugestellt ja oder nein" geschieht in der Dienstklasse.

---

## Phase 4 · Vergleich

| Frage | Entwurf A | Entwurf B |
|---|---|---|
| Welche Änderung wird leichter? | ein weiterer Statuswert | ein Dienst mit ganz anderem Format oder Pfad |
| Welche Kopplung sinkt? | Prüfung hängt nicht mehr an HTTP | Prüfung hängt an keinem Antwortformat |
| Welche neue Komplexität entsteht? | eine Klasse, eine Konstante, eine Funktion | ein Protocol und eine Klasse je Dienst |
| Wie testbar? | mit einem kleinen Objekt, das `status` liefert | mit einem Objekt, das `is_delivered` liefert; die Formatlogik je Dienst braucht eigene Tests |
| Welche Annahme? | alle Dienste liefern einen Status unter demselben Pfad | Dienste unterscheiden sich über den Statuswert hinaus |
| Welche Teamregel steckt dahinter? | Abhängigkeiten sichtbar übergeben | Formatwissen gehört an die Grenze zum Fremdsystem |

**Beide Entwürfe tragen die drei Change Requests.** Welcher besser ist, hängt an einer Frage, die der Code nicht beantwortet: Unterscheidet sich der Partnerdienst nur im Statuswert, oder auch in Pfad und Antwortstruktur? Im ersten Fall genügt A. Im zweiten braucht A bald eine Verzweigung nach Dienst, und B wird einfacher.

---

## Was dieses Beispiel zeigt

**Die Markierungen kommen vor dem Umbau.** Die Liste `checked` fiel in Phase 1 auf und wurde entfernt, weil niemand sie las.

**Der Hotspot bestimmt den Umbau.** Alle drei Change Requests trafen `check_delivered`. Beide Entwürfe zerlegen genau diese Methode und lassen den Rest einfach.

**Zwei Entwürfe, zwei Annahmen.** Der Vergleich macht sichtbar, welche Annahme über die Zukunft in jedem Entwurf steckt. Das ist die Frage, die an den Fachbereich geht.

**Die Vererbung verschwindet in beiden Entwürfen.** `DeliveryCheck` war nie eine Art `HttpToolbox`.
