def stdout(text):
    print("Ausgabe:", text)

def fileout(text):
    with open("ausgabe.txt", "w") as fd:
        print(text, file=fd)

def berechne(a, b, out=None):
    e = a + b
    if out:
        out(f"Ergebnis: {a} + {b} = {e}")
    return a, b, e

print(berechne(1, 2))
berechne(3, 4, stdout)
berechne(5,6, fileout)


def verify(x):
    return x > 0

daten = [1,-1,1,-1,-1,1]
print(list(map(verify, daten)))
print(list(filter(verify, daten)))

print(list(map(lambda x: x > 0, daten)))
print(list(filter(lambda x: x > 0, daten)))

verify = lambda x: x > 0

print(list(map(verify, daten)))
print(list(filter(verify, daten)))
