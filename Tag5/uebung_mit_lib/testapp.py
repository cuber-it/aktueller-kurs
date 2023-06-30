import table
import csv_reader
import console_writer
import file_writer

t = table.Tabelle(has_header=True)
t.load(csv_reader.CsvReader(r"E:\Workspaces\Kurse\aktueller-kurs\Tag4\uebungen\bsp.csv"))
#t.load(DummyReader())
print(t.header())
print(t.row(0))
print(t.cell(0, "Ort"))
print(t.cell(0, 0))
print(t.header_count())
print(t.row_count())
t.dump(file_writer.FileWriter("table_dump.txt"))
t.dump(console_writer.ConsoleWriter())
