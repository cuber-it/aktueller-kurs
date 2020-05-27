def slurp(fname, style=None):
    """
        reads all content of a file
        If nothing specified than all as one string
        else if "LIST" as parameter given it will be converted to a list auf string

        @PARAMS
        fname: as path to a textfile
        style: return as string or list, default = string

        @RETURNS:
        string or list of strings (textlines)
    """
    with open(fname) as fd:
        if style == None:
            data = fd.read()
        elif style == "LIST":
            data = fd.read().split("\n")
        else:
            raise Exception("unknown style: {}".format(style))
    return data


def spit(fname, list_data):
    """
        writes a list of strings as a textfile

        The list of strings will be joined, so that every line
        in the textfile is delimeted by LF

    """
    with open(fname, "w") as fd:
        fd.write("\n".join(list_data))

if __name__ == "__main__":
    l = [ "Willi", "Heinz", "Karl"]
    spit("Test.txt", l)
    l2 = slurp("Test.txt", "LIST")
    
    for i, e in enumerate(l):
        if e != l2[i]:
            print("Error: {} {}".format(e, l2[i]))
