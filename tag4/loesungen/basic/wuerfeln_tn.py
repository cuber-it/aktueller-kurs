import random

def wuerfeln(anzahl):
    if type(anzahl) is not int or anzahl < 0:
        raise ValueError("Die Anzahl muss eine nicht negative ganze Zahl sein.")
    i=0
    augensumme=0
    while i<anzahl:
        augensumme += random.randint(1, 6)
        i += 1
    return augensumme

print("Augensumme aus 3 Würfen: ", wuerfeln(3))

print("Augensumme aus 0 Würfen: ", wuerfeln(0))

print("Augensumme aus 1 Wurf: ", wuerfeln(1))

try:
    x=int(input("wie oft soll gewürfelt werden?: " ))
    print(f"Augensumme aus {x} Würfen: ", wuerfeln(x))
except ValueError as e:
    print(e)
