import os

path = "/home/coder/aktueller-kurs/tag_2"
file = "SampleLog.log"

with open(os.path.join(path,file)) as fd:
    raw_data = []
    for line in fd.readlines():
        if "/" in line:
            raw_data.append(line.strip("\n"))

data = {}

for line in raw_data:
    event = line[15:21]
    if event not in data:
        data[event] = []
    data[event].append(line[22:])

pass
