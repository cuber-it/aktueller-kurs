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

# TODO:
# sub, mul div modulo
# reset
# properties für a, b, e : wert_a, wert_b, ergebnis
#
# -> 8 methoden und properties
# => mindestens!!! 8 tests <- good cases
# Testfrage: verhalten bei div durch 0 z.B?
# Testfrage: Verhalten bei Übergabe von nicht numbers?
