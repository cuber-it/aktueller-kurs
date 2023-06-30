from table_writer import TableWriter

class ConsoleWriter(TableWriter):
    def write(self, daten):
        for row in daten:
            print(row)
