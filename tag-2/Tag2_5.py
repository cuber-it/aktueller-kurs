import pprint
import re

def read_textfile(filename):
    with open(filename, encoding="utf-8") as datei:
        return datei.read().split("\n")

dateiname = "AIM_export_191112.ldif"

rohdaten = read_textfile(dateiname)
ergebnis_daten= {}

for zeile in rohdaten:
    if "dn" in zeile:
        m = re.search(r"onlineUserId=(\d+),", zeile)
        if m:
            dn = m.group(1)
    if "forum.vodafone.de" in zeile:
        m = re.search(r".*\|(.*?)\|(.*)/?$", zeile)
        if m:
            ergebnis_daten[dn] = m.group(2)

for k, v in ergebnis_daten.items():
    print("{} {}".format(k, v))

print(len(ergebnis_daten))