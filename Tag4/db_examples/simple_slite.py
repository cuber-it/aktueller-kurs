import sqlite3

# Verbindung zur SQLite-Datenbank herstellen
connection = sqlite3.connect("daten.db")
cursor = connection.cursor()

# Tabelle anlegen, falls sie noch nicht existiert
cursor.execute('''
CREATE TABLE IF NOT EXISTS addresses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    phone TEXT,
    email TEXT,
    address TEXT
)
''')
connection.commit()

# Daten aus der Tabelle einlesen und ausgeben
print("Daten in der 'addresses'-Tabelle:")
cursor.execute("SELECT * FROM addresses")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Beispiel für das Einfügen neuer Daten
new_data = [
     ("Carl", "Müller", "456-789-0123", "carl.mueller@example.com", "321 Birch St"),
     ("Lisa", "Klein", "567-890-1234", "lisa.klein@example.com", "654 Pine Rd"),
     ("Antje", "Klein", "567-890-1234", "antje.klein@example.com", "654 Pine Rd")
]

cursor.executemany("INSERT INTO addresses (first_name, last_name, phone, email, address) VALUES (?, ?, ?, ?, ?)", new_data)
connection.commit()
print("\nNeue Daten hinzugefügt.")

# Aktualisierte Daten ausgeben
print("\nAktualisierte Daten in der 'addresses'-Tabelle:")
for row in cursor.execute("SELECT * FROM addresses"):
    print(row)

# Verbindung schließen
connection.close()

