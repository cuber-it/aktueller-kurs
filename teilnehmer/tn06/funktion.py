import os

path = "/home/coder/aktueller-kurs/tag_2"
file = "adressen.csv"

def read_file(fname):
    with open(fname) as fd:
        adressen = []
        for line in fd.readlines():
            name, ort, plz, strasse = line.strip("\n").split(";")
            adressen.append({"name": name, "plz": plz, "ort": ort, "strasse": strasse})
            return adressen

def print_adresse(sdata):
    for adresse in sdata:
        for k, v in adresse.items():
            print("{} -> {}".format(k, v))
            print("-"*10)  

def search_in(adressen):
    while True:
        eingabe = input("Name: ").strip()
        if eingabe == "EXIT":
            break
        for adresse in adressen:
            if adresse["name"] == eingabe:
                for k, v in adresse.items():
                    print("{} -> {}".format(k, v))

     



def main():
    gesamt_path = path + "/" + file
    daten = read_file(gesamt_path)
    print_adresse(daten)
    search_in(daten)

main()



