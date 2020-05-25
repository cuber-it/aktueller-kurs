quelle = input("Quelldatei: ")
ziel = input("Zieldatei: ")
try:
    with open(quelle) as fd:
        text = fd.read()

    with open(ziel, "w") as fd:
        fd.write(text)

    print("{} nach {} übertragen".format(quelle, ziel))
    exit(0)
except:
    print("Operation schiefgegangen!")
    exit(1)