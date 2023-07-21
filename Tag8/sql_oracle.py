import cx_Oracle as oracle

# Establish a connection to the database.
# This will create the database if it doesn't exist.
conn = oracle.connect(
    user="username",   # replace with your Oracle username
    password="password", # replace with your Oracle password
    dsn="localhost/XEPDB1" # replace with your Oracle hostname and service name
)

# Create a cursor object.
c = conn.cursor()

# Execute an SQL statement to create a table.
c.execute('''
    CREATE TABLE stocks
    (date_var VARCHAR2(20), trans VARCHAR2(20), symbol VARCHAR2(20), qty NUMBER, price NUMBER)
''')

# Insert a row of data.
c.execute("INSERT INTO stocks (date_var, trans, symbol, qty, price) VALUES (:1, :2, :3, :4, :5)",
          ('2006-01-05', 'BUY', 'RHAT', 100, 35.14))

# Save (commit) the changes.
conn.commit()

# Execute an SQL statement to query some data.
c.execute('SELECT * FROM stocks WHERE symbol = :1', ('RHAT',))
print(c.fetchone())

# Close the connection.
conn.close()
