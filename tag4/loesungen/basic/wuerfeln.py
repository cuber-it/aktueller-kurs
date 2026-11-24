"""Referenzlösung: Zufallswerte in einer Funktion erzeugen und aufsummieren."""

import random


def wuerfeln(anzahl):
    """Liefert die Summe von anzahl Würfen; 0 Würfe ergeben 0."""
    if type(anzahl) is not int or anzahl < 0:
        raise ValueError("Die Anzahl muss eine nicht negative ganze Zahl sein.")
    augensumme = 0
    for _ in range(anzahl):
        augensumme += random.randint(1, 6)
    return augensumme


if __name__ == "__main__":
    print("Summe aus drei Würfen:", wuerfeln(3))
    print("Summe aus null Würfen:", wuerfeln(0))
