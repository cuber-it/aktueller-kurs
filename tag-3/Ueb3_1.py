import csv
import sqlite3

#reader = csv.DictReader(open("report.csv"))
#rows = []
#for row in reader:
#    rows.append(dict(row))

rows = [dict(row) for row in csv.DictReader(open("report.csv"))]

sql = "INSERT INTO T1 VALUES({})"
conn = sqlite3.connect('example.db')
for row in rows:
    field1, field2, field3 = row.values()
    field1 = "'{}'".format(field1)
    field3 = "'{}'".format(field3)
    print(sql.format(",".join([field1, field2, field3])))
