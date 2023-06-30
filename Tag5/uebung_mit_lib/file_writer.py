from table_writer import TableWriter

class FileWriter(TableWriter):
    def __init__(self,fname):
        self._fname = fname

    def write(self, daten):
        with open(self._fname, "w") as fd:
            for row in daten:
                row = str(row)[1:-1]
                print(row, file=fd)
