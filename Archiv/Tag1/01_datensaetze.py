h = ["ID", "PLZ", "Ort"]

v = [
        ["12345", "22559", "Hamburg"],
        ["12346", "22765", "Hamburg"],
]

daten = []
for values in v:
    daten.append(dict(zip(h, values)))

print(daten)

datendict = {}
for values in v:
    datendict[values[0]] = dict(zip(h[1:], values[1:]))
print(datendict)
