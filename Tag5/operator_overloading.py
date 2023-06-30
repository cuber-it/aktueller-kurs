class Calculon:
    def __init__(self, start_value=0):
        self._acc = str(start_value)

    def __add__(self, value):
        # sieht doof aus, aber ich habe entschieden das so zu implementieren
        # da intern, geht es neimand was an!
        berechnung = int(self._acc) + value
        return Calculon(berechnung)

    def __sub__(self, value):
        berechnung = int(self._acc) - value
        return Calculon(berechnung)

    # Properties für den Zugriff - pythonic style
    @property # sog. Decorator
    def value(self):  # ist ein getter
        return int(self._acc)

    @value.setter # value weil es als property eingeführt würde
    def value(self, value): # ist ein setter
        self._acc = str(value)

#------------------------------------------------------------
c = Calculon()
c = c + 5
print(c.value)

c.value = 0
c = c - 5
print(c.value)
