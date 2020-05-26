import os

# Datei - Pfad speichern
path = "/home/coder/aktueller-kurs/teilnehmer/tn08"
file = "adressen.csv"
complete_path = os.path.join(path,file)

# Einlesen der Datei und aus den Datensätzen ein Dict. machen
with open(complete_path) as fd:
    adressen = []
    for line in fd.readlines():
        name, ort, plz, strasse = line.strip("\n").split(",")
        adressen.append({"name":name, "plz":plz , "ort":ort, "strasse":strasse} )

# Dann ausgeben
for adresse in adressen:
    for k,v in adresse.items():
        print("{} -> {}".format(k,v))
    print("-" * 10)
