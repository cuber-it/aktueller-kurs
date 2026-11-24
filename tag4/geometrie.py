"""Kreisberechnungen für die Beispiele zu eigenen Modulen."""

from math import pi as PI


def kreis_flaeche(radius):
    """Liefert die Fläche für einen nicht negativen Radius."""
    if radius < 0:
        raise ValueError("Der Radius darf nicht negativ sein.")
    return PI * radius ** 2


def kreis_umfang(radius):
    """Liefert den Umfang für einen nicht negativen Radius."""
    if radius < 0:
        raise ValueError("Der Radius darf nicht negativ sein.")
    return 2 * PI * radius


if __name__ == "__main__":
    print(f"Fläche bei Radius 2: {kreis_flaeche(2):.2f}")
    print(f"Umfang bei Radius 2: {kreis_umfang(2):.2f}")
