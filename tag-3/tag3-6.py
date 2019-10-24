import os
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

dateiliste = find_files(root, ".txt")
doppelte = find_doubletten(dateiliste)

pprint.pprint(doppelte)
