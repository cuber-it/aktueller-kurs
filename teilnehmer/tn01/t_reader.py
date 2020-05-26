#!/usr/bin/python3
path = "/home/coder/aktueller-kurs/tag_2/openthesaurus.txt"

with open(path) as fd:
    lines = fd.readlines()

for line in lines:
    line = line.strip("\n")
    if(line[:1] != "#"):
        print(line)