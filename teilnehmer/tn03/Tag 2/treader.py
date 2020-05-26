path="/home/coder/aktueller-kurs/tag_2/openthesaurus.txt"

with open(path) as fd:
    lines = fd.readlines()

for line in lines[:20]:
    line = line.strip("\n")
    if line[0] != "#":
        print(line)