import sys

sys.path.insert(0, "/home/coder/aktueller-kurs/tag_3")

#import Person -> hat zur Folge, dass man Person.Person schreiben muss
from Person import Person
import my_io

personen = []
personen.append(Person("Willi", "12345", "Watzingen", "watzplatz 1"))
personen.append(Person("Heinz", "12345", "Watzingen", "watzplatz 1"))
personen.append(Person("Karl", "12345", "Watzingen", "watzplatz 1"))

for e in personen:
    my_io.spit(e.name + ".txt", e.get_values())

name, plz, ort, strasse = my_io.slurp("Karl.txt", "LIST")

p2 = Person(name, plz, ort, strasse)
print(p2.get_values())