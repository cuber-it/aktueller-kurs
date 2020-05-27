import random
import os
import re

eingabe = True
newcard = True
counter = 50
deck=[]
kartenwert=[] ##Test
result=[]     ##Test
wert=[11,10,10,10,10,9,8,7,6,5,4,3,2]
karten=["Ass","König","Dame","Bube","10","9","8","7","6","5","4","3","2"]
farben=["Karo","Herz","Pike","Kreuz"]
x=len(karten)-1
y=len(farben)-1

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
    return output

def restart(eingabe):
    eingabe = "J" in input()

def loss(counter):
    counter=counter-1
    print("Sie haben {} was {} Punkte ergibt. Der Dealer hat mit {} {} Punkte\nSie haben leider verloren\nIhr neuer Kontostand beträgt: {} €\nWollen Sie neu starten? J/N".format(usercards, userpoints, dealercards, dealerpoints,counter))
    restart(eingabe)

def win(counter):
    counter=counter+1
    print("Sie haben {} was {} Punkte ergibt. Der Dealer hat mit {} {} Punkte\nSie haben gewonnen!\nIhr neuer Kontostand beträgt: {} €\nWollen Sie neu starten? J/N".format(usercards, userpoints, dealercards, dealerpoints,counter))

while x >= 0:
    y=len(farben)-1
    while y >= 0:
        y = y - 1
        deck.append(farben[y]+" "+karten[x])
    x = x -1
while eingabe:
    dealercards = []
    dealerpoints = 0
    usercards = []
    userpoints = 0
    dealercards=random.choices(deck, k=2)
    usercards=random.choices(deck, k=2)
    userpoints=count_points(usercards)
    dealerpoints=count_points(dealercards)
    print("Sie haben {} was {} Punkte ergibt. Der Dealer hat mit {} {} Punkte\nWollen Sie noch eine Karte? J/N".format(usercards, userpoints, dealercards, dealerpoints))
    newcard="J" in input()
    while newcard:
        usercards.append(random.choice(deck))
        userpoints=count_points(usercards)
        if userpoints > 21:
            loss(counter)
            counter=counter-1
            print(eingabe)
            break
        print("Sie haben {} was {} Punkte ergibt. Der Dealer hat mit {} {} Punkte\nWollen Sie noch eine Karte? J/N".format(usercards, userpoints, dealercards, dealerpoints))
        newcard="J" in input()
    else:
        while dealerpoints < userpoints:
            dealercards.append(random.choice(deck))
            dealerpoints=count_points(dealercards)
            if dealerpoints > 21:
                win(counter)
                counter=counter+1
                break
            else:
                print("Der Dealer hat eine neue Karte. {} {} Punkte".format(usercards, userpoints, dealercards, dealerpoints))
        while dealerpoints <= 21:
            loss(counter)
            counter=counter-1
            break
        else:
            win(counter)
            counter=counter+1
            break
        if counter == 0:
            print("You lost all your money. Please try again.")
            exit()