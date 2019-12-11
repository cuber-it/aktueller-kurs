def read_textfile(filename):
    with open(filename, encoding="utf-8") as datei:
        return datei.read().split("\n")

dateiname = "openthesaurus.txt"

rohdaten = read_textfile(dateiname)
arbeitsdaten = []

for zeile in rohdaten:
    if not zeile.startswith("#"):
        wort, *woerter = zeile.split(";")
        arbeitsdaten.append([wort, woerter])

#for zeile in arbeitsdaten[:10]:
#    print(zeile)

suchwort = ""
while suchwort != "EXIT":
    suchwort = input("Suchwort: ")
    ersetzung = []
    for zeile in arbeitsdaten:
        if suchwort in zeile:
            ersetzung = zeile[1]
            break
    if ersetzung:
        print("{} oder auch {}".format(suchwort, ersetzung))
    else:
        print("{} nicht gefunden".format(suchwort))
