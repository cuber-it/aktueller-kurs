path = "/home/coder/aktueller-kurs/tag_2/openthesaurus.txt"


with open(path) as fd:
    lines =fd.readlines()

for line in lines[:20]:     #die ersten 20 Zeilen
    line = line.strip("\n")
    if line[0] != ("#"):    #alle zeilen die  mit # beginnen übergehen
        print(line)