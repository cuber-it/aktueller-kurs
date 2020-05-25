import random
counter = 0
randomnumber = None
usernumber = int(input("Geben Sie hier ihre Zahl ein:"))
if usernumber < 1 or usenumber > 6:
    print("Fehlerhafte Eingabe")
    exit()
while randomnumber != usernumber:
    counter = counter + 1
    randomnumber = random.randint(1,6)
    print("You rolled a "+ str(usernumber) + " The PC rolled a " + str(randomnumber))

print("Es waren {} Würfe notwendig".format(counter))