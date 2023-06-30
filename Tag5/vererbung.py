class Basis:
    def __init__(self, name):
        self.value = None
        self.name = name

    def get_value(self):
        return self.value

    def get_name(self):
        return self.name

class Kind(Basis):
    def __init__(self, value=None, data=None):
        super().__init__("Kind")

        self.value = value
        self.data = data

    def set_value(self, value):
        self.value = value

    def set_data(self, value):
        self.data = value

    def get_value(self):
        return self.data * super().get_value()

# b = Basis()
# print(b.get_value())

k = Kind(1234, 500)
print(k.get_value())
k.set_value(99)
print(k.get_value())
print(k.get_name())
#print(b.get_value())
