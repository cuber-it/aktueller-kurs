import shinx_documentation as engine_1
import typehinting as engine_2

lb = engine_1.LottoEngine()
lb = engine_2.LottoEngine()

class Reader:
    def read(self):
        return [1,2,3,4,5,6]

class Writer:
    def write(self, a, b, c):
        print(a)
        print(b)
        print(c)


lb.read(Reader()).play().write(Writer())
