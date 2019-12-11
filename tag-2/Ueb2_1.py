import random

lose = list(range(1, 50))

for i in range(6):
    zahl = random.choice(lose)
    print(zahl)
    lose.remove(zahl)
print(lose)


for n in range(10):
    l = random.sample(range(1,50), 6)
    print(l)