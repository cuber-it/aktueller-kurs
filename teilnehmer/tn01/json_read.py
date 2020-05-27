import os
import json

path = "/home/coder/aktueller-kurs/tag_3"
file = "config.json"

daten = json.load(open(os.path.join(path, file)))

print(type(daten))

for x in daten["web-app"]["servlet"]:
    print(x["servlet-name"])
