#!/usr/bin/env python3
from random import *

zahl = int(input("Gib eine Zahl ein: "))
zufallszahl = None
versuche = 0

if zahl > 100 or zahl < 0:
    print("Zahl muss zwischen 0 und 100 liegen")
    quit()

while zahl != zufallszahl:
    versuche += 1
    zufallszahl = randint(1, 100)

print("Insgesamt {} Würfe".format(versuche))