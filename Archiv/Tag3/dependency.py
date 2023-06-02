import pandas as pd

class Reader:
    def __init__(self, filereader):
        self._data = None
        self._filereader = filereader

    def get_csv(self):
        return self._data.to_csv()

    def read(self):
        self._data = self._filereader.read()
        return self

class CsvReader():
    def __init__(self, fname):
        self._fname = fname

    def read(self):
        return pd.read_csv(self._fname)

class JsonReader():
    def __init__(self, fname):
        self._fname = fname

    def read(self):
        return pd.read_json(self._fname)

d1 = Reader(
    CsvReader(r"E:\Workspaces\Kurse\aktueller-kurs\Material\HistoricalQuotes.csv")
    ).read().get_csv()
d2 = Reader(
    JsonReader(r"E:\Workspaces\Kurse\aktueller-kurs\Material\config.json")
    ).read().get_csv()

print(d1)
print(d2)
