#!usr/bin/python3
path = "/home/coder/aktueller-kurs/tag_2/SampleLog.log"


with open(path) as fd:
    zeilen = fd.readlines()

for zeile in zeilen:
    zeile = zeile.strip("\n")
    datum = zeile[0:5]
    if datum == "03/22":
        print(zeile)
