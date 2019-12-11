def read_textfile(filename):
    with open(filename, encoding="utf-8") as datei:
        return datei.read().split("\n")

dateiname = "openthesaurus.txt"

rohdaten = read_textfile(dateiname)
arbeitsdaten = {}

for zeile in rohdaten:
    if not zeile.startswith("#"):
        wort, *woerter = zeile.split(";")
        arbeitsdaten[wort] = woerter

while True:
    eingabe = input("Suchwort: ")
    if eingabe == "EXIT":
        break
    ergebnis = arbeitsdaten.get(eingabe, "Nicht gefunden")
    print("{} {}:".format(eingabe, ergebnis))
