import os

path = "/home/coder/aktueller-kurs/tag_2"
file = "adressen.csv"

def load_data(filename):
    with open(filename) as fd:
        adressen = []
        for line in fd.readlines():
            name, ort, plz, strasse = line.strip("\n").split(";")
            adressen.append({"name": name, "plz": plz, "ort": ort, "strasse": strasse})
    return adressen

def print_adressen(adressen):
    for adresse in adressen:
        for k, v in adresse.items():
            print("{} -> {}".format(k, v))
        print("-"*10)   

def search_in(adressen):
    while True:
        eingabe = input("Name: ").strip()
        if eingabe == "EXIT":
            break
        if eingabe == "SHOWALL":
            print_adressen(adressen)
        for adresse in adressen:
            if adresse["name"] == eingabe:
                for k, v in adresse.items():
                    print("{} -> {}".format(k, v))
                

adressen = load_data(os.path.join(path, file))
print_adressen(adressen)
search_in(adressen)