# Experiment – Gleichnamige Funktionen aus verschiedenen Modulen
# Start aus dem Repository: python3 -m tag4.experimente.import_2

from . import modul_1, modul_2


def main():
    """Zeigt die Überdeckung eines Namens und den Zugriff über Modulnamen."""
    from .modul_1 import formatiere
    print("Erster gezielter Import:", formatiere("python grundlagen"))

    from .modul_2 import formatiere
    print("Zweiter gezielter Import:", formatiere("python grundlagen"))

    print("Explizit aus Modul 1:", modul_1.formatiere("python grundlagen"))
    print("Explizit aus Modul 2:", modul_2.formatiere("python grundlagen"))


if __name__ == "__main__":
    main()
