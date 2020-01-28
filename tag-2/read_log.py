import re

file_name = "SampleLog.log"

with open(file_name) as fd:
    text = fd.readlines()

log_daten = []
for zeile in text:
    zeile = zeile.strip("\n")
    if re.search(r"^ *$", zeile):
        continue
    if re.search(r"^ \d\d $", zeile):
        continue
    if re.search(r"^Kopieren", zeile):
        continue
    if re.search(r"^\d\d/\d\d", zeile):
        log_daten.append(zeile)
    else:
        log_daten[-1] = log_daten[-1] + zeile

for zeile in log_daten:
    print(zeile)

print(len(log_daten))