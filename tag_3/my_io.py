def slurp(fname, style=None):
    with open(fname) as fd:
        if style == None:
            data = fd.read()
        elif style == "LIST":
            data = fd.read().split("\n")
        else:
            raise Exception("unknown style: {}".format(style))
    return data


def spit(fname, list_data):
    with open(fname, "w") as fd:
        fd.write("\n".join(list_data))

if __name__ == "__main__":
    l = [ "Willi", "Heinz", "Karl"]
    spit("Test.txt", l)
    l2 = slurp("Test.txt", "LIST")
    
    for i, e in enumerate(l):
        if e != l2[i]:
            print("Error: {} {}".format(e, l2[i]))
