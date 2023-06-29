class MiscTools:
    # Code der bei Objektanlage ausgefürt wird
    def __init__(self): # Double Underline Method aka "dunder"
        self.daten = []

    # Code der aufgerufen wird, wenn der gc arbeitet - nicht exakt vorherzusagen wann
    def __del__(self):
        print("Entfernt")

    # Code der beim WITH-Block aufgerufen wird
    def __enter__(self):
        return self

    # Code der beim Verlassen des WITH-Blocks aufgerufen wird
    def __exit__(self, type, value, traceback):
        print("Exit")
        #self.__del__()

    # Code der explizit aufgerufen wird
    def build(self, wert):
        self.daten = [ wert ]

    def add_value(self, wert):
        self.daten.append(wert)

    def dump(self):
        print(self.daten)

def mach_was():
    with MiscTools() as o:
        o = MiscTools()
        o.dump()
    print("Block verlassen")
    return "OK"

def tu_was():
    o = MiscTools()

mach_was()
tu_was()
