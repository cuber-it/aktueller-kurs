import os

path = "/home/coder/aktueller-kurs/tag_2"
file = "openthesaurus.txt"

# Einlesen Thesaurus
with open(os.path.join(path, file)) as fd:
    wortlisten = []
    for line in fd.readlines():
        if not line[0] == "#":
            wortlisten.append(line.strip("\n").split(";"))

eingabe = None
while eingabe != "EXIT":
    eingabe = input("Geben Sie ein Wort ein: ").strip()
    gefunden = False
    for eintrag in wortlisten:
        if eingabe in eintrag:
            gefunden = True
            zeile = []
            for woerter in eintrag:
                if woerter != eingabe:
                    zeile.append(woerter)
            print(zeile)
    if not gefunden:
        print("ist unbekannt")