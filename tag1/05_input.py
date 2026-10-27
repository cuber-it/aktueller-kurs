# Tag 1 – Eingabe mit input()
#
# input() liest eine Zeile von der Tastatur ein
# und liefert IMMER einen str zurück.

name = input("Wie heißt du? ")
print("Hallo,", name)

# Wenn wir mit der Eingabe rechnen wollen, müssen wir
# den Typ konvertieren:
alter_text = input("Wie alt bist du? ")
alter = int(alter_text)

print("Nächstes Jahr bist du", alter + 1)

# Kürzer in einem Schritt:
groesse = float(input("Wie groß bist du in Metern? "))
print("In Zentimetern:", groesse * 100)
