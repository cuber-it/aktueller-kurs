import sqlite3
import csv

# Datenbank und CSV-Datei
database_file = "stock_data.db"
csv_file = "apple_stock_prices.csv"

# Verbindung zur SQLite-Datenbank herstellen
connection = sqlite3.connect(database_file)
cursor = connection.cursor()

# Tabelle für Börsenkurse erstellen
cursor.execute('''
CREATE TABLE IF NOT EXISTS stock_prices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    open REAL,
    high REAL,
    low REAL,
    close REAL,
    volume INTEGER
)
''')
print("Tabelle 'stock_prices' erstellt (falls nicht bereits vorhanden).")

# CSV-Datei lesen und in die Tabelle einfügen
with open(csv_file, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        cursor.execute('''
            INSERT INTO stock_prices (date, open, high, low, close, volume)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (row["Date"], row["Open"], row["High"], row["Low"], row["Close"], row["Volume"]))

# Änderungen speichern und Verbindung schließen
connection.commit()
print("Daten erfolgreich in die Tabelle 'stock_prices' eingefügt.")
connection.close()
