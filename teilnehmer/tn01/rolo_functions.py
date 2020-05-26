import os

def prepare_data(file):
    with open(os.path.join(file)) as fd:
        adressen = []
        for line in fd.readlines():
            name, ort, plz, strasse = line.strip("\n").split(";")
            adressen.append({"name": name, "plz": plz, "ort": ort, "strasse": strasse})
    return adressen

def print_out(adressen):
    for adresse in adressen:
        for k, v in adresse.items():
            print("{} -> {}".format(k, v))
        print("-"*10)   
    return

def search_user_input():
    file = "/home/coder/aktueller-kurs/tag_2/adressen.csv"
    adressen = prepare_data(file)
    print_out(adressen)
    while True:
        eingabe = input("Name: ").strip()
        if eingabe == "EXIT":
            break
        if eingabe == "SHOWALL":
            print_out(adressen)
        for adresse in adressen:
            if adresse["name"] == eingabe:
                for k, v in adresse.items():
                    print("{} -> {}".format(k, v))
    return

search_user_input()