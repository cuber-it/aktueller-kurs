path =r"/home/ucuber/Workspace/kurse/aktueller-kurs/Material/HistoricalQuotes.csv"

def to_float(cell):
    return float(cell.strip()[1:])

with open(path) as fd:
    raw_data = [ row.split(",") for row in fd.read().splitlines() ]

stock_data = {} # key: datum, value: {keys: volumen, Close/Last, Open, High, Low + zugehörige Werte}

for row in raw_data[1:]:
    m, d, y = row[0].split("/")
    stock_data[f"{y}{m}{d}"] = {
        "volumen": int(row[2]),
        "close": to_float(row[1]),
        "open": to_float(row[3]),
        "high": to_float(row[4]),
        "low": to_float(row[5])
    }

for k, v in list(stock_data.items())[:10]:
    print(k, v)
