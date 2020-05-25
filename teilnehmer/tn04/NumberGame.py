#!/usr/bin/python3
import random

i = 0
Zahl = random.randint(0,100)

Eing = int(input("Geben sie eine Zahl ein:    "))

while Eing != Zahl:
    if Zahl < Eing:
        print("Die gesuchte Zahl ist kleiner.")
        i = i + 1
        Eing = int(input("Geben sie eine Zahl ein"))
    else:
        print("Die gesuchte Zahl ist größer.")
        i = i + 1
        Eing = int(input("Geben sie eine Zahl ein"))

if Eing == Zahl:
    i = i + 1
    print("Bingo! Die gesuchte Zahl war " + str(Zahl) + " und sie haben " + str(i) + " Versuche gebraucht, um die Zahl zu erraten")







