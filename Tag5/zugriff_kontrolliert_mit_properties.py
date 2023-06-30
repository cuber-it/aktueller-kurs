class Calculon:
    def __init__(self, start_value=0):
        self._acc = str(start_value)

    def add(self, value):
        # sieht doof aus, aber ich habe entschieden das so zu implementieren
        # da intern, geht es neimand was an!
        berechnung = int(self._acc) + value
        self._acc = str(berechnung)

    def sub(self, value):
        berechnung = int(self._acc) - value
        self._acc = str(berechnung)

    # Properties für den Zugriff - pythonic style
    @property # sog. Decorator
    def value(self):  # ist ein getter
        return int(self._acc)

    @value.setter # value weil es als property eingeführt würde
    def value(self, value): # ist ein setter
        self._acc = str(value)


c = Calculon()
c.add(5)
print(c.value)

c.value = 0
c.sub(5)
print(c.value)
