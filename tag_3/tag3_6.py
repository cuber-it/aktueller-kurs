def f(*args):
    for a in args:
        print(a)


f()
f(1)
f(1, 2)
f("a", 2, 3, "fgdfgdfg", ["sdfgdfg", 3])


def f2(**kwargs):
    for k, v in kwargs.items():
        print("{} -> {}".format(k, v))


f2()
f2(Param1=4711)
f2(P1=2, p2=3)
