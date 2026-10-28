file = r"/home/ucuber/Workspace/kurse/kurse/aktueller-kurs/materialien/beispiel.txt"

with open(file, "r") as fd:
    text = fd.read()

print(text)

with open("obst.txt", "w") as fd:
    fd.write(text)

with open("obst.txt", "a") as fd:
    print("Orange", file=fd)
