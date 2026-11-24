# Experiment – CSV-Daten in SQLite übertragen
# Start aus dem Repository: python3 -m tag4.experimente.quotes_2_sqlite

from pathlib import Path
from tag4 import data_source as ds


def main():
    """Verwendet die vorhandene Bibliothek für Hin- und Rückweg."""
    kurs = Path(__file__).resolve().parents[2]
    ausgabe = kurs / "tag4" / "ausgabe"
    ausgabe.mkdir(exist_ok=True)
    daten = ds.load_csv(kurs / "materialien" / "HistoricalQuotes.csv")
    datenbank = ausgabe / "quotes.db"
    ds.save_sql(daten, datenbank)
    geladen = ds.load_sql(datenbank)
    print("Aus CSV gelesen:", len(daten))
    print("Aus SQLite gelesen:", len(geladen))
    print("Datensätze stimmen überein:", daten == geladen)


if __name__ == "__main__":
    main()
