import os

path = "/home/coder/aktueller-kurs/teilnehmer/tn06"
file = "adressbook.csv"

#Einlesen
with open(os.path.join(path, file)) as fd:
    adressen = []
    for line in  fd.readlines():
        name, ort, plz, strasse = line.strip("\n").split(";")
        adressen.append({"name": name, "plz": plz, "ort": ort, "strasse": strasse})

for adresse in adressen:
    for k, v in adresse.items():
        print("{} -> {}".format(k,v))
    print("-"*10)



