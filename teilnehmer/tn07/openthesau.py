with open("/home/coder/aktueller-kurs/tag_2/openthesaurus.txt") as fd:
    lines = fd.readlines()

    for line in lines[:30]:
        line = line.strip("\n")
        if line[0] != "#":
            print(line)