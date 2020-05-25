import random
eingabe = True
counter = 50
randomnumber = None
usernumber = None
while eingabe:
    randomnumber = random.randint(1,6)
    usernumber = random.randint(1,6)
    print("You rolled a "+ str(usernumber) + " The PC rolled a " + str(randomnumber))
    if usernumber > randomnumber:
        counter = counter + 1
        print("You won 1 €! You now have: "+ str(counter)+" €")
    elif usernumber < randomnumber:
        counter = counter - 1
        print("You lost 1 €! You now have: "+ str(counter)+" €")
    else:
        print("It is a draw! You stay at: "+ str(counter)+" €")
    if counter == 0:
        print("You lost all your money. Please try again.")
        exit()
    else:
        print("Do you want to roll again? Y/N")
        eingabe = "Y" in input()