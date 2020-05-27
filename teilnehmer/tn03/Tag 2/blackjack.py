import random
import os
import re

def count_points(input):
    farben=["Karo","Herz","Pike","Kreuz"]
    y=len(farben)-1
    output = 0
    while y >= 0:
        y = y - 1
        output = input.count(farben[y]+" Ass")*11+output+input.count(farben[y]+" Dame")*10+input.count(farben[y]+" Bube")*10+input.count(farben[y]+" 10")*10+input.count(farben[y]+" König")*10+input.count(farben[y]+" 9")*9++input.count(farben[y]+" 8")*8+input.count(farben[y]+" 7")*7+input.count(farben[y]+" 6")*6+input.count(farben[y]+" 5")*5+input.count(farben[y]+" 4")*4+input.count(farben[y]+" 3")*3+input.count(farben[y]+" 2")*2
    if output > 21:
        y=len(farben)-1
        while y >= 0:
            y = y - 1
            output = output-input.count(farben[y]+" Ass")*11+input.count(farben[y]+" Ass")*1
    print(output)
    return output

eingabe = True
newcard = True
counter = 50
dealercards = []
dealerpoints = 0
usercards = []
userpoints = 0
deck=[]
kartenwert=[] ##Test
result=[]     ##Test
wert=[11,10,10,10,10,9,8,7,6,5,4,3,2]
karten=["Ass","König","Dame","Bube","10","9","8","7","6","5","4","3","2"]
farben=["Karo","Herz","Pike","Kreuz"]
x=len(karten)-1
y=len(farben)-1
while x >= 0:
    y=len(farben)-1
    while y >= 0:
        y = y - 1
        deck.append(farben[y]+" "+karten[x])
    x = x -1
while eingabe:
    dealercards=random.choices(deck, k=2)
    usercards=random.choices(deck, k=2)
    userpoints=count_points(usercards)
    dealerpoints=count_points(dealercards)
    print("Du hast {} was {} Punkte ergibt. Der Dealer hat mit {} {} Punkte""\n""Wollen Sie noch eine Karte? J/N".format(usercards, userpoints, dealercards, dealerpoints))
    newcard="J" in input()
    while newcard:
        usercards.append(random.choice(deck))
        userpoints=count_points(usercards)
        print("Du hast {} was {} Punkte ergibt. Der Dealer hat mit {} {} Punkte".format(usercards, userpoints, dealercards, dealerpoints))
        newcard="J" in input("Wollen Sie noch eine Karte? J/N ")
    else:
        print("Du hast {} was {} Punkte ergibt. Der Dealer hat mit {} {} Punkte".format(usercards, userpoints, dealercards, dealerpoints))
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