text = "Ein langer Text"
wert = 123
template = "Es beginnt: {} und es endet"
liste = [ 1, 2, 3, 4]

print(text)
print("Es beginnt: " + text + " und er endet")
print("Eine Zahl:" + str(wert))
# alt: print "Eine Zahl: %d" % (wert)
print("Eine Zahl {}".format(wert))
print("Es beginnt: {} und es endet".format(text))

print(template.format(text))

print("{}: {} {} {}".format(*liste))