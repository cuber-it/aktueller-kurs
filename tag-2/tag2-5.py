def f1(a, *args):
    print(a)
    for n in args:
        print(n)
    print("-"*5)

def f2(a, **kwargs):
    print(a)
    for k, v in kwargs.items():
        print("{} {}".format(k, v))
    print("-"*5)

def f3(a, *args, **kwargs):
    print(a)
    for n in args:
        print(n)
    for k, v in kwargs.items():
        print("{} {}".format(k, v))

def f4(a, b="B", **kwargs):
    print(a)
    print(b)
    for k, v in kwargs.items():
        print("{} {}".format(k, v))

f1(1)
f1(1, 2, 3, 4, 5, 6)
f2(1, b=2, c=3, d=4)
f3(1, 2, 3, 4, 5, 6,  b=2, c=3, d=4)
f4(1, b="Daddel", x=2, c=3, d=4)