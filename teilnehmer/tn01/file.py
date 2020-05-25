import os

quelldatei = str(input("Welche Datei soll kopiert werden? (kompletter Pfad)"))
zieldatei = str(input("Wie soll die neue Datei heißen? "))

with open(quelldatei) as fd:
    text = fd.read()

with open(zieldatei, "w") as fd:
    fd.write(text)
