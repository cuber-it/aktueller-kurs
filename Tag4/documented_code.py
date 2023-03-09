import random

class LottoEngine:
    """
    Eine Engine für Lottospiele
    """
    def __init__(self, tipp = None):
        """
        Initializes a new instance of the LottoEngine class.

        :param eingabe: optional list of user einput aka "tipp"
        """
        if tipp != None:
            self._tipp = self._verify(tipp)
        else:
            self._tipp = []
        self._ziehung = []
        self._ergebnis = None

    def _analyze(self):
        # Analyzes the user's input and the random drawing, and stores the intersection of both sets in _ergebnis.
        self._ergebnis = list(set(self._tipp).intersection(set(self._ziehung)))

    def _verify(self, eingabe):
        """
        Verifies the user's input by checking the length, duplicates, and range of the numbers.
        :param eingabe: A list of integers representing the user's input.
        """
        self._tipp = [int(n) for n in eingabe]
        if len(self._tipp) != 6:
            raise Exception("wrong number of digits")
        if len(set(self._tipp)) != 6:
            raise Exception("duplicates detected")
        for n in self._tipp:
            if n < 1 or n > 49:
                raise Exception("illegal values detected")

    def _shuffle(self):
        """
        Shuffles the numbers from 1 to 49 and stores the first 6 numbers in _ziehung.
        """
        self._ziehung = random.sample(range(1,50), 6)

    def play(self):
        """
        Plays the lotto game by shuffling the numbers and analyzing the result.
        :return: The current instance of the LottoEngine class.
        """
        self._shuffle()
        self._analyze()
        return self

    def write(self, writer):
        """
        Writes the user's input, the random drawing, and the intersection of both sets to the given writer object.
        :param writer: An object that has a write() method that accepts three parameters (tipp, ziehung, ergebnis).
        :return: The current instance of the LottoEngine class.
        """
        writer.write(self._tipp, self._ziehung, self._ergebnis)
        return self

    def read(self, reader):
        """
        Reads the user's input from the given reader object and verifies it.
        :param reader: An object that has a read() method that returns a list of integers representing the user's input.
        :return: The current instance of the LottoEngine class.
        """
        self._verify(reader.read())
        return self
