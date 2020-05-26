import os

path = "/home/coder/aktueller-kurs/tag_2"
file = "SampleLog.log"

with open(os.path.join(path, file)) as fd:
    raw_data = []
    for line in fd.readlines():
        if "/" in line:
            raw_data.append(line.strip("\n"))


data = {
    "PROTERR": [],
    "TRACE": [],
    "INFO": [],
    "WARNING": [],
    "EVENT": []
}

for line in raw_data:
    event = line[15:22].strip()
    if event in data.keys():
        data[event].append(line[22:])
    

for k, v in data.items():
    print("{} -> {}".format(k, len(v)))

while True:
    eingabe = input("Eventtyp: ").strip()
    if eingabe == "ENDE":
        break
    if eingabe in data:
        for entry in data[eingabe]:
            print("\t{}".format(entry))
    else:
        print("eventtype unknown")