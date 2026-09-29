class Integer:
    def __init__(self, value: int) -> None:
        self.value = value          # läuft über den Setter

    @property
    def value(self) -> int:
        return self._value

    @value.setter
    def value(self, value: int) -> None:
        if value <= 0:
            raise ValueError(f"value must be positive, got {value}")
        self._value = value

    def add(self, value: int) -> None:
        self.value += value         # Ergebnis wird ebenfalls geprüft
