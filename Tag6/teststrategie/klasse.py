class Calculator:
    def __init__(self, a=0, b=0):
        self._type_check(a, "invalid input")
        self._type_check(b, "invalid input")

        self._a = a
        self._b = b
        self._e = None

    def __str__(self):
        return f"{self._a} {self._b} {self._e}"

    def _type_check(self, value, msg="invalud type"):
        if not isinstance(value, int):
            raise TypeError(f"{msg} {value}")

    @property
    def wert_a(self):
        return self._a

    @wert_a.setter
    def wert_a(self, wert):
        self._type_check(wert, "invalid input")
        self._a = wert

    @property
    def wert_b(self):
        return self._b

    @wert_b.setter
    def wert_b(self, wert):
        self._type_check(wert, "invalid input")
        self._b = wert

    @property # readonly, no setter!
    def ergebnis(self):
        return self._e

    def add(self):
        self._e = self._a + self._b
        return self

    def sub(self):
        self._e = self._a - self._b
        return self

    def mul(self):
        pass

    def div(self):
        self._e = int(self._a / self._b)
        return self

    def modulo(self):
        pass

    def reset(self):
        pass



# TODO:
# sub, mul div modulo
# reset
# properties für a, b, e : wert_a, wert_b, ergebnis
#
# -> 8 methoden und properties
# => mindestens!!! 8 tests <- good cases
# Testfrage: verhalten bei div durch 0 z.B?
# Testfrage: Verhalten bei Übergabe von nicht numbers?
