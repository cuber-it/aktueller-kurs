class TableReader:
    def read(self):
        return None

class TableWriter:
    def write(self, data):
        pass

class Tabelle:
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

    def header(self): # TODO: Seltsames Verhalten beim Aufruf - siehe Tests - PRÜFEN!!
        return self._header.copy()

    def change_header(self, new_header):
        if self._has_header:
            self.header = new_header
            return self
        else:
            raise AttributeError("Table has no dedicated headers")

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

if __name__ == "__main__": #ein paar Tests - simpel und nicht "normiert", im Grunde Bastelei
    class DummyData(TableReader): # Testdaten-Mock
        def read(self):
            return [
                [1,2,3],
                [4,5,6],
                [7,8,9]
            ]

    class DummyWriter(TableWriter): # Mock für Ausgabe
        def write(self, data):
            print(data)

    # Tests - noch ohne unittest-Bibliothek
    t1 = Tabelle()
    t1.load(DummyData())
    t1.dump(DummyWriter())
    t1_str = str(t1)
    print(t1_str == "[[1, 2, 3], [4, 5, 6], [7, 8, 9]]")

    t2 = Tabelle(has_header=True)
    t2.load(DummyData())
    t2.dump(DummyWriter())
    t2_str = str(t2)
    print(t2_str == "[[1, 2, 3], [4, 5, 6], [7, 8, 9]]")
