path="/home/coder/aktueller-kurs/tag_2/SampleLog.log"

with open(path) as fd:
    lines = fd.readlines()

for line in lines:
    line = line.strip("\n")
    aktion = line[15:19]
    if aktion == "WARN" or aktion == "INFO" or aktion == "TRAC":
        print(line)