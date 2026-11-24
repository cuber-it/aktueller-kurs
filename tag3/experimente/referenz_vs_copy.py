# Experiment – Äußere und verschachtelte Listen kopieren
# Eine flache Kopie teilt die inneren Listen weiterhin mit dem Original.

from copy import deepcopy

obst = [["Apfel", "Birne"]]
alias = obst
flache_kopie = obst.copy()
tiefe_kopie = deepcopy(obst)

alias[0].append("Kirsche")
print("Original:", obst)
print("Flache Kopie:", flache_kopie)
print("Tiefe Kopie:", tiefe_kopie)

flache_kopie.append(["Orange"])
print("Original nach äußerer Ergänzung der Kopie:", obst)
print("Flache Kopie nach äußerer Ergänzung:", flache_kopie)
