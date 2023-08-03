class Skript:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_values(self):
        return (self.a, self.b)

    def set_values(self, source):
        v = source.request("values")
        self.a, self.b = v

    def multiply(self, x, y):
        self.a *= x
        self.b *= y
