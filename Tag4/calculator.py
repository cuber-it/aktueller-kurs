class CalcException(Exception):
    pass

class Calc:
    def __init__(self, a, b):
        self.set(a, b)
        self.reset()

    def get_numbers(self):
        return self._a, self._b

    def get_result(self):
        return self._r

    def add(self):
        self._r = self._a + self._b
        return self

    def set(self, a, b):
        error = False
        try:
            self._a = float(a)
            self._b = float(b)
        except ValueError:
            raise CalcException("Das war wohl nix!")
        return self

    def reset(self):
        self._r = None
        return self
