import os
import sys

start_verzeichnis = None # optional, fü die Optik
if len(sys.argv) == 1:
    start_verzeichnis = input("Startverzeichnis: ")
else:
    start_verzeichnis = sys.argv[1]

for fname in os.listdir(start_verzeichnis):
    if fname.endswith(".txt"):
        fullpath = os.path.join(start_verzeichnis, fname)
        print("Dateipfad: ", fullpath)
        with open(fullpath) as fd:
            count = 0
            while count < 3:
                text = fd.readline().strip()
                print(count+1, ": ", text)
                count += 1
        print("======================================================")
