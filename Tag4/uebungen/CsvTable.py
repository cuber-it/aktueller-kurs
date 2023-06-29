class CsvTable:
    def __init__(self, delim=","):
        self._data = []
        self._delim = delim

    def load(self, fname):
        pass

    def header_count(self):
        return

    def header(self):
        return []

    def row(self, row_number):
        return []

    def row_count(self):
        return

    def cell(self, row_number, column_name):
        return { }

    def dump(self):
        return [] # gibt Liste von Listen zurück

    def __str__(self):
        return ""

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
