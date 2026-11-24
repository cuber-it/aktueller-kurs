"""Referenzlösung: Eine Funktion aus einem eigenen Modul verwenden."""

from .statistik import statistik


def main():
    """Entpackt die Werteliste beim Aufruf und die Kennzahlen bei der Rückgabe."""
    werte = [-1, 0, 1, 2, 3, 4, 5]
    kleinste, groesste, mittelwert = statistik(*werte)
    print(f"Minimum: {kleinste}; Maximum: {groesste}; Mittelwert: {mittelwert:.2f}")


if __name__ == "__main__":
    main()
