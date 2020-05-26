path = "/home/coder/aktueller-kurs/teilnehmer/tn04/SampleLog.log"
wort = "Warning"

with open(path) as fd:
    infos = []
    for zeile in fd.readlines():
        datum = zeile[0:5]
        if "/" in zeile:
            infos.append(zeile.strip("\n"))

ds = {}
for zeile in infos:
    typ = zeile[15:22]
    if typ not in ds:
        ds[typ] = []
    ds[typ].append(zeile[22:])

for i, j in ds.items():
    print(i, j)

while True:
    ip = input("Typ: ").strip()
    if ip == "Exit":
        break
    if ip in ds:
        for ko in ds[ip]:
            print("\t{})".format(ko))
    else:
        print("Unbekannt")