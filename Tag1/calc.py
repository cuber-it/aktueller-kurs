#!/usr/bin/env python3
import sys

while True:
    eingabe = input("Zahl 1 oder exit: ")
    if eingabe.lower() == "exit":
        break

    try:
        zahl1 = int(eingabe)
    except ValueError:
        print("Falsche Eingabe:", zahl1)
        break

    eingabe = input("Zahl 2: ")

    try:
        zahl2 = int(eingabe)
    except ValueError:
        print("Falsche Eingabe:", zahl2)
        break

    eingabe = input("Operation  (+ - * /): ")

    ergebnis = None

    if eingabe == '+':
        ergebnis = zahl1 + zahl2
    elif eingabe == '-':
        ergebnis = zahl1 - zahl2
    elif eingabe == '*':
        ergebnis = zahl1 * zahl2
    elif eingabe == '/':
        try:
            ergebnis = zahl1 / zahl2
        except ZeroDivisionError:
            print("Division druch Null!")
            break
    else:
        print("Ungültige Operation:", eingabe)
    print("Ergebnis: ", ergebnis)
sys.exit(0)
