import csv

datei_name = "/home/coder/aktueller-kurs/tag_3/100 Sales Records.csv"

daten = []
with open(datei_name) as fd:
    reader = csv.DictReader(fd)
    for row in reader:
        daten.append(row)

print(daten[0]["Region"])
print(daten[-1]["Region"])