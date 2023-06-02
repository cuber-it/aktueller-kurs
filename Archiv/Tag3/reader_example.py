import pandas as pd

class _ReaderBase:
    def __init__(self, fname):
        self._data = None
        self._fname = fname

    def get_csv(self):
        return self._data.to_csv()

    def read(self):
        raise Exception("must be implemented in derived class!")

class CsvReader(_ReaderBase):
    def read(self):
        self._data = pd.read_csv(self._fname)
        return self

class JsonReader(_ReaderBase):
    def read(self):
        self._data = pd.read_json(self._fname)
        return self


d1 = CsvReader(r"E:\Workspaces\Kurse\aktueller-kurs\Material\HistoricalQuotes.csv").read().get_csv()
d2 = JsonReader(r"E:\Workspaces\Kurse\aktueller-kurs\Material\config.json").read().get_csv()

print(d1)
print(d2)
