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

    # Java style - nicht so gut
    # Gewinn: intern können die Daten vorliegen wie sie wollen# der Bentzer bekommt immer int bzw kann immer int geben
    def set_value(self, value):
        self._acc = str(value)

    def get_value(self):
        return int(self._acc)


c = Calculon()
c.add(5)
print(c.get_value())

c.set_value(0)
c.sub(5)
print(c.get_value())
