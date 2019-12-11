dateiname = "SampleLog.log"

with open(dateiname) as datei:
    text = datei.readlines()

arbeits_text = []
for zeile in text:
    arbeits_text.append(zeile.strip("\n"))

#with open(dateiname) as datei:
#    text = datei.read()
#
#arbeits_text = text.split("\n")

zeilennummer = 1
for zeile in arbeits_text:
    if "WARNING" in zeile:
        print("{}: {}".format(zeilennummer, zeile))
    zeilennummer = zeilennummer + 1

