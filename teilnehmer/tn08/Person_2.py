class Person:
    def __init__(self, name, plz=None, ort=None, strasse=None):
        self.set_values(name, plz, ort, strasse)
       
    def get_values(self):
        return self.name, self.plz, self.ort, self.strasse

    def set_values(self, name=None, plz=None, ort=None, strasse=None):
        self.name = name 
        self.plz = plz
        self.ort = ort
        self.strasse = strasse




if __name__ == "__main__":
    p1 = Person("Willi")
    p2 = Person("Heinz", strasse="Erlenweg")

    p_list = []
    for n in "Willi", "heinz", "karl":
        p_list.append(Person(n))

    print(p1.name, p1.strasse)
    print(p2.name, p2.strasse)

    for p in p_list:
        print(p.get_values())

    p1.set_values("Heinz", "22765", "HH", strasse="Museumstr")
    print(p1.get_values())

