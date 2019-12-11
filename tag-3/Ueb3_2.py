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
    writer = csv.DictWriter(
        open(filename, mode='w', newline=""),
        data[0].keys())
    writer.writeheader()
    for row in data:
       writer.writerow(row)

#-----------------------------------------------

data = load_excel_data("mappe1.xlsx")
write_csv_data('daten.csv', data)