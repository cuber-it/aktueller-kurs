from random import randint


wert = int (input("Geben Sie eine Zahl zwischen 1-99: "))
wurf = None
counter = 0
while wurf != wert:
    counter = counter +1
    #counter +=1 alternative für counter = counter + 1
    wurf = randint(1,100)

print ("Es waren {} Würfe notwendig". format(counter))


