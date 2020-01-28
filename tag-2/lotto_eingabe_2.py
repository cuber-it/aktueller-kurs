zahlen = []
while len(zahlen) != 6:
    eingabe = input("Eine Zahl zwischen 1 und 49:")
    if not eingabe.isnumeric():
        print("ungültig, keine Zahl!")
        continue
    zahl = int(eingabe)
    if zahl < 1 or zahl > 49:
        print("ungültig, nicht zwischen 1 und 49!")
        continue
    doublette = False
    for z in zahlen:
        if z == zahl:
           doublette = True
           break
    if doublette:
        print("ungültig, doppelter Wert")
        continue
    zahlen.append(zahl)
print(zahlen)