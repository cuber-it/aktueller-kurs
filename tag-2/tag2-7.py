class ConfigTools:
    def __init__(self, dateiname, autoload=True):
        self._dateiname = dateiname
        if autoload:
            self.load()

    def _read_file(self):
        with open(self._dateiname) as fd:
            return fd.readlines()

    def load(self):
        self._data = {}
        for z in self._read_file()[6:-1]:
            zeile = z.strip().split()
            if len(zeile) == 5:
                self._data[zeile[0]] = {
                    "adm": zeile[1],
                    "opr": zeile[2],
                    "mode": zeile[3],
                    "port": zeile[4],
                    "ipadr": []
                }
                aktrouter = zeile[0]
            elif len(zeile) == 2:
                self._data[aktrouter]["ipadr"].append(zeile)

    def get_first_ip(self, rname):
        return self._data[rname]["ipadr"][0][0]


#-------------------
c = ConfigTools("Routerlist.txt")
print(c.get_first_ip("L0"))
