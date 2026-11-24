"""Referenzlösung: Sechs verschiedene Zahlen aus 1 bis 49 ziehen."""

import random

tipp = set()
while len(tipp) < 6:
    tipp.add(random.randint(1, 49))

print("Tipp:", sorted(tipp))
