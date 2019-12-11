l = [
    {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    },
    {
        "brand": "Opel",
        "model": "Kapitän"

    }
]

print(l[0].keys())
print(l[0].values())

d = l[1]
print(d.get("year", None))
# print(d["year"])

for feldname, wert in d.items():
    print("{} {}".format(feldname, wert))

print("-"*20)
for eintrag in l:
    for feldname, wert in eintrag.items():
        print("{} {}".format(feldname, wert))