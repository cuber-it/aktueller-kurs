class Calculator:
    def __init__(self, a=0, b=0):
        self._a = a
        self._b = b
        self._e = None

    def __str__(self):
        return f"{self._a} {self._b} {self._e}"

    def add(self):
        self._e = self._a + self._b
        return self
