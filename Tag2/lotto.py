import random

eingabe = input("6 Zahlen 1-49, durch Leerzeichen getrennt: ")
rohdaten = eingabe.split(" ")

if len(rohdaten) != 6:
    print("Anzahl stimmt nicht:", eingabe)
    exit(1)

zahlen = []

for x in rohdaten:
    try:
        zahl = int(x)

        if zahl < 1 or zahl > 49:
            print("Ungültiger Wert:", x)
            exit(3)

        if zahl in zahlen:
            print("Doppelter Wert:", x)
            exit(4)

        zahlen.append(zahl)
    except ValueError:
        print("keine gültige Zahl:", x)
        exit(2)

for n in range(0,100):
    ziehung = random.sample(range(1, 50), 6)
    treffer = list(set(zahlen) & set(ziehung))

    # Print the results
    print(f"--- {n} ---")
    print("Your numbers:      ", zahlen)
    print("Drawn numbers:     ", ziehung)
    print("Matches:           ", treffer)
    print("Number of matches: ", len(treffer))

