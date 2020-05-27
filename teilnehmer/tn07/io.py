def slurp(fname, style=None):
    with open(fname) as fd:
        if style == None:
            data =fd.read()
        elif style == "LIST":
            data = fd.readlines()
        else:
            raise Exception("unknown style: {}".foramt(style))
    return data

def spit(fname, list_data):
    with open(fname, "w") as fd:
        fd.write("\n", join(list_data))


