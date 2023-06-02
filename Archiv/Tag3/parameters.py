def machwas(x, *, a=1234): # * erzwingt namend parameters und deren Aufruf zusammen mit dem Namen
    pass

machwas(4711)
machwas(4711, a=1234)

def tuwas(a, b=None):
    pass

tuwas(1)
tuwas(1, 2)
tuwas(1, b=2)
tuwas(b=2, a=1)
