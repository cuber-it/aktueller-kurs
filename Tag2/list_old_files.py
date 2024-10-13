import os
import sys
import time
import datetime

SECONDS_OF_DAY = 86400
DELTA_DAYS = 150 * SECONDS_OF_DAY

if len(sys.argv) == 1:
    start_verzeichnis = input("Startverzeichnis: ")
else:
    start_verzeichnis = sys.argv[1]

present = time.time()

for fname in os.listdir(start_verzeichnis):
    fullpath = os.path.join(start_verzeichnis, fname)
    mtime = os.path.getmtime(fullpath)
    time_delta = present - mtime
    if time_delta > DELTA_DAYS:
        value = datetime.datetime.fromtimestamp(mtime)
        print(fullpath, value.strftime('%Y-%m-%d %H:%M:%S'))
        
print("#------------------------------------------------------------------")


daten = {}
for fname in os.listdir(start_verzeichnis):
    fullpath = os.path.join(start_verzeichnis, fname)
    mtime = os.path.getmtime(fullpath)
    daten[mtime] = fullpath

for key in sorted(daten.keys())[:10]:
    value = datetime.datetime.fromtimestamp(key)
    print(daten[key], value.strftime('%Y-%m-%d %H:%M:%S'))
