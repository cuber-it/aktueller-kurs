quelle = "/home/coder/aktueller-kurs/tag_2/openthesaurus.txt"
suchwert = "Kernspaltung"

with open(quelle) as fd:
    lines = fd.readlines()

for line in lines:
    if line[0] != "#":
        synonym = line[0:len(suchwert)]
        # wenn die zeile mit meinem Suchwert beginnt, gib sie aus
        if synonym == suchwert:
            print(line.strip("\n"))
            exit()
    