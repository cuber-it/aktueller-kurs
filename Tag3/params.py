def f1():
    return

def f2(a: str, b: int, c: float) -> str:
    print(a, b, c)

def f3(a, b=5, c=None, d="Hello"):
    print(a, b, c, d)

def f4(a=None, b=None, c=None):
    print(a, b, c)

f1()
f2("a", 1, 1.1)
f3("a", 10)
f3("B")
f3("P", 44)
f4()
f4(1, 2, 3)
f4(1, None, 3)
f4(a=1, c=3)
f4(1, 3)
f4(c=3, b=2, a=1)