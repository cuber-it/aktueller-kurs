def mach_was(wert, ergaenzung=None, nochwas=10):
    print(wert)
    if ergaenzung:
        print("Ergänzung:", ergaenzung)
    print("Nochwas:", nochwas)
    return True

mach_was(4711)
mach_was(4711, 12)
mach_was(4711, 12, 99)

mach_was(wert=99)
mach_was(wert=99, ergaenzung=10)
mach_was(ergaenzung=10, wert=99)

mach_was(wert=1, nochwas=1000)

# mit Hilfe von * erzwinge ich named parameters:
def mach_was(wert, *, ergaenzung=None, nochwas=10):
    print(wert)
    if ergaenzung:
        print("Ergänzung:", ergaenzung)
    print("Nochwas:", nochwas)
    return True

mach_was(4711)
mach_was(4711, ergaenzung=12)
mach_was(4711, ergaenzung=12, nochwas=99)
