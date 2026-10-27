import openpyxl

path = r"/home/ucuber/Workspace/kurse/kurs-python-gl/materialien/aapl.xlsx"
wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
ws = wb.active

for i, row in enumerate(ws.iter_rows(values_only=True)):
    if i >= 50:
        break
    print(row)

wb.close()
