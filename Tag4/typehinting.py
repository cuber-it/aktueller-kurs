import random
from typing import List, Tuple, Union

class LottoEngine:
    """
    A class that represents a lotto game engine.

    Attributes:
        _tipp (List[int]): A list of integers representing the user's input.
        _ziehung (List[int]): A list of integers representing the random drawing.
        _ergebnis (List[int]): A list of integers representing the intersection of _tipp and _ziehung.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the LottoEngine class.
        """
        self._tipp: List[int] = []
        self._ziehung: List[int] = []
        self._ergebnis: Union[None, List[int]] = None

    def _analyze(self) -> None:
        """
        Analyzes the user's input and the random drawing, and stores the intersection of both sets in _ergebnis.
        """
        self._ergebnis = list(set(self._tipp).intersection(set(self._ziehung)))

    def _verify(self, eingabe: List[int]) -> None:
        """
        Verifies the user's input by checking the length, duplicates, and range of the numbers.

        Args:
            eingabe (List[int]): A list of integers representing the user's input.

        Raises:
            Exception: If the input has an incorrect number of digits, duplicates, or illegal values.
        """
        self._tipp = [int(n) for n in eingabe]
        if len(self._tipp) != 6:
            raise Exception("wrong number of digits")
        if len(set(self._tipp)) != 6:
            raise Exception("duplicates detected")
        for n in self._tipp:
            if n < 1 or n > 49:
                raise Exception("illegal values detected")

    def _shuffle(self) -> None:
        """
        Shuffles the numbers from 1 to 49 and stores the first 6 numbers in _ziehung.
        """
        self._ziehung = random.sample(range(1,50), 6)

    def play(self) -> 'LottoEngine':
        """
        Plays the lotto game by shuffling the numbers and analyzing the result.

        Returns:
            LottoEngine: The current instance of the LottoEngine class.
        """
        self._shuffle()
        self._analyze()
        return self

    def write(self, writer: object) -> 'LottoEngine':
        """
        Writes the user's input, the random drawing, and the intersection of both sets to the given writer object.

        Args:
            writer (object): An object that has a write() method that accepts three parameters (tipp, ziehung, ergebnis).

        Returns:
            LottoEngine: The current instance of the LottoEngine class.
        """
        writer.write(self._tipp, self._ziehung, self._ergebnis)
        return self

    def read(self, reader: object) -> 'LottoEngine':
        """
        Reads the user's input from the given reader object and verifies it.

        Args:
            reader (object): An object that has a read() method that returns a list of integers representing the user's input.

        Returns:
            LottoEngine: The current instance of the LottoEngine class.

        Raises:
            Exception: If the input has an incorrect number of digits, duplicates, or illegal values.
        """
        self._verify(reader.read())
        return self
