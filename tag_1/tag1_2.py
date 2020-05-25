#!/usr/bin/python
wert = float(input("Eingabe: "))

if wert >= 100.00:
    print("Ist grösser")
    if wert > 1000.00:
        print("und zwar ziemlich")
        if wert > 10000.00:
            print("Echt viel!")
else:
    print("Ist kleiner")