def f1(**kwargs):
    for k,v in kwargs.items():
        print(k, v)

f1()
# failt->f1(1)
f1(wert=1)

def f2(a, b=None, c=99, *d, **e):
    print(a, b, c)
    print(d)
    print(e)

f2("Pflicht")
