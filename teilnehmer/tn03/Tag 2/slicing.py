log = [
    "20200501 13:45 AKTION Es ist was passiert",
    "20200501 13:50 BEGINN Es ist was passiert",
    "20200501 13:55 ENDE   Es ist was passiert",
]

for zeile in log:
    aktion = zeile[15:21]
    if aktion == "AKTION":
        print("Stufe 1")
    elif aktion == 'BEGINN':
        print("Stufe 2")
    elif aktion.strip() == "ENDE":
        print("Stufe 3")
    else:
        print("Unbekannt")