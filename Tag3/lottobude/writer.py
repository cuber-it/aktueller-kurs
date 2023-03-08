class Writer:
    def __init__(self, prompt):
        self._prompt = prompt

    def write(self, tipp, ziehung, ergebnis):
        print(self._prompt)
        print("Tipp:    ", sorted(tipp))
        print("Ziehung: ", sorted(ziehung))
        print("Ergebnis:", len(ergebnis), ergebnis)
