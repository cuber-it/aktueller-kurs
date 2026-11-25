tippschein = []

while len(tippschein) < 6:
    eingabe = input("Zahl zwischen 1 und 49: ")
    try:
        zahl = int(eingabe)

        if zahl in tippschein:
            print("Doppelt:", zahl)
        elif zahl < 1 or zahl > 49:
            print("Wertebereich!:", zahl)
        else:
            tippschein.append(zahl)
    except ValueError:
        print("Keine Zahl:", eingabe)

print("Fein gemacht:", tippschein)
