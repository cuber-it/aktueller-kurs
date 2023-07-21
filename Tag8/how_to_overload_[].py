class MyClass:
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        if key in self.data:
            return self.data[key]
        else:
            raise KeyError(f"No such key '{key}' in the data")

    def __setitem__(self, key, value):
        self.data[key] = value

# usage
my_object = MyClass()
my_object['key'] = 'value'  # This calls __setitem__
print(my_object['key'])     # This calls __getitem__
