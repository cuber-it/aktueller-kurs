import yfinance as yf

# Aktie definieren (Apple, AAPL)
ticker_symbol = "AAPL"

# Zeitraum und Intervalle definieren
start_date = "2023-01-01"
end_date = "2023-12-31"

# Börsendaten abrufen
data = yf.download(ticker_symbol, start=start_date, end=end_date)

# Daten in CSV-Datei speichern
csv_file = "apple_stock_prices.csv"
data.to_csv(csv_file)

print(f"Daten wurden erfolgreich in {csv_file} gespeichert.")
