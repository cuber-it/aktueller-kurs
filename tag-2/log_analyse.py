import re

with open("SampleLog.log") as fd:
    text = fd.readlines()

#i = 0
#while i < len(text):
#    zeile = text[i]
#    treffer = re.search(r"(\d{1,3}\.){3}\d{1,3}", zeile)
#    i = i + 1

ergebnis_liste = []
for znr, zeile in enumerate(text, start=1):
    treffer = re.search(r"(\d{1,3}\.){3}\d{1,3}", zeile)
    if treffer:
        print("{}->{}".format(znr, treffer.group(0)))
        ergebnis_liste.append(treffer.group(0))

with open("Ergebnis.txt", "w") as fd:
    fd.write("\n".join(ergebnis_liste))
