#!/usr/bin/python3
from shutil import copy

AF = str(input("Geben sie bitte den Pfad zu der Ausgangsdatei an: "))
ZD = str(input("Geben sie bitte den Pfad zu dem Ziel an: "))

with open(AF) as fd:
    text = fd.read()

with open(ZD, "w") as fd:
    fd.write(text)

copy (AF, ZD)