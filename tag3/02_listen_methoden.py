# Tag 3 – Listen: Methoden
# Hinzufügen, Entfernen und Sortieren verändern die vorhandene Liste.

obst = ["Birne", "Apfel"]
obst.append("Kirsche")
obst.extend(["Orange", "Banane"])
obst.insert(0, "Mango")
print("Nach dem Hinzufügen:", obst)

obst.remove("Mango")             # Entfernt den ersten passenden Wert.
entnommen = obst.pop()          # Entfernt das letzte Element und liefert es.
print("Entnommen:", entnommen)
print("Verbleibend:", obst)

# sort() verändert die Liste und liefert None.
rueckgabe = obst.sort()
print("Alphabetisch:", obst)
print("Rückgabe von sort():", rueckgabe)

obst.reverse()
print("Umgekehrt:", obst)

# append() fügt genau ein Element an; dieses kann selbst eine Liste sein.
verschachtelt = ["Apfel"]
verschachtelt.append(["Birne", "Kirsche"])
print("Liste als einzelnes Element:", verschachtelt)
