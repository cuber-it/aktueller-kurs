import re

eingabe = input("Ihre Zahlen: ")
werte = eingabe.split()

if len(werte) != 6:
    print("Fehler 0")
    exit()

lotto_tip = []
for wert in werte:
    if not wert.isnumeric():
        print("Fehler 1")
        exit()
    zahl = int(wert)
    if zahl < 1 or zahl > 49:
        print("Fehler 2")
        exit()
    lotto_tip.append(zahl)

for i, zahl in enumerate(lotto_tip):
    for j, zahl2 in enumerate(lotto_tip):
        if i != j and zahl == zahl2:
            print("Doublette")
            exit()
