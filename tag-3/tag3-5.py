def mach_was():
    print("in mach_was")
    raise Exception("Bäng!")
    print("immernoch in mach_was")

mach_was()

#try:
#  erg = 1 / 0
#except ZeroDivisionError as e:
#    print(e)
#finally:
#  print("Hier gehts immer durch")
#print("Wenn hier, dann ist nichts passiert")
