
source = input("Quelldatei: ")
target = input("Zieldatei: ")

try:
    with open(source) as fd:
        text = fd.read()

    with open(target,"w") as fd:
        fd.write(text)

    print("{} nach {} übertragen".format(source, target))
    exit(0)
except:
    print("Operation schiefgeganegn!")
    exit(1)