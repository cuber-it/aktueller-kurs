class X:
    def __init__(self, wert):
        self._wert = wert

    def __eq__(self, other):
        if self._wert == other._wert:
            return True
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def _hidden(self):
        print("Hidden")

    def __private(self):
        print("Private")

    def machwas(self):
        self._hidden()
        self.__private()

x1 = X("22")
x2 = X(22)

print(x1 == x2)

x1._hidden() # bitte nicht!
#x1.__private() # auch nicht austricksen, bitte!!

x1.machwas()
