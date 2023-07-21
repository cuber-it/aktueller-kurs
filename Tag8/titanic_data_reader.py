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
import json


def get_db_data(database, table_name):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    table = cursor.execute(f"SELECT * FROM {table_name}")

    # List Comprehension: names = [description[0] for description in cursor.description]
    names = []
    for description in cursor.description:
        names.append(description[0])

    # List Comprehension: daten = [dict(zip(names, row)) for row in table.fetchall()]
    daten = []
    for row in table.fetchall():
        daten.append(dict(zip(names, row,)))
    return daten

def dump_json(fname, daten, indent=4):
    fname += ".json"
    with open(fname, "w") as fp:
        json.dump(daten, fp, indent=indent)

if __name__ == "__main__":
    import pprint

    database = r"E:\Workspaces\Kurse\aktueller-kurs\Material\titanic.sqlite"
    table = "passengers"

    daten = get_db_data(database, table)
    pprint.pprint(daten)
    dump_json(table, daten)
