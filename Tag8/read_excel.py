import openpyxl as xls
import warnings
from typing import List, Dict, Any

def get_excel_data(fname: str, sheet_name: str) -> List[Dict(str, Any)]:
    warnings.filterwarnings("ignore", category=UserWarning, module="openpyxl")

    wb = xls.open(fname)
    sheet = wb[sheet_name]

    header = [cell.value for cell in sheet[1]]
    data = []
    for row in sheet.iter_rows(values_only=True):
        values = [ cell for cell in row ]
        row_dict = dict(zip(header, values))
        data.append(row_dict)
    return data

def set_excel_data(fname: str, sheet_name: str, data: List[Dict(str, Any)]) -> bool:
    """
    Schreibt Daten aus einer Liste von Dict in ein neues Excel Workbook

    :params:
        fname: str - der Dateiname
        sheet_name: str - der Sheetname
        data: List von Dict - die Daten für Excel
    :returns: bool - Success-Flag
    """
    pass


if __name__ == "__main__": # Spielwiese, aber kein Test!!!
    import pprint
    sheet_name = "Titanic_ohne_Name"
    fname = r"E:\Workspaces\Kurse\aktueller-kurs\Material\Titanic_splitted_names.xlsx"

    data = get_excel_data(fname, sheet_name)
    pprint.pprint(data[:2])
    set
