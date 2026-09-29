class Triangle:
    def __init__(self, size: int) -> None:
        self.size = size

    def lines(self) -> list[str]:
        return ["*" * i for i in range(1, self.size + 1)]


class Square:
    def __init__(self, size: int) -> None:
        self.size = size

    def lines(self) -> list[str]:
        return ["*" * self.size] * self.size


class ConsoleOutput:
    def write(self, line: str) -> None:
        print(line)


class ListOutput:
    def __init__(self) -> None:
        self.lines: list[str] = []

    def write(self, line: str) -> None:
        self.lines.append(line)


def draw(shapes, out) -> None:
    """Zeichnet beliebige Formen auf eine injizierte Ausgabe."""
    for shape in shapes:
        for line in shape.lines():
            out.write(line)
        out.write("")


if __name__ == "__main__":
    draw([Triangle(3), Square(2), Triangle(2)], ConsoleOutput())

    buf = ListOutput()                     # z. B. im Test injizieren
    draw([Square(2)], buf)
    assert buf.lines == ["**", "**", ""]
