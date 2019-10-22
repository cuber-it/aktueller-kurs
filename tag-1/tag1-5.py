import re

dateiname=r"D:/Programmierung/aktueller-kurs/tag-1/SampleLog.log"

with open(dateiname) as fd:
    rohdaten = fd.readlines()

daten = []
for zeile in rohdaten:
  zeile = zeile.strip()
  if not re.search(r"^(( *)|(\d{2}))$", zeile):
      daten.append(zeile)

print(daten)