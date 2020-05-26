def read_file(fname):
    with open(fname) as fd:
        text = fd.read().split("/n")
    return text

def create_thesaurus(daten):
    rval = []
    for line in daten:
        if not line.startswith("#"):
            rval.append(line.split(";"))
        return rval


