filea = input("bitte geben sie die Quell-Datei mit Pfad an: ")
fileb = input("bitte geben sie die Ziel-Datei mit Pfad an: ")

with open(filea) as fd:
    text = fd.read()

with open(fileb, "w") as fd:
    fd.write(text)

print ("{} nach {} übertragen".format(filea, fileb))
exit(0)