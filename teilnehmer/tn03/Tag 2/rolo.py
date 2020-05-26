import os
def read_file(fname):
    with open(fname) as fd:
        text = fd.read().split("\n")
    return text
    adressen = []
    for line in fd.readlines():
        name, ort, plz, strasse = line.strip("\n").split(";")
        adressen.append({"name": name, "plz": plz, "ort": ort, "strasse": strasse})
    return adressen
 
def print_adressen(adressen):
    for adresse in adressen:
        for k, v in adresse.items():
            orint("{} -> {}".format(k, v))
        

read_file("/home/coder/aktueller-kurs/tag_2/adressen.csv")
print(adressen)
adressbuch(text)

for adresse in adressen:
    for k, v in adresse.items():
        print("{} -> {}".format(k, v))
    print("-"*10)   

while True:
    eingabe = input("Name: ").strip()
    if eingabe == "EXIT":
        break
    for adresse in adressen:
        if adresse["name"] == eingabe:
            for k, v in adresse.items():
                print("{} -> {}".format(k, v))
                
        
