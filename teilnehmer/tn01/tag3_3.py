import sys

sys.path.insert(0, "/home/coder/aktueller-kurs/tag_3")
print(sys.path)

import Person
import my_io

p = []
p.append(Person.Person("Willi", "12345", "Musterstadt", "Musterstr."))
p.append(Person.Person("Karl", "54321", "Musterstadt", "Musterweg"))
p.append(Person.Person("Heinz", "13579", "Musterstadt", "Musterallee"))

for e in p:
    my_io.spit(e.name + '.txt', e.get_values())
    name, plz, ort, strasse = my_io.slurp(e.name + '.txt', "LIST")
    print(name + " " + plz + " " + ort + " " + strasse)
