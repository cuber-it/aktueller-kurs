import re

dateiname=r"D:/Programmierung/aktueller-kurs/tag-1/SampleLog.log"

def cat(dateiname):
    with open(dateiname) as fd:
        rohdaten = fd.readlines()
    return rohdaten

def grep(muster, rohdaten):
  daten = []
  for zeile in rohdaten:
    zeile = zeile.strip()
    if not re.search(muster, zeile):
      daten.append(zeile)
  return daten

daten = grep(r"^(( *)|(\d{2}))$", cat(dateiname))

print(daten)