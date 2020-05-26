import os

# Datei - Pfad speichern
path = "/home/coder/aktueller-kurs/tag_2"
file = "openthesaurus.txt"
complete_path = os.path.join(path,file)


# Einlesen und Herausfiltern der Zeilen mit # und  Umwandeln der Zeilen in durchsuchbare Listen
with open(complete_path) as fd:
    wortlisten = []
    for line in fd.readlines():
        if not line[0] == "#":
            wortlisten.append(line.strip("\n").split(";"))      # erzeugt Hauptliste = Zeilen         mit unterliste = worte

# Frage und suche, solange der Benutzer nicht "EXIT" eingibt
eingabe = None
while eingabe != "EXIT":
    # Wort einlesen
    eingabe = input("Bitte geben Sie einen Suchbegriff ein, oder EXIT um aufzuhören: ").strip()
    # Wort in Wortliste suchen
    gefunden = False
    for worte in wortlisten:
        if eingabe in worte:
            # Wenn Wort gefunden, die Alternativen (= Zeile) ausgeben
            print(worte)
            gefunden = True
            # break           = Raus, wenn ich den ersten passenden Begriff gefunden habe
    # Wenn Wort nicht gefunden, "ist unbekannt" ausgeben    
    if not gefunden:
        print("Begriff ist nicht bekannt")
    
    
    
    