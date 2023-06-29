import yaml
import json

# Hidden Functions - bitte nicht direkt nutzen,
# können jederzeit ohne Vorarnung geändert werden!!!
# Eingabge/Einlesen
def _read_yaml(fname):
    with open(fname) as fd:
        data = yaml.load(fd, yaml.FullLoader)
    return data

# Verarbeitung

# Ausgabe
def _write_json(data, fname):
    with open(fname, "w") as fd:
        json.dump(data, fd, indent=4, sort_keys=True)

# offizielle Schnittstelle
def yaml2json(quelle, ziel):
    data = _read_yaml(quelle)
    _write_json(data, ziel)
    return data
