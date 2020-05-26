path = "/home/coder/aktueller-kurs/tag_2/openthesaurus.txt"

with open(path) as fd:
    lines = fd.readlines()

for line in lines:
    if line[0] != "#":
        line = line.strip("\n")
        print(line)
    
    
    