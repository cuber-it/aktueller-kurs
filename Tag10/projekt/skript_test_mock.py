class SourceMock:
    def request(self, type):
        if type == "values":
            return 10, 100
