# Tag 4 – Funktionen: Grundlagen
# Eine Definition legt die Funktion an; ein Aufruf führt ihren Körper aus.

def begruesse(name):
    """Liefert eine Begrüßung als Text."""
    return f"Hallo {name}!"


def quadrat(zahl):
    """Liefert das Quadrat einer Zahl."""
    return zahl * zahl


def zeige_doppeltes(zahl):
    """Gibt den doppelten Wert aus und liefert dabei None."""
    print(zahl * 2)


nachricht = begruesse("Anna")
print(nachricht)
print("Quadrat:", quadrat(5))
print("Mit Rückgabewerten rechnen:", quadrat(3) + quadrat(4))

rueckgabe = zeige_doppeltes(10)
print("Rückgabe der Ausgabefunktion:", rueckgabe)
print("Docstring:", quadrat.__doc__)
