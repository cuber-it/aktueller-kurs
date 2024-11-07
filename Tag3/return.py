def f1():
    print("in f1")
    return [1,2,3]

f1()
x = f1()
print(x)

def f2(*werte):
    return werte

x = f2(1,2,3,4)
print(x)

def f3(a, b, c):
    if a > b:
        return c
    if a > c:
        return b
    return a

def f4(a, b, c):
    result = a
    if a > b:
        result = c
    if a > c:
        result = b
    return result