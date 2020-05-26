#!usr/bin/python3

path = "/home/coder/aktueller-kurs/teilnehmer/tn04/Dat.csv"


with open(path) as fd:
    infos = []
    for zeile in fd.readlines():
        name, ort, plz, straße = zeile.strip("\n").split(";")
        infos.append({"Name: ": name, "Postleitzahl: ": plz, "Ort: ": ort, "Straße: ": straße})

for info in infos:
    for i, j in info.items():
        print(i, j)

