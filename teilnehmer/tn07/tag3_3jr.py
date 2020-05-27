import sys

sys.path.insert(0, "/home/coder/aktueller-kurs/tag_3")

import Person
import my_io

P = []
p.append(Person.Person("Willi", "12345", "Watzingen", "Watzplatz 1"))
p.append(Person.Person("Heinz", "12345", "Watzingen", "Watzplatz 1"))
p.append(Person.Person("Karl", "12345", "Watzingen", "Watzplatz 1"))

for e in p:
    my_io.spit(e.name + ".txt", e.get_values())

name, plz, ort, strasse, = my_io.slurp("Karl.txt", "LIST")

p2 = Person.Person(name, plz, ort, strasse)
print(p2.get_values())