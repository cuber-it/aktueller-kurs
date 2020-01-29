import re

with open("SampleLog.log") as fd:
    data = fd.read()

ergebnis = []
for zeile in data.split("\n"):
    if re.search(r"^ \d\d $", zeile):
        ergebnis.append(zeile)

print(len(ergebnis))

ergebnis = [zeile for zeile in data.split("\n") if re.search(r"^ \d\d $", zeile)]

print(len(ergebnis))