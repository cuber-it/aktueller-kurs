import re
import pprint

dateiname=r"D:/Programmierung/aktueller-kurs/tag-1/SampleLog.log"

with open(dateiname) as fd:
    rohdaten = fd.readlines()

daten = []
for zeile in rohdaten:
  zeile = zeile.strip()
  if not re.search(r"^(Kopieren|( *)|(\d{2}))$", zeile):
      if re.search(r"^\d{2}/\d{2}", zeile):
        daten.append(zeile)
      else:
        daten[-1] = daten[-1] + zeile

d = {}
for zeile in daten:
    m = re.search("^(\d{2}/\d{2}) +(\d{2}:\d{2}:\d{2}) +([A-Z]+) *:(.*)$", zeile)
    status = m.groups()[2]
    if not status in d:
        d[status] = []
    d[status].append(m.groups())

print("Infos: {}".format(len(d["INFO"])))
for m in d["INFO"]:
    print("{} {}".format(m[1], m[3]))

#print(d["INFO"][0])
#print(d["INFO"][-1])
#counter = 0
#for zeile in daten:
#  zerlegung = zeile.split(" ", 3)
#  if "INFO" in zerlegung:
#      counter += 1
#  print(zerlegung)
#print(counter)

