import os
import csv

path = "/home/coder/aktueller-kurs/teilnehmer/tn01"
file = "adressdaten.csv"

with open(os.path.join(path, file)) as fd:
    adressen = []
    for line in fd.readlines():
        name, ort, plz, strasse = line.strip("\n").split(";")
        adressen.append({"name": name, "ort": ort, "plz": plz, "strasse": strasse})

for adresse in adressen:
    for k, v in adresse.items():
        print("{}: {}".format(k, v))
    print("-"*10)
