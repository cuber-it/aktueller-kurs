import os

# Datei - Pfad speichern
path = "/home/coder/aktueller-kurs/tag_2"
file = "openthesaurus.txt"
complete_path = os.path.join(path,file)

# Einlesen Thesaurus
with open(complete_path) as fd:
    text = fd.readlines()

# Herausfiltern der Zeilen mit #
Lines = []
for line in text:
    if line[0] != "#":
        Lines.append(line.strip("\n"))

# Umwandeln der Zeilen in durchsuchbare Listen
wortlisten = []
for line in Lines:
    wortlisten.append(line.split(";"))

pass  # nur um dort einen Sprungmarke hinsetzen zu können

# Mache das solange der Benutzer nicht "EXIT" eingibt
eingabe = None
while eingabe != "EXIT":
    # Wort einlesen
    eingabe = input("Bitte geben Sie einen Suchbegriff ein, oder EXIT um aufzuhören: ").strip()
    # Wort in Daten suchen
    gefunden = False
    for worte in wortlisten:
        if eingabe in worte:
            # Wenn Wort gefunden, die Alternativen ausgeben
            print(worte)
            gefunden = True
            # break           = Raus, wenn ich den ersten passenden Begriff gefunden habe
            # break if eingabe == "EXIT" -> alles in einer zeile    
    # Wenn Wort nicht gefunden, "ist unbekannt" ausgeben    
    if not gefunden:
        print("Begriff ist nicht bekannt")
    
    
    
    