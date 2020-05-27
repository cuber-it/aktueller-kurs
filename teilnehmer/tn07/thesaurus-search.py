import os

path = "/home/coder/aktueller-kurs/teilnehmer/tn07"
file = "openthesaurus.txt"

gesamt_pfad = os.path.join(path, file)

# datei einlesen in zeilen
with open(gesamt_pfad) as fd:
    rohtext = fd.readlines()

# heruasfiltern der zeilen mit #
lines = []
for line in rohtext:
    if not line[0] == "#":
        lines.append(line.strip("\n"))

# umwandeln der zeien in durchsuchbare listen
wortlisten = []
for line in lines:
    wortlisten.append(line.split(";"))

# benutzer eingabe
eingabe = None
# solange benutzer nicht exit eingibt
while True:
    eingabe = input("Suchbegriff? (Ende mit EXIT)").strip()
    if eingabe == "EXIT":
        break
    # wort in daten suchen
    gefunden = False
    for worte in wortlisten:
        # wenn wort gefunden die alternativen ausgeben
        if eingabe in worte:
            print(worte)
            gefunden = True
            #break
    if not gefunden:
        print("Wort ist nicht bekannt")

#print(wortlisten)