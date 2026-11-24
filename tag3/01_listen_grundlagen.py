# Tag 3 – Listen: Grundlagen
# Eine Liste speichert Elemente in einer Reihenfolge und ist veränderbar.

obst = ["Apfel", "Birne", "Kirsche", "Zwetschge"]

# Indizes beginnen bei 0. Bei Slices gehört die obere Grenze nicht dazu.
print("Anzahl:", len(obst))
print("Erstes Element:", obst[0])
print("Letztes Element:", obst[-1])
print("Mittlere Elemente:", obst[1:3])

obst[1] = "Orange"
print("Nach dem Ersetzen:", obst)
print("Birne enthalten:", "Birne" in obst)

# Eine Zuweisung bindet einen weiteren Namen an dieselbe Liste.
zweiter_name = obst
zweiter_name.append("Banane")
print("Nach Änderung über den zweiten Namen:", obst)

# copy() erzeugt eine neue äußere Liste.
kopie = obst.copy()
kopie.append("Mango")
print("Original:", obst)
print("Kopie:", kopie)
