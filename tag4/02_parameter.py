# Tag 4 – Parameter und Argumente
# Parameter stehen in der Definition; Argumente werden beim Aufruf übergeben.

def begruesse(name, gruss="Hallo"):
    """Liefert einen Gruß mit optionaler Anrede."""
    return f"{gruss} {name}!"


print(begruesse("Anna"))
print(begruesse("Ben", "Moin"))
print(begruesse(gruss="Servus", name="Cem"))

# Default-Werte werden beim Definieren festgelegt, nicht bei jedem Aufruf.
# None ermöglicht eine frische Liste, wenn keine Liste übergeben wurde.
def sammle(element, liste=None):
    """Ergänzt eine übergebene Liste oder legt für den Aufruf eine neue an."""
    if liste is None:
        liste = []
    liste.append(element)
    return liste


print("Erster Aufruf ohne Liste:", sammle("Apfel"))
print("Zweiter Aufruf ohne Liste:", sammle("Birne"))

obst = ["Kirsche"]
sammle("Orange", obst)
print("Übergebene Liste wurde ergänzt:", obst)
