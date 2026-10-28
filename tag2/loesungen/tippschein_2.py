import os

# Ordner "materialien" in diesem Projekt (relativ zu dieser Datei)
basis = os.path.dirname(__file__)
materialien = os.path.join(basis, "..", "..", "materialien")

dateiname = input("Dateiname: ")
dateipfad = os.path.join(materialien, dateiname)

if not os.path.exists(dateipfad):
    vorhanden = 0
else:
    with open(dateipfad, "r") as f:
        vorhanden = sum(1 for line in f)

if vorhanden >= 10:
    print("Die Datei ist bereits voll.")
    with open(dateipfad, "r") as f:
        for line in f:
            print(line)
    exit()

with open(dateipfad, "a") as f:
    for i in range(vorhanden, 10):
        lotto_zahl = input("Gib eine Lottozahl ein oder 'ende' zum Beenden: ")
        if lotto_zahl.lower() == "ende":
            break
        else:
            f.write(lotto_zahl + "\n")
    print("Die Datei wurde gespeichert.")

with open(dateipfad, "r") as f:
    for line in f:
        print(line)
