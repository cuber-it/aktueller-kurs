import sys
sys.path.append(r"E:\Workspaces\Kurse\aktueller-kurs\Tag3\uebungen\lib")
import yaml2json as y2j

QUELLE = r"E:\Workspaces\Kurse\aktueller-kurs\Material\config.yaml"
ZIEL = r"E:\Workspaces\Kurse\aktueller-kurs\Material\config_neu_2.json"
y2j.yaml2json(QUELLE, ZIEL)
# Besser nicht, da hidden: print("--->", y2j._read_yaml_data(QUELLE))
