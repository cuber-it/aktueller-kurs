wert_1 = 5
wert_2 = 10
liste = [1, 2, 3, 4]

print("{} {}".format(wert_1, wert_2))
print("{} {} {} {}".format(*liste))
print("Beispiel {2} Text {2} Text {0} Info: {1}".format(*liste))