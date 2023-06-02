l = [ "Willi", "Heinz", "Karl", "Karl"]

if len(l) != len(set(l)):
    print("Da ist was doppelt")


l1 = [1, 2, 3, 4]
l2 = [3, 4, 5, 6]
print(set(l1).union(set(l2)))
print(set(l1).intersection(set(l2)))

s1 = set(l1)
s1.add(33)
# geht nicht s1.append(33)
print(s1)

lx = list(s1)
lx.append(44)
s1 = set(lx)
print(s1)
