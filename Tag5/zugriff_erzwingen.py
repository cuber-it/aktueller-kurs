class Calculon:
    def __init__(self, start_value=0):
        self.__acc = start_value

    def add(self, value):
        self.__acc += value

    def sub(self, value):
        self.__acc -= value


c = Calculon()
c.add(5)
print(c._Calculon__acc) # Mist!!!

c._Calculon__acc = 0 # Mist!!!
c.sub(5)
print(c._Calculon__acc) # Mist!!!
