class Daten:
    def __init__(self):
        self._werte = []
        self._texte = []
        self._floats = []

    def init_floats(self, *floats):
        for f in floats:
            assert isinstance(f, float), "Illegal input"
        self._floats += floats
        return self


    def init_werte(self, *werte):
        for w in werte:
            assert isinstance(w, int), "Illegal input"
        self._werte += werte
        return self

    def init_texte(self, *texte):
        for w in texte:
            assert isinstance(w, str), "Illegal input"
        self._texte += texte
        return self

    def init(self, *daten):
        for d in daten:
            if isinstance(d, str):
               self._texte.append(d)
            elif isinstance(d, int):
                self._werte.append(d)
            elif isinstance(d, float):
                self._floats.append(d)
            else:
                raise TypeError("illegal valaue")
        return self

    def values(self):
        return self._texte, self._werte, self._floats


d1 = Daten().init_texte("a", "b")
d2 = Daten().init_werte(1, 2)
d3 = Daten().init_texte("a", "b").init_werte(1, 2)
d4 = Daten().init_texte("a").init_werte(1)
d5 = Daten().init(1, 1, 1, "a", "b").init_werte(55)

print(d1.values())
print(d2.values())
print(d3.values())
print(d4.values())
print(d5.values())
