import os
import yaml

path = "/home/coder/aktueller-kurs/tag_3"
file = "config.yaml"

with open(os.path.join(path, file)) as fd:
    daten = yaml.safe_load(fd)
    print(daten['cloud']['name'])