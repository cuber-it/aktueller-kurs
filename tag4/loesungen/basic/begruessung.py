"""Referenzlösung: Eine Funktion mit einem Default-Parameter aufrufen."""


def begruesse(name, gruss="Hallo"):
    """Liefert einen Gruß als Text."""
    return f"{gruss} {name}!"


if __name__ == "__main__":
    print(begruesse("Anna"))
    print(begruesse("Ben", "Moin"))
    print(begruesse("Cem", gruss="Servus"))
