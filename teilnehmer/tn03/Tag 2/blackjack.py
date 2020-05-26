import random
import os
#def count_points(wessen):
 #   wessen.split(" ",0)[1]
eingabe = True
counter = 50
dealercards = []
dealerpoints = []
usercards = []
userpoints = []
deck=[]
wert=[1,2,3,4,5,6,7,8,9,10,11]
karten=["Ass","König","Dame","Bube","10","9","8","7","6","5","4","3","2"]
farben=["Karo","Herz","Pike","Kreuz"]
x=len(karten)-1
y=len(farben)-1
print("test1")
while x >= 0:
    y=len(farben)-1
    while y >= 0:
        y = y - 1
        deck.append(farben[y]+" "+karten[x])
    x = x -1
while eingabe:
    dealercards=random.choices(deck, k=2)
    usercards.append(random.choices(deck, k=2))
    print("Du hast {} was {} Punkte gibt. Der Dealer hat mit {} {} Punkte".format(usercards, userpoints, dealercards, dealerpoints))
    break
#    if usernumber > randomnumber:
#        counter = counter + 1
#        print("You won 1 €! You now have: "+ str(counter)+" €")
#    elif usernumber < randomnumber:
#        counter = counter - 1
#        print("You lost 1 €! You now have: "+ str(counter)+" €")
#    else:
#        print("It is a draw! You stay at: "+ str(counter)+" €")
#    if counter == 0:
#        print("You lost all your money. Please try again.")
#        exit()
#    else:
#        print("Do you want to roll again? Y/N")
#        eingabe = "Y" in input()