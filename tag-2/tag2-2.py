with open("openthesaurus.txt", encoding="utf-8") as f:
    text = f.readlines()

d = {}
for zeile in text:
    if not zeile.startswith("#"):
        zeile = zeile.strip("\n")
        zeile = zeile.split(";")
        d[zeile[0]] = zeile[1:]

suchwort = ""
while suchwort != "Exit":
    suchwort = input("Welches Wort? ")
    if suchwort != "Exit":
        print(d.get(suchwort, "Nichts gefunden!"))