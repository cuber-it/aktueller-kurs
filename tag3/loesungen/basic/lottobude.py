"""Referenzlösung: Sechs verschiedene Zahlen aus 1 bis 49 ziehen."""

import random

tipp = set()
while len(tipp) < 6:
    tipp.add(random.randint(1, 49))

print("Tipp:", sorted(tipp))

# Kürzer, als Liste nicht Set mit eingebauter Funktion von random
tipp = random.sample(range(1,50), 6)

print("Tipp:", sorted(tipp))

# Langform
tipp = []
while len(tipp) < 6:
    zahl = random.randint(1,49)
    if zahl not in tipp:
        tipp.append(zahl)

print("Tipp:", sorted(tipp))
