l = [("a", 1), ("b", 2), ("c", 3)]

d = dict(l)
print(d)

h = ["ID", "PLZ", "Ort", "Werte"]
v = ["12345", "22559", "Hamburg", (1,2,3,4,5)]

l = zip(h, v)
print(l)
d = dict(l) # oder kürzer: dict(zip(h, v))
print(d)

l2 = list(d)
print(l2)

l2 = list(d.items())
print(l2)

def unzip(l):
    l1 = []
    l2 = []
    for v in l:
        l1.append(v[0])
        l2.append(v[1])
    return l1, l2

h, v = unzip(l2)

print(h)
print(v)
