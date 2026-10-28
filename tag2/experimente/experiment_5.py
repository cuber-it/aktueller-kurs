datei = r"/home/ucuber/Wörkspace/kurse/kurse/aktueller-kurs/materialien/HistoricalQuotes.csv"

#fd = None
#try:
#    fd = open(datei, "r")
#    for znr, zeile in enumerate(fd.read().splitlines()):
#        print(f"{znr:05}:{zeile}")
#except Exception as e:
#    print("Dateifehler:", e)
#    exit()
#finally:
#    if fd:
#        fd.close()

with open(datei, "r") as fd:
    for znr, zeile in enumerate(fd.read().splitlines()):
        print(f"{znr:05}:{zeile}")
