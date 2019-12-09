import re

dateiname = "SampleLog.log"

with open(dateiname) as datei:
    text = datei.read().split("\n")

for zeile in text:
#    m = re.search(r"(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})", zeile)
    m = re.search(r"^(Kopieren| *| \d\d )$", zeile)
    if m == None:
        print(zeile)


