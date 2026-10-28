import json

datei = r"/home/ucuber/Workspace/kurse/kurse/aktueller-kurs/materialien/person.json"

with open(datei) as fd:
    daten = json.load(fd)

print(daten['kenntnisse'][-1])
