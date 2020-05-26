import os

path = "/home/coder/aktueller-kurs/teilnehmer/tn03/Tag 2/"
file = "Adressbuch.csv"
adressen = []
pfad = os.path.join(path, file)
with open(pfad) as fd:
    rohtext = fd.readlines()
lines = []
for line in rohtext:
    name, ort, plz, strasse = line.strip("\n").split(";")
    adressen.append({"name": name,"plz": plz, "ort": ort, "strasse": strasse})
for adresse in adressen
    for k, v in adresse.items():
        print("{} -> {}".format(k, v))
    print("-"*10)
while True:
    eingabe = input("Name: ").strip()
    if eingabe == "EXIT":
        break
    for adresse

