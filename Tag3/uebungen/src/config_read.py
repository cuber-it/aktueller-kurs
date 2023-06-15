import yaml
import json

# Eingabge/Einlesen
def read_yaml_data(fname):
    with open(fname) as fd:
        data = yaml.load(fd, yaml.FullLoader)
    return data

# Verarbeitung

# Ausgabe
def write_json_data(data, fname):
    with open(fname, "w") as fd:
        json.dump(data, fd)

if __name__ == "__main__": # wenn NICHT als modul geladen ...
    QUELLE = r"E:\Workspaces\Kurse\aktueller-kurs\Material\config.yaml"
    ZIEL = r"E:\Workspaces\Kurse\aktueller-kurs\Material\config_neu.json"
    data = read_yaml_data(QUELLE)
    write_json_data(data, ZIEL)
