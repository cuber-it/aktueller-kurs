import os

path = "/home/coder/aktueller-kurs/tag_2"
file = "openthesaurus.txt"

gesamt_path = os.path.join(path, file)
#einlesen
with open(gesamt_path) as fd:
    rohtext =fd.readlines()
#herausfiltern der # zeulen
lines = []
for line in rohtext:
    if not line[0] == "#":
        lines.append(line.strip("\n"))
# umwandeln der zeilen in durchsuchbare listen
wortlisten = []
for line in lines:
    wortlisten.append(line.split(";"))

eingabe = None
while eingabe  != "EXIT":
    eingabe = input("wort Eingabe").strip()

    gefunden = False
    for worte in wortlisten:

        if eingabe in worte:
            print(worte)
            gefunden = True

    if not gefunden:
        print("wort nicht bekannt")
    

