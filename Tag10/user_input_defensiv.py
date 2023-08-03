import re

def get_input():
    eingabe = input("Bitte Integer eingeben zwischen 10 und 90: ")

    rex = re.compile(r"^([1-8][0-9]|90)$")

    if rex.match(eingabe):
        return(int(eingabe))
    else:
        return("Das war nix!")

