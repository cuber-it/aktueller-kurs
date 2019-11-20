import json

daten = json.load(open("config.json"))
#print(daten)

for x in daten["web-app"]["servlet"]:
    print(x["servlet-name"])