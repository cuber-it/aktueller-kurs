tipp = []

while len(tipp) < 6:
    eingabe = int(input("Zahl: "))

    if eingabe < 1 or eingabe > 49:
        print("Ungültig")
        exit(1)

    if eingabe in tipp:
        print("Doppelt")
        exit(2)

    tipp.append(eingabe)

print(tipp)


