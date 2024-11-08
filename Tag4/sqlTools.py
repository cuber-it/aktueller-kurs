import sqlite3

con = None

try:
    con = sqlite3.connect("daten.db")
    csr = con.cursor()

    csr.execute('SELECT * FROM tablleX')

    # Hier passieren Dinge ...
    # z.B fetchone() - ein Ergebnis Satz, Zeiger auf nächste Row gesetzt
    # fetchall() alle Rows als Liste von Dict
    
except sqlite3.DatabaseError as e:
    print("Database error:", e)
except Exception as e:
    print(e)

finally:
    if con:
        con.close()
#-------------------------------------------------------------------
import cx_Oracle

con = None

try:
    # Verbindung zur Oracle-Datenbank herstellen
    # Beispiel: "username/password@hostname:port/SID"
    con = cx_Oracle.connect("username/password@hostname:port/SID")
    csr = con.cursor()

    # Hier passieren Dinge ...
except cx_Oracle.DatabaseError as e:
    print("Database error:", e)
except Exception as e:
    print("Other error:", e)

finally:
    # Cursor und Verbindung schließen
    if csr:
        csr.close()
    if con:
        con.close()