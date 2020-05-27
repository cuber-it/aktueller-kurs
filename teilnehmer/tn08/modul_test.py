import sys

sys.path.insert(0,"/home/coder/aktueller-kurs/tag_3")

import Person
import my_io


# 3 personen anlegen
p1 = Person.Person("Heinz")
p2 = Person.Person("Otto")
p3 = Person.Person("Claudia")

p1.set_values("Heinz", "22765", "HH", strasse="Museumstr")
p2.set_values("Otto", "40625", "DFF", strasse="Königsallee")
p3.set_values("Claudia", "22765", "HH", strasse="Museumstr")

# jede Person in eine eigen Datei
l = [p1, p2, p3]
for e in l:
    my_io.spit(e.name + ".txt",e.get_values())

# Person mittels slurp wieder einlesen
name, plz, ort, strasse = my_io.slurp("Claudia.txt","LIST")

# Diese Daten wieder als personenobjekt anlegen
p4 = Person.Person(name, plz, ort, strasse)
print(p4.get_values())

