tippschein = []

while len(tippschein) < 6:
    eingabe = input("Zahl zwischen 1 und 49: ")
    if not eingabe.isdigit():
        print("Keine Zahl:", eingabe)
    else:
        zahl = int(eingabe)

        if zahl in tippschein:
            print("Doppelt:", zahl)
        elif zahl < 1 or zahl > 49:
            print("Wertebereich!:", zahl)
        else:
            tippschein.append(zahl)

print("Fein gemacht:", tippschein)
