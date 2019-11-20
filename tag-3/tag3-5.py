import csv

def csv_gelesen():
    csv_text = []
    with open("100 Sales Records.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            csv_text.append(dict(row))
