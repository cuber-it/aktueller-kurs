"""
Modulinfo ...
"""
class Tabelle:
    """
    A class to manage table data. This class does not handle any input or output operations, it only manages
    the structure and manipulation of table data.
    """

    def __init__(self, has_header=False):
        """
        Initializes an instance of the Tabelle class.

        Parameters:
            has_header (bool): A boolean indicating whether the table has a header. Defaults to False.
        """
        self._header = []
        self._table = []
        self._has_header = has_header

    def __str__(self):
        """
        Returns the string representation of the table data.
        """
        return str(self._prep_ausgabe())

    def _prep_ausgabe(self):
        """
        Prepares the table data for output. If the table has a header, it will be included in the output.

        Returns:
            A list representing the table data.
        """
        result = []
        if self._has_header:
            result = [self._header]
        return result + self._table

    def header_count(self):
        """
        Returns the number of headers in the table.

        Returns:
            An integer representing the number of headers in the table.
        """
        return len(self._header)

    def header(self):
        """
        Returns a copy of the table's headers.

        Returns:
            A list representing the table's headers.
        """
        return self._header.copy()

    def row(self, row_number, style='simple'):
        """
        Returns a specific row from the table.

        Parameters:
            row_number (int): The index of the row to be returned.
            style (str): The style of the output. Defaults to 'simple'.

        Returns:
            A list representing the specified row of the table.
        """
        if row_number < 0 or row_number > self.row_count():
            raise IndexError(f"table has only {self.row_count()} rows")
        result = []
        if style == 'simple':
            result = self._table[row_number].copy()
        return result

    def row_count(self):
        """
        Returns the number of rows in the table.

        Returns:
            An integer representing the number of rows in the table.
        """
        return len(self._table)

    def cell(self, row_number, column):
        """
        Returns a specific cell from the table.

        Parameters:
            row_number (int): The row index of the cell to be returned.
            column (int/str): The column index or header name of the cell to be returned.

        Returns:
            A dictionary representing the specified cell of the table.
        """
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

        Parameters:
            reader_object (TableReader): The TableReader object from which to load the table data.

        Raises:
            TypeError: If reader_object is not an instance of TableReader.
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

        Parameters:
            writer_object (TableWriter): The TableWriter object to which to write the table data.

        Raises:
            TypeError: If writer_object is not an instance of TableWriter.
        """
        if not isinstance(writer_object, TableWriter):
            raise TypeError("writer_object not of type TableWriter")
        writer_object.write(self._prep_ausgabe())
