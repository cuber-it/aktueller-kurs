#!/bin/python
import sys

#datei = sys.argv[1]
#system = sys.argv[2]

# datei = r"D:\Programmierung\aktueller-kurs\tag-2\syslog.txt"


datei = input("Dateiname eingeben:")
system = input("Systemname eingeben: ")

with open(datei) as fd:
    rohdaten = fd.readlines()

daten = []
for zeile in rohdaten:
    zeile = zeile.strip()
    zeile = zeile.split(None, 4)
    zeile = [ zeile[0] + "/" + zeile[1]] + zeile[2:]
    daten.append(zeile)

infodaten = {}
for zeile in daten:
    if not zeile[2] in infodaten:
        infodaten[zeile[2]] = []
    infodaten[zeile[2]].append(zeile)

#print(infodaten.keys())

print("{}: {}".format(system, len(infodaten[system])))
for eintrag in infodaten[system]:
    print(eintrag)
