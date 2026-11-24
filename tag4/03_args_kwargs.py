# Tag 4 – Flexible Argumentlisten
# * sammelt Positionsargumente als Tupel, ** sammelt Keyword-Argumente als Dict.

def summe(*zahlen):
    """Liefert die Summe aller Argumente; ohne Argumente ist das Ergebnis 0."""
    return sum(zahlen)


def beschreibe(**daten):
    """Liefert die übergebenen Felder als lesbaren Text."""
    beschreibungen = [f"{feld}: {wert}" for feld, wert in daten.items()]
    return ", ".join(beschreibungen)


def begruesse(name, gruss="Hallo"):
    """Liefert einen Gruß."""
    return f"{gruss} {name}!"


print("Zwei Argumente:", summe(1, 2))
print("Keine Argumente:", summe())
print(beschreibe(name="Anna", stadt="Hamburg"))

# Beim Aufruf entpacken * und ** bereits vorhandene Sammlungen.
zahlen = [1, 2, 3]
print("Entpackte Liste:", summe(*zahlen))

aufruf = {"name": "Ben", "gruss": "Moin"}
print(begruesse(**aufruf))
