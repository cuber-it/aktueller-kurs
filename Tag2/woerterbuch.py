thesaurus = r"E:\Workspaces\Kurse\aktueller-kurs\Material\openthesaurus.txt"

#with open(thesaurus, encoding="utf-8") as fd:
#    text = fd.read().splitlines()
##neutext = []
##for zeile in text:
##    # if zeile[0] != "#":
##    if not zeile.startswith("#"):
##        neutext.append(zeile)
#neutext = [zeile for zeile in text if zeile[0] != "#" ]
#print(neutext[:5])
#exit(0)

try:
    with open(thesaurus, encoding="utf-8") as fd:
        text = [zeile for zeile in fd if not zeile.startswith("#")]
except FileNotFoundError as e:
    print("Datei nicht gefunden")
    exit(1)

suchwort = input("Suchwort: ")

for zeile in text:
    if suchwort in zeile:
        woerter = zeile.split(";")
        found = False
        for wort in woerter:
            if wort == suchwort:
                found = True
        if found:
            print(zeile)
