import os

path = "/home/coder/aktueller-kurs/tag_2"
file = "adressen.csv"


def lade_adressdaten(filename)
    with open(filename) as fd:
        adressen = []
        for line in fd.readlines():
            name, ort, plz, strasse = line.strip("\n").split(";")
            adressen.append({"name": name, "plz": plz, "ort": ort, "strasse": strasse})
    return adressen


def show_adress(adressen)
    for adresse in adressen:
        for k, v in adresse.items():
            print("{} -> {}".format(k, v))
        print("-"*10)
   
def suchen(adressen)
    while True:
        eingabe = input("Name: ").strip()
        if eingabe == "EXIT":
            break

        for adresse in adressen:
            if adresse["name"] == eingabe:
                for k, v in adresse.items():
                    print("{} -> {}".format(k, v))
                
adressen = lade_adressdaten(path)
show_adress(adressen)
suchen(adressen)     
