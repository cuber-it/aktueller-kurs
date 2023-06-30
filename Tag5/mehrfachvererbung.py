class BasisA:
    def machwas(self):
        print("Machwas")

class BasisB:
    def tuwas(self):
        print("Tuwas")

class BasisC:
    def machwas(self):
        print("Aloha")

class KindA(BasisC, BasisB, BasisA):
    pass

class KindB(BasisA, BasisB, BasisC):
    pass


#b1 = BasisA()
#b1.machwas()

#b2 = BasisB()
#b2.tuwas()

k1 = KindA()
k1.machwas()
k1.tuwas()

k2 = KindB()
k2.machwas()
k2.tuwas()
