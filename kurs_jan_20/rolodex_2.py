rolofilename = "myRolo.txt"
rolo = {}
kommando = ""

def read_command():
    kommando = input("Kommando [a, s, d, q, p ..]")
    if not kommando in ["a", "r", "w", "p", "d", "s", "q"]:
        print("Unbekannt: {}".format(kommando))
        kommando = None
    return kommando

def search(rolo, name):
    '''
    search searches in rolo for name, gives phonenumber
    :param rolo: dict
    :param name: string - the name to search for
    :return: phonenumber od "unbekannt"
    '''
    return rolo.get(name, "unbekannt")

def delete(rolo, name):
    if name in rolo:
        del rolo[name]

def add(rolo, eingabe):
    name, telefon = eingabe.split(":")
    rolo[name] = telefon

def write(rolo, filename):
    if len(rolo) > 0:
        with open(filename, "w") as fd:
            fd.write("# Mein kleines Rolo\n")
            for k, v in rolo.items():
                fd.write("{}:{}\n".format(k, v))

def read(filename):
    result = {}
    with open(filename) as fd:
        data = fd.readlines()
    for zeile in data:
        if not zeile.startswith("#"):
            zeile = zeile.strip("\n")
            name, telefon = zeile.split(":")
            result[name] = telefon
    return result

def ausgabe(rolo):
    for k, v in rolo.items():
        print("{}-{}".format(k, v))

while kommando != "q":
    kommando = read_command()
    if kommando == "a":
        eingabe = input("Name:Telefon")
        add(rolo, eingabe)
    elif kommando == "s":
        eingabe = input("Wen soll ich suchen: ")
        result = search(rolo, eingabe)
        print("{} - {}".format(eingabe, result))
    elif kommando == "d":
        eingabe = input("Wen soll ich löschen: ")
        delete(rolo, eingabe)
    elif kommando == "p":
        ausgabe(rolo)
    elif kommando == "r":
        rolo = read(rolofilename)
        print("Gelesen")
    elif kommando == "w":
        write(rolo, rolofilename)
