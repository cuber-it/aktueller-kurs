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

