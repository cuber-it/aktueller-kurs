def quersumme(zahl):
    zahl = abs(zahl)
    return zahl and zahl % 10 + quersumme(zahl // 10)


eingabe = int(input("Gib eine Zahl ein: "))
print("Die Quersumme ist:", quersumme(eingabe))
