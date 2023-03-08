class Reader:
    def __init__(self, fname, delim=","):
        self._fname = fname
        self._delim = delim

    def read(self):
        with open(self._fname) as fd:
            yield fd.readline().split(self._delim)
