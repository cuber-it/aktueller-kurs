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
# Solange Benutzer nicht "EXIT" eingibt
while True:
  # Wort einlesen
  eingabe = input("Wort (Ende mit EXIT)").strip()
  if eingabe == "EXIT":
      break
  # Wort in Daten suchen
  gefunden = False
  for worte in wortlisten:
      # Wenn Wort gefunden die Alternativen ausgeben
      if eingabe in worte:
          print(worte)
          gefunden = True
          #break
  # Wenn Wort nicht gefunden "ist unbekannt" ausgeben
  if not gefunden:
      print("Wort ist nicht bekannt")

