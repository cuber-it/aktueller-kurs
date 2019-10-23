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

for zeile in daten:
    m = re.search("^(\d{2}/\d{2}) +(\d{2}:\d{2}:\d{2}) +([A-Z]+) *:(.*)$", zeile)
    print(m.groups())


#counter = 0
#for zeile in daten:
#  zerlegung = zeile.split(" ", 3)
#  if "INFO" in zerlegung:
#      counter += 1
#  print(zerlegung)
#print(counter)

