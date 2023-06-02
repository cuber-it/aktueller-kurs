
dateiname = input("Dateiname: ")

with open(dateiname, "w") as fd:
    eingabe = ""
    while eingabe != "EXIT":
        eingabe = input("Eingabe: ")
        if eingabe != "EXIT":
            fd.write(eingabe + "\n")
            #print(eingabe, file=fd)
