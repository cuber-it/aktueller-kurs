import csv

def csv_gelesen():
    csv_text = []
    with open("100 Sales Records.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            csv_text.append(dict(row))


    for n in csv_text[:5]:
        print("{} - {}".format(n["Region"], n["Item Type"]))


def csv_write():
    l = [
        { "Name": "Willi", "Alter": 55 },
        { "Name": "Klaus", "Schuhgrösse": 45}
    ]

    with open("test.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["Name", "Alter", "Schuhgrösse"])
        writer.writeheader()
        for row in l:
            writer.writerow(row)