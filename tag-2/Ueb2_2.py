import re

def read_log(logname):
    with open(logname) as datei:
        return datei.read().split("\n")

def write_log(logname, logdata):
    with open(logname, "w") as datei:
        datei.write("\n".join(logdata))
        datei.flush()
#----------------------------------------
dateiname = "SampleLog.log"
altlog = read_log(dateiname)
neulog = []

for zeile in altlog:
    if re.search(r"^\d\d/\d\d.*$", zeile):
        neulog.append(zeile)
    elif not re.search(r"^(Kopieren| *| \d\d )$", zeile):
        neulog[-1] = neulog[-1] + zeile

write_log("neu.log", neulog)

