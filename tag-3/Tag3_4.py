import csv
with open('report.csv') as f:
  data = csv.reader(f)
  csvlist = []
  for row in data:
        csvlist.append(row)
header = csvlist[0]
for zeile in csvlist[1:]:
    data_row_dict = dict(zip(header, zeile))
    print(data_row_dict["Units Sold"])

#-----------------------------
print("-"*20)

reader = csv.DictReader(open("report.csv"))
for raw in reader:
    print(raw["Units Sold"])