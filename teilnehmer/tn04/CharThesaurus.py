#!usr/bin/python3
path = "/home/coder/aktueller-kurs/tag_2/openthesaurus.txt"


with open(path) as fd:
    zeilen = fd.readlines()

for zeile in zeilen:
    zeile = zeile.strip("\n")
    if not zeile.startswith("#"):
        print(zeile)
