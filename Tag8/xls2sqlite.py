import data_io_tools as io

data = io.read_excel_data(r"E:\Workspaces\Kurse\aktueller-kurs\Material\Titanic_splitted_names.xlsx", "Titanic_ohne_Name")
io.write_sqlite_data("Titanic_Spezial.sqlite", "Bearbeitet", data)
