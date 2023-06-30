from table_writer import TableWriter
from table_reader import TableReader

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
