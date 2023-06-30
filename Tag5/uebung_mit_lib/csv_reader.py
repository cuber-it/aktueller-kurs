from table_reader import TableReader

class CsvReader(TableReader):
    def __init__(self, fname, delim=","):
        self._fname = fname
        self._delim = delim

    def read(self):
        with open(self._fname) as fd:
            return [row.split(self._delim) for row in fd.read().splitlines()]
