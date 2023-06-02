PROMPT = "Dateiname: "
dateiname = input(PROMPT)

with open(dateiname, "rb") as file:
    daten = file.read()

print(len(daten))

dateiname = input("Ausgabe-Dateiname: ")
with open(dateiname, "wb") as file:
    file.write(daten)
