class Reader:
    def __init__(self, prompt, delim=","):
        self._prompt = prompt
        self._delim = delim

    def read(self):
        eingabe = input(self._prompt)
        return eingabe.split(self._delim)
