import re

with open("neu.log") as fd:
    rohdaten = fd.read().split("\n")

ergebnis_daten = {}

for zeile in rohdaten:
    m = re.search(r"^(\d\d/\d\d) +([0-9:]+) +([^ :]*) *:(.*)$", zeile)
    if not m.group(3) in ergebnis_daten:
        ergebnis_daten[m.group(3)] = []
    ergebnis_daten[m.group(3)].append([m.group(1), m.group(2), m.group(4)])

for k, v in ergebnis_daten.items():
    print("{} hat {} Einträge".format(k, len(v)))
