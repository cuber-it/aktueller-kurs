log = [
    "2019 ERR",
    "2019 OK",
    "2019 WARN",
    "2018 OK",
    "2017 OK",
    "2017 ERR"
]

zeilen_nummer = 1
fehler_nummer = 0
for zeile in log:
    if "OK" not in zeile:
        # print(str(zeilen_nummer) + " " + zeile)
        print("{}\t{}".format(zeilen_nummer, zeile))
        fehler_nummer += 1
    zeilen_nummer += 1
    # zeilen_nummer = zeilen_nummer + 1
print("Gefundene Fehler: {}".format(fehler_nummer))
# print(log)