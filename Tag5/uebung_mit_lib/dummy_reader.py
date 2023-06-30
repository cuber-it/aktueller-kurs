from table_reader import TableReader

class DummyReader(TableReader):
    def read(self):
        return [
            ["Ort", "PLZ"],
            ["HH", "22559"],
            ["HH", "22765"],
            ["WND", "66606"]
        ]
