#!/usr/bin/python3
import openpyxl as xls
import csv
import sys


def load_excel_data(filename):
    workbook = xls.load_workbook(filename=filename, data_only=True)
    data = workbook["Tabelle1"]["A1:M13"]

    dict_data = []
    data_header = []

    for cell in data[0]:
        data_header.append(cell.value)
    data_header[-1] = "Result"
    data_header[0] = "Jan"

    for row in data[1:]:
        data_row = []
        for cell in row:
            data_row.append(cell.value)
        dict_data.append(dict(zip(data_header, data_row)))
    return dict_data


def write_csv_data(filename, data):
    with open(filename, mode='w', newline="") as fd:
        writer = csv.DictWriter(fd, data[0].keys())
        writer.writeheader()
        for row in data:
            writer.writerow(row)

args = sys.argv[1:]
if len(args) != 2:
    print("usage: {} xls-source csv-target".format(sys.argv[0]))
    sys.exit(1)

try:
    data = load_excel_data(args[0])
    #...
    write_csv_data(args[1], data)
except Exception as e:
    print(e)
    sys.exit(2)
sys.exit(0)