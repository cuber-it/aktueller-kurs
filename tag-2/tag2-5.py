import random

tipp = []

while len(tipp) < 6:
    zahl = random.randint(1, 49)
    if not zahl in tipp:
        tipp.append(zahl)

print(tipp)