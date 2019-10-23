datei = "Routerlist.txt"

with open(datei) as fd:
    rdaten = fd.readlines()[6:-1]

router = {}
for z in rdaten:
    zeile = z.strip().split()
    if len(zeile) == 5:
        router[zeile[0]] = {
            "adm": zeile[1],
            "opr": zeile[2],
            "mode": zeile[3],
            "port": zeile[4],
            "ipadr": []
        }
        aktrouter = zeile[0]
    elif len(zeile) == 2:
        router[aktrouter]["ipadr"].append(zeile)

for k, v in router.items():
    print("{} -> {}".format(k, v))


