import mysql.connector as mysql

# Establish a connection to the database.
# This will create the database if it doesn't exist.
conn = mysql.connect(
    host="localhost",  # replace with your host, e.g. "127.0.0.1"
    user="username",   # replace with your MySQL username
    password="password", # replace with your MySQL password
    database="example" # replace with your database name
)

# Create a cursor object.
c = conn.cursor()

# Execute an SQL statement to create a table.
c.execute('''
    CREATE TABLE IF NOT EXISTS stocks
    (date text, trans text, symbol text, qty real, price real)
''')

# Insert a row of data.
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes.
conn.commit()

# Execute an SQL statement to query some data.
c.execute('SELECT * FROM stocks WHERE symbol=%s', ('RHAT',))
print(c.fetchone())

# Close the connection.
conn.close()
