class StockValues:
    def __init__(self, stock_name, source_file):
        self._name = stock_name
        self._filename = source_file
        self._data = []

    def read(self):
        self._data = self._read_csv()
        return self

    def _read_csv(self):
        pass

    def __str__(self):
        ausgabe = f"Daten für: {self._name}\n"
        if len(self._data) == 0:
            ausgabe += "- keine Daten gelesen"
        else:
            for zeile in self._data[:5]:
                ausgabe += str(zeile) + "\n"
        return ausgabe

    def __repr__(self):
        return f"StockValues(\"{self._name}\", \"{self._filename}\")"



x = StockValues("aapl", "daten.csv")

print(x)
print(str(x))

print(repr(x))
