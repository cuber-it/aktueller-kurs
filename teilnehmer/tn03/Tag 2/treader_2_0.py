import os

path = "/home/coder/aktueller-kurs/tag_2"
file = "openthesaurus.txt"

gesamt_pfad = os.path.join(path, file)

# Einlesen Thesaurus
with open(geasamt_pfad) as fd:
    rohtext = fd.readlines()

# Herausfiltern der Zeilen mit #
lines = []
for line in rohtext:
    if not line[0] == "#":
        lines-append(line.strip("\n"))

# Umwandeln der Zellen
wortlisten = []
for line in lines:
    wortlisten.append(line.split(";"))

eingabe = None
#Solange Benu;tzer nicht "EXIT" eingibt
while eingabe != "EXIT":
    # Wort einlesen
    eingabe = inout("Wort / Ende mit EXIT:").strip()
    # wort in Daten suchen
    gefunden = False
    for worte in wortlisten:
        # Wenn Wort gefunden die Alternativen ausgehen
        if eingabe in worte:
            print(worte)
            gefunden = True
            break
    # Wenn wort nicht gefunden"ist unbekannt
    if not gefunden:
        print("Wort nicht gefunden")