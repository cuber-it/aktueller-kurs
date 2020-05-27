import os
import csv

path = "/home/coder/aktueller-kurs/tag_3"
file = "100 Sales Records.csv"

daten = []

with open(os.path.join(path, file)) as fd:
    for row in csv.DictReader(fd):
        daten.append(row)

    for row in daten:
        print(row["Region"])