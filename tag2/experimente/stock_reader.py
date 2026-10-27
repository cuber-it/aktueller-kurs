path = r"/home/ucuber/Workspace/kurse/kurs-python-gl/materialien/HistoricalQuotes.csv"

with open(path) as fd:
    quotes = fd.read()


print(quotes)
print(type(quotes))
print(len(quotes))

rows = quotes.splitlines() # Liste ohne \n
print(type(rows))
print(len(rows))

with open("converted.data", "w") as fd:
    for row in rows:
        row = row.split(", ")
        for field in row:
            field = field.replace("$", "")
            try:
                field = float(field)
            except ValueError:
                pass# Pfui! Frickelei!!! :-)
            print(field, file=fd, end=" ")
        print("", file=fd)
