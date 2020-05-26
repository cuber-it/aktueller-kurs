def read_file(fname):
    with open(fname) as fd:
        text = fd.read().split("\n")    # zeilenweise in text abspeichern
    return text

quelle="/home/coder/aktueller-kurs/tag_2/openthesaurus.txt"
daten = read_file(quelle)

print(len(daten))
print(daten[-20])       # 20. Zeile vom Ende aus ausgeben