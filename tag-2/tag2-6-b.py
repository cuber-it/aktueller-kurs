datei = "Routerlist.txt"

def read_data(datei):
    with open(datei) as fd:
        rdaten = fd.readlines()
    return rdaten

def build_router_table(rdaten):
    router = {}
    for z in rdaten[6:-1]:
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
    return router

#-------------------------------------------------
for k, v in build_router_table(read_data(datei)).items():
    print("{} -> {}".format(k, v))


