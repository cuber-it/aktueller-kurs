import sys

sys.path.insert(0,"/home/coder/aktueller-kurs/tag_3")
print(sys.path)

import Person
import my_io

p = []
p.append(Person.Person("Willi","11111","Berlin","Gehweg1"))
p.append(Person.Person("Heinz","99999","München","Gehweg2"))
p.append(Person.Person("Karl","444444","Frankfurt","Gehweg5"))

for e in p:
    my_io.spit(e.name + ".txt", e.get_values())

name, plz, ort, strasse = my_io.slurp("Karl.txt", "LIST")

p2 = Person.Person(name, plz, ort, strasse)
print(p2.get_values())