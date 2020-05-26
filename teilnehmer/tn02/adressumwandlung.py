import os

path = "/home/coder/aktueller-kurs/teilnehmer/tn02"
file = "adressen.csv"

with open(os.path.join(path, file)) as fd:
    adressen = []
    for line in fd.readlines():
        name, ort, plz, strasse = line.strip("\n").split(";")
        adressen.append({"name": name, "plz": plz, "ort": ort, "strasse": strasse})

for adresse in adressen:
    for k,v in adresse.items():
        print("{} -> {}".format(k, v))
    print("-"*10)

while True:
    eingabe = input("Name: ").strip()
    if eingabe == "EXIT":
        break
    for adresse in adressen:
        if adresse["name"] == eingabe:
            for k,v in adresse.items():
                print("{} -> {}".format(k, v))
                