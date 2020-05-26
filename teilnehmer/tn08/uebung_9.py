import os

# Datei - Pfad speichern
path = "/home/coder/aktueller-kurs/tag_2"
file = "SampleLog.log"
complete_path = os.path.join(path,file)

# Einlesen der Datei und aus den Datensätzen ein Dict. machen
with open(complete_path) as fd:
    lines = []
    for line in fd.readlines():
        if "/" in line:
            lines.append(line.strip("\n"))

# elegant :)
data = {}
for line in lines:
    action = line[15:22].strip()
    if action not in data:
        data[action]=[]
    data[action].append(line[23:])

# Eventtype bereits vorher initialisieren
data_2 = {
    "INFO": [],
    "WARNING": [],
    "TRACE": [],
    "PROTERR": [],
    "EVENT": []
}

# Zeilen passend anhängen
for line in lines:
    action = line[15:22].strip()
    data_2[action].append(line[23:])

# Übersicht ausgeben
for k, v in data_2.items():
    print("{} -> {}".format(k,len(v)))

# Details eines Events ausgeben
while True:
    typ = input("Eventttyp: ")
    if typ =="EXIT":
        break
    if typ in data_2:
        for zeile in data_2[typ]:
            print(zeile)
