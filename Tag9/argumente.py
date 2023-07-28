def tu_was(wert, *, a=..., b=..., c=...):
    print(wert)
    #print(args)
    #print(kwargs)


    if a:
            print("Gefunden: ", a)
    if b:
            print("Gefunden: ", b)
    if c:
            print("Gefunden: ", c)


def mach_was(wert, *args, **kwargs):
    print(wert)
    print(args)
    print(kwargs)

    if not kwargs: # Anlage von default Werten
        kwargs = dict(a=0, b=0, c=0)

    if kwargs:
        if "a" in kwargs:
            print("Gefunden: ", kwargs["a"])
        elif "b" in kwargs:
            print("Gefunden: ", kwargs["b"])
        elif "c" in kwargs:
            print("Gefunden: ", kwargs["c"])
        else:
            print("keine validen Werte gefunden")



mach_was(42)
print("-"*80)
mach_was(42, 1, 2, 3)
print("-"*80)
mach_was(42, 1, 2, 3, a=10, b=11, c=12)
print("-"*80)
mach_was(42, 1, 2, 3, d=13)
print("-"*80)
tu_was(43, a=99, c=101)
