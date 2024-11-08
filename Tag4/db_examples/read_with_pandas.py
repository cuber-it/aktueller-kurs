import pandas as pd
from sqlalchemy import create_engine

# SQLite-Engine mit SQLAlchemy erstellen
engine = create_engine("sqlite:///daten.db")

# Tabelle einlesen und in DataFrame umwandeln
try:
    # Lese die Daten aus der 'addresses'-Tabelle in einen DataFrame
    df = pd.read_sql_table("addresses", con=engine)
    print("Daten erfolgreich eingelesen:")
    print(df)
except Exception as e:
    print("Fehler beim Einlesen der Daten:", e)

# Neue Daten zum Beispiel hinzufügen und speichern
new_data = pd.DataFrame({
    "first_name": ["Carl", "Lisa"],
    "last_name": ["Müller", "Klein"],
    "phone": ["456-789-0123", "567-890-1234"],
    "email": ["carl.mueller@example.com", "lisa.klein@example.com"],
    "address": ["321 Birch St", "654 Pine Rd"]
})

try:
    # Neue Daten anhängen
    new_data.to_sql("addresses", con=engine, if_exists="append", index=False)
    print("\nNeue Daten hinzugefügt.")

    # Daten erneut einlesen und ausgeben
    df_updated = pd.read_sql_table("addresses", con=engine)
    print("\nAktualisierte Daten:")
    print(df_updated)
except Exception as e:
    print("Fehler beim Hinzufügen der Daten:", e)
 