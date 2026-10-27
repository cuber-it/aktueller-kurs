#Username-Generator

#  Aufgabe: Vorname, Nachname und Geburtsjahr einlesen, daraus einen
#  kleingeschriebenen Username der Form vorname.nachname.jahr bauen.
#  Eingabe: Anna / Schmidt / 1995
#  Ausgabe: anna.schmidt.1995

name = input("Name: ")
vorname = input("Vorname: ")
gebjahr = input("Geburtsjahr: ")

username = f"{vorname}.{name}.{gebjahr}"

print("Username: ", username)

username = input("Vorname / Nachname / Geburtsjahr").replace(" ", "").replace("/", ".")

print("Username: ", username)
