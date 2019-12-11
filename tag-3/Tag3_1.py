class Incr:
    '''
    Incr: Klasse zum Inkrementieren
    '''
    def __init__(self, wert):
        '''
        Initialisierung

        Legt Startwert fest

        @params: wert - integer
        @returns: object
        '''
        self._wert = wert

    def set(self, wert):
        self._wert = wert

    def get(self):
        return self._wert

    def calc(self):
        self._wert += 1

#-----------------------------------
i1 = Incr(1000)
#i1.set(1000)

i2 = Incr(100)
#i2.set(100)

for n in range(100):
    i1.calc()
    i2.calc()

print(i1.get())
print(i2.get())
