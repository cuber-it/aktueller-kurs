# Tag 3 – Sets
# Eine Menge enthält eindeutige, hashbare Elemente und hat keine Indexordnung.

obst = {"Apfel", "Birne", "Apfel"}
print("Eindeutige Werte:", sorted(obst))
print("Anzahl:", len(obst))

obst.add("Kirsche")
obst.discard("Mango")           # Ein fehlender Wert ist hier kein Fehler.
print("Nach dem Ergänzen:", sorted(obst))

python_kurs = {"Anna", "Ben", "Cem"}
sql_kurs = {"Ben", "Dora"}
print("Mindestens ein Kurs:", sorted(python_kurs | sql_kurs))
print("Beide Kurse:", sorted(python_kurs & sql_kurs))
print("Nur Python:", sorted(python_kurs - sql_kurs))
print("Genau einer der beiden Kurse:", sorted(python_kurs ^ sql_kurs))

# sorted() liefert für die Ausgabe eine geordnete Liste.
print("Teilmenge:", {"Anna", "Ben"} <= python_kurs)
print("Leeres Set:", type(set()))
print("Leeres Dictionary:", type({}))

feste_menge = frozenset(python_kurs)
print("Unveränderliche Menge:", sorted(feste_menge))
