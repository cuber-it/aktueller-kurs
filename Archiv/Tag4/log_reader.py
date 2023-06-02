dateiname = r"E:/Workspaces/Kurse/aktueller-kurs/daten.txt"

file = open(dateiname, 'r', encoding='latin-1')
text = file.read()
file.close()
print(text)

text = ""
print(text)

# Abkürzung:
with open(dateiname) as file:
    text = file.read()
    zeilen = text.splitlines()
print(text)

zeilen_nummer = 0
for zeile in zeilen:
    print(zeilen_nummer, zeile)
    zeilen_nummer += 1
print("Fertig!")

for zeilen_nummer, zeile in enumerate(zeilen):
    print(zeilen_nummer, zeile)
print("Fertig!")
