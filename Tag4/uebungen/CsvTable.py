class CsvTable:
    def __init__(self, delim=","):
        self._data = []
        self._delim = delim
        self._header = []
        self._table = []

    def load(self, fname):
        with open(fname) as fd:
            raw = [row.split(self._delim) for row in fd.read().splitlines()]
        self._header = raw[0]
        self._table = raw[1:]
        return self

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

    def cell(self, row_number, column_name):
        row = self.row(row_number)
        col = self._header.index(column_name)
        if col < 0:
            raise IndexError(f"table has no {column_name} column")
        return { column_name: row[col], "col_index": col }

    def search(self, value, what='row_wise'):
        if what == 'row_wise':
            pass
        elif what == 'col_wise':
            pass

    def dump(self):
        return [self._header] + self._table

    def __str__(self):
        return str(self.dump())

if __name__ == "__main__":
    t = CsvTable()
    t.load(r"E:\Workspaces\Kurse\aktueller-kurs\Tag4\uebungen\bsp.csv")
    print(t.header())
    print(t.row(0))
    print(t.cell(0, "Ort"))
    print(t.header_count())
    print(t.row_count())
    print(t.dump())
    print(t)
