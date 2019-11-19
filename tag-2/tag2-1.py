with open("openthesaurus.txt", encoding="utf-8") as f:
    text = f.readlines()

d = {}
for zeile in text:
    if not zeile.startswith("#"):
        zeile = zeile.strip("\n")
        zeile = zeile.split(";")
        d[zeile[0]] = zeile[1:]

#for k, v in d.items():
#    print("{} -> {}".format(k, v))

#print("{}".format(d["#"]))

print(list(d.keys()))

for n in d.keys():
    print(n)
