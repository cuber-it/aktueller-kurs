import random

def tippeingabe():
    result = []
    count = 0
    while count < 6:
        eingabe = input("Ihre Zahl: ")
        try:
            eingabe = int(eingabe)

            if eingabe in result:
                print("das war leider eine doppelte")
            elif eingabe < 1 or eingabe > 49:
                print("das war leider keine gültige")
            else:
                result.append(eingabe)
                count += 1
        except ValueError as err:
            print("bitte eine Zahl!")
    return result

def ziehung():
    return random.sample(range(1, 50), 6)

def auswertung(tipp, ziehung):
    result = 0
    for z in ziehung:
        if z in tipp:
            result += 1
    return result

t = tippeingabe()
t.sort()

ergebnisse = dict(zip([str(n) for n in range(0,7)], [0]*7))
print(ergebnisse)

for n in range(1000):
    z = ziehung()
    z.sort()
    ergebnis = auswertung(t, z)
    ergebnisse[str(ergebnis)] += 1
    print("{} {} -> {}".format(t, z, ergebnis))

for k, v in ergebnisse.items():
    print("{} -> {}".format(k, v))
