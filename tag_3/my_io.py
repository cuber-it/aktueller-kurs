def slurp(fname, style=None):
    """
        Reads all content of a file

        If nothing specified then all as on string
        else if "LIST as parameter given it will be converted to a list of string

        @PARAMS:
        fname: a path to a textfile
        style: return as stroing or list. default = String
        @RETURNS:
        String or list of strings (aka. textlines)
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
        Writes a list of strings as a textfile

        The list of tring will be joined, so that every line
        in the textfile ist delimited by LF

        ...
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
