"""Referenzlösung: Einen festen Tipp mit einer zufälligen Ziehung vergleichen."""

import random

tipp = {7, 13, 19, 23, 31, 42}
ziehung = set(random.sample(range(1, 50), 6))
treffer = tipp & ziehung

print("Tipp:", sorted(tipp))
print("Ziehung:", sorted(ziehung))
print("Richtige:", sorted(treffer))
print("Treffer:", len(treffer))
