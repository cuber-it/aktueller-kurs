class Box[T]:
    def __init__(self, value: T, label: str = "") -> None:
        self.value = value
        self.label = label

    def __repr__(self) -> str:
        return f"{type(self).__name__}(value={self.value!r}, label={self.label!r})"

    def __str__(self) -> str:
        return f"{self.label}: {self.value}" if self.label else str(self.value)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Box):
            return NotImplemented
        return (self.value, self.label) == (other.value, other.label)

    __hash__ = None  # mutable + __eq__ → nicht hashbar


b1 = Box(42, "Antwort")
b2 = Box(42, "Antwort")
print(repr(b1))   # Box(value=42, label='Antwort')
print(b1)         # Antwort: 42
print(b1 == b2)   # True
