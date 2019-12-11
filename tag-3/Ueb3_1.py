import csv
reader = csv.DictReader(open("report.csv"))
rows = []
for row in reader:
    rows.append(row)

print(" | ".join(rows[0].keys()))
print("-" * 40)
for row in rows:
    print(" | ".join(row.values()))

sql = "INSERT INTO Tabelle VALUES({})"
for row in rows:
    u, w, l = row.values()
    l = "'{}'".format(l)
    print(sql.format(",".join([u, w, l])))
