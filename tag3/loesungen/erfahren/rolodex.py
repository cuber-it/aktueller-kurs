"""Referenzlösung: Kontakte als Liste von Dictionaries verwalten."""

kontakte = []
felder = ("name", "vorname", "telefon", "plz", "ort", "strasse")

while True:
    print("n: neu | f: suchen | d: löschen | p: anzeigen | x: Ende")
    befehl = input("Befehl: ").strip().casefold()
    if befehl == "x":
        break
    if befehl == "n":
        kontakt = {}
        for feld in felder:
            kontakt[feld] = input(f"{feld}: ").strip()
        telefonnummern = {eintrag["telefon"] for eintrag in kontakte}
        if "" in kontakt.values():
            print("Alle Felder müssen ausgefüllt sein.")
        elif kontakt["telefon"] in telefonnummern:
            print("Telefonnummer ist bereits vorhanden.")
        else:
            kontakte.append(kontakt)
            print("Kontakt angelegt.")
    elif befehl == "f":
        name = input("Nachname: ").strip().casefold()
        plz = input("Postleitzahl: ").strip()
        treffer = [
            kontakt for kontakt in kontakte
            if kontakt["name"].casefold() == name and kontakt["plz"] == plz
        ]
        print("Treffer:", len(treffer))
        for kontakt in treffer:
            print(kontakt)
    elif befehl == "d":
        nummer = input("Zu löschende Telefonnummer: ").strip()
        if nummer not in {kontakt["telefon"] for kontakt in kontakte}:
            print("Telefonnummer nicht gefunden.")
        elif input("Löschen bestätigen (j/n): ").strip().casefold() == "j":
            kontakte = [kontakt for kontakt in kontakte if kontakt["telefon"] != nummer]
            print("Kontakt gelöscht.")
        else:
            print("Löschen abgebrochen.")
    elif befehl == "p":
        print("Kontakte:", len(kontakte))
        for kontakt in kontakte:
            print(kontakt)
    else:
        print("Unbekannter Befehl.")
