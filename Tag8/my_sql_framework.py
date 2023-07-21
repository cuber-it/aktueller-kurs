class SqlFramework:
    def __init__(self, connector, connect_string):
        self.connector = connector
        self.connect_string = connect_string

    def connect(self):
        self.connection = self.connector.connect(self.connect_string)
        return self.connection


    # ...



import sqlite3
import cx_Oracle


db_a = SqlFramework(sqlite3, "exampele.db").connect()
db_b = SqlFramework(cx_Oracle, "username|password|localhost/XEPDB1").connect()

# ...
