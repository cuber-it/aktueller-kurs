import os

path = "/home/coder/aktueller-kurs/tag_2"
file = "SampleLog.log"

with open(os.path.join(path, file)) as fd:
    raw_data = []
    for line in fd.readlines():
        if "/" in line:
            raw_data.append(line.strip("\n"))

data = {}

for line in raw_data:
    event = line[15:22]
    if event not in data:
        data[event] = []
    data[event].append(line[23:])

for k, v in data.items():
    print("{} -> {}".format(k, len(v)))

while True:
    eingabe = input("Eventtyp: ")
    if eingabe == "Ende":
        break
    if eingabe in data:
        for entry in data[eingabe]:
            print("\t{}".format(entry))
    else:
        print("entrytype unknown")