
#Datei zeilenweise einlesen und zeilenweise ausgeben, allerdings nur valide zeilen
quelle = "/home/coder/aktueller-kurs/tag_2/SampleLog.log"

with open(quelle) as fd:
    lines = fd.readlines()

for line in lines:
    if len(line)>4  and line[2] == "/":
        print(line.strip("\n"))
        