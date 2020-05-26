path = "/home/coder/aktueller-kurs/tag_2/SampleLog.log"

with open(path) as fd:
    lines = fd.readlines()

for line in lines:
    line = line.strip("\n")
    #if len(line) >= 4 and line[2] == "/":
    if line.startswith("03/"):
        print(line)