#IFC interactive file copy

#quelldatei erfragen   # normalen slash verwenden
#Zieldatei name erfragen
#quelle lesen
#quelle nach ziel schreiben


quelle = input("zu kopierende Quelldatei")
ziel = input("Zielpfad und Zieldateiname")

try:
    with open(quelle) as fd:
        text = fd.read()

    with open(ziel,"w") as fd:
        fd.write(text)

    print("{} nach {} übertragen".format(quelle, ziel))
    exit(0)
except:
    print("Da ist etwas schief gegangen!")
    exit(1)