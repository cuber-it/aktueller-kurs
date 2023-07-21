#from sqlitedict import SqliteDict
#
#db = SqliteDict(
#    r"E:\Workspaces\Kurse\aktueller-kurs\Material\titanic.sqlite",
#    tablename="Passengers",
#)
#
#print("There are %d items in the database" % len(db))
#
#for n in db.items(): # Funktioniert nicht - ein Bug in der Lib? Ein Fehler von uns?
#    print(n)
#
# db.close()


# Eigenentwicklung:
# - ffnet sqlite-Datenbank
# holt die Inhalte der passengers
# erzeugt eine Liste mit Dictionaries
# jedes Dict entspricht einem Datensatz
# Bentigt ist auch der Column header

# Frage wie können wir das machen?

import sqlite3
database = r"E:\Workspaces\Kurse\aktueller-kurs\Material\titanic.sqlite"
daten = [] #Typ: [ von {} ] - jedes Dict = ein Datensatz
