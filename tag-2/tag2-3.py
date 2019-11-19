
def read_data(file_name, used_encoding="utf-8"):
    """

    :param file_name: mandtory, the file
    :param used_encoding: optional, default utf-8
    :return: list of strings
    """
    with open(file_name, encoding=used_encoding) as f:
        return f.readlines()

# build_thesaurus
# Autor: ulrich
# Parameter: list
# Return: dict
def build_thesaurus(text):
    d = {}
    for zeile in text:
        if not zeile.startswith("#"):
            zeile = zeile.strip("\n")
            zeile = zeile.split(";")
            d[zeile[0]] = zeile[1:]
    return d

def suche_worte(thesaurus):
    """
    Searches for word in Thesaurus
    :param thesaurus: dict of wordlists
    :return: None
    """
    suchwort = ""
    while suchwort != "Exit":
        suchwort = input("Welches Wort? ")
        if suchwort != "Exit":
            print(thesaurus.get(suchwort, "Nichts gefunden!"))

#---usage---
text = read_data("openthesaurus.txt")
thesaurus = build_thesaurus(text)
suche_worte(thesaurus)
