import pprint
import re

fname = r"D:\Kurse\python\aktueller-kurs\tag-1\SampleLog.log"

with open(fname) as f:
    alt = f.readlines()

print("Roh {}".format(len(alt)))

neu = []
for zeile in alt:
    zeile = zeile.strip("\n")
    if not (re.search("^ *$", zeile) or re.search("^ \d\d $", zeile)):
        if not re.search("^\d\d/\d\d.*", zeile):
            neu[-1] = neu[-1] + zeile
        else:
            neu.append(zeile)

print("Neu {}".format(len(neu)))

with open("neudaten.log", "w") as f:
    f.write("\n".join(neu))

