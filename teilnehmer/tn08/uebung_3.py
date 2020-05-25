import random

eingabe = int(input("Bitte geben Sie eine Zahl zwischen 1 und 20 ein: "))

# Abbruch?
if eingabe < 1 and eingabe > 20:
    print("Bitte passenden Wert eingeben!")
    exit()

i = 0
x = 0

while eingabe != x:
    x = random.randint(1, 20)
    i = i + 1      # counter += 1
    
print("Wir mussten " + str(i) + " mal würfeln!")

