import os

path = "/home/coder/aktueller-kurs/tag_2"
file = "openthesaurus.txt"

gesamt_pfad = os.path.join(path, file)

# Einlesen Thesaurus
with open(gesamt_pfad) as fd:
    rohtext = fd.readlines()

# Herausfiltern der Zeilen mit #
lines = []
for line in rohtext:
    if not line[0] == "#":
        lines.append(line.strip("\n"))

# Umwandeln der Zeilen in durchsuchbare Listen
wortlisten = []
for line in lines:
    wortlisten.append(line.split(";"))

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