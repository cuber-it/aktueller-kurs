#! /usr/bin/python3

quelle = input ("Quelldatei: ")
ziel = input ("Zieldatei: ")
try:
    with open (quelle) as fd:
        text = fd.read()

    with open (ziel, "w") as fd:
        fd.write(text)


    print ("{} nach {} ├╝bertragen".format(quelle, ziel))
    exit(0)
except:
    print("Operation fehlgeschlagen")
    exit (1)
    
