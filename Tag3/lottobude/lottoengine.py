import random

class LottoEngine:
    def __init__(self):
        self._tipp = []
        self._ziehung = []
        self._ergebnis = None

    def _analyze(self):
        self._ergebnis = list(set(self._tipp).intersection(set(self._ziehung)))

    def _verify(self, eingabe):
        self._tipp = [int(n) for n in eingabe]
        if len(self._tipp) != 6:
            raise Exception("wrong number of digits")
        if len(set(self._tipp)) != 6:
            raise Exception("duplicates detected")
        for n in self._tipp:
            if n < 1 or n > 49:
                raise Exception("illegal values detected")

    def _shuffle(self):
        self._ziehung = random.sample(range(1,50), 6)

    def play(self):
        self._shuffle()
        self._analyze()
        return self

    def write(self, writer):
        writer.write(self._tipp, self._ziehung, self._ergebnis)
        return self

    def read(self, reader):
        self._verify(reader.read())
        return self
