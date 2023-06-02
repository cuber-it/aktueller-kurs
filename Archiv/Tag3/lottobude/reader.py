class Reader:
    def __init__(self, eingabe, delim=","):
        self._eingabe = eingabe
        self._delim = delim

    def read(self):
        return self._eingabe.split(self._delim)
