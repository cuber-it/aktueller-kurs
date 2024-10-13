import os
import sys

start_verzeichnis = None # optional, fü die Optik
if len(sys.argv) == 1:
    start_verzeichnis = input("Startverzeichnis: ")
else:
    start_verzeichnis = sys.argv[1]

filenames = {}

for fname in os.listdir(start_verzeichnis):
    fullpath = os.path.join(start_verzeichnis, fname)
    print("Dateipfad: ", fullpath)
    if not os.path.isdir(fullpath):
        with open(fullpath, mode="r+b") as fd:
            filenames[fullpath] = fd.read()

for name, inhalt in filenames.items():
    print(f"{name}: {len(inhalt)} Bytes")