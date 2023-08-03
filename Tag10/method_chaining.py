class Skript:
    def __init__(self, a, b):
        self._a = a
        self._b = b

    def multiply(self, x, y):
        self._a *= x
        self._b *= y
        return self
        # ohne Möglichkeit des Chainings, als alternative: return (self._a, self._b)

    def add(self, x, y):
        self._a += x
        self._b += y
        return self

    def values(self):
        return self._a, self._b

s1 = Skript(0,0)
s2 = Skript(10, 10)

e = s2.multiply(5, 6).add(3,4).multiply(2,-1).values()
print(e)
