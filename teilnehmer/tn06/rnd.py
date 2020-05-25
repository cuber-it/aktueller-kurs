import random

deine_zahl = int(input("Wähle eine Zahl zwischen 1 und 100 aus: "))
if deine_zahl < 1 or deine_zahl > 100:
    print("Gebe eine gültige Zahl von 1 bis 100 ein!")
    exit()

wuerfe = None
counter = 0
while wuerfe != deine_zahl:
    print(wuerfe)
    counter += 1
    wuerfe = random.randint(1, 100)

print("Es waren {} Würfe notwendig".format(counter))

