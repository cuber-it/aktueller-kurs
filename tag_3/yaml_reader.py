import yaml

file = "/home/coder/aktueller-kurs/tag_3/config.json"

with open(file) as fd:
    data_loaded = yaml.safe_load(fd)

print(type(data_loaded))
print(data_loaded.keys())