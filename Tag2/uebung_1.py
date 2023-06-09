minnumber = 1
maxnumber = 49

eingabe = "1,2,3,4,5,6"
rohdaten = eingabe.split(",")

tipp = []

for ziffer in rohdaten:
    ziffer = int(ziffer)

    if ziffer < minnumber or ziffer > maxnumber:
        print("Fehler in der Eingabe: Zahlen ausserhalb der gueltigen Lottozahlen")
        exit(2)

    if ziffer in tipp:
        print("Fehler in der Eingabe: Ziffer doppelt vorhanden.")
        exit(3)

    tipp.append(ziffer)

print(tipp)
