def read_file(fname):
    with open(fname) as fd:
        text = fd.read().split("\n")
    return text

def create_thesaurus(daten):
    rval = []
    for line in daten:
        if not line.startswith("#"):
            rval.append(line.split(";"))
    return rval


#-------------------------------------------------
def main():
    path = "/home/coder/aktueller-kurs/tag_2/openthesaurus.txt"
    daten = read_file(path)
    thesaurus = create_thesaurus(daten)
    print(len(thesaurus))


#---------------------------
main()