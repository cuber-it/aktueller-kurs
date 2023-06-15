def a():
    return("Funktion a")

def b(a):
    return("Funktion b:", a)

def c(a, b):
    return("Funktion c:", a, b)

def d(a, b="Optionaler Text"):
    return("Funktion d:", a, b)


def e(a, b=None, c=""):
    return("Funktion e:", a, b, c)

def f(a, *b):
    if a not in ["add", "mul"]:
        raise "Unknown Command"

    result = None

    if len(b) > 0:
        result = b[0]
        for n in b[1:]:
            if(a == "mul"):
                result *= n
            elif a == "add":
                result += n
    return result

def g(a, **b):
    pass

def h(a, *b, **c):
    pass

def i(a, b=None, *c, **d):
    print(a)
    print(b)
    print(c)
    print(d)

print(f("add", 1, 2, 3, 4, 5) )


i(42, "HUHU", 1, 2, 3, name="Willi", ort="HH")
