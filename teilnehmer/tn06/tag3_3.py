import sys

sys.path.insert(0,"/home/coder/aktueller-kurs/tag_3/")
#print(sys.path)

import Person
#from Person import Person -> alternative das man nicht Person.Person schreiben muss
import my_io

user = []
user.append(Person.Person("Peter","01256","Bautzen","Moritzplatz"))
user.append(Person.Person("Luise","13558","Berlin","Schumannstraße"))
user.append(Person.Person("Douglas","88542","Erlangen","Budapester Straße"))

#durch iste durchgehen und Datei erstellen
for x in user:
    my_io.spit(x.name + ".txt", x.get_values()) #Dateien mit Namen der Personen anlegen
    #Bsp.      Peter.txt , Inhalt der Person Peter

#Unpacking, wenn Aufbau bekannt ist
name, plz, ort, strasse = my_io.slurp("Luise.txt", "LIST")

p2 = Person.Person(name, plz, ort, strasse)
print(p2.get_values())






