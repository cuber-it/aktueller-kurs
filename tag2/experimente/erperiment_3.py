zaehler = 0

while zaehler < 10:
    print(zaehler, end=" ")
    zaehler += 1
print()

for zaehler in range(10):
    print(zaehler, end=" ")
print()

""" Simuliert einen mehrzeiligen Kommentar/Codeausblendung mit den drei Anführungszeichen
eingabe = input("Ein Text: ")
for i, zeichen in enumerate(eingabe):
    print(i, zeichen, end="->")
    print(eingabe[i])
"""

for name in ["Willi", "Heinz", "Karl"]:
    print("Kunde:", name)
