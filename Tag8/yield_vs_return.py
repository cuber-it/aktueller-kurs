def mit_return(max):
    print("mit return")
    return list(range(0, max))

def mit_yield(max):
    print("mit yield")
    for n in list(range(0, max)):
        print("neuer wert ...")
        yield n

for _ in mit_return(10):
    print(_)

for _ in mit_yield(10):
    print(_)
