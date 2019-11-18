import random
lose = list(range(1, 50))

for i in list(range(6)):
    zahl = random.choice(lose)
    print(zahl)
    lose.remove(zahl)
print(lose)


print(
    random.sample(
        list(
            range(1, 50)), 6)
    )




