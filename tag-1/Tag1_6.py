import pprint

dateiname = "SampleLog.log"

# Variante:
#datei = open(dateiname)
#textblock = datei.read()
#datei.close()

with open(dateiname) as datei:
  textblock = datei.read()

#print(len(textblock))
#print(textblock[0:256])

zeilen = textblock.split("\n")

#print(len(zeilen))
#print(zeilen[3])
#print(zeilen[-1])
#
#for zeile in zeilen[0:10]:
#    print(zeile)

for zeile in zeilen:
    if "WARNING" in zeile or "ERR" in zeile:
        print(zeile)