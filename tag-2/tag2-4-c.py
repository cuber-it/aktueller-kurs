#!/bin/python
import sys

def get_user_arguments():
  datei = sys.argv[1]
  system = sys.argv[2]
  return [datei, system]

def get_user_input():
  datei = input("Dateiname eingeben:")
  system = input("Systemname eingeben: ")
  return [datei, system]

def read_log_data(datei):
  with open(datei) as fd:
    rohdaten = fd.readlines()
  return rohdaten

def clean_data(rohdaten):
  daten = []
  for zeile in rohdaten:
    zeile = zeile.strip()
    zeile = zeile.split(None, 4)
    zeile = [ zeile[0] + "/" + zeile[1]] + zeile[2:]
    daten.append(zeile)
  return daten

def prepare_infos(daten):
  infodaten = {}
  for zeile in daten:
    if not zeile[2] in infodaten:
        infodaten[zeile[2]] = []
    infodaten[zeile[2]].append(zeile)
  return infodaten

#-----------------------------------------------------------------

if len(sys.argv) > 1:
    datei, system = get_user_arguments()
else:
    datei, system = get_user_input()

rohdaten = read_log_data(datei)
daten = clean_data(rohdaten)
infodaten = prepare_infos(daten)

print("{}: {}".format(system, len(infodaten[system])))
for eintrag in infodaten[system]:
    print(eintrag)
