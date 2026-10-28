zahl1 = input("Zahl: ")
zahl2 = input("Zahl: ")

try:
    zahl1 = int(zahl1)
    zahl2 = int(zahl2)

    if not(1 <= zahl1 <= 10 and 1 <= zahl2 <= 10):
        raise ValueError("Ungültiger Wertebereich")

    ergebnis = zahl1 / zahl2
    print(ergebnis)
except ValueError as e:
    print("Fehler: ", e)
