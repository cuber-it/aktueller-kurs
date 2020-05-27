import json

with open("/home/coder/aktueller-kurs/tag_3/config.json") as json_file:
    data = json.load(json_file)
    print(type(data))

    for x in data["web-app"]["servlet"]:
        print (x["servlet-name"])