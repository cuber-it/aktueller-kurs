import json

file = "/home/coder/aktueller-kurs/tag_3/config.json"

daten = json.load(open(file))
print(type(daten))

for x in daten["web-app"]["servlet"]:
    print(x["servlet-name"])

    


