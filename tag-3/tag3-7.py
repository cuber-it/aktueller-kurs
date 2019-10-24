import os
import hashlib
import pprint

root = r"D:\\"
daten = {}

def find_files(root, ext):
    daten = {}
    for dirName, subdirList, fileList in os.walk(root):
        for fname in fileList:
            if fname.endswith(ext):
              if not dirName in daten:
                  daten[dirName] = []
              daten[dirName].append(fname)
    return daten

def find_doubletten(daten):
    ergebnis = {}
    for verz, dateien in daten.items():
        for datei in dateien:
            if not datei in ergebnis:
                ergebnis[datei] = []
            ergebnis[datei].append(verz)
    for k in list(ergebnis.keys()):
        if len(ergebnis[k]) <= 1:
            del ergebnis[k]
    return ergebnis

def make_md5(filename):
    return hashlib.md5(open(filename, 'rb').read()).hexdigest()

def find_identische(doppelte):
    ergebnis = {}
    for k, v in doppelte.items():
        for verz in v:
            pfad = os.path.join(verz, k)
            md5 = make_md5(pfad)
            if not md5 in ergebnis:
                ergebnis[md5] = []
            ergebnis[md5].append(pfad)
    return ergebnis

dateiliste = find_files(root, ".txt")
doppelte = find_doubletten(dateiliste)
identische = find_identische(doppelte)

pprint.pprint(identische)


