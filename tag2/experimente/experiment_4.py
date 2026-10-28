zahl1 = input("Zahl: ")
zahl2 = input("Zahl: ")

# Prüfung - sind das Ganzzahlen?
if zahl1.isdecimal() and zahl2.isdecimal():
    zahl1 = int(zahl1)
    zahl2 = int(zahl2)

    if zahl2 != 0:
        if 1 <= zahl1 <= 10 and 1 <= zahl2 <= 10:
            ergebnis = zahl1 / zahl2
            print(ergebnis)
        else:
            print("Ungültiger Wertebereich")
    else:
        print("Division durch Null verboten")
else:
    print("Eingabe prüfen: ", zahl1, zahl2)
