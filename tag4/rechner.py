"""Kleine Rechenfunktionen als Gegenstand der Unittests."""


def addiere(a, b):
    """Liefert die Summe zweier Zahlen."""
    return a + b


def teile(a, b):
    """Liefert den Quotienten; bei Nenner 0 entsteht ZeroDivisionError."""
    return a / b


def ist_gerade(zahl):
    """Liefert True, wenn die ganze Zahl ohne Rest durch 2 teilbar ist."""
    return zahl % 2 == 0
