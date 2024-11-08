import sqlite3

con = None

def insert_address(csr, first_name, last_name, phone, email, address):
    csr.execute('''
    INSERT INTO addresses (first_name, last_name, phone, email, address)
    VALUES (?, ?, ?, ?, ?)
    ''', (first_name, last_name, phone, email, address))
    print(f"Inserted {first_name} {last_name} into 'addresses'.")

# Sample data to insert
sample_data = [
    ("John", "Doe", "123-456-7890", "johndoe@example.com", "123 Elm St"),
    ("Jane", "Smith", "234-567-8901", "janesmith@example.com", "456 Oak Ave"),
    ("Alice", "Johnson", "345-678-9012", "alicejohnson@example.com", "789 Maple Dr")
]

try:
    con = sqlite3.connect("daten.db")
    csr = con.cursor()

    csr.execute('''
CREATE TABLE IF NOT EXISTS addresses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    phone TEXT,
    email TEXT,
    address TEXT
)
''')


    for entry in sample_data:
        insert_address(csr, *entry)

    # Commit the transaction
    con.commit()
except sqlite3.DatabaseError as e:
    print("Database error:", e)
except Exception as e:
    print(e)

finally:
    if con:
        con.close()