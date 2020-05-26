#!/usr/bin/python3
path = "/home/coder/aktueller-kurs/tag_2/SampleLog.log"

with open(path) as fd:
    lines = fd.readlines()

for line in lines:
    line = line.strip("\n")
    if line.startswith("03/22"):
        print(line)
