"""
Modulbeschreibung
"""
class Tabelle:
    """
    A class to manage table data. This class does not handle any input or output operations,
    it only manages the structure and manipulation of table data.

    :param bool has_header: A boolean indicating whether the table has a header. Defaults to False.
    """
    def __init__(self, has_header=False):
        self._header = []
        self._table = []
        self._has_header = has_header

    def __str__(self):
        """
        Returns the string representation of the table data.

        :return: A string representing the table data.
        :rtype: str
        """
        return str(self._prep_ausgabe())

    def _prep_ausgabe(self):
        result = []
        if self._has_header:
            result = [self._header]
        return result + self._table

    def header_count(self):
        """
        Returns the count of table's headers.

        :return: An integer representing the count of table's headers.
        :rtype: int
        """
        return len(self._header)

    def header(self):
        """
        Returns a copy of the table's headers.

        :return: A list representing the table's headers.
        :rtype: list
        """
        return self._header.copy()

    def row(self, row_number, style='simple'):
        """
        Returns a specific row from the table.

        :param int row_number: The index of the row to be returned.
        :param str style: The style of the output. Defaults to 'simple'.
        :return: A list representing the specified row of the table.
        :rtype: list
        :raises IndexError: If the row number is not valid.
        """
        if row_number < 0 or row_number > self.row_count():
            raise IndexError(f"table has only {self.row_count()} rows")
        result = []
        if style == 'simple':
            result = self._table[row_number].copy()
        return result

    def row_count(self):
        """
        Returns the count of table's rows.

        :return: An integer representing the count of table's rows.
        :rtype: int
        """
        return len(self._table)

    def cell(self, row_number, column):
        """
        Returns the content of a specific cell from the table.

        :param int row_number: The index of the row.
        :param int/str column: The index or name of the column.
        :return: A dictionary with one key-value pair. Key is the column name, value is the cell content.
        :rtype: dict
        :raises IndexError: If the column name is not valid.
        :raises AttributeError: If the table does not have dedicated headers and column name is used.
        """
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
        """
        Loads table data from a TableReader object.

        :param TableReader reader_object: The TableReader object from which to load the table data.
        :raises TypeError: If reader_object is not an instance of TableReader.
        """
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
        """
        Writes table data to a TableWriter object.

        :param TableWriter writer_object: The TableWriter object to which to write the table data.
        :raises TypeError: If writer_object is not an instance of TableWriter.
        """
        if not isinstance(writer_object, TableWriter):
            raise TypeError("writer_object not of type TableWriter")
        writer_object.write(self._prep_ausgabe())
