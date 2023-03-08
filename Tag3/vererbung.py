class Basis:
    def __init__(self, wert):
        self.kram = wert

    def _wasanderes(self):
        print("WAS ANDERES")

    def __nichtsichtbar(self):
        print("NICHT SICHTBAR")

    def tuwas(self):
        print(self.__class__, "tuwas", self.kram)

class Kind(Basis):
    # nur wenn ich im Kind einen anderen Init haben will, sonst halt so wie es Basis erwartet
    #def __init__(self):
    #    super().__init__("ABCD")

    def machwas(self):
        print(self.__class__, "machwas", self.kram)
        # hidden wird vererbt
        self._wasanderes()
        # wurde nicht offiziell mit vererbt
        #self.__nichtsichtbar()

    def tuwas(self): # überdeckt das geerbte tuwas
        print("Spezial-tuwas", self.__class__, self.kram)
        # aber ich will auch das geerbte noch mitnutzen!
        super().tuwas()


#print("Basis:", dir(Basis))
#print("Kind: ", dir(Kind))

Basis(1234).tuwas()
Kind("ABCD").tuwas()
Kind("XYZ").machwas()
