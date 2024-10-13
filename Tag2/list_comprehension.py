fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

def fruitfilter_b(filter, source):
    return [x for x in source if filter in x]

def fruitfilter_a(filter, source):
    newlist = []

    for x in source:
        if filter in x:
            newlist.append(x)
    return newlist

print(fruitfilter_a("a", fruits))
print(fruitfilter_b("a", fruits))