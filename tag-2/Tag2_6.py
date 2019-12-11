import pprint
import re

def read_textfile(filename):
    with open(filename, encoding="utf-8") as datei:
        return datei.read().split("\n")

def write_data(filename, data):
    with open(filename, "w") as fd:
      fd.write("\n".join(data))

dateiname = "AIM_export_191112.ldif"

rohdaten = read_textfile(dateiname)
print(len(rohdaten))

count = 0
for zeile in rohdaten:
    if "dn" in zeile:
        m = re.search(r"onlineUserId=(\d+),", zeile)
        if m:
            count += 1
print(count)

count = 0
data= []
for zeile in rohdaten:
    if "forum.vodafone.de" in zeile:
        #m = re.search(r".*\|(.*?)\|(.*)/$", zeile)
        #if m:
            count += 1
            data.append(zeile)
write_data("test.txt", data)
print(count)