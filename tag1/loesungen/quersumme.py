# Quersumme einer dreistelligen Zahl

#  Aufgabe: Eine dreistellige Zahl einlesen, jede Ziffer einzeln und die Quersumme
#  ausgeben — ohne über den String zu iterieren.
#  Eingabe: 538
#  Ausgabe: 5 + 3 + 8 = 16

zahl = input("Zahl (3-stellig): ")
if len(zahl) != 3:
    print("Kann nicht berechnet werden für:", zahl)
    exit()

zahl = int(zahl)
hunderter = zahl // 100
zehner = zahl % 100 // 10
einer = zahl % 10

print("Quersumme: ", hunderter + zehner + einer)
