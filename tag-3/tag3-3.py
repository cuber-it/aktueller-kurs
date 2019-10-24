import csv
import pprint

def read_data(fname, delim):
    daten = []
    with open(fname, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=delim)
        for row in reader:
            daten.append(dict(row))
    return daten

daten = read_data("fdgsd-day-sysstat.csv", ";")
pprint.pprint(daten)