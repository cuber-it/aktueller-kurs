import csv

def csv_spalten_name(fname, delimiter=","):
    with open(fname) as f:
        return f.readline().strip("\n").split(delimiter)

def csv_lesen(fname):
    csv_text = []
    with open(fname) as f:
        reader = csv.DictReader(f)
        for row in reader:
            csv_text.append(dict(row))
    return csv_text

def csv_schreiben(fname, csv_daten):
    with open(fname, "w", newline="") as f:
        fieldnames = csv_daten[0].keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in csv_daten:
            writer.writerow(row)

datei_name = "/home/coder/aktueller-kurs/tag_3/100 Sales Records.csv"
#print(csv_spalten_name(datei_name))
csv_quell_daten = csv_lesen(datei_name)
zwischendaten = {}
for row in csv_quell_daten:
    region = row["Region"]
    sold = row["Units Sold"]
    profit = row["Total Profit"]
    if not region in zwischendaten:
        zwischendaten[region] = { "Units Sold": 0, "Total Profit": 0 }
    zwischendaten[region]["Units Sold"] += int(sold)
    zwischendaten[region]["Total Profit"] += float(profit)

csv_zieldaten = []
for k, v in zwischendaten.items():
    v["Region"] = k
    csv_zieldaten.append(v)

csv_schreiben("report.csv", csv_zieldaten)