quelle = input("Wie heißt die Quelldatei?")
ziel = input("Wie lautet die Zieldatei?")
try:
    with open(quelle) as fd:
        text = fd.read()
    with open(ziel, "x") as fd:
        fd.write(text)

    print("{} nach {} übertragen".format(quelle, ziel))
    exit(0)
except:
    print("Operation ist schiefgegangen!")
    exit(1)