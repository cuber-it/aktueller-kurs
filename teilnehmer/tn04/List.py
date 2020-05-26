#!usr/bin/python3
import random

a = [1,3,5,7,11,13,17,19]

a[2] = 23

#print(a[2])

#print(a[:4])

#for x in a:
#    print(x)

#if 3 in a:
#    print("Zahl exisitiert")
x = 0 
i = 0
Try = None
Zahlen = []

while x < 9:
    Num = random.randint(0,100)
    Zahlen[x] = Num
    x = x + 1 

while i < 9:
    Try = input("Zahl eingeben:   ")
    i = i + 1
    if Try in Zahlen:
        print ("Die Nummer ist dabei. Du hast " + i + " Versuche gebraucht")
    else:
        print ("Die Nummer ist nicht dabei")




