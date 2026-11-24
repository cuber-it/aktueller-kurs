"""Referenzlösung: Ein eigenes Modul aus einem Paket nutzen."""

from . import werkzeug


def main():
    """Gibt je Wort die Ergebnisse der beiden importierten Funktionen aus."""
    for wort in ["Anna", "Otto", "Python", "Reliefpfeiler"]:
        print(f"{wort}: Palindrom={werkzeug.ist_palindrom(wort)}, "
              f"Vokale={werkzeug.vokale_zaehlen(wort)}")


if __name__ == "__main__":
    main()
