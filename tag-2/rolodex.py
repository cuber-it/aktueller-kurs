rolofilename = "myRolo.txt"
rolo = {}
kommando = ""
while kommando != "q":
    kommando = input("Kommando [a, s, d, q, p ..]")
    if kommando == "a":
        eingabe = input("Name:Telefon")
        name, telefon = eingabe.split(":")
        rolo[name] = telefon
    elif kommando == "s":
        eingabe = input("Wen soll ich suchen: ")
        telefon = rolo.get(eingabe, "unbekannt")
        print("{} - {}".format(eingabe, telefon))
    elif kommando == "d":
        eingabe = input("Wen soll ich löschen: ")
        if eingabe in rolo:
            del rolo[eingabe]
    elif kommando == "p":
        for k, v in rolo.items():
            print("{} - {}".format(k, v))
    elif kommando == "r":
        pass
    elif kommando == "w":
        if len(rolo) > 0:
            with open(rolofilename, "w") as fd:
                fd.write("# Mein kleines Rolo\n")
                for k, v in rolo.items():
                    fd.write("{}:{}\n".format(k, v))
            print("Geschrieben")
        else:
            print("Nichts zu schreiben!")
    else:
        if kommando != "q":
            print("Unbekanntes Kommando {}".format(kommando))
