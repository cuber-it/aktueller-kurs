import os

def read_file(fpath, ffile):
    with open(os.path.join(fpath, ffile)) as fd:
        adressen = []
        for line in fd.readlines():
            name, ort, plz, strasse = line.strip("\n").split(";")
            adressen.append({"name": name, "plz": plz, "ort": ort, "strasse": strasse})
    return adressen

def ausgabe_wertpaare(adressen):
    for adresse in adressen:
        for k, v in adresse.items():
            print("{} -> {}".format(k, v))
        print("-"*10)   


path = "/home/coder/aktueller-kurs/tag_2"
file = "adressen.csv"

daten = read_file(path, file)
ausgabe_wertpaare(daten)


while True:
    eingabe = input("Name: ").strip()
    if eingabe == "EXIT":
        break
    for adresse in adressen:
        if adresse["name"] == eingabe:
            for k, v in adresse.items():
                print("{} -> {}".format(k, v))
                