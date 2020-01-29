import re

def read_log(fname):
    with open(fname) as fd:
        return fd.read().split("\n")

def write_log(fname, log):
    with open(fname, "w") as fd:
        fd.write("\n".join(log))

def prepare_log(rohdaten):
    neudaten = []

    for zeile in rohdaten:
        zeile = zeile.strip("\n")
        if re.search(r"^ *$", zeile):
            continue
        if re.search(r"^ \d\d $", zeile):
            continue
        if re.search(r"^Kopieren", zeile):
            continue
        if re.search(r"^\d\d/\d\d", zeile):
            neudaten.append(zeile)
        else:
            neudaten[-1] = neudaten[-1] + zeile
    return neudaten