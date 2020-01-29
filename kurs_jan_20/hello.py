import random

template = "Hello, world {}, du hast Los {}"

losnummer = random.randint(1,49)
name = input("Dein Name: ")

print(template.format(name, losnummer))
