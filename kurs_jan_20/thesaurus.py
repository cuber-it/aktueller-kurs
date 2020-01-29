with open("openthesaurus.txt") as fd:
    daten = fd.read().split("\n")

print(len(daten))

#text = [ zeile for zeile in daten if not zeile.startswith("#")]

text = []
for zeile in daten:
    if not zeile.startswith("#"):
        text.append(zeile)

print(len(text))

t = {}
for zeile in text:
    key, *alternativen  = zeile.split(";")
    t[key] = alternativen

#for key in list(t.keys())[:10]:
#    print("{} -> {}".format(key, t[key]))

# print(t["Daddel"])
print(t.get("Daddel", "Unbekannt"))
print(t.get("Kernspaltung", "Unbekannt"))

if "Daddel" in t:
    print("Ist bekannt")
else:
    print("Ist nicht bekannt")

for k, v in t.items():
    print("{} -> {}".format(k, v))



