class Integer:
    def __init__(self, value: int) -> None:
        self._value = self._validate(value)

    @property
    def value(self) -> int:
        return self._value

    @value.setter
    def value(self, value: int) -> None:
        self._value = self._validate(value)

    def add(self, value: int) -> None:
        self._value = self._validate(self._value + value)

    @staticmethod
    def _validate(value: int) -> int:
        if value <= 0:
            raise ValueError(f"value must be positive, got {value}")
        return value
