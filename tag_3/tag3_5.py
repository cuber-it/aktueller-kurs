n = [ "Willi", "Heinz", "Karl"]
w = [ 1, 2, 3]

d = dict(zip(n, w))

print(d)
print(d["Willi"])

import string
n = [z for z in string.ascii_lowercase]
w = [None] * len(n)
d = dict(zip(n, w))
print(d)

d = dict(zip([z for z in string.ascii_lowercase], [None]*24))

