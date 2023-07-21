import sqlite3

# Establish a connection to the database.
# This will create the database if it doesn't exist.
conn = sqlite3.connect('example.db')

# Create a cursor object.
c = conn.cursor()

# Execute an SQL statement to create a table.
c.execute('''
    CREATE TABLE stocks
    (date text, trans text, symbol text, qty real, price real)
''')

# Insert a row of data.
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes.
conn.commit()

# Execute an SQL statement to query some data.
c.execute('SELECT * FROM stocks WHERE symbol=?', ('RHAT',))
print(c.fetchone())

# Close the connection.
conn.close()
