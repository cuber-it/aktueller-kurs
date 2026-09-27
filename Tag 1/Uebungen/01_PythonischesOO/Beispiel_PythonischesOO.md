# Beispiel · Pythonisch oder übertragen – in klein

Dieselbe Aufgabe an einem kleineren Gegenstand, vollständig durchgeführt.

---

## Der Gegenstand

Eine Bibliothekssoftware, übertragen aus C#. Es geht um **Medien** und ihre Ausleihfrist.

```python
class Medium:
    def __init__(self, title, loan_days):
        self.__title = title
        self.__loan_days = loan_days

    def getTitle(self):
        return self.__title

    def getLoanDays(self):
        return self.__loan_days

    def setLoanDays(self, loan_days):
        self.__loan_days = loan_days

    def toString(self):
        return self.__title + " (" + str(self.__loan_days) + " Tage)"


class IsbnHelper:
    @staticmethod
    def is_valid(isbn):
        digits = isbn.replace("-", "")
        return len(digits) == 13 and digits.isdigit()
```

Neue Anforderung: **Die Ausleihfrist liegt zwischen 7 und 42 Tagen.**

---

## Schritt 1 · Was ist übertragen?

| Konstrukt | Herkunft | Absicht |
|---|---|---|
| `getTitle`, `getLoanDays`, `setLoanDays` | C#-Properties bzw. Java-Getter | Zugriff kontrollieren |
| `self.__title` | `private` | Feld verbergen |
| `toString()` | `ToString()` in C# | lesbare Darstellung |
| `IsbnHelper` mit `@staticmethod` | statische Hilfsklasse | Funktion unterbringen |

**Vier Konstrukte, eine gemeinsame Ursache:** Die Sprache, aus der übertragen wurde, verlangt eine Klasse oder eine Methode, wo Python ohne auskommt.

---

## Schritt 2 · Was tut der doppelte Unterstrich?

```python
medium = Medium("Faust", 28)
print(medium._Medium__loan_days)   # 28
```

Der Name wird umbenannt, aber nicht geschützt. Die Absicht „nicht von außen verwenden" drückt in Python der einfache Unterstrich aus: `_loan_days`.

---

## Schritt 3 · Der Umbau

```python
class Medium:
    """Ein ausleihbares Medium mit seiner Ausleihfrist in Tagen."""

    def __init__(self, title: str, loan_days: int) -> None:
        self.title = title
        self.loan_days = loan_days

    @property
    def loan_days(self) -> int:
        return self._loan_days

    @loan_days.setter
    def loan_days(self, value: int) -> None:
        if not 7 <= value <= 42:
            raise ValueError(f"loan_days must be between 7 and 42, got {value}")
        self._loan_days = value

    def __repr__(self) -> str:
        return f"Medium({self.title!r}, {self.loan_days!r})"

    def __str__(self) -> str:
        return f"{self.title} ({self.loan_days} Tage)"


def is_valid_isbn(isbn: str) -> bool:
    """Prüft das Format einer ISBN-13, nicht die Prüfziffer."""
    digits = isbn.replace("-", "")
    return len(digits) == 13 and digits.isdigit()
```

**Was sich geändert hat:**

- `title` ist ein einfaches Attribut. Es gibt keine Regel dafür, also keine Property.
- `loan_days` ist eine Property, weil es eine Regel gibt. Im Konstruktor wird über die Property zugewiesen, damit die Prüfung auch dort greift.
- `toString()` ist durch `__str__` ersetzt, dazu kommt `__repr__` für Diagnose.
- `IsbnHelper` ist eine Funktion auf Modulebene.

---

## Schritt 4 · Die Aufrufstellen

| Vorher | Nachher |
|---|---|
| `medium.getTitle()` | `medium.title` |
| `medium.setLoanDays(14)` | `medium.loan_days = 14` |
| `print(medium.toString())` | `print(medium)` |
| `IsbnHelper.is_valid(isbn)` | `is_valid_isbn(isbn)` |

Die Aufrufstellen ändern sich **einmal**. Käme später eine Regel für `title` hinzu, etwa „nicht leer", würde `title` zur Property. `medium.title = "..."` bliebe an jeder Aufrufstelle unverändert.

---

## Schritt 5 · Wo bleibt eine Methode?

Angenommen, die Ausleihfrist hängt künftig von einer Verbundregel ab, die aus einem Webdienst geladen wird.

```python
def current_loan_days(self, catalog_service) -> int:
    return catalog_service.loan_days_for(self.title)
```

Das ist bewusst **keine** Property: Der Aufruf braucht einen Parameter, kostet einen Netzwerkzugriff und kann fehlschlagen. Wer `medium.loan_days` liest, rechnet damit nicht.

---

## Was dieses Beispiel zeigt

**Eine Property gehört dort hin, wo eine Regel gilt.** `title` braucht keine, `loan_days` braucht eine.

**Die Aufrufstellen bleiben stabil, wenn eine Regel später dazukommt.** Das war die Absicht hinter den Gettern. In Python erreicht die Property sie ohne Vorleistung.

**Der doppelte Unterstrich löst ein anderes Problem.** Er verhindert Namenskollisionen in Klassenhierarchien, er verbirgt nichts.

**Nicht jede Funktion braucht eine Klasse.** `is_valid_isbn` hat keinen Zustand und kein Gegenüber, das sie besitzen müsste.
