import sys
import traceback
import sqlite3
import mysql.connector as mysql
import mysql.connector.errors as errors

db = None

try:
    db = mysql.connect(
        host = "localhost",  # or the name of your MySQL server if not on your local machine
        user = "username",  # replace with your MySQL username
        passwd = "password",  # replace with your MySQL password
        database = "database_name"  # replace with your database name
    )
    # hier passiern viele Dinge
    # auch Dinge die shiefgehen können
    print("Dinge ")
    pass
    sys.exit(0)
except errors.DatabaseError as e:
    print("FEHLER!!!", e)
    raise e
finally:
    print("Was noch zu erledigen ist ...")
    # Hier kümmern sich sich ums aufräumen
    # und zwar auch wenns Fehler gab
    if db:
        db.close()
    pass
    # wenn man wissen will ob ein Fehler auftrat und ggf welcher kann man das so erfahren:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    if exc_value is not None:
            print("Exception has been caught.")
            #print(traceback.print_exception(exc_type, exc_value, exc_traceback))
            sys.exit(2)
