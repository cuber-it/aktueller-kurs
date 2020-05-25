import random

wert = int(input("Ihre Zahl zwischen 1 und 99: "))
if wert < 1 or wert > 99:
    print("falscher Wert")
    exit()
    
wurf = None
counter = 0
while wurf != wert:
    counter = counter + 1
    wurf = random.randint(1 ,99)

print("Es waren {} Würfe notwendig".format(counter))
