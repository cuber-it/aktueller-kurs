# Tag 3 – Tupel
# Ein Tupel hält zusammengehörige Werte in einer festen Reihenfolge.

punkt = (3, 4)
x, y = punkt
print("Koordinaten:", x, y)
print("Erster Wert:", punkt[0])

ein_wert = (42,)
nur_klammern = (42)
print("Mit Komma:", type(ein_wert))
print("Ohne Komma:", type(nur_klammern))

a, b = 1, 2
a, b = b, a
print("Vertauscht:", a, b)

# Tupel-Einträge können nicht neu zugewiesen werden.
try:
    punkt[0] = 9
except TypeError:
    print("Ein Tupel-Eintrag lässt sich nicht ersetzen.")

# Ein enthaltenes veränderbares Objekt bleibt veränderbar.
profil = ("Anna", ["Python"])
profil[1].append("SQL")
print("Tupel mit veränderbarer Liste:", profil)
