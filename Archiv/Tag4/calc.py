import sys

while True:
    eingabe = input("Zahl 1 oder exit: ")
    if eingabe == "exit":
        break

    zahl1 = int(eingabe)

    eingabe = input("Zahl 2: ")
    zahl2 = int(eingabe)

    eingabe = input("Operation  (+ - * /): ")

    ergebnis = None

    if eingabe == '+':
        ergebnis = zahl1 + zahl2
    elif eingabe == '-':
        ergebnis = zahl1 - zahl2
    elif eingabe == '*':
        ergebnis = zahl1 * zahl2
    elif eingabe == '/':
        ergebnis = zahl1 / zahl2
    else:
        print("Ungültige Operation:", eingabe)
    print("Ergebnis: ", ergebnis)
sys.exit(0)
