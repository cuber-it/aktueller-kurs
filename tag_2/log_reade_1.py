path = "/home/coder/aktueller-kurs/tag_2/SampleLog.log"

# Einlesen
with open(path) as fd:
    lines = fd.readlines()

# Durchgehen
for line in lines:
  # "\n" strippen
  line = line.strip("\n")
  # Wenn valide Zeile
  #if len(line) >= 4 and line[2] == "/":
  if line.startswith("03/"):
    # Ausgeben
    print(line)


