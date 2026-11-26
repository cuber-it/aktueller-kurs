quotes = r"materialien/HistoricalQuotes.csv"

stock_values = {}

with open(quotes)  as fd:
    data = fd.read().splitlines() # Eine Liste von Zeilen als gnaze Strings

for row in data[1:]:
    elements = row.split(",") # die einzelnen Werte auf einer Zeile

    # Idenx 0: ist immer das Datum
    datum = elements[0].strip()
    eroeffnung  = float(elements[3].strip().replace("$", ""))
    schlusskurs = float(elements[1].strip().replace("$", ""))

    stock_values[datum] = {
        "open": eroeffnung,
        "close": schlusskurs}

start_datum = input("Startdatum (MM/TT/JJJJ): ")
ende_datum = input("Endedatum   (MM/TT/JJJJ): ")

print(start_datum,
      stock_values[start_datum]["open"],
      stock_values[start_datum]["close"])
print(ende_datum,
      stock_values[ende_datum]["open"],
      stock_values[ende_datum]["close"])

print("Differenz", stock_values[ende_datum]["close"] - stock_values[start_datum]["open"])
