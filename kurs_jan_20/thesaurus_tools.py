class Thesaurus:

    def __init__(self, fname):
        self._fname = fname
        self._daten = None

    def _prepare(self, roh):
        neu = []
        for z in roh:
            if not z.startswith("#"):
                neu.append(z)
        return neu

    def load(self):
        roh = []
        with open(self._fname) as fd:
            roh = fd.read().split("\n")
        self._daten = self._prepare(roh)

    def search(self, what):
        pass

    def get(self):
        return self._daten



#--------------------------------------
t = Thesaurus("openthesaurus.txt")
t.load()
# print(t.search("Kernspaltung"))
for z in t.get():
    print(z)