def f1():
    print("f1")

def f2(p1):
    print("f2", p1)

def f3(p1, p2):
    print("f3", p1, p2)

def f4(p1, p2="X"):
    print("f4", p1, p2)

def f5(p1="1", p2="X"):
    print("f5", p1, p2)





def f6(a, *args):
    print("f6", a)
    for n in args:
        print(n)

def f7(a, **kwargs):
    print("f7", a)
    for k, v in kwargs.items():
        print("{} {}".format(k, v))
    print("-"*5)

def f8(a, *args, **kwargs):
    print("f8", a)
    for n in args:
        print(n)
    for k, v in kwargs.items():
        print("{} {}".format(k, v))

def f9(a, b="B", **kwargs):
    print("f9", a, b)
    for k, v in kwargs.items():
        print("{} {}".format(k, v))

