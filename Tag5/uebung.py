class TableReader:
    def read(self):
        raise RuntimeError("Not yet implemented")

class DummyReader(TableReader):
    def read(self):
        return [
            ["Ort", "PLZ"],
            ["HH", "22559"],
            ["HH", "22765"],
            ["WND", "66606"]
        ]

class CsvReader(TableReader):
    def __init__(self, fname, delim=","):
        self._fname = fname
        self._delim = delim

    def read(self):
        with open(self._fname) as fd:
            return [row.split(self._delim) for row in fd.read().splitlines()]

class TableWriter:
    def write(self, daten):
        raise RuntimeError("Not yet implemented")

class ConsoleWriter(TableWriter):
    def write(self, daten):
        for row in daten:
            print(row)

class FileWriter(TableWriter):
    def __init__(self,fname):
        self._fname = fname

    def write(self, daten):
        with open(self._fname, "w") as fd:
            for row in daten:
                row = str(row)[1:-1]
                print(row, file=fd)

#------------------------------------------------------
class Tabelle: # weiss nichts von Input und output, kennt sichnur mit Tabellen aus
    def __init__(self, has_header=False):
        self._header = []
        self._table = []
        self._has_header = has_header

    def __str__(self):
        return str(self._prep_ausgabe())

    def _prep_ausgabe(self):
        result = []
        if self._has_header:
            result = [self._header]
        return result + self._table

    def header_count(self):
        return len(self._header)

    def header(self):
        return self._header.copy()

    def row(self, row_number, style='simple'):
        if row_number < 0 or row_number > self.row_count():
            raise IndexError(f"table has only {self.row_count()} rows")
        result = []
        if style == 'simple':
            result = self._table[row_number].copy()
        return result

    def row_count(self):
        return len(self._table)

    def cell(self, row_number, column):
        # welcher Zugriff: mit Spaltennummer oder Spaltenname, wenn Header existiert
        # Grundannahme: Zahl
        col = column
        if isinstance(column, str):
            if self._has_header:
                col = self._header.index(column)
                if col < 0:
                    raise IndexError(f"table has no {column} column")
            else:
                raise AttributeError("Table has no dedicated headers")
        row = self.row(row_number)
        return { column: row[col] }

    def load(self, reader_object):
        if not isinstance(reader_object, TableReader):
            raise TypeError("reader_object not of type TableReader")
        raw = reader_object.read()
        if self._has_header:
            self._header = raw[0]
            self._table = raw[1:]
        else:
            self._header = []
            self._table = raw

    def dump(self, writer_object):
        if not isinstance(writer_object, TableWriter):
            raise TypeError("writer_object not of type TableWriter")
        writer_object.write(self._prep_ausgabe())


 #-------------------------------------------
 # Anwendung
t = Tabelle(has_header=True)
t.load(CsvReader(r"E:\Workspaces\Kurse\aktueller-kurs\Tag4\uebungen\bsp.csv"))
#t.load(DummyReader())
print(t.header())
print(t.row(0))
print(t.cell(0, "Ort"))
print(t.cell(0, 0))
print(t.header_count())
print(t.row_count())
t.dump(FileWriter("table_dump.txt"))
t.dump(ConsoleWriter())